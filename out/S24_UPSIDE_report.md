# ROI Report: S24_UPSIDE - 24-table upside

## Scenario Inputs
- Tables: 24
- Size: 15000 sf
- Pricing style: hourly
- Rent/CAM: $18.00/sf/yr, $4.00/sf/yr
- Estimated guests per month: 9680
- Bar-only guests per day (weekday/weekend): 25 / 60
- Bar-only spend + food attach: $18 bar, 25.0% @ $10 food

## Legal Hours Constraint
- Legal max open hours/day: 16.0
- Modeled open hours/day (capped): 14.0
- NOTE: All-night operation is not modeled for alcohol venues; this model enforces legal max hours.

## Revenue Drivers
- Table rates (offpeak/prime/late): $12/hr, $16/hr, $20/hr
- Avg table hours sold per table (weekday/weekend): 3.00 / 5.00
- Avg guests per table hour: 3.00
- Bar attach + spend per guest: 70.0% @ $20
- Food attach + spend per guest: 35.0% @ $11
- Multipliers (utilization/spend): 1.15 / 1.10

## Monthly P&L
- Table revenue: $52,105
- Bar revenue (table-driven): $134,167
- Food revenue (table-driven): $37,269
- Bar-only bar revenue: $18,540
- Bar-only food revenue: $2,575
- Total monthly sales: $244,656

- Bar COGS: $30,541
- Food COGS: $11,953
- Labor: $53,824
- Rent: $24,000
- CAM: $5,333
- Property tax/insurance (NNN): $2,667
- Utilities: $5,700
- Insurance: $500
- Security: $0
- POS software: $180
- Payment processing: $6,165
- Music licensing: $204
- Marketing: $750
- HVAC service: $100
- HVAC filters: $100
- HVAC reserve: $167
- Maintenance reserve: $1,417
- Licenses & fees: $135
- Other opex (misc): $1,200
- Total expenses: $231,732

- Monthly net: $12,924
- Annual net: $155,093

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
- Occupancy (rent/CAM/NNN): $32,000
- Utilities total: $5,700
- Insurance: $500
- Baseline labor (schedule): $86,795
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
- Fixed costs total: $129,247

## CAPEX & Financing
- Total capex: $824,500
- Down payment (assumed): $164,900
- Loan amount (assumed): $650,000
- Implied equity: $174,500

## Debt & Coverage
- Monthly debt service: $9,326
- NOI (monthly): $12,924
- Cash flow after debt: $3,599
- DSCR: 1.39x (138.6%)

## What Must Be True (Targets)
- Cash gap (monthly): $3,599 (negative means shortfall)
- Required utilization multiplier (cash break-even): 0.97x
- Required additional sales (per day): $0
- Notes: n/a

## Sensitivity (Cash After Debt)
| Lever | Cash after debt (monthly) |
| --- | --- |
| Utilization +10% | $17,816 |
| Utilization -10% | $-10,618 |
| Spend +10% | $13,561 |
| Spend -10% | $-6,364 |
| Fixed costs +10% | $-9,326 |
| Fixed costs -10% | $16,524 |

## ROI Metrics
- Startup cost (likely): $1,190,000
- Payback period: 7.67 years

## Break-even Snapshots
- Monthly fixed costs: $129,247
- Gross margin (after variable costs): 58.1%
- Break-even sales (monthly): $222,415
- Break-even sales (per day, operating): $7,414
- Break-even sales (per day, after debt): $7,949

## Compliance Warnings
- Alcohol sales are prohibited from 02:00-10:00 and before Sunday noon.
- Late-night mode may require a special exception for midnight-2am alcohol service.
- Last call should be 01:30-01:45 to clear drinks by 02:00.
- Operating after 2am without alcohol is high risk; docs say 24-hour operation is not feasible.

## Notes
- Food COGS and other opex are placeholders; adjust in model/assumptions.yaml before decision-making.