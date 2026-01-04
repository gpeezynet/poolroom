# ROI Report: S24_BASE_LATE - 24-table base late-night

## Scenario Inputs
- Tables: 24
- Size: 15000 sf
- Pricing style: hourly
- Rent/CAM: $18.50/sf/yr, $3.50/sf/yr
- Lease band: mid
- Estimated guests per month: 11473
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
- Table revenue: $65,677
- Bar revenue (table-driven): $148,406
- Food revenue (table-driven): $41,224
- Bar-only bar revenue: $18,540
- Bar-only food revenue: $2,575
- Total monthly sales: $276,423

- Bar COGS: $33,389
- Food COGS: $13,140
- Labor: $60,813
- Rent: $24,667
- CAM: $4,667
- Property tax/insurance (NNN): $2,667
- Utilities: $6,600
- Total occupancy cost: $32,000
- Insurance: $500
- Security: $0
- POS software: $180
- Payment processing: $6,966
- Music licensing: $204
- Marketing: $750
- HVAC service: $100
- HVAC filters: $100
- HVAC reserve: $167
- Maintenance reserve: $1,417
- Licenses & fees: $135
- Other opex (misc): $1,200
- Total expenses: $250,182

- Monthly net: $26,241
- Annual net: $314,893

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
- Utilities total: $6,600
- Insurance: $500
- Baseline labor (schedule): $92,522
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
- Fixed costs total: $135,874

## CAPEX & Financing
- CAPEX total (incl. working capital): $1,190,000
- Tenant improvement allowance: $0
- Total project cost (net TI): $1,190,000
- Equity required at close: $540,000
- Loan amount (modeled): $650,000
- Lease deposit (months / amount): 1.0 / $32,000
- Total cash required to open: $572,000
- Working capital / runway months: $180,000 / 180000.0

## Underwriting Summary
- Total project cost: $1,190,000
- Equity required: $540,000
- Total cash required to open: $572,000
- Runway months: 180000.0

## Debt & Coverage
- Monthly debt service: $9,326
- NOI (monthly): $26,241
- Cash flow after debt: $16,915
- DSCR: 2.81x (281.4%)

## What Must Be True (Targets)
- Cash gap (monthly): $16,915 (negative means shortfall)
- Required utilization multiplier (cash break-even): 0.90x
- Required additional sales (per day): $0
- Notes: n/a

## Sensitivity (Cash After Debt)
| Lever | Cash after debt (monthly) |
| --- | --- |
| Utilization +10% | $33,127 |
| Utilization -10% | $704 |
| Spend +10% | $28,037 |
| Spend -10% | $5,794 |
| Fixed costs +10% | $3,328 |
| Fixed costs -10% | $30,503 |

## Late-Night Incremental (Bridge)
- Incremental sales (monthly): $74,477
- Incremental variable costs (monthly): $30,260
- Incremental gross profit (monthly): $44,217
- Incremental fixed costs (monthly): $5,726
- Incremental NOI (monthly): $38,491
- Incremental cash flow after debt (monthly): $38,491
- Break-even incremental sales (per day): $322
- Late-night worth it?: True

## ROI Metrics
- Startup cost (likely): $1,190,000
- Payback period: 3.78 years

## Break-even Snapshots
- Monthly fixed costs: $135,874
- Gross margin (after variable costs): 58.6%
- Break-even sales (monthly): $231,679
- Break-even sales (per day, operating): $7,723
- Break-even sales (per day, after debt): $8,253

## Compliance Warnings
- Alcohol sales are prohibited from 02:00-10:00 and before Sunday noon.
- Late-night mode may require a special exception for midnight-2am alcohol service.
- Last call should be 01:30-01:45 to clear drinks by 02:00.
- Operating after 2am without alcohol is high risk; docs say 24-hour operation is not feasible.

## Notes
- Food COGS and other opex are placeholders; adjust in model/assumptions.yaml before decision-making.