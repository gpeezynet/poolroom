# ROI Report: S24 - 24-table phase-2 model

## Scenario Inputs
- Tables: 24
- Size: 15000 sf
- Pricing style: hourly
- Rent/CAM: $18.00/sf/yr, $4.00/sf/yr
- Estimated guests per month: 8418
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
- Bar attach + spend per guest: 70.0% @ $18
- Food attach + spend per guest: 35.0% @ $10
- Multipliers (utilization/spend): 1.00 / 1.00

## Monthly P&L
- Table revenue: $45,309
- Bar revenue (table-driven): $106,061
- Food revenue (table-driven): $29,461
- Bar-only bar revenue: $23,929
- Bar-only food revenue: $3,324
- Total monthly sales: $208,084

- Bar COGS: $25,998
- Food COGS: $9,835
- Labor: $45,778
- Rent: $24,000
- CAM: $5,333
- Property tax/insurance (NNN): $2,667
- Utilities: $5,700
- Insurance: $500
- Security: $1,732
- POS software: $180
- Payment processing: $5,244
- Music licensing: $204
- Marketing: $750
- HVAC service: $100
- HVAC filters: $100
- HVAC reserve: $167
- Maintenance reserve: $1,417
- Licenses & fees: $135
- Other opex (misc): $1,200
- Total expenses: $217,835

- Monthly net: $-9,751
- Annual net: $-117,014

## Fixed Cost Breakdown
- Occupancy (rent/CAM/NNN): $32,000
- Utilities total: $5,700
- Insurance: $500
- Baseline labor (schedule): $86,795
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
- Fixed costs total: $130,979

## CAPEX & Financing
- Total capex: $824,500
- Down payment (assumed): $164,900
- Loan amount (assumed): $650,000
- Implied equity: $174,500

## Debt & Coverage
- Monthly debt service: $9,326
- NOI (monthly): $-9,751
- Cash flow after debt: $-19,077
- DSCR: 0.00x (0.0%)

## What Must Be True (Targets)
- Cash gap (monthly): $-19,077 (negative means shortfall)
- Required utilization multiplier (cash break-even): 1.16x
- Required additional sales (per day): $1,091
- Notes: n/a

## Sensitivity (Cash After Debt)
| Lever | Cash after debt (monthly) |
| --- | --- |
| Utilization +10% | $-6,954 |
| Utilization -10% | $-31,200 |
| Spend +10% | $-11,181 |
| Spend -10% | $-26,972 |
| Fixed costs +10% | $-32,175 |
| Fixed costs -10% | $-5,979 |

## ROI Metrics
- Startup cost (likely): $1,190,000
- Payback period: n/a

## Break-even Snapshots
- Monthly fixed costs: $130,979
- Gross margin (after variable costs): 58.3%
- Break-even sales (monthly): $224,821
- Break-even sales (per day, operating): $7,494
- Break-even sales (per day, after debt): $8,028

## Compliance Warnings
- Alcohol sales are prohibited from 02:00-10:00 and before Sunday noon.
- Late-night mode may require a special exception for midnight-2am alcohol service.
- Last call should be 01:30-01:45 to clear drinks by 02:00.
- Operating after 2am without alcohol is high risk; docs say 24-hour operation is not feasible.

## Notes
- Food COGS and other opex are placeholders; adjust in model/assumptions.yaml before decision-making.