# DR-19 Financing (SBA/Banks)

## Meta
id: DR-19
name: Financing (SBA/Banks)
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
| Loan amount | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| Interest rate | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |
| Term length (years) | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |  |  |

## YAML Mapping
Update these keys in model/assumptions.yaml (match existing structure):
- financing.loan_amount
- financing.interest_rate
- financing.term_years
- financing.down_payment_pct
- financing.sba_guarantee_fee
- financing.dscr_target

Citations format requirement: each numeric claim must have a citation or be tagged PLACEHOLDER.

## FINDINGS
### Summary

### Numbers Table

### Risks

### Recommendations

### Citations
