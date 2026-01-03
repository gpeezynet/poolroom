# ROI Report: S24_BASE_LATE - 24-table base late-night

## Scenario Inputs
- Tables: 24
- Size: 15000 sf
- Pricing style: hourly
- Rent/CAM: $18.00/sf/yr, $4.00/sf/yr
- Estimated guests per month: 11473
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
- Bar attach + spend per guest: 70.0% @ $18
- Food attach + spend per guest: 35.0% @ $10
- Multipliers (utilization/spend): 1.00 / 1.00

## Monthly P&L
- Table revenue: $65,677
- Bar revenue (table-driven): $148,406
- Food revenue (table-driven): $41,224
- Bar-only bar revenue: $23,929
- Bar-only food revenue: $3,324
- Total monthly sales: $282,561

- Bar COGS: $34,467
- Food COGS: $13,364
- Labor: $62,163
- Rent: $24,000
- CAM: $5,333
- Property tax/insurance (NNN): $2,667
- Utilities: $5,700
- Insurance: $500
- Security: $1,732
- POS software: $180
- Payment processing: $7,121
- Music licensing: $204
- Marketing: $750
- HVAC service: $100
- HVAC filters: $100
- HVAC reserve: $167
- Maintenance reserve: $1,417
- Licenses & fees: $135
- Other opex (misc): $1,200
- Total expenses: $253,821

- Monthly net: $28,739
- Annual net: $344,873

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
- NOI (monthly): $28,739
- Cash flow after debt: $19,414
- DSCR: 3.08x (308.2%)

## What Must Be True (Targets)
- Cash gap (monthly): $19,414 (negative means shortfall)
- Required utilization multiplier (cash break-even): 0.88x
- Required additional sales (per day): $0
- Notes: n/a

## Sensitivity (Cash After Debt)
| Lever | Cash after debt (monthly) |
| --- | --- |
| Utilization +10% | $35,958 |
| Utilization -10% | $2,869 |
| Spend +10% | $30,517 |
| Spend -10% | $8,311 |
| Fixed costs +10% | $5,743 |
| Fixed costs -10% | $33,084 |

## Late-Night Incremental (Bridge)
- Incremental sales (monthly): $74,477
- Incremental variable costs (monthly): $30,260
- Incremental gross profit (monthly): $44,217
- Incremental fixed costs (monthly): $5,726
- Incremental NOI (monthly): $38,491
- Incremental cash flow after debt (monthly): $38,491
- Break-even incremental sales (per day): $322
- Late-night worth it?: True

## ROI Metrics
- Startup cost (likely): $1,190,000
- Payback period: 3.45 years

## Break-even Snapshots
- Monthly fixed costs: $136,706
- Gross margin (after variable costs): 58.6%
- Break-even sales (monthly): $233,477
- Break-even sales (per day, operating): $7,783
- Break-even sales (per day, after debt): $8,313

## Compliance Warnings
- Alcohol sales are prohibited from 02:00-10:00 and before Sunday noon.
- Late-night mode may require a special exception for midnight-2am alcohol service.
- Last call should be 01:30-01:45 to clear drinks by 02:00.
- Operating after 2am without alcohol is high risk; docs say 24-hour operation is not feasible.

## Notes
- Food COGS and other opex are placeholders; adjust in model/assumptions.yaml before decision-making.