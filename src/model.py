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


def _select_by_tables(tables: int, s12_value: float, s24_value: float) -> float:
    if tables <= 12:
        return float(s12_value)
    if tables >= 24:
        return float(s24_value)
    t = (tables - 12) / 12
    return float(s12_value + (s24_value - s12_value) * t)


def _period_metrics(
    tables: int,
    hours_per_table: float,
    avg_guests_per_table_hour: float,
    days_per_month: float,
    utilization_multiplier: float,
) -> Dict[str, float]:
    table_hours = tables * hours_per_table * days_per_month * utilization_multiplier
    guests = table_hours * avg_guests_per_table_hour
    return {
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

    modeling = assumptions["modeling"]
    weeks_per_month = float(modeling["weeks_per_month"])
    weekdays_per_week = float(modeling["weekdays_per_week"])
    weekend_days_per_week = float(modeling["weekend_days_per_week"])

    revenue = assumptions["revenue"]
    pricing_windows = revenue["pricing_windows"]
    core_hours = float(pricing_windows["core_hours"])
    late_hours = float(pricing_windows["late_hours"])
    total_window_hours = core_hours + late_hours
    if total_window_hours <= 0:
        raise ValueError("pricing_windows core + late hours must be > 0")
    core_share = core_hours / total_window_hours
    late_share = late_hours / total_window_hours

    table_rate_offpeak = float(revenue["table_hourly_rate_offpeak"])
    table_rate_prime = float(revenue["table_hourly_rate_prime"])
    table_rate_late = float(revenue["table_hourly_rate_late"])
    avg_hours_weekday = float(revenue["avg_table_hours_sold_per_table_weekday"])
    avg_hours_weekend = float(revenue["avg_table_hours_sold_per_table_weekend"])
    avg_guests_per_table_hour = float(revenue["avg_guests_per_table_hour"])

    bar_attach_rate = float(revenue["bar_attach_rate"])
    avg_bar_spend = float(revenue["avg_bar_spend_per_guest"])
    food_attach_rate = float(revenue["food_attach_rate"])
    avg_food_spend = float(revenue["avg_food_spend_per_guest"])

    pricing_style = scenario.get(
        "pricing_style", modeling.get("table_pricing_style_default", "hourly")
    )
    table_pricing = revenue["table_pricing"]
    wristband_price = float(table_pricing.get("per_person_wristband_high", 6))
    wristband_count_method = modeling.get("wristband_count_method", "core_only")

    utilization_multiplier = float(scenario.get("utilization_multiplier", 1.0))
    spend_multiplier = float(scenario.get("spend_multiplier", 1.0))
    avg_bar_spend *= spend_multiplier
    avg_food_spend *= spend_multiplier

    weekday_days_per_month = weeks_per_month * weekdays_per_week
    weekend_days_per_month = weeks_per_month * weekend_days_per_week

    periods = []
    for day_type, days_per_month, hours_per_table_day, core_rate in (
        ("weekday", weekday_days_per_month, avg_hours_weekday, table_rate_offpeak),
        ("weekend", weekend_days_per_month, avg_hours_weekend, table_rate_prime),
    ):
        for period_name, share, rate in (
            ("core", core_share, core_rate),
            ("late", late_share, table_rate_late),
        ):
            metrics = _period_metrics(
                tables=tables,
                hours_per_table=hours_per_table_day * share,
                avg_guests_per_table_hour=avg_guests_per_table_hour,
                days_per_month=days_per_month,
                utilization_multiplier=utilization_multiplier,
            )

            if pricing_style == "hourly":
                table_revenue = metrics["table_hours"] * rate
            else:
                guests_for_revenue = metrics["guests"]
                if wristband_count_method == "core_only" and period_name != "core":
                    guests_for_revenue = 0.0
                table_revenue = guests_for_revenue * wristband_price

            bar_revenue = metrics["guests"] * bar_attach_rate * avg_bar_spend
            food_revenue = metrics["guests"] * food_attach_rate * avg_food_spend

            periods.append(
                {
                    "day_type": day_type,
                    "period": period_name,
                    "metrics": metrics,
                    "table_revenue": table_revenue,
                    "bar_revenue": bar_revenue,
                    "food_revenue": food_revenue,
                }
            )

    table_revenue = sum(p["table_revenue"] for p in periods)
    bar_revenue = sum(p["bar_revenue"] for p in periods)
    food_revenue = sum(p["food_revenue"] for p in periods)
    total_guests = sum(p["metrics"]["guests"] for p in periods)

    total_revenue = table_revenue + bar_revenue + food_revenue

    cogs = assumptions["cogs"]
    bar_cogs = bar_revenue * float(cogs["bar_cogs_pct"]["blended_target"])
    food_cogs = food_revenue * float(cogs["food_cogs_pct_placeholder"])

    labor_pct = float(assumptions["labor"]["target_pct_of_sales"]["default"])
    labor = total_revenue * labor_pct

    site = assumptions.get("site", {})
    s12_sqft = _num(site.get("s12_sqft", size_sf), "site.s12_sqft")
    s24_sqft = _num(site.get("s24_sqft", size_sf), "site.s24_sqft")
    occupancy_sqft = _select_by_tables(tables, s12_sqft, s24_sqft)

    rent_tier = scenario.get("rent_tier")
    cam_tier = scenario.get("cam_tier")
    fallback_rent_per_sf = pick_tier(assumptions["facility"]["rent_per_sf_yr"], rent_tier)
    fallback_cam_per_sf = pick_tier(assumptions["facility"]["cam_per_sf_yr"], cam_tier)
    rent_per_sf = _num(
        site.get("rent_per_sqft_nnn_year", fallback_rent_per_sf),
        "site.rent_per_sqft_nnn_year",
    )
    cam_per_sf = _num(
        site.get("cam_per_sqft_year", fallback_cam_per_sf),
        "site.cam_per_sqft_year",
    )
    tax_insurance_per_sf = _num(
        site.get("property_tax_insurance_per_sqft_year", 0),
        "site.property_tax_insurance_per_sqft_year",
    )

    rent = occupancy_sqft * rent_per_sf / 12
    cam = occupancy_sqft * cam_per_sf / 12
    property_tax_insurance = occupancy_sqft * tax_insurance_per_sf / 12
    occupancy_cost_monthly = rent + cam + property_tax_insurance

    utilities = assumptions.get("utilities", {})
    electric = _select_by_tables(
        tables,
        _num(utilities.get("electric_per_month_s12", 0), "utilities.electric_per_month_s12"),
        _num(utilities.get("electric_per_month_s24", 0), "utilities.electric_per_month_s24"),
    )
    gas = _select_by_tables(
        tables,
        _num(utilities.get("gas_per_month_s12", 0), "utilities.gas_per_month_s12"),
        _num(utilities.get("gas_per_month_s24", 0), "utilities.gas_per_month_s24"),
    )
    water_sewer = _select_by_tables(
        tables,
        _num(utilities.get("water_sewer_per_month_s12", 0), "utilities.water_sewer_per_month_s12"),
        _num(utilities.get("water_sewer_per_month_s24", 0), "utilities.water_sewer_per_month_s24"),
    )
    trash = _select_by_tables(
        tables,
        _num(utilities.get("trash_per_month_s12", 0), "utilities.trash_per_month_s12"),
        _num(utilities.get("trash_per_month_s24", 0), "utilities.trash_per_month_s24"),
    )
    utilities_cost_monthly = electric + gas + water_sewer + trash

    insurance_per_year = float(
        assumptions["insurance"]["combined_policy_per_year"]["default"]
    )
    insurance = insurance_per_year / 12

    security_weekly = float(assumptions["security"]["weekly_cost_range"]["default"])
    security = security_weekly * weeks_per_month

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
        + property_tax_insurance
        + utilities_cost_monthly
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
    monthly_fixed_costs = fixed_costs
    total_expenses = total_cogs + labor + processing_fees + monthly_fixed_costs

    monthly_net = total_revenue - total_expenses
    annual_net = monthly_net * 12

    startup_cost = float(scenario["startup_costs"]["likely"])
    payback_years = None
    payback_months = None
    if annual_net > 0:
        payback_years = startup_cost / annual_net
        payback_months = startup_cost / monthly_net if monthly_net > 0 else None

    capex = assumptions.get("capex", {})
    s12_buildout = _num(capex.get("s12_buildout", 0), "capex.s12_buildout")
    s24_buildout = _num(capex.get("s24_buildout", 0), "capex.s24_buildout")
    s12_tables_and_lights = _num(capex.get("s12_tables_and_lights", 0), "capex.s12_tables_and_lights")
    s24_tables_and_lights = _num(capex.get("s24_tables_and_lights", 0), "capex.s24_tables_and_lights")
    s12_bar_and_ff_e = _num(capex.get("s12_bar_and_ff_e", 0), "capex.s12_bar_and_ff_e")
    s24_bar_and_ff_e = _num(capex.get("s24_bar_and_ff_e", 0), "capex.s24_bar_and_ff_e")
    s12_kitchen_lite = _num(capex.get("s12_kitchen_lite", 0), "capex.s12_kitchen_lite")
    s24_kitchen_lite = _num(capex.get("s24_kitchen_lite", 0), "capex.s24_kitchen_lite")
    s12_soft_cost_pct = _num(capex.get("s12_soft_cost_pct", 0), "capex.s12_soft_cost_pct")
    s24_soft_cost_pct = _num(capex.get("s24_soft_cost_pct", 0), "capex.s24_soft_cost_pct")
    working_capital = _num(capex.get("opening_working_capital", 0), "capex.opening_working_capital")

    buildout = _select_by_tables(tables, s12_buildout, s24_buildout)
    tables_and_lights = _select_by_tables(tables, s12_tables_and_lights, s24_tables_and_lights)
    bar_and_ff_e = _select_by_tables(tables, s12_bar_and_ff_e, s24_bar_and_ff_e)
    kitchen_lite = _select_by_tables(tables, s12_kitchen_lite, s24_kitchen_lite)
    soft_cost_pct = _select_by_tables(tables, s12_soft_cost_pct, s24_soft_cost_pct)
    hard_costs = buildout + tables_and_lights + bar_and_ff_e + kitchen_lite
    soft_costs = hard_costs * soft_cost_pct
    total_capex = hard_costs + soft_costs + working_capital

    financing = assumptions.get("financing", {})
    loan_amount = _num(financing.get("loan_amount", 0), "financing.loan_amount")
    interest_rate = _num(financing.get("interest_rate", 0), "financing.interest_rate")
    term_years = _num(financing.get("term_years", 0), "financing.term_years")
    down_payment_pct = _num(financing.get("down_payment_pct", 0), "financing.down_payment_pct")

    down_payment_amount = total_capex * down_payment_pct
    loan_principal = loan_amount if loan_amount > 0 else max(total_capex - down_payment_amount, 0)
    implied_equity = total_capex - loan_principal

    monthly_debt_service = 0.0
    annual_debt_service = 0.0
    if loan_principal > 0 and term_years > 0:
        months = int(term_years * 12)
        if interest_rate <= 0:
            monthly_debt_service = loan_principal / months
        else:
            rate = interest_rate / 12
            monthly_debt_service = loan_principal * rate * (1 + rate) ** months / ((1 + rate) ** months - 1)
        annual_debt_service = monthly_debt_service * 12

    variable_costs = total_cogs + labor + processing_fees
    contribution_margin = total_revenue - variable_costs
    noi = contribution_margin - monthly_fixed_costs
    dscr = None
    if annual_debt_service > 0:
        dscr = (noi * 12) / annual_debt_service
    cash_flow_after_debt = noi - monthly_debt_service

    breakeven_revenue = None
    breakeven_revenue_after_debt = None
    gross_margin_pct = None
    if total_revenue > 0:
        variable_ratio = variable_costs / total_revenue
        gross_margin_pct = 1 - variable_ratio
        if variable_ratio < 1:
            breakeven_revenue = monthly_fixed_costs / (1 - variable_ratio)
            if monthly_debt_service > 0:
                breakeven_revenue_after_debt = (monthly_fixed_costs + monthly_debt_service) / (1 - variable_ratio)

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
            "property_tax_insurance": property_tax_insurance,
            "occupancy_cost_monthly": occupancy_cost_monthly,
            "utilities": utilities_cost_monthly,
            "utilities_cost_monthly": utilities_cost_monthly,
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
            "fixed_costs": monthly_fixed_costs,
            "monthly_fixed_costs": monthly_fixed_costs,
            "total_expenses": total_expenses,
            "monthly_net": monthly_net,
            "annual_net": annual_net,
            "breakeven_revenue": breakeven_revenue,
            "breakeven_revenue_after_debt": breakeven_revenue_after_debt,
            "gross_margin_pct": gross_margin_pct,
            "monthly_debt_service": monthly_debt_service,
            "annual_debt_service": annual_debt_service,
            "noi": noi,
            "cash_flow_after_debt": cash_flow_after_debt,
            "dscr": dscr,
        },
        "total_capex": total_capex,
        "down_payment_amount": down_payment_amount,
        "loan_principal": loan_principal,
        "implied_equity": implied_equity,
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
            "utilities_per_month": utilities_cost_monthly,
            "bar_attach_rate": bar_attach_rate,
            "food_attach_rate": food_attach_rate,
        },
        "revenue_drivers": {
            "table_hourly_rate_offpeak": table_rate_offpeak,
            "table_hourly_rate_prime": table_rate_prime,
            "table_hourly_rate_late": table_rate_late,
            "avg_table_hours_sold_per_table_weekday": avg_hours_weekday,
            "avg_table_hours_sold_per_table_weekend": avg_hours_weekend,
            "avg_guests_per_table_hour": avg_guests_per_table_hour,
            "bar_attach_rate": bar_attach_rate,
            "avg_bar_spend_per_guest": avg_bar_spend,
            "food_attach_rate": food_attach_rate,
            "avg_food_spend_per_guest": avg_food_spend,
            "utilization_multiplier": utilization_multiplier,
            "spend_multiplier": spend_multiplier,
        },
        "periods": periods,
        "warnings": warnings,
    }
