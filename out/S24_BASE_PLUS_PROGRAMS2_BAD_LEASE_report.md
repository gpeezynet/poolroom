# ROI Report: S24_BASE_PLUS_PROGRAMS2_BAD_LEASE - 24-table base + programs (drivers) bad lease

## Scenario Inputs
- Tables: 24
- Size: 15000 sf
- Pricing style: hourly
- Rent/CAM: $25.00/sf/yr, $5.00/sf/yr
- Lease band: high
- Estimated guests per month: 9655
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
- Bar attach + spend per guest: 70.0% @ $19
- Food attach + spend per guest: 35.0% @ $10
- Multipliers (utilization/spend): 1.05 / 1.03

## Monthly P&L
- Table revenue: $50,841
- Bar revenue (table-driven): $125,303
- Food revenue (table-driven): $34,806
- Bar-only bar revenue: $28,976
- Bar-only food revenue: $4,024
- Total monthly sales: $251,542

- Bar COGS: $30,856
- Food COGS: $11,649
- Labor: $55,339
- Rent: $33,333
- CAM: $6,667
- Property tax/insurance (NNN): $2,667
- Utilities: $7,333
- Total occupancy cost: $42,667
- Insurance: $500
- Security: $0
- POS software: $180
- Payment processing: $6,339
- Music licensing: $204
- Marketing: $750
- HVAC service: $100
- HVAC filters: $100
- HVAC reserve: $167
- Maintenance reserve: $1,417
- Licenses & fees: $135
- Other opex (misc): $1,200
- Total expenses: $248,424

- Monthly net: $3,118
- Annual net: $37,413

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
- Program incremental labor cost (monthly): $1,505
- Program incremental security cost (monthly): $1,189
- Program net contribution (monthly): $3,287

## Fixed Cost Breakdown
- Occupancy (rent/CAM/NNN): $42,667
- Utilities total: $7,333
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
- Fixed costs total: $144,241

## CAPEX & Financing
- CAPEX total (incl. working capital): $1,190,000
- Tenant improvement allowance: $0
- Total project cost (net TI): $1,190,000
- Equity required at close: $540,000
- Loan amount (modeled): $650,000
- Lease deposit (months / amount): 1.0 / $42,667
- Total cash required to open: $582,667
- Working capital / runway months: $180,000 / 23.0

## Underwriting Summary
- Total project cost: $1,190,000
- Equity required: $540,000
- Total cash required to open: $582,667
- Runway months: 23.0

## Debt & Coverage
- Monthly debt service: $9,326
- NOI (monthly): $1,508
- Cash flow after debt: $-7,817
- DSCR: 0.16x (16.2%)

## What Must Be True (Targets)
- Cash gap (monthly): $-7,817 (negative means shortfall)
- Required utilization multiplier (cash break-even): 1.05x
- Required additional sales (per day): $450
- Notes: n/a

## Sensitivity (Cash After Debt)
| Lever | Cash after debt (monthly) |
| --- | --- |
| Utilization +10% | $6,758 |
| Utilization -10% | $-22,392 |
| Spend +10% | $1,460 |
| Spend -10% | $-17,094 |
| Fixed costs +10% | $-22,241 |
| Fixed costs -10% | $6,607 |

## ROI Metrics
- Startup cost (likely): $1,190,000
- Payback period: 31.81 years

## Break-even Snapshots
- Monthly fixed costs: $144,241
- Gross margin (after variable costs): 57.9%
- Break-even sales (monthly): $248,939
- Break-even sales (per day, operating): $8,298
- Break-even sales (per day, after debt): $8,834

## Compliance Warnings
- Alcohol sales are prohibited from 02:00-10:00 and before Sunday noon.
- Late-night mode may require a special exception for midnight-2am alcohol service.
- Last call should be 01:30-01:45 to clear drinks by 02:00.
- Operating after 2am without alcohol is high risk; docs say 24-hour operation is not feasible.

## Notes
- Food COGS and other opex are placeholders; adjust in model/assumptions.yaml before decision-making.