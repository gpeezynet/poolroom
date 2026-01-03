# ROI Report: S24_UPSIDE_LATE - 24-table upside late-night

## Scenario Inputs
- Tables: 24
- Size: 15000 sf
- Pricing style: hourly
- Rent/CAM: $18.00/sf/yr, $4.00/sf/yr
- Estimated guests per month: 12735
- Bar-only guests per day (weekday/weekend): 25 / 60
- Bar-only spend + food attach: $18 bar, 25.0% @ $10 food
- Late bar/food fractions: 1.00 / 1.00

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
- Multipliers (utilization/spend): 1.15 / 1.10

## Monthly P&L
- Table revenue: $72,474
- Bar revenue (table-driven): $180,747
- Food revenue (table-driven): $50,208
- Bar-only bar revenue: $23,929
- Bar-only food revenue: $3,324
- Total monthly sales: $330,681

- Bar COGS: $40,935
- Food COGS: $16,059
- Labor: $72,750
- Rent: $24,000
- CAM: $5,333
- Property tax/insurance (NNN): $2,667
- Utilities: $5,700
- Insurance: $500
- Security: $1,732
- POS software: $180
- Payment processing: $8,333
- Music licensing: $204
- Marketing: $750
- HVAC service: $100
- HVAC filters: $100
- HVAC reserve: $167
- Maintenance reserve: $1,417
- Licenses & fees: $135
- Other opex (misc): $1,200
- Total expenses: $274,784

- Monthly net: $55,898
- Annual net: $670,772

## Programs (Non-table Revenue)
- Membership revenue + contribution: $0 / $0
- League revenue + contribution: $0 / $0
- Event revenue + contribution: $0 / $0
- Total programs contribution: $0

## Fixed Cost Breakdown
- Occupancy (rent/CAM/NNN): $32,000
- Utilities total: $5,700
- Insurance: $500
- Baseline labor (schedule): $92,522
- Variable labor: percent of sales (not in fixed costs)
- Marketing: $750
- Music licensing: $204
- Security monitoring: $1,732
- POS software: $180
- HVAC service: $100
- HVAC filters: $100
- HVAC reserve: $167
- Maintenance reserve: $1,417
- Licenses & fees: $135
- Other opex (misc): $1,200
- Fixed costs total: $136,706

## CAPEX & Financing
- Total capex: $824,500
- Down payment (assumed): $164,900
- Loan amount (assumed): $650,000
- Implied equity: $174,500

## Debt & Coverage
- Monthly debt service: $9,326
- NOI (monthly): $55,898
- Cash flow after debt: $46,572
- DSCR: 5.99x (599.4%)

## What Must Be True (Targets)
- Cash gap (monthly): $46,572 (negative means shortfall)
- Required utilization multiplier (cash break-even): 0.76x
- Required additional sales (per day): $0
- Notes: n/a

## Sensitivity (Cash After Debt)
| Lever | Cash after debt (monthly) |
| --- | --- |
| Utilization +10% | $65,832 |
| Utilization -10% | $27,312 |
| Spend +10% | $60,024 |
| Spend -10% | $33,120 |
| Fixed costs +10% | $32,901 |
| Fixed costs -10% | $60,243 |

## Late-Night Incremental (Bridge)
- Incremental sales (monthly): $79,888
- Incremental variable costs (monthly): $32,786
- Incremental gross profit (monthly): $47,101
- Incremental fixed costs (monthly): $5,726
- Incremental NOI (monthly): $41,375
- Incremental cash flow after debt (monthly): $41,375
- Break-even incremental sales (per day): $324
- Late-night worth it?: True

## ROI Metrics
- Startup cost (likely): $1,190,000
- Payback period: 1.77 years

## Break-even Snapshots
- Monthly fixed costs: $136,706
- Gross margin (after variable costs): 58.2%
- Break-even sales (monthly): $234,711
- Break-even sales (per day, operating): $7,824
- Break-even sales (per day, after debt): $8,357

## Compliance Warnings
- Alcohol sales are prohibited from 02:00-10:00 and before Sunday noon.
- Late-night mode may require a special exception for midnight-2am alcohol service.
- Last call should be 01:30-01:45 to clear drinks by 02:00.
- Operating after 2am without alcohol is high risk; docs say 24-hour operation is not feasible.

## Notes
- Food COGS and other opex are placeholders; adjust in model/assumptions.yaml before decision-making.