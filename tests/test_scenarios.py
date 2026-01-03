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
            ):
                self.assertIn(key, totals, f"Missing totals.{key} in summary for {scenario_id}")
            self.assertIn("total_capex", data, f"Missing total_capex in summary for {scenario_id}")
            dscr = totals.get("dscr")
            self.assertIsInstance(dscr, (int, float), f"DSCR is not numeric for {scenario_id}")
            self.assertGreaterEqual(dscr, 0, f"DSCR is negative for {scenario_id}")
            self.assertLessEqual(dscr, 20, f"DSCR is unusually high for {scenario_id}")
            if "LATE" in scenario_id:
                for key in (
                    "late_incremental_noi_monthly",
                    "late_incremental_cashflow_after_debt_monthly",
                ):
                    self.assertIn(key, totals, f"Missing totals.{key} in summary for {scenario_id}")

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
