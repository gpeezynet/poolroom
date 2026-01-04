import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path
import unittest

import yaml

from src.sensitivity import run_sensitivity
from src.report import render_report
from src.model import compute_scenario


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
                "program_membership_revenue_monthly",
                "program_league_revenue_monthly",
                "program_event_revenue_monthly",
                "program_total_revenue_monthly",
                "program_total_contribution_monthly",
                "program_membership_discount_cost_monthly",
                "program_membership_net_contribution_monthly",
                "program_membership_net_after_discount_monthly",
                "program_membership_break_even_avg_sales_per_visit",
                "program_incremental_labor_cost_monthly",
                "program_incremental_security_cost_monthly",
                "program_net_contribution_monthly",
                "program_uplift_utilization_multiplier",
                "program_uplift_spend_multiplier",
                "program_incremental_bar_only_guests_monthly",
                "program_incremental_table_hours_sold_monthly",
                "capex_total",
                "total_project_cost",
                "equity_required_at_close",
                "loan_amount",
                "total_cash_required_to_open",
                "runway_months",
                "rent_monthly",
                "cam_monthly",
                "utilities_monthly",
                "total_occupancy_cost_monthly",
            ):
                self.assertIn(key, totals, f"Missing totals.{key} in summary for {scenario_id}")
            self.assertIn("total_capex", data, f"Missing total_capex in summary for {scenario_id}")
            dscr = totals.get("dscr")
            self.assertIsInstance(dscr, (int, float), f"DSCR is not numeric for {scenario_id}")
            self.assertGreaterEqual(dscr, 0, f"DSCR is negative for {scenario_id}")
            self.assertLessEqual(dscr, 20, f"DSCR is unusually high for {scenario_id}")
            self.assertGreater(
                totals.get("rent_monthly", 0), 0, f"Rent is not positive for {scenario_id}"
            )
            self.assertGreater(
                totals.get("cam_monthly", 0), 0, f"CAM is not positive for {scenario_id}"
            )
            self.assertGreater(
                totals.get("utilities_monthly", 0),
                0,
                f"Utilities are not positive for {scenario_id}",
            )
            drivers = data.get("revenue_drivers", {})
            open_hours = drivers.get("open_hours_per_day_modeled")
            periods = data.get("periods", [])
            if open_hours is not None and periods:
                total_table_hours = sum(
                    p.get("metrics", {}).get("table_hours", 0) for p in periods
                )
                max_table_hours = data.get("tables", 0) * open_hours * 30
                self.assertLessEqual(
                    total_table_hours,
                    max_table_hours + 1e-6,
                    f"Table hours exceed cap for {scenario_id}",
                )
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
            if "PLUS_PROGRAMS" in scenario_id:
                self.assertGreater(
                    totals.get("program_total_revenue_monthly", 0),
                    0,
                    f"Programs should be active for {scenario_id}",
                )
            if "PLUS_PROGRAMS2" in scenario_id:
                self.assertTrue(
                    totals.get("program_incremental_table_hours_sold_monthly", 0) > 0
                    or totals.get("program_incremental_bar_only_guests_monthly", 0) > 0,
                    f"Program drivers should add demand for {scenario_id}",
                )
                self.assertGreater(
                    totals.get("program_incremental_labor_cost_monthly", 0),
                    0,
                    f"Program labor costs should be positive for {scenario_id}",
                )

            capex_total = totals.get("capex_total", 0)
            total_project_cost = totals.get("total_project_cost", 0)
            ti_allowance = totals.get("ti_allowance", 0)
            equity_required = totals.get("equity_required_at_close", 0)
            loan_amount = totals.get("loan_amount", 0)
            self.assertAlmostEqual(
                total_project_cost,
                max(capex_total - ti_allowance, 0),
                places=6,
                msg=f"Total project cost mismatch for {scenario_id}",
            )
            self.assertAlmostEqual(
                total_project_cost,
                equity_required + loan_amount,
                places=6,
                msg=f"Equity + loan mismatch for {scenario_id}",
            )
            self.assertGreaterEqual(
                totals.get("total_cash_required_to_open", 0),
                equity_required,
                f"Total cash required should cover equity for {scenario_id}",
            )

            matrix_path = out_dir / "SCENARIO_MATRIX.csv"
            self.assertTrue(matrix_path.exists(), "Missing SCENARIO_MATRIX.csv")
            header = matrix_path.read_text(encoding="utf-8").splitlines()[0]
            for col in (
                "lease_band",
                "rent_monthly",
                "cam_monthly",
                "utilities_monthly",
                "total_occupancy_cost_monthly",
                "program_membership_discount_pct",
                "program_membership_discount_cost_monthly",
            ):
                self.assertIn(col, header, f"Missing matrix column {col} for {scenario_id}")
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
            "capex.scenario.S12.buildout",
            "capex.scenario.S12.ffe",
            "capex.scenario.S12.tables",
            "capex.scenario.S12.soft_costs",
            "capex.scenario.S12.contingency",
            "capex.scenario.S12.working_capital",
            "capex.scenario.S24.buildout",
            "capex.scenario.S24.ffe",
            "capex.scenario.S24.tables",
            "capex.scenario.S24.soft_costs",
            "capex.scenario.S24.contingency",
            "capex.scenario.S24.working_capital",
            "capex.ti_allowance",
            "capex.lease_deposit_months",
            "facility.sqft_by_scenario.S12",
            "facility.sqft_by_scenario.S24",
            "facility.rent_per_sqft_year.low",
            "facility.rent_per_sqft_year.mid",
            "facility.rent_per_sqft_year.high",
            "facility.cam_per_sqft_year.low",
            "facility.cam_per_sqft_year.mid",
            "facility.cam_per_sqft_year.high",
            "facility.utilities_per_sqft_year.low",
            "facility.utilities_per_sqft_year.mid",
            "facility.utilities_per_sqft_year.high",
            "facility.utilities_hours_multiplier.core",
            "facility.utilities_hours_multiplier.late",
            "revenue.programs.memberships.discount_pct",
            "revenue.programs.memberships.member_visits_per_month",
            "revenue.programs.memberships.discountable_sales_share",
            "memberships.member_visits_per_month",
            "memberships.discountable_sales_share",
            "financing.interest_rate",
            "financing.term_years",
            "financing.down_payment_pct",
        ]
        for p in required_paths:
            v = get_path(a, p)
            self.assertNotEqual(str(v).strip().upper(), "PLACEHOLDER", f"{p} is PLACEHOLDER")

    def test_s12_outputs(self):
        self._assert_outputs("S12")

    def test_s24_outputs(self):
        self._assert_outputs("S24")

    def test_lockup_programs2_outputs(self):
        for scenario_id in (
            "S12_BASE_LATE_LOCKUP_PLUS_PROGRAMS2",
            "S12_UPSIDE_LATE_LOCKUP_PLUS_PROGRAMS2",
            "S24_BASE_LATE_LOCKUP_PLUS_PROGRAMS2",
            "S24_UPSIDE_LATE_LOCKUP_PLUS_PROGRAMS2",
        ):
            self._assert_outputs(scenario_id)

    def test_lease_band_outputs(self):
        for scenario_id in (
            "S12_BASE_PLUS_PROGRAMS2_GOOD_LEASE",
            "S24_BASE_PLUS_PROGRAMS2_BAD_LEASE",
        ):
            self._assert_outputs(scenario_id)

    def test_lease_impact_section(self):
        assumptions = load_assumptions()
        scenarios = yaml.safe_load(
            (ROOT / "model" / "scenarios.yaml").read_text(encoding="utf-8-sig")
        )["scenarios"]
        scenario_ids = [
            "S12_BASE_PLUS_PROGRAMS2_GOOD_LEASE",
            "S12_BASE_PLUS_PROGRAMS2_BASE_LEASE",
            "S12_BASE_PLUS_PROGRAMS2_BAD_LEASE",
        ]
        results = {
            scenario_id: compute_scenario(assumptions, scenario_id, scenarios[scenario_id])
            for scenario_id in scenario_ids
        }
        report = render_report(results[scenario_ids[0]], results)
        self.assertIn("## Lease Impact", report)
        self.assertIn("delta vs BASE", report)

    def test_program_sensitivity_outputs(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            out_dir = Path(tmpdir)
            run_sensitivity(
                ROOT / "model" / "assumptions.yaml",
                ROOT / "model" / "scenarios.yaml",
                out_dir,
                "S12_BASE_PLUS_PROGRAMS2",
            )
            csv_path = out_dir / "PROGRAM_SENSITIVITY.csv"
            md_path = out_dir / "PROGRAM_SENSITIVITY.md"
            self.assertTrue(csv_path.exists(), "Missing PROGRAM_SENSITIVITY.csv")
            self.assertTrue(md_path.exists(), "Missing PROGRAM_SENSITIVITY.md")
            self.assertTrue(md_path.read_text(encoding="utf-8").strip())

    def test_security_mode_guard(self):
        assumptions = load_assumptions()
        scenarios = yaml.safe_load(
            (ROOT / "model" / "scenarios.yaml").read_text(encoding="utf-8-sig")
        )["scenarios"]
        scenario = scenarios["S12_BASE"]

        in_house = copy.deepcopy(assumptions)
        in_house["security_mode"] = "in_house"
        result_in_house = compute_scenario(in_house, "S12_BASE", scenario)

        contract = copy.deepcopy(assumptions)
        contract["security_mode"] = "contract"
        result_contract = compute_scenario(contract, "S12_BASE", scenario)

        self.assertAlmostEqual(
            result_in_house["totals"].get("security", 0),
            0,
            places=6,
            msg="In-house mode should zero out contract security cost",
        )
        self.assertGreater(
            result_contract["totals"].get("security", 0),
            0,
            "Contract mode should include security weekly cost",
        )
        self.assertLessEqual(
            result_contract["totals"].get("semi_fixed_labor_monthly", 0),
            result_in_house["totals"].get("semi_fixed_labor_monthly", 0),
            "Contract mode should not double-count security labor hours",
        )

    def test_membership_discount_cost_applies_to_revenue(self):
        assumptions = load_assumptions()
        scenarios = yaml.safe_load(
            (ROOT / "model" / "scenarios.yaml").read_text(encoding="utf-8-sig")
        )["scenarios"]
        scenario = copy.deepcopy(scenarios["S12_BASE"])
        scenario["programs_enabled"] = True

        revenue_programs = assumptions.setdefault("revenue", {}).setdefault("programs", {})
        membership_programs = revenue_programs.setdefault("memberships", {})
        top_memberships = assumptions.setdefault("memberships", {})

        membership_programs.update(
            {
                "active_members": 50,
                "monthly_fee": 25,
                "net_margin_pct": 0.85,
                "member_visits_per_month": 2.0,
                "discountable_sales_share": 0.60,
            }
        )
        top_memberships.update(
            {
                "target_member_count": 50,
                "monthly_fee": 25,
                "discount_pct": 0.0,
                "member_visits_per_month": 2.0,
                "discountable_sales_share": 0.60,
            }
        )

        membership_programs["discount_pct"] = 0.0
        result_no_discount = compute_scenario(assumptions, "S12_BASE", scenario)

        assumptions_with_discount = copy.deepcopy(assumptions)
        assumptions_with_discount["memberships"]["discount_pct"] = 0.10
        assumptions_with_discount["revenue"]["programs"]["memberships"]["discount_pct"] = 0.10
        result_with_discount = compute_scenario(
            assumptions_with_discount, "S12_BASE", scenario
        )

        self.assertGreater(
            result_with_discount["totals"].get("program_membership_discount_cost_monthly", 0),
            0,
            "Membership discount cost should be positive with discount pct",
        )
        self.assertLess(
            result_with_discount["totals"].get("total_revenue", 0),
            result_no_discount["totals"].get("total_revenue", 0),
            "Discount cost should reduce total revenue",
        )
        self.assertEqual(
            result_with_discount["revenue_drivers"].get("program_membership_discount_method"),
            "discount_pct_on_member_visits",
            "Discount method should use member visits model when inputs are present",
        )


if __name__ == "__main__":
    unittest.main()
