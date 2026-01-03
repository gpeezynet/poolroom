from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List


def pick_tier(mapping: Dict[str, Any], tier: str | None, default_key: str = "mid") -> float:
    if tier and tier in mapping and isinstance(mapping[tier], (int, float)):
        return float(mapping[tier])
    if default_key in mapping and isinstance(mapping[default_key], (int, float)):
        return float(mapping[default_key])
    for value in mapping.values():
        if isinstance(value, (int, float)):
            return float(value)
    raise ValueError("No numeric value found for tier selection")


def _period_metrics(
    tables: int,
    utilization: float,
    guests_per_table: float,
    hours: float,
) -> Dict[str, float]:
    active_tables = tables * utilization
    table_hours = active_tables * hours
    guests = active_tables * guests_per_table
    return {
        "active_tables": active_tables,
        "table_hours": table_hours,
        "guests": guests,
    }


def compute_scenario(
    assumptions: Dict[str, Any],
    scenario_id: str,
    scenario: Dict[str, Any],
) -> Dict[str, Any]:
    tables = int(scenario["tables"])
    size_sf = float(scenario["size_sf"]["default"])

    modeling = assumptions["modeling"]
    weeks_per_month = float(modeling["weeks_per_month"])
    weekdays_per_week = float(modeling["weekdays_per_week"])
    weekend_days_per_week = float(modeling["weekend_days_per_week"])

    revenue = assumptions["revenue"]
    utilization = revenue["utilization"]
    guests_per_active_table = revenue["guests_per_active_table"]
    pricing_windows = revenue["pricing_windows"]
    core_hours = float(pricing_windows["core_hours"])
    late_hours = float(pricing_windows["late_hours"])

    pricing_style = scenario.get(
        "pricing_style", modeling.get("table_pricing_style_default", "hourly")
    )
    table_pricing = revenue["table_pricing"]
    hourly_rate = float(table_pricing["hourly_rate_per_table"])
    wristband_price = float(table_pricing.get("per_person_wristband_high", 6))
    wristband_count_method = modeling.get("wristband_count_method", "core_only")

    avg_check = revenue["average_check"]

    weekday_days_per_month = weeks_per_month * weekdays_per_week
    weekend_days_per_month = weeks_per_month * weekend_days_per_week

    periods = []
    for day_type, days_per_month in (
        ("weekday", weekday_days_per_month),
        ("weekend", weekend_days_per_month),
    ):
        for period_name, hours in (("core", core_hours), ("late", late_hours)):
            util_key = f"{day_type}_{period_name}"
            metrics = _period_metrics(
                tables=tables,
                utilization=float(utilization[util_key]),
                guests_per_table=float(guests_per_active_table[util_key]),
                hours=hours,
            )

            if pricing_style == "hourly":
                table_revenue = metrics["table_hours"] * hourly_rate
            else:
                if wristband_count_method == "core_only" and period_name != "core":
                    table_revenue = 0.0
                else:
                    table_revenue = metrics["guests"] * wristband_price

            bar_revenue = metrics["guests"] * float(avg_check[period_name])

            periods.append(
                {
                    "day_type": day_type,
                    "period": period_name,
                    "days_per_month": days_per_month,
                    "metrics": metrics,
                    "table_revenue": table_revenue,
                    "bar_revenue": bar_revenue,
                }
            )

    table_revenue = sum(p["table_revenue"] * p["days_per_month"] for p in periods)
    bar_revenue = sum(p["bar_revenue"] * p["days_per_month"] for p in periods)
    total_guests = sum(p["metrics"]["guests"] * p["days_per_month"] for p in periods)

    food_pct = float(modeling["food_revenue_pct_of_bar_placeholder"])
    food_revenue = bar_revenue * food_pct

    total_revenue = table_revenue + bar_revenue + food_revenue

    cogs = assumptions["cogs"]
    bar_cogs = bar_revenue * float(cogs["bar_cogs_pct"]["blended_target"])
    food_cogs = food_revenue * float(cogs["food_cogs_pct_placeholder"])

    labor_pct = float(assumptions["labor"]["target_pct_of_sales"]["default"])
    labor = total_revenue * labor_pct

    rent_tier = scenario.get("rent_tier")
    cam_tier = scenario.get("cam_tier")
    rent_per_sf = pick_tier(assumptions["facility"]["rent_per_sf_yr"], rent_tier)
    cam_per_sf = pick_tier(assumptions["facility"]["cam_per_sf_yr"], cam_tier)

    rent = size_sf * rent_per_sf / 12
    cam = size_sf * cam_per_sf / 12

    utilities = float(assumptions["facility"]["utilities_per_month"]["mid"])

    insurance_per_year = float(
        assumptions["insurance"]["combined_policy_per_year"]["default"]
    )
    insurance = insurance_per_year / 12

    security_weekly = float(assumptions["security"]["weekly_cost_range"]["default"])
    security = security_weekly * weeks_per_month

    def _num(value: Any, path: str) -> float:
        if isinstance(value, (int, float)):
            return float(value)
        if isinstance(value, str):
            if value.strip().upper() == "PLACEHOLDER":
                raise ValueError(f"Assumption {path} is PLACEHOLDER")
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Assumption {path} must be numeric, got {value!r}")

    # POS & payment processing
    pos = assumptions.get("pos_stack", {})
    pos_software = _num(pos.get("monthly_software_fee", 0), "pos_stack.monthly_software_fee")
    card_mix_pct = float(pos.get("card_mix_pct", 0.9))
    processing_pct = _num(pos.get("payment_processing_pct", 0), "pos_stack.payment_processing_pct")
    processing_fees = total_revenue * card_mix_pct * processing_pct

    # Music licensing
    music_annual = _num(
        assumptions.get("music_licensing", {}).get("total_music_licenses_per_year", 0),
        "music_licensing.total_music_licenses_per_year",
    )
    music_licensing = music_annual / 12

    # Marketing
    marketing = _num(assumptions.get("marketing", {}).get("monthly_budget", 0), "marketing.monthly_budget")

    # HVAC maintenance (contract + filters + reserve)
    hvac = assumptions.get("facility", {}).get("hvac", {})
    hvac_service = _num(hvac.get("service_contract_per_year", 0), "facility.hvac.service_contract_per_year") / 12
    hvac_filters = _num(hvac.get("filter_replacement_per_month", 0), "facility.hvac.filter_replacement_per_month")
    hvac_reserve = _num(hvac.get("hvac_maintenance_reserve_per_year", 0), "facility.hvac.hvac_maintenance_reserve_per_year") / 12

    # Pool table + equipment maintenance reserve (scales between 12-table and 24-table budgets)
    maint = assumptions.get("maintenance", {})
    maint12 = _num(maint.get("annual_budget_12_tables", {}).get("total_high", 0), "maintenance.annual_budget_12_tables.total_high")
    maint24 = _num(maint.get("annual_budget_24_tables", {}).get("total_high", 0), "maintenance.annual_budget_24_tables.total_high")
    if tables <= 12:
        maintenance_reserve = maint12 / 12
    elif tables >= 24:
        maintenance_reserve = maint24 / 12
    else:
        t = (tables - 12) / (24 - 12)
        maintenance_reserve = (maint12 + (maint24 - maint12) * t) / 12

    # Annual licenses & fees (monthly equivalent)
    fees = assumptions.get("licenses_and_fees", {})
    annual_fees = 0.0
    annual_fees += _num(fees.get("abc_state_fee_per_year", 0), "licenses_and_fees.abc_state_fee_per_year")
    annual_fees += _num(fees.get("beer_license_per_year", 0), "licenses_and_fees.beer_license_per_year")
    annual_fees += _num(fees.get("wine_license_per_year", 0), "licenses_and_fees.wine_license_per_year")
    annual_fees += _num(fees.get("tobacco_license_per_year", 0), "licenses_and_fees.tobacco_license_per_year")
    annual_fees += _num(fees.get("soft_drink_license_fountain_per_year", 0), "licenses_and_fees.soft_drink_license_fountain_per_year")
    annual_fees += _num(fees.get("soft_drink_license_bottled_per_year", 0), "licenses_and_fees.soft_drink_license_bottled_per_year")
    annual_fees += _num(fees.get("pool_hall_bond_cost_per_year", 0), "licenses_and_fees.pool_hall_bond_cost_per_year")
    annual_fees += _num(fees.get("pool_table_license_per_table_per_year", 0), "licenses_and_fees.pool_table_license_per_table_per_year") * tables
    licenses_fees = annual_fees / 12

    other_opex = float(modeling["other_opex_per_month_placeholder"])

    total_cogs = bar_cogs + food_cogs
    fixed_costs = (
        rent
        + cam
        + utilities
        + insurance
        + security
        + pos_software
        + music_licensing
        + marketing
        + hvac_service
        + hvac_filters
        + hvac_reserve
        + maintenance_reserve
        + licenses_fees
        + other_opex
    )
    total_expenses = total_cogs + labor + processing_fees + fixed_costs


    monthly_net = total_revenue - total_expenses
    annual_net = monthly_net * 12

    startup_cost = float(scenario["startup_costs"]["likely"])
    payback_years = None
    payback_months = None
    if annual_net > 0:
        payback_years = startup_cost / annual_net
        payback_months = startup_cost / monthly_net if monthly_net > 0 else None

    variable_costs = total_cogs + labor + processing_fees
    breakeven_revenue = None
    if total_revenue > 0:
        variable_ratio = variable_costs / total_revenue
        if variable_ratio < 1:
            breakeven_revenue = fixed_costs / (1 - variable_ratio)

    warnings = []
    legal = assumptions["legal_hours"]
    warnings.append(
        "Alcohol sales are prohibited from 02:00-10:00 and before Sunday noon."
    )
    if scenario.get("late_night_mode") and legal.get("late_hours_permit_required"):
        warnings.append(
            "Late-night mode may require a special exception for midnight-2am alcohol service."
        )
    if scenario.get("late_night_mode"):
        warnings.append(
            "Last call should be 01:30-01:45 to clear drinks by 02:00."
        )
    if scenario.get("no_alcohol_after_2am_but_stay_open"):
        warnings.append(
            "Operating after 2am without alcohol is high risk; docs say 24-hour operation is not feasible."
        )

    return {
        "scenario_id": scenario_id,
        "scenario_name": scenario.get("name", scenario_id),
        "tables": tables,
        "size_sf": size_sf,
        "pricing_style": pricing_style,
        "wristband_count_method": wristband_count_method,
        "totals": {
            "table_revenue": table_revenue,
            "bar_revenue": bar_revenue,
            "food_revenue": food_revenue,
            "total_revenue": total_revenue,
            "bar_cogs": bar_cogs,
            "food_cogs": food_cogs,
            "total_cogs": total_cogs,
            "labor": labor,
            "rent": rent,
            "cam": cam,
            "utilities": utilities,
            "insurance": insurance,
            "security": security,
            "pos_software": pos_software,
            "processing_fees": processing_fees,
            "music_licensing": music_licensing,
            "marketing": marketing,
            "hvac_service": hvac_service,
            "hvac_filters": hvac_filters,
            "hvac_reserve": hvac_reserve,
            "maintenance_reserve": maintenance_reserve,
            "licenses_fees": licenses_fees,
            "other_opex": other_opex,
            "total_expenses": total_expenses,
            "monthly_net": monthly_net,
            "annual_net": annual_net,
            "breakeven_revenue": breakeven_revenue,
        },
        "startup_cost": startup_cost,
        "payback_years": payback_years,
        "payback_months": payback_months,
        "total_guests": total_guests,
        "rent_per_sf": rent_per_sf,
        "cam_per_sf": cam_per_sf,
        "assumptions_used": {
            "labor_pct": labor_pct,
            "bar_cogs_pct": float(cogs["bar_cogs_pct"]["blended_target"]),
            "food_cogs_pct_placeholder": float(cogs["food_cogs_pct_placeholder"]),
            "food_revenue_pct_placeholder": food_pct,
            "utilities_per_month": utilities,
        },
        "periods": periods,
        "warnings": warnings,
    }
