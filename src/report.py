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


def render_report(result: Dict[str, Any]) -> str:
    totals = result["totals"]
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
    lines.append("")

    drivers = result.get("revenue_drivers", {})
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
    lines.append(f"- Bar revenue: {_money(totals['bar_revenue'])}")
    lines.append(f"- Food revenue: {_money(totals['food_revenue'])}")
    lines.append(f"- Total revenue: {_money(totals['total_revenue'])}")
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
    lines.append("- Labor: variable (not included in fixed costs)")
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
    lines.append(f"- DSCR: {_pct(totals.get('dscr'))}")
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
