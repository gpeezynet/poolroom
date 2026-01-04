# ROI Report: S12_BASE_PLUS_PROGRAMS2_GOOD_LEASE - 12-table base + programs (drivers) good lease

## Scenario Inputs
- Tables: 12
- Size: 8000 sf
- Pricing style: hourly
- Rent/CAM: $12.00/sf/yr, $2.00/sf/yr
- Lease band: low
- Estimated guests per month: 4828
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
- Table revenue: $25,421
- Bar revenue (table-driven): $62,652
- Food revenue (table-driven): $17,403
- Bar-only bar revenue: $28,976
- Bar-only food revenue: $4,024
- Total monthly sales: $146,066

- Bar COGS: $18,326
- Food COGS: $6,428
- Labor: $32,135
- Rent: $9,000
- CAM: $1,500
- Property tax/insurance (NNN): $1,500
- Utilities: $2,625
- Total occupancy cost: $12,000
- Insurance: $500
- Security: $0
- POS software: $180
- Payment processing: $3,681
- Music licensing: $204
- Marketing: $750
- HVAC service: $100
- HVAC filters: $100
- HVAC reserve: $167
- Maintenance reserve: $708
- Licenses & fees: $96
- Other opex (misc): $1,200
- Total expenses: $135,591

- Monthly net: $10,475
- Annual net: $125,702

## Programs (Non-table Revenue)
- Membership revenue + contribution: $3,750 / $3,188
- League revenue + contribution: $240 / $192
- Event revenue + contribution: $3,600 / $2,601
- Total programs contribution: $5,980
- Membership discount leakage (not applied): $1,500

## Programs Impact
- Program-driven table hours (monthly): 136.1
- Program-driven bar-only guests (monthly): 580
- Membership utilization uplift: 5.0%
- Membership spend uplift: 3.0%
- Program incremental labor cost (monthly): $1,505
- Program incremental security cost (monthly): $1,189
- Program net contribution (monthly): $3,287

## Fixed Cost Breakdown
- Occupancy (rent/CAM/NNN): $12,000
- Utilities total: $2,625
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
- Fixed costs total: $75,022

## CAPEX & Financing
- CAPEX total (incl. working capital): $620,000
- Tenant improvement allowance: $0
- Total project cost (net TI): $620,000
- Equity required at close: $124,000
- Loan amount (modeled): $496,000
- Lease deposit (months / amount): 1.0 / $12,000
- Total cash required to open: $136,000
- Working capital / runway months: $100,000 / 100000.0

## Underwriting Summary
- Total project cost: $620,000
- Equity required: $124,000
- Total cash required to open: $136,000
- Runway months: 100000.0

## Debt & Coverage
- Monthly debt service: $7,116
- NOI (monthly): $8,866
- Cash flow after debt: $1,749
- DSCR: 1.25x (124.6%)

## What Must Be True (Targets)
- Cash gap (monthly): $1,749 (negative means shortfall)
- Required utilization multiplier (cash break-even): 0.98x
- Required additional sales (per day): $0
- Notes: n/a

## Sensitivity (Cash After Debt)
| Lever | Cash after debt (monthly) |
| --- | --- |
| Utilization +10% | $10,138 |
| Utilization -10% | $-6,639 |
| Spend +10% | $6,347 |
| Spend -10% | $-2,848 |
| Fixed costs +10% | $-5,753 |
| Fixed costs -10% | $9,252 |

## ROI Metrics
- Startup cost (likely): $620,000
- Payback period: 4.93 years

## Break-even Snapshots
- Monthly fixed costs: $75,022
- Gross margin (after variable costs): 57.4%
- Break-even sales (monthly): $130,629
- Break-even sales (per day, operating): $4,354
- Break-even sales (per day, after debt): $4,767

## Compliance Warnings
- Alcohol sales are prohibited from 02:00-10:00 and before Sunday noon.
- Late-night mode may require a special exception for midnight-2am alcohol service.
- Last call should be 01:30-01:45 to clear drinks by 02:00.
- Operating after 2am without alcohol is high risk; docs say 24-hour operation is not feasible.

## Notes
- Food COGS and other opex are placeholders; adjust in model/assumptions.yaml before decision-making.