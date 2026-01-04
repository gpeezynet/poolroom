# ROI Report: S12_UPSIDE_PLUS_PROGRAMS - 12-table upside + programs

## Scenario Inputs
- Tables: 12
- Size: 8000 sf
- Pricing style: hourly
- Rent/CAM: $18.50/sf/yr, $3.50/sf/yr
- Lease band: mid
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
- Bar-only bar revenue: $18,540
- Bar-only food revenue: $2,575
- Total monthly sales: $140,475

- Bar COGS: $17,125
- Food COGS: $6,363
- Labor: $30,905
- Rent: $13,875
- CAM: $2,625
- Property tax/insurance (NNN): $1,500
- Utilities: $3,375
- Total occupancy cost: $18,000
- Insurance: $500
- Security: $0
- POS software: $180
- Payment processing: $3,540
- Music licensing: $204
- Marketing: $750
- HVAC service: $100
- HVAC filters: $100
- HVAC reserve: $167
- Maintenance reserve: $708
- Licenses & fees: $96
- Other opex (misc): $1,200
- Total expenses: $137,010

- Monthly net: $3,465
- Annual net: $41,580

## Programs (Non-table Revenue)
- Membership revenue + contribution: $3,750 / $3,188
- League revenue + contribution: $240 / $192
- Event revenue + contribution: $3,600 / $2,601
- Total programs contribution: $5,980
- Membership discount leakage (not applied): $1,500

## Programs Impact
- Program-driven table hours (monthly): 0.0
- Program-driven bar-only guests (monthly): 0
- Membership utilization uplift: 0.0%
- Membership spend uplift: 0.0%
- Program incremental labor cost (monthly): $0
- Program incremental security cost (monthly): $0
- Program net contribution (monthly): $5,980

## Fixed Cost Breakdown
- Occupancy (rent/CAM/NNN): $18,000
- Utilities total: $3,375
- Insurance: $500
- Baseline labor (schedule): $53,698
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
- Fixed costs total: $79,078

## CAPEX & Financing
- CAPEX total (incl. working capital): $620,000
- Tenant improvement allowance: $0
- Total project cost (net TI): $620,000
- Equity required at close: $124,000
- Loan amount (modeled): $496,000
- Lease deposit (months / amount): 1.0 / $18,000
- Total cash required to open: $142,000
- Working capital / runway months: $100,000 / 19.0

## Underwriting Summary
- Total project cost: $620,000
- Equity required: $124,000
- Total cash required to open: $142,000
- Runway months: 19.0

## Debt & Coverage
- Monthly debt service: $7,116
- NOI (monthly): $1,855
- Cash flow after debt: $-5,261
- DSCR: 0.26x (26.1%)

## What Must Be True (Targets)
- Cash gap (monthly): $-5,261 (negative means shortfall)
- Required utilization multiplier (cash break-even): 1.06x
- Required additional sales (per day): $304
- Notes: n/a

## Sensitivity (Cash After Debt)
| Lever | Cash after debt (monthly) |
| --- | --- |
| Utilization +10% | $2,833 |
| Utilization -10% | $-13,354 |
| Spend +10% | $-322 |
| Spend -10% | $-10,199 |
| Fixed costs +10% | $-13,169 |
| Fixed costs -10% | $2,647 |

## ROI Metrics
- Startup cost (likely): $620,000
- Payback period: 14.91 years

## Break-even Snapshots
- Monthly fixed costs: $79,078
- Gross margin (after variable costs): 57.6%
- Break-even sales (monthly): $137,255
- Break-even sales (per day, operating): $4,575
- Break-even sales (per day, after debt): $4,987

## Compliance Warnings
- Alcohol sales are prohibited from 02:00-10:00 and before Sunday noon.
- Late-night mode may require a special exception for midnight-2am alcohol service.
- Last call should be 01:30-01:45 to clear drinks by 02:00.
- Operating after 2am without alcohol is high risk; docs say 24-hour operation is not feasible.

## Notes
- Food COGS and other opex are placeholders; adjust in model/assumptions.yaml before decision-making.