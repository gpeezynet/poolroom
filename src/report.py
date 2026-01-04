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

def _num(value: float | None, fmt: str = "{:.2f}") -> str:
    if value is None:
        return "n/a"
    return fmt.format(value)


def _dscr(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value:.2f}x ({_pct(value)})"

def render_report(
    result: Dict[str, Any],
    all_results: Dict[str, Dict[str, Any]] | None = None,
) -> str:
    totals = result["totals"]
    drivers = result.get("revenue_drivers", {})
    cash_after_debt_monthly = totals.get("cash_flow_after_debt")
    working_capital = totals.get("working_capital")
    weeks_per_month = drivers.get("weeks_per_month", 4.333)
    runway_display = "n/a"
    if cash_after_debt_monthly is not None and working_capital is not None:
        if cash_after_debt_monthly >= 0:
            runway_display = "n/a (cashflow positive)"
        else:
            runway = (
                working_capital / abs(cash_after_debt_monthly)
                if cash_after_debt_monthly
                else 0.0
            )
            runway_display = f"{runway:.1f}"
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
    lines.append(f"- Lease band: {drivers.get('lease_band', 'mid')}")
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

    legal_max_hours = drivers.get("legal_max_open_hours_per_day")
    modeled_open_hours = drivers.get("open_hours_per_day_modeled")
    lines.append("## Legal Hours Constraint")
    lines.append(
        f"- Legal max open hours/day: {legal_max_hours:.1f}" if legal_max_hours is not None else "- Legal max open hours/day: n/a"
    )
    lines.append(
        f"- Modeled open hours/day (capped): {modeled_open_hours:.1f}" if modeled_open_hours is not None else "- Modeled open hours/day (capped): n/a"
    )
    if result.get("late_night"):
        lines.append(
            "- Capped late extra hours/day: "
            f"{drivers.get('late_extra_hours_per_day_capped', 0):.1f}"
        )
        lines.append(
            "- Capped late extra hours/week: "
            f"{drivers.get('late_extra_hours_per_week_capped', 0):.1f}"
        )
    lines.append(
        "- NOTE: All-night operation is not modeled for alcohol venues; this model enforces legal max hours."
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

    if result.get("demand_method") == "week_reality":
        day_sales_by_dow = result.get("day_sales_by_dow") or {}
        day_types_by_dow = result.get("day_types_by_dow") or {}
        lines.append("## Weekly Reality Pattern")
        for key, label in (
            ("mon", "Mon"),
            ("tue", "Tue"),
            ("wed", "Wed"),
            ("thu", "Thu"),
            ("fri", "Fri"),
            ("sat", "Sat"),
            ("sun", "Sun"),
        ):
            day_type = day_types_by_dow.get(key, "n/a")
            lines.append(
                f"- {label} ({day_type}): {_money(day_sales_by_dow.get(key))}"
            )
        lines.append(
            "- Modeled day sales range: "
            f"{_money(result.get('day_sales_min'))} - {_money(result.get('day_sales_max'))}"
        )
        if result.get("capacity_violation"):
            lines.append(
                "- WARNING: Implied table hours exceed capacity by "
                f"{_num(result.get('capacity_overage_hours'), '{:.1f}')} hours/month"
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
    lines.append(f"- Labor (top-up): {_money(totals.get('variable_labor_monthly'))}")
    lines.append(
        f"- Labor (schedule baseline): {_money(totals.get('semi_fixed_labor_monthly'))}"
    )
    lines.append(f"- Labor (total): {_money(totals.get('labor_total_monthly'))}")
    lines.append(f"- Rent: {_money(totals['rent'])}")
    lines.append(f"- CAM: {_money(totals['cam'])}")
    lines.append(f"- Property tax/insurance (NNN): {_money(totals.get('property_tax_insurance'))}")
    lines.append(f"- Utilities: {_money(totals['utilities'])}")
    lines.append(
        f"- Total occupancy cost: {_money(totals.get('total_occupancy_cost_monthly'))}"
    )
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

    lines.append("## Programs (Non-table Revenue)")
    lines.append(
        "- Membership revenue + contribution: "
        f"{_money(totals.get('program_membership_revenue_monthly'))} / "
        f"{_money(totals.get('program_membership_contribution_monthly'))}"
    )
    membership_discount_pct = drivers.get("program_membership_discount_pct")
    membership_visits = drivers.get(
        "program_membership_member_visits_per_month",
        drivers.get("program_membership_visits_per_month"),
    )
    membership_discountable_share = drivers.get("program_membership_discountable_sales_share")
    membership_estimated_share = drivers.get("program_membership_estimated_share_of_guests")
    membership_discount_method = drivers.get("program_membership_discount_method", "none")
    lines.append(
        "- Membership discount cost (applied to revenue): "
        f"{_money(totals.get('program_membership_discount_cost_monthly'))} "
        f"(disc {_pct(membership_discount_pct)}, "
        f"visits/mo {_num(membership_visits)}, "
        f"discountable share {_pct(membership_discountable_share)}, "
        f"estimated share of guests {_pct(membership_estimated_share)}, "
        f"method {membership_discount_method})"
    )
    lines.append(
        "- Membership net after discounts: "
        f"{_money(totals.get('program_membership_net_after_discount_monthly'))}"
    )
    break_even_avg_sales = totals.get("program_membership_break_even_avg_sales_per_visit")
    if break_even_avg_sales is not None:
        lines.append(
            "- Membership discount break-even avg sales/visit: "
            f"{_money(break_even_avg_sales)}"
        )
    lines.append(
        "- League revenue + contribution: "
        f"{_money(totals.get('program_league_revenue_monthly'))} / "
        f"{_money(totals.get('program_league_contribution_monthly'))}"
    )
    lines.append(
        "- Event revenue + contribution: "
        f"{_money(totals.get('program_event_revenue_monthly'))} / "
        f"{_money(totals.get('program_event_contribution_monthly'))}"
    )
    lines.append(
        f"- Total programs contribution: {_money(totals.get('program_total_contribution_monthly'))}"
    )
    lines.append("")

    lines.append("## Programs Impact")
    lines.append(
        "- Program-driven table hours (monthly): "
        f"{totals.get('program_incremental_table_hours_sold_monthly', 0):.1f}"
    )
    lines.append(
        "- Program-driven bar-only guests (monthly): "
        f"{totals.get('program_incremental_bar_only_guests_monthly', 0):.0f}"
    )
    lines.append(
        "- Membership utilization uplift: "
        f"{_pct(drivers.get('program_uplift_utilization_multiplier', 0))}"
    )
    lines.append(
        "- Membership spend uplift: "
        f"{_pct(drivers.get('program_uplift_spend_multiplier', 0))}"
    )
    lines.append(
        "- Program incremental labor cost (monthly): "
        f"{_money(totals.get('program_incremental_labor_cost_monthly'))}"
    )
    lines.append(
        "- Program incremental security cost (monthly): "
        f"{_money(totals.get('program_incremental_security_cost_monthly'))}"
    )
    lines.append(
        "- Program net contribution (monthly): "
        f"{_money(totals.get('program_net_contribution_monthly'))}"
    )
    lines.append("")

    lines.append("## Fixed Cost Breakdown")
    lines.append(f"- Occupancy (rent/CAM/NNN): {_money(totals.get('occupancy_cost_monthly'))}")
    lines.append(f"- Utilities total: {_money(totals.get('utilities_cost_monthly'))}")
    lines.append(f"- Insurance: {_money(totals.get('insurance'))}")
    lines.append(f"- Baseline labor (schedule): {_money(totals.get('semi_fixed_labor_monthly'))}")
    lines.append("- Variable labor (top-up): max(0, labor_pct*sales - baseline labor)")
    lines.append("- Variable labor (monthly): "
                 f"{_money(totals.get('variable_labor_monthly'))}")
    lines.append("- Total labor (monthly): "
                 f"{_money(totals.get('labor_total_monthly'))}")
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

    lease_impact_rows = None
    if all_results:
        scenario_id = result.get("scenario_id", "")
        base_id = scenario_id
        for suffix in ("_GOOD_LEASE", "_BASE_LEASE", "_BAD_LEASE"):
            if scenario_id.endswith(suffix):
                base_id = scenario_id[: -len(suffix)]
                break
        base_key = f"{base_id}_BASE_LEASE"
        good_key = f"{base_id}_GOOD_LEASE"
        bad_key = f"{base_id}_BAD_LEASE"
        if base_key in all_results and (good_key in all_results or bad_key in all_results):
            lease_impact_rows = {
                "base": all_results.get(base_key),
                "good": all_results.get(good_key),
                "bad": all_results.get(bad_key),
            }

    if lease_impact_rows:
        def _dscr_short(value: float | None) -> str:
            if value is None:
                return "n/a"
            return f"{value:.2f}x"

        def _row(label: str, payload: Dict[str, Any]) -> str:
            totals_row = payload.get("totals", {})
            return (
                f"| {label} | {_money(totals_row.get('total_occupancy_cost_monthly'))} | "
                f"{_money(totals_row.get('cash_flow_after_debt'))} | "
                f"{_dscr_short(totals_row.get('dscr'))} |"
            )

        lines.append("## Lease Impact")
        lines.append("| lease_band | occupancy_cost | cash_after_debt | dscr |")
        lines.append("| --- | --- | --- | --- |")

        for label, key in (("GOOD", "good"), ("BASE", "base"), ("BAD", "bad")):
            row_result = lease_impact_rows.get(key)
            if row_result:
                lease_band = row_result.get("revenue_drivers", {}).get(
                    "lease_band", label.lower()
                )
                lines.append(_row(lease_band, row_result))

        base_totals = lease_impact_rows["base"]["totals"]
        for label, key in (("GOOD", "good"), ("BAD", "bad")):
            row_result = lease_impact_rows.get(key)
            if not row_result:
                continue
            totals_row = row_result.get("totals", {})
            base_occupancy = base_totals.get("total_occupancy_cost_monthly") or 0
            base_cash = base_totals.get("cash_flow_after_debt") or 0
            base_dscr = base_totals.get("dscr") or 0
            lines.append(
                f"| {label} delta vs BASE | "
                f"{_money((totals_row.get('total_occupancy_cost_monthly') or 0) - base_occupancy)} | "
                f"{_money((totals_row.get('cash_flow_after_debt') or 0) - base_cash)} | "
                f"{_dscr_short((totals_row.get('dscr') or 0) - base_dscr)} |"
            )

        rent_cam_util_rows = []
        for label, key in (("GOOD", "good"), ("BASE", "base"), ("BAD", "bad")):
            row_result = lease_impact_rows.get(key)
            if not row_result:
                continue
            totals_row = row_result.get("totals", {})
            rent_val = totals_row.get("rent_monthly")
            cam_val = totals_row.get("cam_monthly")
            util_val = totals_row.get("utilities_monthly")
            if rent_val is None and cam_val is None and util_val is None:
                continue
            lease_band = row_result.get("revenue_drivers", {}).get(
                "lease_band", label.lower()
            )
            rent_cam_util_rows.append(
                f"| {lease_band} | {_money(rent_val)} | {_money(cam_val)} | {_money(util_val)} |"
            )
        if rent_cam_util_rows:
            lines.append("")
            lines.append("| lease_band | rent | cam | utilities |")
            lines.append("| --- | --- | --- | --- |")
            lines.extend(rent_cam_util_rows)
        lines.append("")

    lines.append("## CAPEX & Financing")
    lines.append(f"- CAPEX total (incl. working capital): {_money(totals.get('capex_total'))}")
    lines.append(f"- Tenant improvement allowance: {_money(totals.get('ti_allowance'))}")
    lines.append(f"- Total project cost (net TI): {_money(totals.get('total_project_cost'))}")
    lines.append(f"- Equity required at close: {_money(totals.get('equity_required_at_close'))}")
    lines.append(f"- Loan amount (modeled): {_money(totals.get('loan_amount'))}")
    lines.append(
        "- Lease deposit (months / amount): "
        f"{totals.get('lease_deposit_months', 0):.1f} / "
        f"{_money(totals.get('lease_deposit_amount'))}"
    )
    lines.append(
        f"- Total cash required to open: {_money(totals.get('total_cash_required_to_open'))}"
    )
    lines.append(
        "- Working capital / runway months: "
        f"{_money(working_capital)} / {runway_display}"
    )
    lines.append("")

    lines.append("## Underwriting Summary")
    lines.append(f"- Total project cost: {_money(totals.get('total_project_cost'))}")
    lines.append(f"- Equity required: {_money(totals.get('equity_required_at_close'))}")
    lines.append(
        f"- Total cash required to open: {_money(totals.get('total_cash_required_to_open'))}"
    )
    lines.append(f"- Runway months: {runway_display}")
    lines.append("")

    lines.append("## Debt & Coverage")
    lines.append(f"- Monthly debt service: {_money(totals.get('monthly_debt_service'))}")
    lines.append(f"- NOI (monthly): {_money(totals.get('noi'))}")
    lines.append(f"- Cash flow after debt: {_money(totals.get('cash_flow_after_debt'))}")
    lines.append(f"- DSCR: {_dscr(totals.get('dscr'))}")
    lines.append("")

    if cash_after_debt_monthly is not None:
        lines.append("## Works Check")
        works = cash_after_debt_monthly >= 0
        lines.append(f"- Works? {'YES' if works else 'NO'}")
        per_week = None
        per_day = None
        if isinstance(weeks_per_month, (int, float)) and weeks_per_month > 0:
            per_week = abs(cash_after_debt_monthly) / weeks_per_month
            per_day = abs(cash_after_debt_monthly) / (weeks_per_month * 7)
        if works:
            lines.append(f"- Surplus per week: {_money(per_week)}")
            lines.append(f"- Surplus per day avg: {_money(per_day)}")
        else:
            lines.append(f"- Shortfall per week: {_money(per_week)}")
            lines.append(f"- Shortfall per day avg: {_money(per_day)}")
        lines.append("")

    lines.append("## What Must Be True (Targets)")
    required_util = totals.get("required_utilization_multiplier_for_cash_break_even")
    required_sales_day = totals.get("sales_gap_per_day_for_cash_break_even")
    lines.append(
        "- Cash after debt (monthly): "
        f"{_money(cash_after_debt_monthly)} (negative means shortfall)"
    )
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
