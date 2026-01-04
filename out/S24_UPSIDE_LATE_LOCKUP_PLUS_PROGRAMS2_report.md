# ROI Report: S24_UPSIDE_LATE_LOCKUP_PLUS_PROGRAMS2 - 24-table upside late-night lockup + programs (drivers)

## Scenario Inputs
- Tables: 24
- Size: 15000 sf
- Pricing style: hourly
- Rent/CAM: $18.50/sf/yr, $3.50/sf/yr
- Lease band: mid
- Estimated guests per month: 14036
- Bar-only guests per day (weekday/weekend): 25 / 60
- Bar-only spend + food attach: $18 bar, 25.0% @ $10 food
- Late bar/food fractions: 0.00 / 0.00

## Legal Hours Constraint
- Legal max open hours/day: 16.0
- Modeled open hours/day (capped): 16.0
- Capped late extra hours/day: 2.0
- Capped late extra hours/week: 14.0
- NOTE: All-night operation is not modeled for alcohol venues; this model enforces legal max hours.

## Revenue Drivers
- Table rates (offpeak/prime/late): $12/hr, $16/hr, $20/hr
- Avg table hours sold per table (weekday/weekend): 3.00 / 5.00
- Avg guests per table hour: 3.00
- Bar attach + spend per guest: 70.0% @ $20
- Food attach + spend per guest: 35.0% @ $11
- Multipliers (utilization/spend): 1.21 / 1.13

## Monthly P&L
- Table revenue: $78,346
- Bar revenue (table-driven): $156,760
- Food revenue (table-driven): $43,544
- Bar-only bar revenue: $28,976
- Bar-only food revenue: $4,024
- Total monthly sales: $318,882

- Bar COGS: $37,147
- Food COGS: $14,271
- Labor: $70,154
- Rent: $24,667
- CAM: $4,667
- Property tax/insurance (NNN): $2,667
- Utilities: $6,600
- Total occupancy cost: $32,000
- Insurance: $500
- Security: $0
- POS software: $180
- Payment processing: $8,036
- Music licensing: $204
- Marketing: $750
- HVAC service: $100
- HVAC filters: $100
- HVAC reserve: $167
- Maintenance reserve: $1,417
- Licenses & fees: $135
- Other opex (misc): $1,200
- Total expenses: $268,175

- Monthly net: $50,707
- Annual net: $608,486

## Programs (Non-table Revenue)
- Membership revenue + contribution: $3,750 / $3,188
- Membership discount cost (applied to revenue): $359 (disc 10.0%, visits/mo 2.00, discountable share 60.0%, estimated share of guests 1.9%, method discount_pct_on_member_visits)
- Membership net after discounts: $2,829
- Membership discount break-even avg sales/visit: $177
- League revenue + contribution: $240 / $192
- Event revenue + contribution: $3,600 / $2,601
- Total programs contribution: $5,980

## Programs Impact
- Program-driven table hours (monthly): 272.2
- Program-driven bar-only guests (monthly): 580
- Membership utilization uplift: 5.0%
- Membership spend uplift: 3.0%
- Program incremental labor cost (monthly): $1,505
- Program incremental security cost (monthly): $1,189
- Program net contribution (monthly): $2,929

## Fixed Cost Breakdown
- Occupancy (rent/CAM/NNN): $32,000
- Utilities total: $6,600
- Insurance: $500
- Baseline labor (schedule): $92,522
- Variable labor: percent of sales (not in fixed costs)
- Marketing: $750
- Music licensing: $204
- Security monitoring: $0
- POS software: $180
- HVAC service: $100
- HVAC filters: $100
- HVAC reserve: $167
- Maintenance reserve: $1,417
- Licenses & fees: $135
- Other opex (misc): $1,200
- Fixed costs total: $138,567

## CAPEX & Financing
- CAPEX total (incl. working capital): $1,190,000
- Tenant improvement allowance: $0
- Total project cost (net TI): $1,190,000
- Equity required at close: $540,000
- Loan amount (modeled): $650,000
- Lease deposit (months / amount): 1.0 / $32,000
- Total cash required to open: $572,000
- Working capital / runway months: $180,000 / 180000.0

## Underwriting Summary
- Total project cost: $1,190,000
- Equity required: $540,000
- Total cash required to open: $572,000
- Runway months: 180000.0

## Debt & Coverage
- Monthly debt service: $9,326
- NOI (monthly): $49,098
- Cash flow after debt: $39,772
- DSCR: 5.26x (526.5%)

## What Must Be True (Targets)
- Cash gap (monthly): $39,772 (negative means shortfall)
- Required utilization multiplier (cash break-even): 0.79x
- Required additional sales (per day): $0
- Notes: n/a

## Sensitivity (Cash After Debt)
| Lever | Cash after debt (monthly) |
| --- | --- |
| Utilization +10% | $58,539 |
| Utilization -10% | $21,006 |
| Spend +10% | $51,560 |
| Spend -10% | $27,984 |
| Fixed costs +10% | $25,915 |
| Fixed costs -10% | $53,629 |

## Late-Night Incremental (Bridge)
- Incremental sales (monthly): $20,368
- Late bar/food fractions: 0.00 / 0.00
- Incremental variable costs (monthly): $4,994
- Incremental gross profit (monthly): $15,374
- Incremental fixed costs (monthly): $5,726
- Incremental NOI (monthly): $9,648
- Incremental cash flow after debt (monthly): $9,648
- Break-even incremental sales (per day): $253
- Late-night worth it?: True

## ROI Metrics
- Startup cost (likely): $1,190,000
- Payback period: 1.96 years

## Break-even Snapshots
- Monthly fixed costs: $138,567
- Gross margin (after variable costs): 58.9%
- Break-even sales (monthly): $235,455
- Break-even sales (per day, operating): $7,849
- Break-even sales (per day, after debt): $8,377

## Compliance Warnings
- Alcohol sales are prohibited from 02:00-10:00 and before Sunday noon.
- Late-night mode may require a special exception for midnight-2am alcohol service.
- Last call should be 01:30-01:45 to clear drinks by 02:00.
- Operating after 2am without alcohol is high risk; docs say 24-hour operation is not feasible.

## Notes
- Food COGS and other opex are placeholders; adjust in model/assumptions.yaml before decision-making.