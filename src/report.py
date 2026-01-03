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

    lines.append("## ROI Metrics")
    lines.append(f"- Startup cost (likely): {_money(result['startup_cost'])}")
    lines.append(f"- Payback period: {result['payback_years']:.2f} years" if result["payback_years"] is not None else "- Payback period: n/a")
    lines.append(
        f"- Break-even revenue (monthly): {_money(totals['breakeven_revenue'])}"
    )
    lines.append("")

    lines.append("## Compliance Warnings")
    for warning in result["warnings"]:
        lines.append(f"- {warning}")
    lines.append("")

    lines.append("## Notes")
    lines.append(
        "- Food revenue and other opex are placeholders; adjust in model/assumptions.yaml before decision-making."
    )
    if result["pricing_style"] == "wristband" and result["wristband_count_method"] == "core_only":
        lines.append(
            "- Wristband revenue is counted only in core hours to avoid double-counting late guests."
        )

    return "\n".join(lines)
