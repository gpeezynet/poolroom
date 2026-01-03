# DR-06 Insurance (General + Liquor Liability)

## Meta
id: DR-06
name: Insurance (General + Liquor Liability)
gate: Gate 1
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
| General liability premium (annual) | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| Liquor liability premium (annual) | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| Assault/battery coverage limit | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |

## YAML Mapping
Update these keys in model/assumptions.yaml (match existing structure):
- insurance.general_liability_per_year.low/mid/high
- insurance.liquor_liability_per_year.low/mid/high
- insurance.liability_limits.assault_battery
- insurance.deductible_per_claim
- insurance.broker_fee_per_year

Citations format requirement: each numeric claim must have a citation or be tagged PLACEHOLDER.

## FINDINGS
### Summary

### Numbers Table

### Risks

### Recommendations

### Citations
