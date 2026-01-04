# ROI Report: S24 - 24-table phase-2 model

## Scenario Inputs
- Tables: 24
- Size: 15000 sf
- Pricing style: hourly
- Rent/CAM: $18.50/sf/yr, $3.50/sf/yr
- Lease band: mid
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
- Bar-only bar revenue: $18,540
- Bar-only food revenue: $2,575
- Total monthly sales: $201,946

- Bar COGS: $24,920
- Food COGS: $9,611
- Labor: $44,428
- Rent: $24,667
- CAM: $4,667
- Property tax/insurance (NNN): $2,667
- Utilities: $6,000
- Total occupancy cost: $32,000
- Insurance: $500
- Security: $0
- POS software: $180
- Payment processing: $5,089
- Music licensing: $204
- Marketing: $750
- HVAC service: $100
- HVAC filters: $100
- HVAC reserve: $167
- Maintenance reserve: $1,417
- Licenses & fees: $135
- Other opex (misc): $1,200
- Total expenses: $213,596

- Monthly net: $-11,650
- Annual net: $-139,794

## Programs (Non-table Revenue)
- Membership revenue + contribution: $0 / $0
- Membership discount cost (applied to revenue): $0 (disc 0.0%, visits/mo 0.00, discountable share 0.0%, estimated share of guests 0.0%, method none)
- Membership net after discounts: $0
- League revenue + contribution: $0 / $0
- Event revenue + contribution: $0 / $0
- Total programs contribution: $0

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
- Utilities total: $6,000
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
- Fixed costs total: $129,547

## CAPEX & Financing
- CAPEX total (incl. working capital): $1,190,000
- Tenant improvement allowance: $0
- Total project cost (net TI): $1,190,000
- Equity required at close: $540,000
- Loan amount (modeled): $650,000
- Lease deposit (months / amount): 1.0 / $32,000
- Total cash required to open: $572,000
- Working capital / runway months: $180,000 / 8.6

## Underwriting Summary
- Total project cost: $1,190,000
- Equity required: $540,000
- Total cash required to open: $572,000
- Runway months: 8.6

## Debt & Coverage
- Monthly debt service: $9,326
- NOI (monthly): $-11,650
- Cash flow after debt: $-20,975
- DSCR: 0.00x (0.0%)

## What Must Be True (Targets)
- Cash gap (monthly): $-20,975 (negative means shortfall)
- Required utilization multiplier (cash break-even): 1.18x
- Required additional sales (per day): $1,198
- Notes: n/a

## Sensitivity (Cash After Debt)
| Lever | Cash after debt (monthly) |
| --- | --- |
| Utilization +10% | $-9,185 |
| Utilization -10% | $-32,765 |
| Spend +10% | $-13,063 |
| Spend -10% | $-28,887 |
| Fixed costs +10% | $-33,930 |
| Fixed costs -10% | $-8,020 |

## ROI Metrics
- Startup cost (likely): $1,190,000
- Payback period: n/a

## Break-even Snapshots
- Monthly fixed costs: $129,547
- Gross margin (after variable costs): 58.4%
- Break-even sales (monthly): $221,901
- Break-even sales (per day, operating): $7,397
- Break-even sales (per day, after debt): $7,929

## Compliance Warnings
- Alcohol sales are prohibited from 02:00-10:00 and before Sunday noon.
- Late-night mode may require a special exception for midnight-2am alcohol service.
- Last call should be 01:30-01:45 to clear drinks by 02:00.
- Operating after 2am without alcohol is high risk; docs say 24-hour operation is not feasible.

## Notes
- Food COGS and other opex are placeholders; adjust in model/assumptions.yaml before decision-making.