# ROI Report: S12_BASE_PLUS_PROGRAMS2_BASE_LEASE - 12-table base + programs (drivers) base lease

## Scenario Inputs
- Tables: 12
- Size: 8000 sf
- Pricing style: hourly
- Rent/CAM: $18.50/sf/yr, $3.50/sf/yr
- Lease band: mid
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
- Total monthly sales: $145,679

- Bar COGS: $18,326
- Food COGS: $6,428
- Labor: $21,725
- Rent: $13,875
- CAM: $2,625
- Property tax/insurance (NNN): $1,500
- Utilities: $3,375
- Total occupancy cost: $18,000
- Insurance: $500
- Security: $0
- POS software: $180
- Payment processing: $3,671
- Music licensing: $204
- Marketing: $750
- HVAC service: $100
- HVAC filters: $100
- HVAC reserve: $167
- Maintenance reserve: $708
- Licenses & fees: $96
- Other opex (misc): $1,200
- Total expenses: $85,855

- Monthly net: $59,824
- Annual net: $717,891

## Programs (Non-table Revenue)
- Membership revenue + contribution: $3,750 / $3,188
- Membership discount cost (applied to revenue): $387 (disc 10.0%, visits/mo 2.00, discountable share 60.0%, estimated share of guests 4.7%, method discount_pct_on_member_visits)
- Membership net after discounts: $2,800
- Membership discount break-even avg sales/visit: $177
- League revenue + contribution: $240 / $192
- Event revenue + contribution: $3,600 / $2,601
- Total programs contribution: $5,980

## Programs Impact
- Program-driven table hours (monthly): 136.1
- Program-driven bar-only guests (monthly): 580
- Membership utilization uplift: 5.0%
- Membership spend uplift: 3.0%
- Program incremental labor cost (monthly): $1,128
- Program incremental security cost (monthly): $1,189
- Program net contribution (monthly): $3,276

## Fixed Cost Breakdown
- Occupancy (rent/CAM/NNN): $18,000
- Utilities total: $3,375
- Insurance: $500
- Baseline labor (schedule): $8,007
- Variable labor (top-up): max(0, labor_pct*sales - baseline labor)
- Variable labor (monthly): $21,725
- Total labor (monthly): $32,049
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
- Fixed costs total: $35,705

## Lease Impact
| lease_band | occupancy_cost | cash_after_debt | dscr |
| --- | --- | --- | --- |
| low | $12,000 | $57,849 | 9.13x |
| mid | $18,000 | $51,099 | 8.18x |
| high | $24,000 | $44,349 | 7.23x |
| GOOD delta vs BASE | $-6,000 | $6,750 | 0.95x |
| BAD delta vs BASE | $6,000 | $-6,750 | -0.95x |

| lease_band | rent | cam | utilities |
| --- | --- | --- | --- |
| low | $9,000 | $1,500 | $2,625 |
| mid | $13,875 | $2,625 | $3,375 |
| high | $18,750 | $3,750 | $4,125 |

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
- NOI (monthly): $58,215
- Cash flow after debt: $51,099
- DSCR: 8.18x (818.1%)

## What Must Be True (Targets)
- Cash gap (monthly): $51,099 (negative means shortfall)
- Required utilization multiplier (cash break-even): 0.46x
- Required additional sales (per day): $0
- Notes: n/a

## Sensitivity (Cash After Debt)
| Lever | Cash after debt (monthly) |
| --- | --- |
| Utilization +10% | $60,491 |
| Utilization -10% | $41,707 |
| Spend +10% | $56,260 |
| Spend -10% | $45,937 |
| Fixed costs +10% | $47,528 |
| Fixed costs -10% | $54,669 |

## ROI Metrics
- Startup cost (likely): $620,000
- Payback period: 0.86 years

## Break-even Snapshots
- Monthly fixed costs: $35,705
- Gross margin (after variable costs): 64.5%
- Break-even sales (monthly): $55,382
- Break-even sales (per day, operating): $1,846
- Break-even sales (per day, after debt): $2,214

## Compliance Warnings
- Alcohol sales are prohibited from 02:00-10:00 and before Sunday noon.
- Late-night mode may require a special exception for midnight-2am alcohol service.
- Last call should be 01:30-01:45 to clear drinks by 02:00.
- Operating after 2am without alcohol is high risk; docs say 24-hour operation is not feasible.

## Notes
- Food COGS and other opex are placeholders; adjust in model/assumptions.yaml before decision-making.