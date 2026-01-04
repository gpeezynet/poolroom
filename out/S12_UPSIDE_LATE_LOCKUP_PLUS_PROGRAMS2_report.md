# ROI Report: S12_UPSIDE_LATE_LOCKUP_PLUS_PROGRAMS2 - 12-table upside late-night lockup + programs (drivers)

## Scenario Inputs
- Tables: 12
- Size: 8000 sf
- Pricing style: hourly
- Rent/CAM: $18.50/sf/yr, $3.50/sf/yr
- Lease band: mid
- Estimated guests per month: 7018
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
- Table revenue: $39,173
- Bar revenue (table-driven): $78,380
- Food revenue (table-driven): $21,772
- Bar-only bar revenue: $28,976
- Bar-only food revenue: $4,024
- Total monthly sales: $179,556

- Bar COGS: $21,471
- Food COGS: $7,739
- Labor: $39,502
- Rent: $13,875
- CAM: $2,625
- Property tax/insurance (NNN): $1,500
- Utilities: $3,713
- Total occupancy cost: $18,000
- Insurance: $500
- Security: $0
- POS software: $180
- Payment processing: $4,525
- Music licensing: $204
- Marketing: $750
- HVAC service: $100
- HVAC filters: $100
- HVAC reserve: $167
- Maintenance reserve: $708
- Licenses & fees: $96
- Other opex (misc): $1,200
- Total expenses: $161,073

- Monthly net: $18,483
- Annual net: $221,797

## Programs (Non-table Revenue)
- Membership revenue + contribution: $3,750 / $3,188
- Membership discount cost (applied to revenue): $360 (disc 10.0%, visits/mo 2.00, discountable share 60.0%, estimated share of guests 3.5%, method discount_pct_on_member_visits)
- Membership net after discounts: $2,828
- Membership discount break-even avg sales/visit: $177
- League revenue + contribution: $240 / $192
- Event revenue + contribution: $3,600 / $2,601
- Total programs contribution: $5,980

## Programs Impact
- Program-driven table hours (monthly): 136.1
- Program-driven bar-only guests (monthly): 580
- Membership utilization uplift: 5.0%
- Membership spend uplift: 3.0%
- Program incremental labor cost (monthly): $1,505
- Program incremental security cost (monthly): $1,189
- Program net contribution (monthly): $2,928

## Fixed Cost Breakdown
- Occupancy (rent/CAM/NNN): $18,000
- Utilities total: $3,713
- Insurance: $500
- Baseline labor (schedule): $59,424
- Variable labor: percent of sales (not in fixed costs)
- Marketing: $750
- Music licensing: $204
- Security monitoring: $0
- POS software: $180
- HVAC service: $100
- HVAC filters: $100
- HVAC reserve: $167
- Maintenance reserve: $708
- Licenses & fees: $96
- Other opex (misc): $1,200
- Fixed costs total: $87,836

## CAPEX & Financing
- CAPEX total (incl. working capital): $620,000
- Tenant improvement allowance: $0
- Total project cost (net TI): $620,000
- Equity required at close: $124,000
- Loan amount (modeled): $496,000
- Lease deposit (months / amount): 1.0 / $18,000
- Total cash required to open: $142,000
- Working capital / runway months: $100,000 / 100000.0

## Underwriting Summary
- Total project cost: $620,000
- Equity required: $124,000
- Total cash required to open: $142,000
- Runway months: 100000.0

## Debt & Coverage
- Monthly debt service: $7,116
- NOI (monthly): $16,874
- Cash flow after debt: $9,757
- DSCR: 2.37x (237.1%)

## What Must Be True (Targets)
- Cash gap (monthly): $9,757 (negative means shortfall)
- Required utilization multiplier (cash break-even): 0.91x
- Required additional sales (per day): $0
- Notes: n/a

## Sensitivity (Cash After Debt)
| Lever | Cash after debt (monthly) |
| --- | --- |
| Utilization +10% | $20,228 |
| Utilization -10% | $-714 |
| Spend +10% | $15,598 |
| Spend -10% | $3,917 |
| Fixed costs +10% | $974 |
| Fixed costs -10% | $18,541 |

## Late-Night Incremental (Bridge)
- Incremental sales (monthly): $10,184
- Late bar/food fractions: 0.00 / 0.00
- Incremental variable costs (monthly): $2,497
- Incremental gross profit (monthly): $7,687
- Incremental fixed costs (monthly): $5,726
- Incremental NOI (monthly): $1,961
- Incremental cash flow after debt (monthly): $1,961
- Break-even incremental sales (per day): $253
- Late-night worth it?: True

## ROI Metrics
- Startup cost (likely): $620,000
- Payback period: 2.80 years

## Break-even Snapshots
- Monthly fixed costs: $87,836
- Gross margin (after variable costs): 58.3%
- Break-even sales (monthly): $150,622
- Break-even sales (per day, operating): $5,021
- Break-even sales (per day, after debt): $5,427

## Compliance Warnings
- Alcohol sales are prohibited from 02:00-10:00 and before Sunday noon.
- Late-night mode may require a special exception for midnight-2am alcohol service.
- Last call should be 01:30-01:45 to clear drinks by 02:00.
- Operating after 2am without alcohol is high risk; docs say 24-hour operation is not feasible.

## Notes
- Food COGS and other opex are placeholders; adjust in model/assumptions.yaml before decision-making.