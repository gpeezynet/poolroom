# DR-17 Utilities & HVAC

## Meta
id: DR-17
name: Utilities & HVAC
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
| HVAC service contract (annual) | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| Utility deposit months | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| Seasonal utility variance | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |

## YAML Mapping
Update these keys in model/assumptions.yaml (match existing structure):
- facility.utilities_per_month.low/mid/high
- facility.hvac.service_contract_per_year
- facility.utility_deposit_months
- facility.hvac.hvac_maintenance_reserve_per_year
- facility.hvac.filter_replacement_per_month

Citations format requirement: each numeric claim must have a citation or be tagged PLACEHOLDER.

## FINDINGS
### Summary

### Numbers Table

### Risks

### Recommendations

### Citations
