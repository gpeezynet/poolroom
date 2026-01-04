from __future__ import annotations

import csv
import copy
from pathlib import Path
from typing import Any, Dict, List

import yaml

from .model import compute_scenario


def load_yaml(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8-sig") as handle:
        return yaml.safe_load(handle)


def run_sensitivity(
    assumptions_path: Path,
    scenarios_path: Path,
    out_dir: Path,
    scenario_id: str,
) -> List[Dict[str, Any]]:
    assumptions = load_yaml(assumptions_path)
    scenarios = load_yaml(scenarios_path)["scenarios"]
    if scenario_id not in scenarios:
        raise SystemExit(f"Unknown scenario '{scenario_id}'.")
    scenario = scenarios[scenario_id]

    league_nights_options = [0, 1, 2, 3, 4, 5]
    events_per_month_options = [0, 2, 4, 6, 8]
    retention_uplift_options = [0.00, 0.03, 0.05, 0.07]
    active_members_options = [0, 50, 150, 300]
    discount_pct_options = [0.00, 0.05, 0.10, 0.15]

    rows: List[Dict[str, Any]] = []
    for league_nights in league_nights_options:
        for events_per_month in events_per_month_options:
            for retention_uplift in retention_uplift_options:
                for active_members in active_members_options:
                    for discount_pct in discount_pct_options:
                        sweep_assumptions = copy.deepcopy(assumptions)
                        program_drivers = sweep_assumptions.setdefault("program_drivers", {})
                        leagues = program_drivers.setdefault("leagues", {})
                        events = program_drivers.setdefault("events", {})
                        memberships = program_drivers.setdefault("memberships", {})

                        leagues["league_nights_per_week"] = league_nights
                        events["events_per_month"] = events_per_month
                        memberships["retention_utilization_uplift"] = retention_uplift

                        memberships = sweep_assumptions.setdefault("memberships", {})
                        memberships["target_member_count"] = active_members
                        memberships["discount_pct"] = discount_pct

                        revenue_programs = sweep_assumptions.setdefault("revenue", {}).setdefault(
                            "programs", {}
                        )
                        membership_programs = revenue_programs.setdefault("memberships", {})
                        membership_programs["active_members"] = active_members
                        membership_programs["discount_pct"] = discount_pct

                        result = compute_scenario(sweep_assumptions, scenario_id, scenario)
                        totals = result.get("totals", {})
                        rows.append(
                            {
                                "scenario_id": scenario_id,
                                "league_nights_per_week": league_nights,
                                "events_per_month": events_per_month,
                                "retention_utilization_uplift": retention_uplift,
                                "membership_active_members": active_members,
                                "membership_discount_pct": discount_pct,
                                "cash_after_debt": totals.get("cash_flow_after_debt"),
                                "dscr": totals.get("dscr"),
                                "required_utilization_multiplier_for_cash_break_even": totals.get(
                                    "required_utilization_multiplier_for_cash_break_even"
                                ),
                            }
                        )

    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = out_dir / "PROGRAM_SENSITIVITY.csv"
    md_path = out_dir / "PROGRAM_SENSITIVITY.md"

    fieldnames = [
        "scenario_id",
        "league_nights_per_week",
        "events_per_month",
        "retention_utilization_uplift",
        "membership_active_members",
        "membership_discount_pct",
        "cash_after_debt",
        "dscr",
        "required_utilization_multiplier_for_cash_break_even",
    ]

    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    def _fmt(value: Any) -> str:
        if value is None:
            return ""
        if isinstance(value, float):
            return f"{value:.2f}"
        return str(value)

    best_rows = sorted(
        rows,
        key=lambda r: (r["cash_after_debt"] if r["cash_after_debt"] is not None else -1e9),
        reverse=True,
    )[:10]

    md_lines = [
        "# Program Sensitivity Sweep",
        "",
        f"- Scenario: {scenario_id}",
        f"- Combos: {len(rows)}",
        "",
        "## Best Cash After Debt (Top 10)",
        "| league_nights_per_week | events_per_month | retention_utilization_uplift | membership_active_members | membership_discount_pct | cash_after_debt | dscr | required_utilization_multiplier_for_cash_break_even |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in best_rows:
        md_lines.append(
            "| "
            + " | ".join(
                _fmt(row.get(key))
                for key in (
                    "league_nights_per_week",
                    "events_per_month",
                    "retention_utilization_uplift",
                    "membership_active_members",
                    "membership_discount_pct",
                    "cash_after_debt",
                    "dscr",
                    "required_utilization_multiplier_for_cash_break_even",
                )
            )
            + " |"
        )

    md_path.write_text("\n".join(md_lines) + "\n", encoding="utf-8")
    return rows
