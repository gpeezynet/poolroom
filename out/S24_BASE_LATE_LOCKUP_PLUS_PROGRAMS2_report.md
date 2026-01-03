# ROI Report: S24_BASE_LATE_LOCKUP_PLUS_PROGRAMS2 - 24-table base late-night lockup + programs (drivers)

## Scenario Inputs
- Tables: 24
- Size: 15000 sf
- Pricing style: hourly
- Rent/CAM: $18.00/sf/yr, $4.00/sf/yr
- Estimated guests per month: 12710
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
- Bar attach + spend per guest: 70.0% @ $19
- Food attach + spend per guest: 35.0% @ $10
- Multipliers (utilization/spend): 1.05 / 1.03

## Monthly P&L
- Table revenue: $71,210
- Bar revenue (table-driven): $125,303
- Food revenue (table-driven): $34,806
- Bar-only bar revenue: $28,976
- Bar-only food revenue: $4,024
- Total monthly sales: $271,910

- Bar COGS: $30,856
- Food COGS: $11,649
- Labor: $59,820
- Rent: $24,000
- CAM: $5,333
- Property tax/insurance (NNN): $2,667
- Utilities: $5,700
- Insurance: $500
- Security: $0
- POS software: $180
- Payment processing: $6,852
- Music licensing: $204
- Marketing: $750
- HVAC service: $100
- HVAC filters: $100
- HVAC reserve: $167
- Maintenance reserve: $1,417
- Licenses & fees: $135
- Other opex (misc): $1,200
- Total expenses: $246,845

- Monthly net: $25,065
- Annual net: $300,783

## Programs (Non-table Revenue)
- Membership revenue + contribution: $3,750 / $3,188
- League revenue + contribution: $240 / $192
- Event revenue + contribution: $3,600 / $2,601
- Total programs contribution: $5,980
- Membership discount leakage (not applied): $1,500

## Programs Impact
- Program-driven table hours (monthly): 272.2
- Program-driven bar-only guests (monthly): 580
- Membership utilization uplift: 5.0%
- Membership spend uplift: 3.0%
- Program incremental labor cost (monthly): $1,505
- Program incremental security cost (monthly): $1,189
- Program net contribution (monthly): $3,287

## Fixed Cost Breakdown
- Occupancy (rent/CAM/NNN): $32,000
- Utilities total: $5,700
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
- Fixed costs total: $137,667

## CAPEX & Financing
- Total capex: $824,500
- Down payment (assumed): $164,900
- Loan amount (assumed): $650,000
- Implied equity: $174,500

## Debt & Coverage
- Monthly debt service: $9,326
- NOI (monthly): $23,456
- Cash flow after debt: $14,130
- DSCR: 2.52x (251.5%)

## What Must Be True (Targets)
- Cash gap (monthly): $14,130 (negative means shortfall)
- Required utilization multiplier (cash break-even): 0.91x
- Required additional sales (per day): $0
- Notes: n/a

## Sensitivity (Cash After Debt)
| Lever | Cash after debt (monthly) |
| --- | --- |
| Utilization +10% | $30,242 |
| Utilization -10% | $-1,982 |
| Spend +10% | $23,618 |
| Spend -10% | $4,643 |
| Fixed costs +10% | $363 |
| Fixed costs -10% | $27,897 |

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
- Payback period: 3.96 years

## Break-even Snapshots
- Monthly fixed costs: $137,667
- Gross margin (after variable costs): 59.3%
- Break-even sales (monthly): $232,326
- Break-even sales (per day, operating): $7,744
- Break-even sales (per day, after debt): $8,269

## Compliance Warnings
- Alcohol sales are prohibited from 02:00-10:00 and before Sunday noon.
- Late-night mode may require a special exception for midnight-2am alcohol service.
- Last call should be 01:30-01:45 to clear drinks by 02:00.
- Operating after 2am without alcohol is high risk; docs say 24-hour operation is not feasible.

## Notes
- Food COGS and other opex are placeholders; adjust in model/assumptions.yaml before decision-making.