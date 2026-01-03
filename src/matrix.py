from __future__ import annotations

import csv
from pathlib import Path
from typing import Any, Dict, List


def _format_md(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, float):
        return f"{value:.2f}"
    return str(value)


def write_scenario_matrix(results: List[Dict[str, Any]], out_dir: Path) -> None:
    columns = [
        "scenario_id",
        "table_count",
        "is_late",
        "utilization_multiplier",
        "spend_multiplier",
        "program_uplift_utilization_multiplier",
        "program_uplift_spend_multiplier",
        "late_bar_fraction",
        "late_food_fraction",
        "monthly_sales",
        "monthly_fixed_costs",
        "monthly_noi",
        "cash_after_debt",
        "dscr",
        "break_even_sales_per_day",
        "gross_margin_rate",
        "cash_gap_monthly",
        "required_utilization_multiplier_for_cash_break_even",
        "sales_gap_per_day_for_cash_break_even",
        "bar_only_bar_sales_monthly",
        "bar_only_food_sales_monthly",
        "program_incremental_table_hours_sold_monthly",
        "program_incremental_bar_only_guests_monthly",
        "program_total_revenue_monthly",
        "program_total_contribution_monthly",
        "late_incremental_noi",
        "late_incremental_cash_after_debt",
    ]

    rows = []
    for result in results:
        totals = result.get("totals", {})
        drivers = result.get("revenue_drivers", {})
        late_incremental = result.get("late_incremental") or {}

        breakeven_revenue = totals.get("breakeven_revenue")
        breakeven_sales_per_day = (
            breakeven_revenue / 30 if breakeven_revenue is not None else None
        )

        row = {
            "scenario_id": result.get("scenario_id"),
            "table_count": result.get("tables"),
            "is_late": bool(result.get("late_night")),
            "utilization_multiplier": drivers.get("utilization_multiplier"),
            "spend_multiplier": drivers.get("spend_multiplier"),
            "program_uplift_utilization_multiplier": totals.get(
                "program_uplift_utilization_multiplier"
            ),
            "program_uplift_spend_multiplier": totals.get(
                "program_uplift_spend_multiplier"
            ),
            "late_bar_fraction": result.get("late_bar_fraction"),
            "late_food_fraction": result.get("late_food_fraction"),
            "monthly_sales": totals.get("total_revenue"),
            "monthly_fixed_costs": totals.get("monthly_fixed_costs"),
            "monthly_noi": totals.get("noi"),
            "cash_after_debt": totals.get("cash_flow_after_debt"),
            "dscr": totals.get("dscr"),
            "break_even_sales_per_day": breakeven_sales_per_day,
            "gross_margin_rate": totals.get("gross_margin_rate"),
            "cash_gap_monthly": totals.get("cash_gap_monthly"),
            "required_utilization_multiplier_for_cash_break_even": totals.get(
                "required_utilization_multiplier_for_cash_break_even"
            ),
            "sales_gap_per_day_for_cash_break_even": totals.get(
                "sales_gap_per_day_for_cash_break_even"
            ),
            "bar_only_bar_sales_monthly": totals.get("bar_only_bar_sales_monthly"),
            "bar_only_food_sales_monthly": totals.get("bar_only_food_sales_monthly"),
            "program_incremental_table_hours_sold_monthly": totals.get(
                "program_incremental_table_hours_sold_monthly"
            ),
            "program_incremental_bar_only_guests_monthly": totals.get(
                "program_incremental_bar_only_guests_monthly"
            ),
            "program_total_revenue_monthly": totals.get("program_total_revenue_monthly"),
            "program_total_contribution_monthly": totals.get(
                "program_total_contribution_monthly"
            ),
            "late_incremental_noi": late_incremental.get("noi_monthly"),
            "late_incremental_cash_after_debt": late_incremental.get(
                "cash_after_debt_monthly"
            ),
        }
        rows.append(row)

    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = out_dir / "SCENARIO_MATRIX.csv"
    md_path = out_dir / "SCENARIO_MATRIX.md"

    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    md_lines = []
    md_lines.append("| " + " | ".join(columns) + " |")
    md_lines.append("| " + " | ".join(["---"] * len(columns)) + " |")
    for row in rows:
        md_lines.append(
            "| " + " | ".join(_format_md(row.get(col)) for col in columns) + " |"
        )

    md_path.write_text("\n".join(md_lines) + "\n", encoding="utf-8")
