# ROI Report: S12_BASE_LATE - 12-table base late-night

## Scenario Inputs
- Tables: 12
- Size: 8000 sf
- Pricing style: hourly
- Rent/CAM: $18.50/sf/yr, $3.50/sf/yr
- Lease band: mid
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
- Labor: $19,772
- Rent: $13,875
- CAM: $2,625
- Property tax/insurance (NNN): $1,500
- Utilities: $3,713
- Total occupancy cost: $18,000
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
- Total expenses: $87,701

- Monthly net: $61,068
- Annual net: $732,818

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
- Utilities total: $3,713
- Insurance: $500
- Baseline labor (schedule): $12,957
- Variable labor (top-up): max(0, labor_pct*sales - baseline labor)
- Variable labor (monthly): $19,772
- Total labor (monthly): $32,729
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
- Fixed costs total: $38,675

## CAPEX & Financing
- CAPEX total (incl. working capital): $620,000
- Tenant improvement allowance: $0
- Total project cost (net TI): $620,000
- Equity required at close: $124,000
- Loan amount (modeled): $496,000
- Lease deposit (months / amount): 1.0 / $18,000
- Total cash required to open: $142,000
- Working capital / runway months: $100,000 / 100000.0

## Underwriting Summary
- Total project cost: $620,000
- Equity required: $124,000
- Total cash required to open: $142,000
- Runway months: 100000.0

## Debt & Coverage
- Monthly debt service: $7,116
- NOI (monthly): $61,068
- Cash flow after debt: $53,952
- DSCR: 8.58x (858.2%)

## What Must Be True (Targets)
- Cash gap (monthly): $53,952 (negative means shortfall)
- Required utilization multiplier (cash break-even): 0.46x
- Required additional sales (per day): $0
- Notes: n/a

## Sensitivity (Cash After Debt)
| Lever | Cash after debt (monthly) |
| --- | --- |
| Utilization +10% | $63,926 |
| Utilization -10% | $43,978 |
| Spend +10% | $60,309 |
| Spend -10% | $47,595 |
| Fixed costs +10% | $50,084 |
| Fixed costs -10% | $57,820 |

## Late-Night Incremental (Bridge)
- Incremental sales (monthly): $37,238
- Incremental variable costs (monthly): $10,180
- Incremental gross profit (monthly): $27,059
- Incremental fixed costs (monthly): $4,950
- Incremental NOI (monthly): $22,109
- Incremental cash flow after debt (monthly): $22,109
- Break-even incremental sales (per day): $227
- Late-night worth it?: True

## ROI Metrics
- Startup cost (likely): $620,000
- Payback period: 0.85 years

## Break-even Snapshots
- Monthly fixed costs: $38,675
- Gross margin (after variable costs): 67.0%
- Break-even sales (monthly): $57,685
- Break-even sales (per day, operating): $1,923
- Break-even sales (per day, after debt): $2,277

## Compliance Warnings
- Alcohol sales are prohibited from 02:00-10:00 and before Sunday noon.
- Late-night mode may require a special exception for midnight-2am alcohol service.
- Last call should be 01:30-01:45 to clear drinks by 02:00.
- Operating after 2am without alcohol is high risk; docs say 24-hour operation is not feasible.

## Notes
- Food COGS and other opex are placeholders; adjust in model/assumptions.yaml before decision-making.