# ROI Report: S12_UPSIDE - 12-table upside

## Scenario Inputs
- Tables: 12
- Size: 8000 sf
- Pricing style: hourly
- Rent/CAM: $18.00/sf/yr, $4.00/sf/yr
- Estimated guests per month: 4840
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
- Table revenue: $26,053
- Bar revenue (table-driven): $67,083
- Food revenue (table-driven): $18,634
- Bar-only bar revenue: $23,929
- Bar-only food revenue: $3,324
- Total monthly sales: $139,023

- Bar COGS: $18,203
- Food COGS: $6,587
- Labor: $30,585
- Rent: $13,500
- CAM: $3,000
- Property tax/insurance (NNN): $1,500
- Utilities: $3,400
- Insurance: $500
- Security: $1,732
- POS software: $180
- Payment processing: $3,503
- Music licensing: $204
- Marketing: $750
- HVAC service: $100
- HVAC filters: $100
- HVAC reserve: $167
- Maintenance reserve: $708
- Licenses & fees: $96
- Other opex (misc): $1,200
- Total expenses: $139,714

- Monthly net: $-691
- Annual net: $-8,287

## Fixed Cost Breakdown
- Occupancy (rent/CAM/NNN): $18,000
- Utilities total: $3,400
- Insurance: $500
- Baseline labor (schedule): $53,698
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
- Fixed costs total: $80,835

## CAPEX & Financing
- Total capex: $522,000
- Down payment (assumed): $104,400
- Loan amount (assumed): $650,000
- Implied equity: $-128,000

## Debt & Coverage
- Monthly debt service: $9,326
- NOI (monthly): $-691
- Cash flow after debt: $-10,016
- DSCR: 0.00x (0.0%)

## What Must Be True (Targets)
- Cash gap (monthly): $-10,016 (negative means shortfall)
- Required utilization multiplier (cash break-even): 1.12x
- Required additional sales (per day): $579
- Notes: n/a

## Sensitivity (Cash After Debt)
| Lever | Cash after debt (monthly) |
| --- | --- |
| Utilization +10% | $-2,002 |
| Utilization -10% | $-18,031 |
| Spend +10% | $-5,075 |
| Spend -10% | $-14,958 |
| Fixed costs +10% | $-18,100 |
| Fixed costs -10% | $-1,933 |

## ROI Metrics
- Startup cost (likely): $620,000
- Payback period: n/a

## Break-even Snapshots
- Monthly fixed costs: $80,835
- Gross margin (after variable costs): 57.6%
- Break-even sales (monthly): $140,221
- Break-even sales (per day, operating): $4,674
- Break-even sales (per day, after debt): $5,213

## Compliance Warnings
- Alcohol sales are prohibited from 02:00-10:00 and before Sunday noon.
- Late-night mode may require a special exception for midnight-2am alcohol service.
- Last call should be 01:30-01:45 to clear drinks by 02:00.
- Operating after 2am without alcohol is high risk; docs say 24-hour operation is not feasible.

## Notes
- Food COGS and other opex are placeholders; adjust in model/assumptions.yaml before decision-making.