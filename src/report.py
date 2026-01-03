from __future__ import annotations

from typing import Any, Dict


def _money(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"${value:,.0f}"


def _pct(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value * 100:.1f}%"


def _dscr(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value:.2f}x ({_pct(value)})"

def render_report(result: Dict[str, Any]) -> str:
    totals = result["totals"]
    drivers = result.get("revenue_drivers", {})
    lines = []
    lines.append(f"# ROI Report: {result['scenario_id']} - {result['scenario_name']}")
    lines.append("")

    lines.append("## Scenario Inputs")
    lines.append(f"- Tables: {result['tables']}")
    lines.append(f"- Size: {result['size_sf']:.0f} sf")
    lines.append(f"- Pricing style: {result['pricing_style']}")
    lines.append(
        f"- Rent/CAM: ${result['rent_per_sf']:.2f}/sf/yr, ${result['cam_per_sf']:.2f}/sf/yr"
    )
    lines.append(f"- Estimated guests per month: {result['total_guests']:.0f}")
    lines.append(
        "- Bar-only guests per day (weekday/weekend): "
        f"{drivers.get('bar_only_weekday_guests_per_day', 0):.0f} / "
        f"{drivers.get('bar_only_weekend_guests_per_day', 0):.0f}"
    )
    lines.append(
        "- Bar-only spend + food attach: "
        f"{_money(drivers.get('bar_only_bar_spend_per_guest'))} bar, "
        f"{_pct(drivers.get('bar_only_food_attach_rate'))} @ "
        f"{_money(drivers.get('bar_only_food_spend_per_guest'))} food"
    )
    if result.get("late_night"):
        lines.append(
            "- Late bar/food fractions: "
            f"{result.get('late_bar_fraction', 1.0):.2f} / "
            f"{result.get('late_food_fraction', 1.0):.2f}"
        )
    lines.append("")

    lines.append("## Revenue Drivers")
    lines.append(
        "- Table rates (offpeak/prime/late): "
        f"{_money(drivers.get('table_hourly_rate_offpeak'))}/hr, "
        f"{_money(drivers.get('table_hourly_rate_prime'))}/hr, "
        f"{_money(drivers.get('table_hourly_rate_late'))}/hr"
    )
    lines.append(
        "- Avg table hours sold per table (weekday/weekend): "
        f"{drivers.get('avg_table_hours_sold_per_table_weekday', 0):.2f} / "
        f"{drivers.get('avg_table_hours_sold_per_table_weekend', 0):.2f}"
    )
    lines.append(
        "- Avg guests per table hour: "
        f"{drivers.get('avg_guests_per_table_hour', 0):.2f}"
    )
    lines.append(
        "- Bar attach + spend per guest: "
        f"{_pct(drivers.get('bar_attach_rate'))} @ "
        f"{_money(drivers.get('avg_bar_spend_per_guest'))}"
    )
    lines.append(
        "- Food attach + spend per guest: "
        f"{_pct(drivers.get('food_attach_rate'))} @ "
        f"{_money(drivers.get('avg_food_spend_per_guest'))}"
    )
    lines.append(
        "- Multipliers (utilization/spend): "
        f"{drivers.get('utilization_multiplier', 1.0):.2f} / "
        f"{drivers.get('spend_multiplier', 1.0):.2f}"
    )
    lines.append("")

    lines.append("## Monthly P&L")
    lines.append(f"- Table revenue: {_money(totals['table_revenue'])}")
    lines.append(f"- Bar revenue (table-driven): {_money(totals['bar_revenue'])}")
    lines.append(f"- Food revenue (table-driven): {_money(totals['food_revenue'])}")
    lines.append(
        f"- Bar-only bar revenue: {_money(totals.get('bar_only_bar_sales_monthly'))}"
    )
    lines.append(
        f"- Bar-only food revenue: {_money(totals.get('bar_only_food_sales_monthly'))}"
    )
    lines.append(f"- Total monthly sales: {_money(totals['total_revenue'])}")
    lines.append("")
    lines.append(f"- Bar COGS: {_money(totals['bar_cogs'])}")
    lines.append(f"- Food COGS: {_money(totals['food_cogs'])}")
    lines.append(f"- Labor: {_money(totals['labor'])}")
    lines.append(f"- Rent: {_money(totals['rent'])}")
    lines.append(f"- CAM: {_money(totals['cam'])}")
    lines.append(f"- Property tax/insurance (NNN): {_money(totals.get('property_tax_insurance'))}")
    lines.append(f"- Utilities: {_money(totals['utilities'])}")
    lines.append(f"- Insurance: {_money(totals['insurance'])}")
    lines.append(f"- Security: {_money(totals['security'])}")
    lines.append(f"- POS software: {_money(totals.get('pos_software'))}")
    lines.append(f"- Payment processing: {_money(totals.get('processing_fees'))}")
    lines.append(f"- Music licensing: {_money(totals.get('music_licensing'))}")
    lines.append(f"- Marketing: {_money(totals.get('marketing'))}")
    lines.append(f"- HVAC service: {_money(totals.get('hvac_service'))}")
    lines.append(f"- HVAC filters: {_money(totals.get('hvac_filters'))}")
    lines.append(f"- HVAC reserve: {_money(totals.get('hvac_reserve'))}")
    lines.append(f"- Maintenance reserve: {_money(totals.get('maintenance_reserve'))}")
    lines.append(f"- Licenses & fees: {_money(totals.get('licenses_fees'))}")
    lines.append(f"- Other opex (misc): {_money(totals['other_opex'])}")
    lines.append(f"- Total expenses: {_money(totals['total_expenses'])}")
    lines.append("")
    lines.append(f"- Monthly net: {_money(totals['monthly_net'])}")
    lines.append(f"- Annual net: {_money(totals['annual_net'])}")
    lines.append("")

    lines.append("## Fixed Cost Breakdown")
    lines.append(f"- Occupancy (rent/CAM/NNN): {_money(totals.get('occupancy_cost_monthly'))}")
    lines.append(f"- Utilities total: {_money(totals.get('utilities_cost_monthly'))}")
    lines.append(f"- Insurance: {_money(totals.get('insurance'))}")
    lines.append(f"- Baseline labor (schedule): {_money(totals.get('semi_fixed_labor_monthly'))}")
    lines.append("- Variable labor: percent of sales (not in fixed costs)")
    lines.append(f"- Marketing: {_money(totals.get('marketing'))}")
    lines.append(f"- Music licensing: {_money(totals.get('music_licensing'))}")
    lines.append(f"- Security monitoring: {_money(totals.get('security'))}")
    lines.append(f"- POS software: {_money(totals.get('pos_software'))}")
    lines.append(f"- HVAC service: {_money(totals.get('hvac_service'))}")
    lines.append(f"- HVAC filters: {_money(totals.get('hvac_filters'))}")
    lines.append(f"- HVAC reserve: {_money(totals.get('hvac_reserve'))}")
    lines.append(f"- Maintenance reserve: {_money(totals.get('maintenance_reserve'))}")
    lines.append(f"- Licenses & fees: {_money(totals.get('licenses_fees'))}")
    lines.append(f"- Other opex (misc): {_money(totals.get('other_opex'))}")
    lines.append(f"- Fixed costs total: {_money(totals.get('monthly_fixed_costs'))}")
    lines.append("")

    lines.append("## CAPEX & Financing")
    lines.append(f"- Total capex: {_money(result.get('total_capex'))}")
    lines.append(f"- Down payment (assumed): {_money(result.get('down_payment_amount'))}")
    lines.append(f"- Loan amount (assumed): {_money(result.get('loan_principal'))}")
    lines.append(f"- Implied equity: {_money(result.get('implied_equity'))}")
    lines.append("")

    lines.append("## Debt & Coverage")
    lines.append(f"- Monthly debt service: {_money(totals.get('monthly_debt_service'))}")
    lines.append(f"- NOI (monthly): {_money(totals.get('noi'))}")
    lines.append(f"- Cash flow after debt: {_money(totals.get('cash_flow_after_debt'))}")
    lines.append(f"- DSCR: {_dscr(totals.get('dscr'))}")
    lines.append("")

    lines.append("## What Must Be True (Targets)")
    cash_gap = totals.get("cash_gap_monthly")
    required_util = totals.get("required_utilization_multiplier_for_cash_break_even")
    required_sales_day = totals.get("sales_gap_per_day_for_cash_break_even")
    lines.append(f"- Cash gap (monthly): {_money(cash_gap)} (negative means shortfall)")
    if required_util is None:
        lines.append("- Required utilization multiplier (cash break-even): n/a")
    else:
        lines.append(
            "- Required utilization multiplier (cash break-even): "
            f"{required_util:.2f}x"
        )
    lines.append(
        f"- Required additional sales (per day): {_money(required_sales_day)}"
    )
    notes = []
    if required_util is not None:
        if required_util > 2.00:
            notes.append("Required utilization > 2.00 (unlikely)")
        elif required_util > 1.50:
            notes.append("Required utilization > 1.50 (very aggressive)")
        elif required_util > 1.25:
            notes.append("Required utilization > 1.25 (aggressive)")
    lines.append(f"- Notes: {', '.join(notes) if notes else 'n/a'}")
    lines.append("")

    gross_profit_before_fixed = totals.get("gross_profit_before_fixed")
    fixed_costs = totals.get("monthly_fixed_costs")
    debt_service = totals.get("monthly_debt_service")
    cash_after_debt = totals.get("cash_flow_after_debt")
    gross_margin_rate = totals.get("gross_margin_rate") or 0.0
    bar_revenue = totals.get("bar_revenue") or 0.0
    food_revenue = totals.get("food_revenue") or 0.0

    def _cash_after_debt_with_util(factor: float) -> float | None:
        if gross_profit_before_fixed is None or fixed_costs is None or debt_service is None:
            return None
        return gross_profit_before_fixed * factor - fixed_costs - debt_service

    def _cash_after_debt_with_spend(factor: float) -> float | None:
        if cash_after_debt is None:
            return None
        delta_sales = (bar_revenue + food_revenue) * (factor - 1)
        return cash_after_debt + delta_sales * gross_margin_rate

    def _cash_after_debt_with_fixed(factor: float) -> float | None:
        if cash_after_debt is None or fixed_costs is None:
            return None
        return cash_after_debt - fixed_costs * (factor - 1)

    sensitivity_rows = [
        ("Utilization +10%", _cash_after_debt_with_util(1.10)),
        ("Utilization -10%", _cash_after_debt_with_util(0.90)),
        ("Spend +10%", _cash_after_debt_with_spend(1.10)),
        ("Spend -10%", _cash_after_debt_with_spend(0.90)),
        ("Fixed costs +10%", _cash_after_debt_with_fixed(1.10)),
        ("Fixed costs -10%", _cash_after_debt_with_fixed(0.90)),
    ]

    lines.append("## Sensitivity (Cash After Debt)")
    lines.append("| Lever | Cash after debt (monthly) |")
    lines.append("| --- | --- |")
    for label, value in sensitivity_rows:
        lines.append(f"| {label} | {_money(value)} |")
    lines.append("")

    if result.get("late_night"):
        late_incremental = result.get("late_incremental") or {}
        lines.append("## Late-Night Incremental (Bridge)")
        lines.append(
            f"- Incremental sales (monthly): {_money(late_incremental.get('sales_monthly'))}"
        )
        if (
            result.get("late_bar_fraction", 1.0) != 1.0
            or result.get("late_food_fraction", 1.0) != 1.0
        ):
            lines.append(
                "- Late bar/food fractions: "
                f"{result.get('late_bar_fraction', 1.0):.2f} / "
                f"{result.get('late_food_fraction', 1.0):.2f}"
            )
        lines.append(
            "- Incremental variable costs (monthly): "
            f"{_money(late_incremental.get('variable_costs_monthly'))}"
        )
        lines.append(
            "- Incremental gross profit (monthly): "
            f"{_money(late_incremental.get('gross_profit_monthly'))}"
        )
        lines.append(
            "- Incremental fixed costs (monthly): "
            f"{_money(late_incremental.get('fixed_costs_monthly'))}"
        )
        lines.append(
            f"- Incremental NOI (monthly): {_money(late_incremental.get('noi_monthly'))}"
        )
        lines.append(
            "- Incremental cash flow after debt (monthly): "
            f"{_money(late_incremental.get('cash_after_debt_monthly'))}"
        )
        lines.append(
            "- Break-even incremental sales (per day): "
            f"{_money(late_incremental.get('break_even_sales_per_day'))}"
        )
        worth_it = late_incremental.get("cash_after_debt_monthly")
        lines.append(f"- Late-night worth it?: {worth_it is not None and worth_it > 0}")
        lines.append("")

    lines.append("## ROI Metrics")
    lines.append(f"- Startup cost (likely): {_money(result['startup_cost'])}")
    lines.append(f"- Payback period: {result['payback_years']:.2f} years" if result["payback_years"] is not None else "- Payback period: n/a")
    lines.append("")

    breakeven_monthly = totals.get("breakeven_revenue")
    breakeven_daily = breakeven_monthly / 30 if breakeven_monthly is not None else None
    breakeven_after_debt = totals.get("breakeven_revenue_after_debt")
    breakeven_after_debt_daily = breakeven_after_debt / 30 if breakeven_after_debt is not None else None
    lines.append("## Break-even Snapshots")
    lines.append(f"- Monthly fixed costs: {_money(totals.get('fixed_costs'))}")
    lines.append(
        f"- Gross margin (after variable costs): {_pct(totals.get('gross_margin_pct'))}"
    )
    lines.append(f"- Break-even sales (monthly): {_money(breakeven_monthly)}")
    lines.append(f"- Break-even sales (per day, operating): {_money(breakeven_daily)}")
    lines.append(f"- Break-even sales (per day, after debt): {_money(breakeven_after_debt_daily)}")
    lines.append("")

    lines.append("## Compliance Warnings")
    for warning in result["warnings"]:
        lines.append(f"- {warning}")
    lines.append("")

    lines.append("## Notes")
    lines.append(
        "- Food COGS and other opex are placeholders; adjust in model/assumptions.yaml before decision-making."
    )
    if result["pricing_style"] == "wristband" and result["wristband_count_method"] == "core_only":
        lines.append(
            "- Wristband revenue is counted only in core hours to avoid double-counting late guests."
        )

    return "\n".join(lines)
