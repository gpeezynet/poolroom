# ROI Report: S12_BASE_PLUS_PROGRAMS - 12-table base + programs

## Scenario Inputs
- Tables: 12
- Size: 8000 sf
- Pricing style: hourly
- Rent/CAM: $18.50/sf/yr, $3.50/sf/yr
- Lease band: mid
- Estimated guests per month: 4209
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
- Table revenue: $22,655
- Bar revenue (table-driven): $53,030
- Food revenue (table-driven): $14,731
- Bar-only bar revenue: $18,540
- Bar-only food revenue: $2,575
- Total monthly sales: $118,737

- Bar COGS: $14,314
- Food COGS: $5,192
- Labor: $18,115
- Rent: $13,875
- CAM: $2,625
- Property tax/insurance (NNN): $1,500
- Utilities: $3,375
- Total occupancy cost: $18,000
- Insurance: $500
- Security: $0
- POS software: $180
- Payment processing: $2,992
- Music licensing: $204
- Marketing: $750
- HVAC service: $100
- HVAC filters: $100
- HVAC reserve: $167
- Maintenance reserve: $708
- Licenses & fees: $96
- Other opex (misc): $1,200
- Total expenses: $74,001

- Monthly net: $44,737
- Annual net: $536,841

## Programs (Non-table Revenue)
- Membership revenue + contribution: $3,750 / $3,188
- Membership discount cost (applied to revenue): $383 (disc 10.0%, visits/mo 2.00, discountable share 60.0%, estimated share of guests 5.7%, method discount_pct_on_member_visits)
- Membership net after discounts: $2,804
- Membership discount break-even avg sales/visit: $177
- League revenue + contribution: $240 / $192
- Event revenue + contribution: $3,600 / $2,601
- Total programs contribution: $5,980

## Programs Impact
- Program-driven table hours (monthly): 0.0
- Program-driven bar-only guests (monthly): 0
- Membership utilization uplift: 0.0%
- Membership spend uplift: 0.0%
- Program incremental labor cost (monthly): $0
- Program incremental security cost (monthly): $0
- Program net contribution (monthly): $5,597

## Fixed Cost Breakdown
- Occupancy (rent/CAM/NNN): $18,000
- Utilities total: $3,375
- Insurance: $500
- Baseline labor (schedule): $8,007
- Variable labor (top-up): max(0, labor_pct*sales - baseline labor)
- Variable labor (monthly): $18,115
- Total labor (monthly): $26,122
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
- Working capital / runway months: $100,000 / 100000.0

## Underwriting Summary
- Total project cost: $620,000
- Equity required: $124,000
- Total cash required to open: $142,000
- Runway months: 100000.0

## Debt & Coverage
- Monthly debt service: $7,116
- NOI (monthly): $43,127
- Cash flow after debt: $36,011
- DSCR: 6.06x (606.0%)

## What Must Be True (Targets)
- Cash gap (monthly): $36,011 (negative means shortfall)
- Required utilization multiplier (cash break-even): 0.53x
- Required additional sales (per day): $0
- Notes: n/a

## Sensitivity (Cash After Debt)
| Lever | Cash after debt (monthly) |
| --- | --- |
| Utilization +10% | $43,663 |
| Utilization -10% | $28,360 |
| Spend +10% | $40,378 |
| Spend -10% | $31,645 |
| Fixed costs +10% | $32,672 |
| Fixed costs -10% | $39,350 |

## ROI Metrics
- Startup cost (likely): $620,000
- Payback period: 1.15 years

## Break-even Snapshots
- Monthly fixed costs: $33,388
- Gross margin (after variable costs): 64.4%
- Break-even sales (monthly): $51,812
- Break-even sales (per day, operating): $1,727
- Break-even sales (per day, after debt): $2,095

## Compliance Warnings
- Alcohol sales are prohibited from 02:00-10:00 and before Sunday noon.
- Late-night mode may require a special exception for midnight-2am alcohol service.
- Last call should be 01:30-01:45 to clear drinks by 02:00.
- Operating after 2am without alcohol is high risk; docs say 24-hour operation is not feasible.

## Notes
- Food COGS and other opex are placeholders; adjust in model/assumptions.yaml before decision-making.