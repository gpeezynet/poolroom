# ROI Report: S24_BASE_LATE_PLUS_PROGRAMS2 - 24-table base late-night + programs (drivers)

## Scenario Inputs
- Tables: 24
- Size: 15000 sf
- Pricing style: hourly
- Rent/CAM: $18.00/sf/yr, $4.00/sf/yr
- Estimated guests per month: 12710
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
- Bar attach + spend per guest: 70.0% @ $19
- Food attach + spend per guest: 35.0% @ $10
- Multipliers (utilization/spend): 1.05 / 1.03

## Monthly P&L
- Table revenue: $71,210
- Bar revenue (table-driven): $168,919
- Food revenue (table-driven): $46,922
- Bar-only bar revenue: $28,976
- Bar-only food revenue: $4,024
- Total monthly sales: $327,642

- Bar COGS: $39,579
- Food COGS: $15,284
- Labor: $72,081
- Rent: $24,000
- CAM: $5,333
- Property tax/insurance (NNN): $2,667
- Utilities: $5,700
- Insurance: $500
- Security: $1,732
- POS software: $180
- Payment processing: $8,257
- Music licensing: $204
- Marketing: $750
- HVAC service: $100
- HVAC filters: $100
- HVAC reserve: $167
- Maintenance reserve: $1,417
- Licenses & fees: $135
- Other opex (misc): $1,200
- Total expenses: $271,907

- Monthly net: $55,735
- Annual net: $668,820

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
- NOI (monthly): $54,126
- Cash flow after debt: $44,800
- DSCR: 5.80x (580.4%)

## What Must Be True (Targets)
- Cash gap (monthly): $44,800 (negative means shortfall)
- Required utilization multiplier (cash break-even): 0.77x
- Required additional sales (per day): $0
- Notes: n/a

## Sensitivity (Cash After Debt)
| Lever | Cash after debt (monthly) |
| --- | --- |
| Utilization +10% | $63,883 |
| Utilization -10% | $25,717 |
| Spend +10% | $57,371 |
| Spend -10% | $32,228 |
| Fixed costs +10% | $31,129 |
| Fixed costs -10% | $58,471 |

## Late-Night Incremental (Bridge)
- Incremental sales (monthly): $76,100
- Incremental variable costs (monthly): $31,018
- Incremental gross profit (monthly): $45,082
- Incremental fixed costs (monthly): $5,726
- Incremental NOI (monthly): $39,356
- Incremental cash flow after debt (monthly): $39,356
- Break-even incremental sales (per day): $322
- Late-night worth it?: True

## ROI Metrics
- Startup cost (likely): $1,190,000
- Payback period: 1.78 years

## Break-even Snapshots
- Monthly fixed costs: $136,706
- Gross margin (after variable costs): 58.2%
- Break-even sales (monthly): $234,713
- Break-even sales (per day, operating): $7,824
- Break-even sales (per day, after debt): $8,357

## Compliance Warnings
- Alcohol sales are prohibited from 02:00-10:00 and before Sunday noon.
- Late-night mode may require a special exception for midnight-2am alcohol service.
- Last call should be 01:30-01:45 to clear drinks by 02:00.
- Operating after 2am without alcohol is high risk; docs say 24-hour operation is not feasible.

## Notes
- Food COGS and other opex are placeholders; adjust in model/assumptions.yaml before decision-making.