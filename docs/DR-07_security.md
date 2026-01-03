# DR-07 Security Staffing & Controls

## Meta
id: DR-07
name: Security Staffing & Controls
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
| Security guard hourly rate | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| CCTV system upfront cost | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| ID scanner monthly fee | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |

## YAML Mapping
Update these keys in model/assumptions.yaml (match existing structure):
- security.hourly_rate.low/high/default
- security.camera_system.upfront_cost
- security.camera_system.monthly_monitoring
- security.id_scanner.upfront_cost
- security.id_scanner.monthly_service
- security.staffing_ratio_per_100_patrons

Citations format requirement: each numeric claim must have a citation or be tagged PLACEHOLDER.

## FINDINGS
### Summary

### Numbers Table

### Risks

### Recommendations

### Citations
