# DR-16 Equipment Procurement

## Meta
id: DR-16
name: Equipment Procurement
gate: Gate 3
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
| Pool table cost per unit | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| Table install cost per unit | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| Table lighting cost per unit | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |

## YAML Mapping
Update these keys in model/assumptions.yaml (match existing structure):
- equipment_procurement.table_cost_per_unit
- equipment_procurement.table_install_per_unit
- equipment_procurement.table_light_per_unit
- equipment_procurement.accessories_budget

Citations format requirement: each numeric claim must have a citation or be tagged PLACEHOLDER.

## FINDINGS
### Summary

### Numbers Table

### Risks

### Recommendations

### Citations
