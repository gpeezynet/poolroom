import json
import subprocess
import sys
import tempfile
from pathlib import Path
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[1]


def load_assumptions() -> dict:
    path = ROOT / "model" / "assumptions.yaml"
    # utf-8-sig safely handles BOM if present
    return yaml.safe_load(path.read_text(encoding="utf-8-sig"))


def get_path(d: dict, path: str):
    cur = d
    for part in path.split("."):
        if not isinstance(cur, dict) or part not in cur:
            raise KeyError(path)
        cur = cur[part]
    return cur


def run_cli(args):
    cmd = [sys.executable, "-m", "src.cli", "run"] + args
    result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    if result.returncode != 0:
        raise AssertionError(result.stderr or result.stdout)


class ScenarioSmokeTests(unittest.TestCase):
    def _assert_outputs(self, scenario_id: str) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            out_dir = Path(tmpdir)
            run_cli(["--scenario", scenario_id, "--out-dir", str(out_dir)])

            report = out_dir / f"{scenario_id}_report.md"
            summary = out_dir / f"{scenario_id}_summary.json"

            self.assertTrue(report.exists(), f"Missing report for {scenario_id}")
            self.assertTrue(summary.exists(), f"Missing summary for {scenario_id}")

            self.assertTrue(report.read_text(encoding="utf-8").strip())
            data = json.loads(summary.read_text(encoding="utf-8"))
            self.assertEqual(data.get("scenario_id"), scenario_id)
            totals = data.get("totals", {})
            for key in (
                "monthly_fixed_costs",
                "occupancy_cost_monthly",
                "utilities_cost_monthly",
                "semi_fixed_labor_monthly",
                "monthly_debt_service",
                "dscr",
                "cash_gap_monthly",
                "required_utilization_multiplier_for_cash_break_even",
                "sales_gap_per_day_for_cash_break_even",
                "bar_only_bar_sales_monthly",
                "bar_only_food_sales_monthly",
                "total_table_sales_monthly",
                "total_bar_sales_monthly",
                "total_food_sales_monthly",
            ):
                self.assertIn(key, totals, f"Missing totals.{key} in summary for {scenario_id}")
            self.assertIn("total_capex", data, f"Missing total_capex in summary for {scenario_id}")
            dscr = totals.get("dscr")
            self.assertIsInstance(dscr, (int, float), f"DSCR is not numeric for {scenario_id}")
            self.assertGreaterEqual(dscr, 0, f"DSCR is negative for {scenario_id}")
            self.assertLessEqual(dscr, 20, f"DSCR is unusually high for {scenario_id}")
            late_incremental = data.get("late_incremental")
            if "LATE" in scenario_id:
                self.assertIsNotNone(late_incremental, f"Missing late_incremental for {scenario_id}")
                for key in (
                    "sales_monthly",
                    "variable_costs_monthly",
                    "gross_profit_monthly",
                    "fixed_costs_monthly",
                    "noi_monthly",
                    "cash_after_debt_monthly",
                    "break_even_sales_per_day",
                    "bar_sales_monthly",
                    "food_sales_monthly",
                ):
                    self.assertIn(key, late_incremental, f"Missing late_incremental.{key} for {scenario_id}")
                drivers = data.get("revenue_drivers", {})
                legal_max = drivers.get("legal_max_open_hours_per_day")
                modeled_open = drivers.get("open_hours_per_day_modeled")
                self.assertIsNotNone(legal_max, f"Missing legal_max_open_hours_per_day for {scenario_id}")
                self.assertIsNotNone(modeled_open, f"Missing open_hours_per_day_modeled for {scenario_id}")
                self.assertLessEqual(
                    modeled_open,
                    legal_max + 1e-6,
                    f"Modeled hours exceed legal max for {scenario_id}",
                )
                standard_hours = drivers.get("standard_open_hours_per_day", 0)
                capped_week = late_incremental.get("extra_hours_per_week_capped")
                self.assertIsNotNone(
                    capped_week, f"Missing extra_hours_per_week_capped for {scenario_id}"
                )
                max_extra_week = max((legal_max - standard_hours), 0) * 7
                self.assertLessEqual(
                    capped_week,
                    max_extra_week + 1e-6,
                    f"Late hours/week exceed legal cap for {scenario_id}",
                )
            if "LOCKUP" in scenario_id:
                self.assertIsNotNone(late_incremental, f"Missing late_incremental for {scenario_id}")
                self.assertGreater(
                    late_incremental.get("sales_monthly", 0), 0, f"No late sales for {scenario_id}"
                )
                self.assertAlmostEqual(
                    late_incremental.get("bar_sales_monthly", 0),
                    0,
                    places=6,
                    msg=f"Late bar sales should be zero for {scenario_id}",
                )
                self.assertAlmostEqual(
                    late_incremental.get("food_sales_monthly", 0),
                    0,
                    places=6,
                    msg=f"Late food sales should be zero for {scenario_id}",
                )
            if late_incremental and late_incremental.get("sales_monthly", 0) > 0:
                sales = late_incremental["sales_monthly"]
                variable_costs = late_incremental.get("variable_costs_monthly", 0)
                gross_profit = late_incremental.get("gross_profit_monthly", 0)
                fixed_costs = late_incremental.get("fixed_costs_monthly", 0)
                noi = late_incremental.get("noi_monthly", 0)
                cash_after_debt = late_incremental.get("cash_after_debt_monthly", 0)
                incremental_debt = late_incremental.get("incremental_debt_service_monthly", 0)
                self.assertAlmostEqual(
                    gross_profit,
                    sales - variable_costs,
                    places=6,
                    msg=f"Late gross profit mismatch for {scenario_id}",
                )
                self.assertAlmostEqual(
                    noi,
                    gross_profit - fixed_costs,
                    places=6,
                    msg=f"Late NOI mismatch for {scenario_id}",
                )
                self.assertAlmostEqual(
                    cash_after_debt,
                    noi - incremental_debt,
                    places=6,
                    msg=f"Late cash-after-debt mismatch for {scenario_id}",
                )

    def test_required_assumptions_are_not_placeholders(self):
        a = load_assumptions()
        required_paths = [
            "facility.hvac.service_contract_per_year",
            "facility.hvac.filter_replacement_per_month",
            "facility.hvac.hvac_maintenance_reserve_per_year",
            "music_licensing.total_music_licenses_per_year",
            "pos_stack.monthly_software_fee",
            "pos_stack.payment_processing_pct",
            "pos_stack.card_mix_pct",
            "marketing.monthly_budget",
            "maintenance.annual_budget_12_tables.total_high",
            "maintenance.annual_budget_24_tables.total_high",
        ]
        for p in required_paths:
            v = get_path(a, p)
            self.assertNotEqual(str(v).strip().upper(), "PLACEHOLDER", f"{p} is PLACEHOLDER")

    def test_s12_outputs(self):
        self._assert_outputs("S12")

    def test_s24_outputs(self):
        self._assert_outputs("S24")


if __name__ == "__main__":
    unittest.main()
