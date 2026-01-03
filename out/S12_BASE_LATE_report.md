# ROI Report: S12_BASE_LATE - 12-table base late-night

## Scenario Inputs
- Tables: 12
- Size: 8000 sf
- Pricing style: hourly
- Rent/CAM: $18.00/sf/yr, $4.00/sf/yr
- Estimated guests per month: 5736
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
- Table revenue: $32,839
- Bar revenue (table-driven): $74,203
- Food revenue (table-driven): $20,612
- Bar-only bar revenue: $18,540
- Bar-only food revenue: $2,575
- Total monthly sales: $148,769

- Bar COGS: $18,549
- Food COGS: $6,956
- Labor: $32,729
- Rent: $13,500
- CAM: $3,000
- Property tax/insurance (NNN): $1,500
- Utilities: $3,400
- Insurance: $500
- Security: $0
- POS software: $180
- Payment processing: $3,749
- Music licensing: $204
- Marketing: $750
- HVAC service: $100
- HVAC filters: $100
- HVAC reserve: $167
- Maintenance reserve: $708
- Licenses & fees: $96
- Other opex (misc): $1,200
- Total expenses: $146,813

- Monthly net: $1,956
- Annual net: $23,474

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
- NOI (monthly): $1,956
- Cash flow after debt: $-7,369
- DSCR: 0.21x (21.0%)

## What Must Be True (Targets)
- Cash gap (monthly): $-7,369 (negative means shortfall)
- Required utilization multiplier (cash break-even): 1.08x
- Required additional sales (per day): $421
- Notes: n/a

## Sensitivity (Cash After Debt)
| Lever | Cash after debt (monthly) |
| --- | --- |
| Utilization +10% | $1,309 |
| Utilization -10% | $-16,048 |
| Spend +10% | $-1,838 |
| Spend -10% | $-12,901 |
| Fixed costs +10% | $-15,852 |
| Fixed costs -10% | $1,114 |

## Late-Night Incremental (Bridge)
- Incremental sales (monthly): $37,238
- Incremental variable costs (monthly): $15,130
- Incremental gross profit (monthly): $22,109
- Incremental fixed costs (monthly): $5,726
- Incremental NOI (monthly): $16,382
- Incremental cash flow after debt (monthly): $16,382
- Break-even incremental sales (per day): $322
- Late-night worth it?: True

## ROI Metrics
- Startup cost (likely): $620,000
- Payback period: 26.41 years

## Break-even Snapshots
- Monthly fixed costs: $84,830
- Gross margin (after variable costs): 58.3%
- Break-even sales (monthly): $145,416
- Break-even sales (per day, operating): $4,847
- Break-even sales (per day, after debt): $5,380

## Compliance Warnings
- Alcohol sales are prohibited from 02:00-10:00 and before Sunday noon.
- Late-night mode may require a special exception for midnight-2am alcohol service.
- Last call should be 01:30-01:45 to clear drinks by 02:00.
- Operating after 2am without alcohol is high risk; docs say 24-hour operation is not feasible.

## Notes
- Food COGS and other opex are placeholders; adjust in model/assumptions.yaml before decision-making.