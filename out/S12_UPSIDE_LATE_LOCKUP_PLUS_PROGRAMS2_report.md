# ROI Report: S12_UPSIDE_LATE_LOCKUP_PLUS_PROGRAMS2 - 12-table upside late-night lockup + programs (drivers)

## Scenario Inputs
- Tables: 12
- Size: 8000 sf
- Pricing style: hourly
- Rent/CAM: $18.00/sf/yr, $4.00/sf/yr
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
- Total monthly sales: $179,916

- Bar COGS: $21,471
- Food COGS: $7,739
- Labor: $39,582
- Rent: $13,500
- CAM: $3,000
- Property tax/insurance (NNN): $1,500
- Utilities: $3,400
- Insurance: $500
- Security: $1,732
- POS software: $180
- Payment processing: $4,534
- Music licensing: $204
- Marketing: $750
- HVAC service: $100
- HVAC filters: $100
- HVAC reserve: $167
- Maintenance reserve: $708
- Licenses & fees: $96
- Other opex (misc): $1,200
- Total expenses: $159,888

- Monthly net: $20,028
- Annual net: $240,340

## Programs (Non-table Revenue)
- Membership revenue + contribution: $3,750 / $3,188
- League revenue + contribution: $240 / $192
- Event revenue + contribution: $3,600 / $2,601
- Total programs contribution: $5,980
- Membership discount leakage (not applied): $1,500

## Programs Impact
- Program-driven table hours (monthly): 136.1
- Program-driven bar-only guests (monthly): 580
- Membership utilization uplift: 5.0%
- Membership spend uplift: 3.0%

## Fixed Cost Breakdown
- Occupancy (rent/CAM/NNN): $18,000
- Utilities total: $3,400
- Insurance: $500
- Baseline labor (schedule): $59,424
- Variable labor: percent of sales (not in fixed costs)
- Marketing: $750
- Music licensing: $204
- Security monitoring: $1,732
- POS software: $180
- HVAC service: $100
- HVAC filters: $100
- HVAC reserve: $167
- Maintenance reserve: $708
- Licenses & fees: $96
- Other opex (misc): $1,200
- Fixed costs total: $86,562

## CAPEX & Financing
- Total capex: $522,000
- Down payment (assumed): $104,400
- Loan amount (assumed): $650,000
- Implied equity: $-128,000

## Debt & Coverage
- Monthly debt service: $9,326
- NOI (monthly): $18,419
- Cash flow after debt: $9,093
- DSCR: 1.98x (197.5%)

## What Must Be True (Targets)
- Cash gap (monthly): $9,093 (negative means shortfall)
- Required utilization multiplier (cash break-even): 0.91x
- Required additional sales (per day): $0
- Notes: n/a

## Sensitivity (Cash After Debt)
| Lever | Cash after debt (monthly) |
| --- | --- |
| Utilization +10% | $19,591 |
| Utilization -10% | $-1,405 |
| Spend +10% | $14,937 |
| Spend -10% | $3,249 |
| Fixed costs +10% | $437 |
| Fixed costs -10% | $17,749 |

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
- Payback period: 2.58 years

## Break-even Snapshots
- Monthly fixed costs: $86,562
- Gross margin (after variable costs): 58.3%
- Break-even sales (monthly): $148,350
- Break-even sales (per day, operating): $4,945
- Break-even sales (per day, after debt): $5,478

## Compliance Warnings
- Alcohol sales are prohibited from 02:00-10:00 and before Sunday noon.
- Late-night mode may require a special exception for midnight-2am alcohol service.
- Last call should be 01:30-01:45 to clear drinks by 02:00.
- Operating after 2am without alcohol is high risk; docs say 24-hour operation is not feasible.

## Notes
- Food COGS and other opex are placeholders; adjust in model/assumptions.yaml before decision-making.