# ROI Report: S12_CONSERVATIVE_LATE - 12-table conservative late-night

## Scenario Inputs
- Tables: 12
- Size: 8000 sf
- Pricing style: hourly
- Rent/CAM: $18.00/sf/yr, $4.00/sf/yr
- Estimated guests per month: 4895
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
- Bar attach + spend per guest: 70.0% @ $16
- Food attach + spend per guest: 35.0% @ $9
- Multipliers (utilization/spend): 0.80 / 0.90

## Monthly P&L
- Table revenue: $28,308
- Bar revenue (table-driven): $57,237
- Food revenue (table-driven): $15,899
- Bar-only bar revenue: $23,929
- Bar-only food revenue: $3,324
- Total monthly sales: $128,697

- Bar COGS: $16,233
- Food COGS: $5,767
- Labor: $28,313
- Rent: $13,500
- CAM: $3,000
- Property tax/insurance (NNN): $1,500
- Utilities: $3,400
- Insurance: $500
- Security: $1,732
- POS software: $180
- Payment processing: $3,243
- Music licensing: $204
- Marketing: $750
- HVAC service: $100
- HVAC filters: $100
- HVAC reserve: $167
- Maintenance reserve: $708
- Licenses & fees: $96
- Other opex (misc): $1,200
- Total expenses: $140,119

- Monthly net: $-11,421
- Annual net: $-137,057

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
- NOI (monthly): $-11,421
- Cash flow after debt: $-20,747
- DSCR: 0.00x (0.0%)

## What Must Be True (Targets)
- Cash gap (monthly): $-20,747 (negative means shortfall)
- Required utilization multiplier (cash break-even): 1.28x
- Required additional sales (per day): $1,184
- Notes: Required utilization > 1.25 (aggressive)

## Sensitivity (Cash After Debt)
| Lever | Cash after debt (monthly) |
| --- | --- |
| Utilization +10% | $-13,233 |
| Utilization -10% | $-28,261 |
| Spend +10% | $-16,477 |
| Spend -10% | $-25,017 |
| Fixed costs +10% | $-29,403 |
| Fixed costs -10% | $-12,091 |

## Late-Night Incremental (Bridge)
- Incremental sales (monthly): $34,533
- Incremental variable costs (monthly): $13,867
- Incremental gross profit (monthly): $20,666
- Incremental fixed costs (monthly): $5,726
- Incremental NOI (monthly): $14,940
- Incremental cash flow after debt (monthly): $14,940
- Break-even incremental sales (per day): $319
- Late-night worth it?: True

## ROI Metrics
- Startup cost (likely): $620,000
- Payback period: n/a

## Break-even Snapshots
- Monthly fixed costs: $86,562
- Gross margin (after variable costs): 58.4%
- Break-even sales (monthly): $148,259
- Break-even sales (per day, operating): $4,942
- Break-even sales (per day, after debt): $5,474

## Compliance Warnings
- Alcohol sales are prohibited from 02:00-10:00 and before Sunday noon.
- Late-night mode may require a special exception for midnight-2am alcohol service.
- Last call should be 01:30-01:45 to clear drinks by 02:00.
- Operating after 2am without alcohol is high risk; docs say 24-hour operation is not feasible.

## Notes
- Food COGS and other opex are placeholders; adjust in model/assumptions.yaml before decision-making.