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
    max_table_hours: float | None = None,
) -> Dict[str, float]:
    table_hours = tables * hours_per_table * days_per_month * utilization_multiplier
    if max_table_hours is not None:
        table_hours = min(table_hours, max_table_hours)
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

    def _time_to_hours(value: Any, path: str) -> float:
        if not isinstance(value, str):
            raise ValueError(f"Assumption {path} must be time string, got {value!r}")
        parts = value.split(":")
        if len(parts) != 2:
            raise ValueError(f"Assumption {path} must be HH:MM, got {value!r}")
        hours = int(parts[0])
        minutes = int(parts[1])
        return hours + minutes / 60

    modeling = assumptions["modeling"]
    weeks_per_month = float(modeling["weeks_per_month"])
    weekdays_per_week = float(modeling["weekdays_per_week"])
    weekend_days_per_week = float(modeling["weekend_days_per_week"])
    bar_only_weekdays_per_month = float(
        modeling.get("weekdays_per_month", weeks_per_month * weekdays_per_week)
    )
    bar_only_weekend_days_per_month = float(
        modeling.get("weekend_days_per_month", weeks_per_month * weekend_days_per_week)
    )
    labor_weeks_per_month = 4.333

    revenue = assumptions["revenue"]
    late_night = bool(scenario.get("late_night", False))
    legal = assumptions["legal_hours"]
    prohibited = legal["alcohol_sales_prohibited"]
    prohibited_start = _time_to_hours(
        prohibited["start"], "legal_hours.alcohol_sales_prohibited.start"
    )
    prohibited_end = _time_to_hours(
        prohibited["end"], "legal_hours.alcohol_sales_prohibited.end"
    )
    if prohibited_end <= prohibited_start:
        prohibited_hours = (24 - prohibited_start) + prohibited_end
    else:
        prohibited_hours = prohibited_end - prohibited_start
    legal_max_open_hours_per_day = max(24 - prohibited_hours, 0)
    legal_hours_enforced = bool(legal.get("no_alcohol_after_2am_enforced", False))

    pricing_windows = revenue["pricing_windows"]
    core_hours = float(pricing_windows["core_hours"])
    late_hours = float(pricing_windows["late_hours"])
    total_window_hours = core_hours + late_hours
    if total_window_hours <= 0:
        raise ValueError("pricing_windows core + late hours must be > 0")
    core_share = core_hours / total_window_hours
    late_share = late_hours / total_window_hours

    hours_assumptions = assumptions.get("hours", {})
    standard_open_hours_per_day = _num(
        hours_assumptions.get("standard_open_hours_per_day", 0),
        "hours.standard_open_hours_per_day",
    )
    late_extra_hours_per_day = _num(
        hours_assumptions.get("late_extra_hours_per_day", 0),
        "hours.late_extra_hours_per_day",
    )
    late_extra_hours_per_day_capped = late_extra_hours_per_day
    if legal_hours_enforced:
        max_late_extra_per_day = max(
            legal_max_open_hours_per_day - standard_open_hours_per_day, 0
        )
        late_extra_hours_per_day_capped = min(
            late_extra_hours_per_day, max_late_extra_per_day
        )
    open_hours_per_day = standard_open_hours_per_day + (
        late_extra_hours_per_day_capped if late_night else 0
    )
    if legal_hours_enforced:
        open_hours_per_day = min(open_hours_per_day, legal_max_open_hours_per_day)

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
    bar_only = revenue.get("bar_only_guests", {})
    bar_only_weekday_guests = _num(
        bar_only.get("weekday_guests_per_day", 0),
        "revenue.bar_only_guests.weekday_guests_per_day",
    )
    bar_only_weekend_guests = _num(
        bar_only.get("weekend_guests_per_day", 0),
        "revenue.bar_only_guests.weekend_guests_per_day",
    )
    bar_only_bar_spend = _num(
        bar_only.get("bar_spend_per_guest", 0),
        "revenue.bar_only_guests.bar_spend_per_guest",
    )
    bar_only_food_attach = _num(
        bar_only.get("food_attach_rate", 0),
        "revenue.bar_only_guests.food_attach_rate",
    )
    bar_only_food_spend = _num(
        bar_only.get("food_spend_per_guest", 0),
        "revenue.bar_only_guests.food_spend_per_guest",
    )

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
    modeled_days_per_month = weekday_days_per_month + weekend_days_per_month

    periods = []
    for day_type, days_per_month, hours_per_table_day, core_rate in (
        ("weekday", weekday_days_per_month, avg_hours_weekday, table_rate_offpeak),
        ("weekend", weekend_days_per_month, avg_hours_weekend, table_rate_prime),
    ):
        for period_name, share, rate in (
            ("core", core_share, core_rate),
            ("late", late_share, table_rate_late),
        ):
            cap_days = 0.0
            if modeled_days_per_month > 0:
                cap_days = 30.0 * (days_per_month / modeled_days_per_month)
            max_table_hours = tables * open_hours_per_day * cap_days * share
            metrics = _period_metrics(
                tables=tables,
                hours_per_table=hours_per_table_day * share,
                avg_guests_per_table_hour=avg_guests_per_table_hour,
                days_per_month=days_per_month,
                utilization_multiplier=utilization_multiplier,
                max_table_hours=max_table_hours,
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
    bar_only_guest_count = (
        bar_only_weekday_guests * bar_only_weekdays_per_month
        + bar_only_weekend_guests * bar_only_weekend_days_per_month
    )
    bar_only_bar_sales_monthly = bar_only_guest_count * bar_only_bar_spend
    bar_only_food_sales_monthly = (
        bar_only_guest_count * bar_only_food_attach * bar_only_food_spend
    )
    programs = revenue.get("programs", {})
    programs_enabled = bool(scenario.get("programs_enabled", False))
    program_membership_revenue_monthly = 0.0
    program_membership_contribution_monthly = 0.0
    program_membership_discount_leakage_monthly = 0.0
    program_league_revenue_monthly = 0.0
    program_league_contribution_monthly = 0.0
    program_event_revenue_monthly = 0.0
    program_event_contribution_monthly = 0.0
    if programs_enabled:
        memberships = programs.get("memberships", {})
        active_members = _num(
            memberships.get("active_members", 0),
            "revenue.programs.memberships.active_members",
        )
        membership_fee = _num(
            memberships.get("monthly_fee", 0),
            "revenue.programs.memberships.monthly_fee",
        )
        membership_net_margin = _num(
            memberships.get("net_margin_pct", 0),
            "revenue.programs.memberships.net_margin_pct",
        )
        membership_leakage_pct = _num(
            memberships.get("discount_leakage_pct", 0),
            "revenue.programs.memberships.discount_leakage_pct",
        )
        program_membership_revenue_monthly = active_members * membership_fee
        program_membership_contribution_monthly = (
            program_membership_revenue_monthly * membership_net_margin
        )
        program_membership_discount_leakage_monthly = (
            program_membership_revenue_monthly * membership_leakage_pct
        )

        leagues = programs.get("leagues", {})
        league_players = _num(
            leagues.get("active_league_players_per_month", 0),
            "revenue.programs.leagues.active_league_players_per_month",
        )
        league_fee = _num(
            leagues.get("league_fee_per_player", 0),
            "revenue.programs.leagues.league_fee_per_player",
        )
        league_net_margin = _num(
            leagues.get("net_margin_pct", 0),
            "revenue.programs.leagues.net_margin_pct",
        )
        program_league_revenue_monthly = league_players * league_fee
        program_league_contribution_monthly = (
            program_league_revenue_monthly * league_net_margin
        )

        events = programs.get("events", {})
        events_per_month = _num(
            events.get("events_per_month", 0),
            "revenue.programs.events.events_per_month",
        )
        avg_event_revenue = _num(
            events.get("avg_event_revenue", 0),
            "revenue.programs.events.avg_event_revenue",
        )
        event_variable_cost_pct = _num(
            events.get("variable_cost_pct", 0),
            "revenue.programs.events.variable_cost_pct",
        )
        event_net_margin = _num(
            events.get("net_margin_pct", 0),
            "revenue.programs.events.net_margin_pct",
        )
        program_event_revenue_monthly = events_per_month * avg_event_revenue
        event_variable_costs_monthly = (
            program_event_revenue_monthly * event_variable_cost_pct
        )
        program_event_contribution_monthly = (
            (program_event_revenue_monthly - event_variable_costs_monthly)
            * event_net_margin
        )

    program_total_revenue_monthly = (
        program_membership_revenue_monthly
        + program_league_revenue_monthly
        + program_event_revenue_monthly
    )
    program_total_contribution_monthly = (
        program_membership_contribution_monthly
        + program_league_contribution_monthly
        + program_event_contribution_monthly
    )
    program_variable_costs_monthly = (
        program_total_revenue_monthly - program_total_contribution_monthly
    )
    base_table_hours_total = sum(p["metrics"]["table_hours"] for p in periods)
    total_available_table_hours = tables * open_hours_per_day * 30

    late_settings = assumptions.get("late_night", {})
    late_bar_fraction = _num(
        scenario.get("late_bar_fraction", late_settings.get("late_bar_fraction", 1.0)),
        "late_night.late_bar_fraction",
    )
    late_food_fraction = _num(
        scenario.get("late_food_fraction", late_settings.get("late_food_fraction", 1.0)),
        "late_night.late_food_fraction",
    )
    late_incremental_table_revenue = 0.0
    late_incremental_bar_revenue = 0.0
    late_incremental_food_revenue = 0.0
    late_incremental_sales_monthly = 0.0
    late_incremental_guests = 0.0
    extra_hours_per_week_capped = 0.0
    if late_night:
        extra_hours_per_week = _num(
            late_settings.get("extra_hours_per_week", 0),
            "late_night.extra_hours_per_week",
        )
        extra_hours_per_week_capped = extra_hours_per_week
        if legal_hours_enforced:
            max_late_extra_per_day = max(
                legal_max_open_hours_per_day - standard_open_hours_per_day, 0
            )
            extra_hours_per_week_capped = min(
                extra_hours_per_week, max_late_extra_per_day * 7
            )
        utilization_multiplier_late = _num(
            late_settings.get("utilization_multiplier_late", 1),
            "late_night.utilization_multiplier_late",
        )
        spend_multiplier_late = _num(
            late_settings.get("spend_multiplier_late", 1),
            "late_night.spend_multiplier_late",
        )
        late_incremental_table_hours = (
            tables * extra_hours_per_week_capped * weeks_per_month * utilization_multiplier_late
        )
        remaining_table_hours = max(
            total_available_table_hours - base_table_hours_total, 0
        )
        late_incremental_table_hours = min(
            late_incremental_table_hours, remaining_table_hours
        )
        late_incremental_guests = late_incremental_table_hours * avg_guests_per_table_hour
        late_incremental_table_revenue = late_incremental_table_hours * table_rate_late
        late_incremental_bar_revenue = (
            late_incremental_guests
            * bar_attach_rate
            * avg_bar_spend
            * spend_multiplier_late
            * late_bar_fraction
        )
        late_incremental_food_revenue = (
            late_incremental_guests
            * food_attach_rate
            * avg_food_spend
            * spend_multiplier_late
            * late_food_fraction
        )
        late_incremental_sales_monthly = (
            late_incremental_table_revenue
            + late_incremental_bar_revenue
            + late_incremental_food_revenue
        )
        table_revenue += late_incremental_table_revenue
        bar_revenue += late_incremental_bar_revenue
        food_revenue += late_incremental_food_revenue
        total_guests += late_incremental_guests

    total_table_sales_monthly = table_revenue
    total_bar_sales_monthly = bar_revenue + bar_only_bar_sales_monthly
    total_food_sales_monthly = food_revenue + bar_only_food_sales_monthly
    total_revenue = (
        total_table_sales_monthly
        + total_bar_sales_monthly
        + total_food_sales_monthly
        + program_total_revenue_monthly
    )

    cogs = assumptions["cogs"]
    bar_cogs = total_bar_sales_monthly * float(cogs["bar_cogs_pct"]["blended_target"])
    food_cogs = total_food_sales_monthly * float(cogs["food_cogs_pct_placeholder"])

    labor_pct = float(assumptions["labor"]["target_pct_of_sales"]["default"])
    labor = total_revenue * labor_pct
    labor_assumptions = assumptions.get("labor", {})
    burden_pct = float(labor_assumptions.get("burden_pct", 0))
    rates = labor_assumptions.get("rates", {})
    s12_schedule = labor_assumptions.get("s12_schedule", {})
    s24_schedule = labor_assumptions.get("s24_schedule", {})

    def _schedule_hours(key: str) -> float:
        return _select_by_tables(
            tables,
            _num(s12_schedule.get(key, 0), f"labor.s12_schedule.{key}"),
            _num(s24_schedule.get(key, 0), f"labor.s24_schedule.{key}"),
        )

    def _rate(role: str) -> float:
        return _num(rates.get(role, 0), f"labor.rates.{role}")

    weekly_labor_cost = (
        _schedule_hours("manager_hours_per_week") * _rate("manager")
        + _schedule_hours("bartender_hours_per_week") * _rate("bartender")
        + _schedule_hours("barback_hours_per_week") * _rate("barback")
        + _schedule_hours("floor_hours_per_week") * _rate("floor")
        + _schedule_hours("kitchen_hours_per_week") * _rate("kitchen")
        + _schedule_hours("security_hours_per_week") * _rate("security")
        + _schedule_hours("cleaner_hours_per_week") * _rate("cleaner")
    )
    semi_fixed_labor_monthly = weekly_labor_cost * labor_weeks_per_month * (1 + burden_pct)
    late_incremental_labor_cost_monthly = 0.0
    if late_night:
        extra_security_hours = _num(
            late_settings.get("extra_security_hours_per_week", 0),
            "late_night.extra_security_hours_per_week",
        )
        extra_floor_hours = _num(
            late_settings.get("extra_floor_hours_per_week", 0),
            "late_night.extra_floor_hours_per_week",
        )
        extra_bartender_hours = _num(
            late_settings.get("extra_bartender_hours_per_week", 0),
            "late_night.extra_bartender_hours_per_week",
        )
        late_weekly_labor_cost = (
            extra_security_hours * _rate("security")
            + extra_floor_hours * _rate("floor")
            + extra_bartender_hours * _rate("bartender")
        )
        late_incremental_labor_cost_monthly = (
            late_weekly_labor_cost * labor_weeks_per_month * (1 + burden_pct)
        )
        semi_fixed_labor_monthly += late_incremental_labor_cost_monthly

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
        + semi_fixed_labor_monthly
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

    variable_costs = (
        total_cogs + labor + processing_fees + program_variable_costs_monthly
    )
    contribution_margin = total_revenue - variable_costs
    gross_profit_before_fixed = contribution_margin
    required_gross_profit = monthly_fixed_costs + monthly_debt_service
    required_utilization_multiplier_for_cash_break_even = None
    if gross_profit_before_fixed > 0:
        required_utilization_multiplier_for_cash_break_even = max(
            required_gross_profit / gross_profit_before_fixed, 0.0
        )
    noi = contribution_margin - monthly_fixed_costs
    dscr = None
    if annual_debt_service > 0:
        dscr = max((noi * 12) / annual_debt_service, 0)
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

    cash_gap_monthly = cash_flow_after_debt
    gross_margin_rate = gross_margin_pct if gross_margin_pct is not None else 0.0
    sales_gap_per_day_for_cash_break_even = (
        max(0.0, -cash_flow_after_debt) / max(gross_margin_rate, 0.01) / 30
    )

    late_incremental = None
    if late_night:
        late_incremental_variable_costs_monthly = 0.0
        late_incremental_gross_profit_monthly = None
        late_incremental_fixed_costs_monthly = late_incremental_labor_cost_monthly
        late_incremental_noi_monthly = None
        late_incremental_cash_after_debt_monthly = None
        late_incremental_debt_service_monthly = 0.0
        late_break_even_incremental_sales_per_day = None

        if late_incremental_sales_monthly > 0:
            late_incremental_bar_cogs = late_incremental_bar_revenue * float(
                cogs["bar_cogs_pct"]["blended_target"]
            )
            late_incremental_food_cogs = late_incremental_food_revenue * float(
                cogs["food_cogs_pct_placeholder"]
            )
            late_incremental_processing_fees = (
                late_incremental_sales_monthly * card_mix_pct * processing_pct
            )
            late_incremental_variable_labor = late_incremental_sales_monthly * labor_pct
            late_incremental_variable_costs_monthly = (
                late_incremental_bar_cogs
                + late_incremental_food_cogs
                + late_incremental_processing_fees
                + late_incremental_variable_labor
            )
            late_incremental_gross_profit_monthly = (
                late_incremental_sales_monthly - late_incremental_variable_costs_monthly
            )

        if late_incremental_gross_profit_monthly is not None:
            late_incremental_noi_monthly = (
                late_incremental_gross_profit_monthly - late_incremental_fixed_costs_monthly
            )
            late_incremental_cash_after_debt_monthly = (
                late_incremental_noi_monthly - late_incremental_debt_service_monthly
            )
            late_incremental_gross_margin_rate = None
            if late_incremental_sales_monthly > 0:
                late_incremental_gross_margin_rate = (
                    late_incremental_gross_profit_monthly / late_incremental_sales_monthly
                )
            if late_incremental_gross_margin_rate and late_incremental_gross_margin_rate > 0:
                late_break_even_incremental_sales_per_day = (
                    late_incremental_fixed_costs_monthly / late_incremental_gross_margin_rate / 30
                )

        late_incremental = {
            "sales_monthly": late_incremental_sales_monthly,
            "variable_costs_monthly": late_incremental_variable_costs_monthly,
            "gross_profit_monthly": late_incremental_gross_profit_monthly,
            "fixed_costs_monthly": late_incremental_fixed_costs_monthly,
            "noi_monthly": late_incremental_noi_monthly,
            "cash_after_debt_monthly": late_incremental_cash_after_debt_monthly,
            "break_even_sales_per_day": late_break_even_incremental_sales_per_day,
            "incremental_debt_service_monthly": late_incremental_debt_service_monthly,
            "table_sales_monthly": late_incremental_table_revenue,
            "bar_sales_monthly": late_incremental_bar_revenue,
            "food_sales_monthly": late_incremental_food_revenue,
            "extra_hours_per_week_capped": extra_hours_per_week_capped,
        }

    late_incremental_variable_costs_monthly = None
    late_incremental_gross_profit_monthly = None
    late_incremental_fixed_costs_monthly = None
    late_incremental_noi_monthly = None
    late_incremental_cash_after_debt_monthly = None
    late_incremental_break_even_sales_per_day = None
    late_incremental_debt_service_monthly = 0.0
    if late_incremental:
        late_incremental_variable_costs_monthly = late_incremental["variable_costs_monthly"]
        late_incremental_gross_profit_monthly = late_incremental["gross_profit_monthly"]
        late_incremental_fixed_costs_monthly = late_incremental["fixed_costs_monthly"]
        late_incremental_noi_monthly = late_incremental["noi_monthly"]
        late_incremental_cash_after_debt_monthly = late_incremental["cash_after_debt_monthly"]
        late_incremental_break_even_sales_per_day = late_incremental["break_even_sales_per_day"]
        late_incremental_debt_service_monthly = late_incremental["incremental_debt_service_monthly"]

    warnings = []
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
            "bar_only_bar_sales_monthly": bar_only_bar_sales_monthly,
            "bar_only_food_sales_monthly": bar_only_food_sales_monthly,
            "total_table_sales_monthly": total_table_sales_monthly,
            "total_bar_sales_monthly": total_bar_sales_monthly,
            "total_food_sales_monthly": total_food_sales_monthly,
            "program_membership_revenue_monthly": program_membership_revenue_monthly,
            "program_membership_contribution_monthly": program_membership_contribution_monthly,
            "program_league_revenue_monthly": program_league_revenue_monthly,
            "program_league_contribution_monthly": program_league_contribution_monthly,
            "program_event_revenue_monthly": program_event_revenue_monthly,
            "program_event_contribution_monthly": program_event_contribution_monthly,
            "program_total_revenue_monthly": program_total_revenue_monthly,
            "program_total_contribution_monthly": program_total_contribution_monthly,
            "total_revenue": total_revenue,
            "bar_cogs": bar_cogs,
            "food_cogs": food_cogs,
            "total_cogs": total_cogs,
            "monthly_variable_costs": variable_costs,
            "gross_profit_before_fixed": gross_profit_before_fixed,
            "labor": labor,
            "semi_fixed_labor_monthly": semi_fixed_labor_monthly,
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
            "gross_margin_rate": gross_margin_rate,
            "required_gross_profit": required_gross_profit,
            "required_utilization_multiplier_for_cash_break_even": required_utilization_multiplier_for_cash_break_even,
            "cash_gap_monthly": cash_gap_monthly,
            "sales_gap_per_day_for_cash_break_even": sales_gap_per_day_for_cash_break_even,
            "monthly_debt_service": monthly_debt_service,
            "annual_debt_service": annual_debt_service,
            "noi": noi,
            "cash_flow_after_debt": cash_flow_after_debt,
            "dscr": dscr,
            "late_incremental_sales_monthly": late_incremental_sales_monthly,
            "late_incremental_costs_monthly": late_incremental_fixed_costs_monthly,
            "late_incremental_noi_monthly": late_incremental_noi_monthly,
            "late_incremental_cashflow_after_debt_monthly": late_incremental_cash_after_debt_monthly,
            "late_break_even_incremental_sales_per_day": late_incremental_break_even_sales_per_day,
        },
        "total_capex": total_capex,
        "down_payment_amount": down_payment_amount,
        "loan_principal": loan_principal,
        "implied_equity": implied_equity,
        "late_night": late_night,
        "late_bar_fraction": late_bar_fraction,
        "late_food_fraction": late_food_fraction,
        "late_incremental": late_incremental,
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
            "bar_only_weekday_guests_per_day": bar_only_weekday_guests,
            "bar_only_weekend_guests_per_day": bar_only_weekend_guests,
            "bar_only_bar_spend_per_guest": bar_only_bar_spend,
            "bar_only_food_attach_rate": bar_only_food_attach,
            "bar_only_food_spend_per_guest": bar_only_food_spend,
            "bar_only_weekdays_per_month": bar_only_weekdays_per_month,
            "bar_only_weekend_days_per_month": bar_only_weekend_days_per_month,
            "open_hours_per_day_modeled": open_hours_per_day,
            "legal_max_open_hours_per_day": legal_max_open_hours_per_day,
            "standard_open_hours_per_day": standard_open_hours_per_day,
            "late_extra_hours_per_day_capped": late_extra_hours_per_day_capped,
            "late_extra_hours_per_week_capped": extra_hours_per_week_capped,
            "legal_hours_enforced": legal_hours_enforced,
            "programs_enabled": programs_enabled,
            "program_membership_active_members": programs.get("memberships", {}).get("active_members", 0),
            "program_membership_monthly_fee": programs.get("memberships", {}).get("monthly_fee", 0),
            "program_membership_discount_leakage_pct": programs.get("memberships", {}).get("discount_leakage_pct", 0),
            "program_membership_net_margin_pct": programs.get("memberships", {}).get("net_margin_pct", 0),
            "program_league_active_players": programs.get("leagues", {}).get("active_league_players_per_month", 0),
            "program_league_fee_per_player": programs.get("leagues", {}).get("league_fee_per_player", 0),
            "program_league_net_margin_pct": programs.get("leagues", {}).get("net_margin_pct", 0),
            "program_events_per_month": programs.get("events", {}).get("events_per_month", 0),
            "program_event_avg_revenue": programs.get("events", {}).get("avg_event_revenue", 0),
            "program_event_variable_cost_pct": programs.get("events", {}).get("variable_cost_pct", 0),
            "program_event_net_margin_pct": programs.get("events", {}).get("net_margin_pct", 0),
            "program_membership_discount_leakage_monthly": program_membership_discount_leakage_monthly,
        },
        "periods": periods,
        "warnings": warnings,
    }
