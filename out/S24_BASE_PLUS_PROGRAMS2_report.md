# ROI Report: S24_BASE_PLUS_PROGRAMS2 - 24-table base + programs (drivers)

## Scenario Inputs
- Tables: 24
- Size: 15000 sf
- Pricing style: hourly
- Rent/CAM: $18.50/sf/yr, $3.50/sf/yr
- Lease band: mid
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
- Total monthly sales: $251,152

- Bar COGS: $30,856
- Food COGS: $11,649
- Labor: $0
- Rent: $24,667
- CAM: $4,667
- Property tax/insurance (NNN): $2,667
- Utilities: $6,000
- Total occupancy cost: $32,000
- Insurance: $500
- Security: $0
- POS software: $180
- Payment processing: $6,329
- Music licensing: $204
- Marketing: $750
- HVAC service: $100
- HVAC filters: $100
- HVAC reserve: $167
- Maintenance reserve: $1,417
- Licenses & fees: $135
- Other opex (misc): $1,200
- Total expenses: $170,605

- Monthly net: $80,547
- Annual net: $966,567

## Programs (Non-table Revenue)
- Membership revenue + contribution: $3,750 / $3,188
- Membership discount cost (applied to revenue): $390 (disc 10.0%, visits/mo 2.00, discountable share 60.0%, estimated share of guests 2.7%, method discount_pct_on_member_visits)
- Membership net after discounts: $2,798
- Membership discount break-even avg sales/visit: $177
- League revenue + contribution: $240 / $192
- Event revenue + contribution: $3,600 / $2,601
- Total programs contribution: $5,980

## Programs Impact
- Program-driven table hours (monthly): 272.2
- Program-driven bar-only guests (monthly): 580
- Membership utilization uplift: 5.0%
- Membership spend uplift: 3.0%
- Program incremental labor cost (monthly): $1,128
- Program incremental security cost (monthly): $1,189
- Program net contribution (monthly): $3,273

## Fixed Cost Breakdown
- Occupancy (rent/CAM/NNN): $32,000
- Utilities total: $6,000
- Insurance: $500
- Baseline labor (schedule): $76,701
- Variable labor (top-up): max(0, labor_pct*sales - baseline labor)
- Variable labor (monthly): $0
- Total labor (monthly): $79,018
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
- Fixed costs total: $121,771

## Lease Impact
| lease_band | occupancy_cost | cash_after_debt | dscr |
| --- | --- | --- | --- |
| low | $21,333 | $81,612 | 9.75x |
| mid | $32,000 | $69,612 | 8.46x |
| high | $42,667 | $57,612 | 7.18x |
| GOOD delta vs BASE | $-10,667 | $12,000 | 1.29x |
| BAD delta vs BASE | $10,667 | $-12,000 | -1.29x |

| lease_band | rent | cam | utilities |
| --- | --- | --- | --- |
| low | $16,000 | $2,667 | $4,667 |
| mid | $24,667 | $4,667 | $6,000 |
| high | $33,333 | $6,667 | $7,333 |

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
- NOI (monthly): $78,938
- Cash flow after debt: $69,612
- DSCR: 8.46x (846.5%)

## What Must Be True (Targets)
- Cash gap (monthly): $69,612 (negative means shortfall)
- Required utilization multiplier (cash break-even): 0.65x
- Required additional sales (per day): $0
- Notes: n/a

## Sensitivity (Cash After Debt)
| Lever | Cash after debt (monthly) |
| --- | --- |
| Utilization +10% | $89,683 |
| Utilization -10% | $49,541 |
| Spend +10% | $82,407 |
| Spend -10% | $56,817 |
| Fixed costs +10% | $57,435 |
| Fixed costs -10% | $81,789 |

## ROI Metrics
- Startup cost (likely): $1,190,000
- Payback period: 1.23 years

## Break-even Snapshots
- Monthly fixed costs: $121,771
- Gross margin (after variable costs): 79.9%
- Break-even sales (monthly): $152,375
- Break-even sales (per day, operating): $5,079
- Break-even sales (per day, after debt): $5,468

## Compliance Warnings
- Alcohol sales are prohibited from 02:00-10:00 and before Sunday noon.
- Late-night mode may require a special exception for midnight-2am alcohol service.
- Last call should be 01:30-01:45 to clear drinks by 02:00.
- Operating after 2am without alcohol is high risk; docs say 24-hour operation is not feasible.

## Notes
- Food COGS and other opex are placeholders; adjust in model/assumptions.yaml before decision-making.