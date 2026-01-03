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
- Bar-only bar revenue: $18,540
- Bar-only food revenue: $2,575
- Total monthly sales: $122,560

- Bar COGS: $15,155
- Food COGS: $5,542
- Labor: $26,963
- Rent: $13,500
- CAM: $3,000
- Property tax/insurance (NNN): $1,500
- Utilities: $3,400
- Insurance: $500
- Security: $0
- POS software: $180
- Payment processing: $3,089
- Music licensing: $204
- Marketing: $750
- HVAC service: $100
- HVAC filters: $100
- HVAC reserve: $167
- Maintenance reserve: $708
- Licenses & fees: $96
- Other opex (misc): $1,200
- Total expenses: $135,579

- Monthly net: $-13,020
- Annual net: $-156,237

## Programs (Non-table Revenue)
- Membership revenue + contribution: $0 / $0
- League revenue + contribution: $0 / $0
- Event revenue + contribution: $0 / $0
- Total programs contribution: $0
- Membership discount leakage (not applied): $0

## Programs Impact
- Program-driven table hours (monthly): 0.0
- Program-driven bar-only guests (monthly): 0
- Membership utilization uplift: 0.0%
- Membership spend uplift: 0.0%
- Program incremental labor cost (monthly): $0
- Program incremental security cost (monthly): $0
- Program net contribution (monthly): $0

## Fixed Cost Breakdown
- Occupancy (rent/CAM/NNN): $18,000
- Utilities total: $3,400
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
- Fixed costs total: $84,830

## CAPEX & Financing
- Total capex: $522,000
- Down payment (assumed): $104,400
- Loan amount (assumed): $650,000
- Implied equity: $-128,000

## Debt & Coverage
- Monthly debt service: $9,326
- NOI (monthly): $-13,020
- Cash flow after debt: $-22,345
- DSCR: 0.00x (0.0%)

## What Must Be True (Targets)
- Cash gap (monthly): $-22,345 (negative means shortfall)
- Required utilization multiplier (cash break-even): 1.31x
- Required additional sales (per day): $1,271
- Notes: Required utilization > 1.25 (aggressive)

## Sensitivity (Cash After Debt)
| Lever | Cash after debt (monthly) |
| --- | --- |
| Utilization +10% | $-15,164 |
| Utilization -10% | $-29,526 |
| Spend +10% | $-18,060 |
| Spend -10% | $-26,631 |
| Fixed costs +10% | $-30,828 |
| Fixed costs -10% | $-13,862 |

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
- Monthly fixed costs: $84,830
- Gross margin (after variable costs): 58.6%
- Break-even sales (monthly): $144,781
- Break-even sales (per day, operating): $4,826
- Break-even sales (per day, after debt): $5,357

## Compliance Warnings
- Alcohol sales are prohibited from 02:00-10:00 and before Sunday noon.
- Late-night mode may require a special exception for midnight-2am alcohol service.
- Last call should be 01:30-01:45 to clear drinks by 02:00.
- Operating after 2am without alcohol is high risk; docs say 24-hour operation is not feasible.

## Notes
- Food COGS and other opex are placeholders; adjust in model/assumptions.yaml before decision-making.