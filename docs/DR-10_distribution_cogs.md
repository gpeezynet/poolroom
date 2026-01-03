# DR-10 Distribution & COGS

## Meta
id: DR-10
name: Distribution & COGS
gate: Gate 2
status: PENDING
last_updated: YYYY-MM-DD
owner: TBD

## Prompt
```text
You are running Deep Research for the poolroom model. Use the Meta section above for id, name, and gate. Scope is Huntsville, AL unless explicitly noted. Do not invent numbers. Extract numeric assumptions with low/mid/high ranges and cite sources for each numeric claim, or tag it PLACEHOLDER. Return findings by filling the FINDINGS section below, keeping headings intact.
```

## Deliverables
- Summary for the topic scope.
- Numbers table with low/mid/high ranges.
- Risks and recommendations tied to the ROI model.
- Citations list with URLs.

## Assumptions to Extract
| Assumption | Low | Mid | High | Notes | Source |
| --- | --- | --- | --- | --- | --- |
| Distributor discount percent (beer/liquor/wine) | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| Delivery fees (monthly) | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| Keg deposit per keg | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |

## YAML Mapping
Update these keys in model/assumptions.yaml (match existing structure):
- cogs.distribution.beer_discount_pct
- cogs.distribution.liquor_discount_pct
- cogs.distribution.wine_discount_pct
- cogs.distribution.delivery_fee_per_month
- cogs.distribution.keg_deposit_per_keg

Citations format requirement: each numeric claim must have a citation or be tagged PLACEHOLDER.

## FINDINGS
### Summary

### Numbers Table

### Risks

### Recommendations

### Citations
