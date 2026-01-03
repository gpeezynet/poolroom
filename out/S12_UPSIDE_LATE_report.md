# ROI Report: S12_UPSIDE_LATE - 12-table upside late-night

## Scenario Inputs
- Tables: 12
- Size: 8000 sf
- Pricing style: hourly
- Rent/CAM: $18.00/sf/yr, $4.00/sf/yr
- Estimated guests per month: 6368
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
- Table revenue: $36,237
- Bar revenue (table-driven): $90,374
- Food revenue (table-driven): $25,104
- Bar-only bar revenue: $23,929
- Bar-only food revenue: $3,324
- Total monthly sales: $178,967

- Bar COGS: $22,861
- Food COGS: $8,528
- Labor: $39,373
- Rent: $13,500
- CAM: $3,000
- Property tax/insurance (NNN): $1,500
- Utilities: $3,400
- Insurance: $500
- Security: $1,732
- POS software: $180
- Payment processing: $4,510
- Music licensing: $204
- Marketing: $750
- HVAC service: $100
- HVAC filters: $100
- HVAC reserve: $167
- Maintenance reserve: $708
- Licenses & fees: $96
- Other opex (misc): $1,200
- Total expenses: $161,833

- Monthly net: $17,134
- Annual net: $205,603

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
- NOI (monthly): $17,134
- Cash flow after debt: $7,808
- DSCR: 1.84x (183.7%)

## What Must Be True (Targets)
- Cash gap (monthly): $7,808 (negative means shortfall)
- Required utilization multiplier (cash break-even): 0.92x
- Required additional sales (per day): $0
- Notes: n/a

## Sensitivity (Cash After Debt)
| Lever | Cash after debt (monthly) |
| --- | --- |
| Utilization +10% | $18,178 |
| Utilization -10% | $-2,562 |
| Spend +10% | $14,499 |
| Spend -10% | $1,117 |
| Fixed costs +10% | $-848 |
| Fixed costs -10% | $16,464 |

## Late-Night Incremental (Bridge)
- Incremental sales (monthly): $39,944
- Incremental variable costs (monthly): $16,393
- Incremental gross profit (monthly): $23,551
- Incremental fixed costs (monthly): $5,726
- Incremental NOI (monthly): $17,824
- Incremental cash flow after debt (monthly): $17,824
- Break-even incremental sales (per day): $324
- Late-night worth it?: True

## ROI Metrics
- Startup cost (likely): $620,000
- Payback period: 3.02 years

## Break-even Snapshots
- Monthly fixed costs: $86,562
- Gross margin (after variable costs): 57.9%
- Break-even sales (monthly): $149,396
- Break-even sales (per day, operating): $4,980
- Break-even sales (per day, after debt): $5,516

## Compliance Warnings
- Alcohol sales are prohibited from 02:00-10:00 and before Sunday noon.
- Late-night mode may require a special exception for midnight-2am alcohol service.
- Last call should be 01:30-01:45 to clear drinks by 02:00.
- Operating after 2am without alcohol is high risk; docs say 24-hour operation is not feasible.

## Notes
- Food COGS and other opex are placeholders; adjust in model/assumptions.yaml before decision-making.