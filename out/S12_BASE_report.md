# ROI Report: S12_BASE - 12-table base

## Scenario Inputs
- Tables: 12
- Size: 8000 sf
- Pricing style: hourly
- Rent/CAM: $18.50/sf/yr, $3.50/sf/yr
- Lease band: mid
- Estimated guests per month: 2838
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

## Weekly Reality Pattern
- Mon (slow): $1,200
- Tue (slow): $1,200
- Wed (slow): $1,200
- Thu (warm): $2,500
- Fri (hot): $5,000
- Sat (hot): $5,000
- Sun (slow): $1,200
- Modeled day sales range: $1,200 - $5,000

## Monthly P&L
- Table revenue: $15,415
- Bar revenue (table-driven): $35,753
- Food revenue (table-driven): $9,931
- Bar-only bar revenue: $12,171
- Bar-only food revenue: $1,690
- Total monthly sales: $74,961

- Bar COGS: $9,585
- Food COGS: $3,487
- Labor (top-up): $8,484
- Labor (schedule baseline): $8,007
- Labor (total): $16,491
- Rent: $13,875
- CAM: $2,625
- Property tax/insurance (NNN): $1,500
- Utilities: $3,375
- Total occupancy cost: $18,000
- Insurance: $500
- Security: $0
- POS software: $180
- Payment processing: $1,889
- Music licensing: $204
- Marketing: $750
- HVAC service: $100
- HVAC filters: $100
- HVAC reserve: $167
- Maintenance reserve: $708
- Licenses & fees: $96
- Other opex (misc): $1,200
- Total expenses: $56,832

- Monthly net: $18,129
- Annual net: $217,544

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
- Occupancy (rent/CAM/NNN): $18,000
- Utilities total: $3,375
- Insurance: $500
- Baseline labor (schedule): $8,007
- Variable labor (top-up): max(0, labor_pct*sales - baseline labor)
- Variable labor (monthly): $8,484
- Total labor (monthly): $16,491
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
- Fixed costs total: $33,388

## CAPEX & Financing
- CAPEX total (incl. working capital): $620,000
- Tenant improvement allowance: $0
- Total project cost (net TI): $620,000
- Equity required at close: $124,000
- Loan amount (modeled): $496,000
- Lease deposit (months / amount): 1.0 / $18,000
- Total cash required to open: $142,000
- Working capital / runway months: $100,000 / n/a (cashflow positive)

## Underwriting Summary
- Total project cost: $620,000
- Equity required: $124,000
- Total cash required to open: $142,000
- Runway months: n/a (cashflow positive)

## Debt & Coverage
- Monthly debt service: $7,116
- NOI (monthly): $18,129
- Cash flow after debt: $11,012
- DSCR: 2.55x (254.8%)

## Works Check
- Works? YES
- Surplus per week: $2,543
- Surplus per day avg: $363

## What Must Be True (Targets)
- Cash after debt (monthly): $11,012 (negative means shortfall)
- Required utilization multiplier (cash break-even): 0.79x
- Required additional sales (per day): $0
- Notes: n/a

## Sensitivity (Cash After Debt)
| Lever | Cash after debt (monthly) |
| --- | --- |
| Utilization +10% | $16,164 |
| Utilization -10% | $5,861 |
| Spend +10% | $14,152 |
| Spend -10% | $7,873 |
| Fixed costs +10% | $7,674 |
| Fixed costs -10% | $14,351 |

## ROI Metrics
- Startup cost (likely): $620,000
- Payback period: 2.85 years

## Break-even Snapshots
- Monthly fixed costs: $33,388
- Gross margin (after variable costs): 68.7%
- Break-even sales (monthly): $48,582
- Break-even sales (per day, operating): $1,619
- Break-even sales (per day, after debt): $1,965

## Compliance Warnings
- Alcohol sales are prohibited from 02:00-10:00 and before Sunday noon.
- Late-night mode may require a special exception for midnight-2am alcohol service.
- Last call should be 01:30-01:45 to clear drinks by 02:00.
- Operating after 2am without alcohol is high risk; docs say 24-hour operation is not feasible.

## Notes
- Food COGS and other opex are placeholders; adjust in model/assumptions.yaml before decision-making.