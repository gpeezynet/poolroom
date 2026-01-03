# DR-20 Ops Binder & SOPs

## Meta
id: DR-20
name: Ops Binder & SOPs
gate: Gate 4
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
| Training hours per role | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| SOP update cadence (months) | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| Compliance audit frequency | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |

## YAML Mapping
Update these keys in model/assumptions.yaml (match existing structure):
- ops_binder.training_hours_per_role
- ops_binder.sop_update_cadence_months
- ops_binder.compliance_audit_frequency_per_year
- ops_binder.checklist_count

Citations format requirement: each numeric claim must have a citation or be tagged PLACEHOLDER.

## FINDINGS
### Summary

### Numbers Table

### Risks

### Recommendations

### Citations
