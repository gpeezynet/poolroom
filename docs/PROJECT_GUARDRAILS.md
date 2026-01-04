# Poolroom Model  Project Guardrails

## North Star
Build a decision-grade ROI model for a Huntsville, AL poolroom + full bar that can answer:
- Go / No-Go
- 12-table open vs 24-table expansion
- Standard hours vs late-night mode
- Financing feasibility (debt service + DSCR)
- What must be true for profitability (thresholds)

This is not a fun calculator. Its a decision machine.

---

## Output Artifacts (Repo Deliverables)
### Always maintained
- `model/assumptions.yaml`  real-world defaults (no placeholders) + source notes in docs
- `model/scenarios.yaml`  scenario definitions (S12, S24 + variants)
- `src/`  model + report generation
- `tests/`  smoke tests + placeholder guards (must stay green)
- `docs/SOURCES.md`  citations + links used to set assumptions
- `docs/ASSUMPTIONS_CATALOG.md`  human-auditable list of assumptions + where they live + why

### Generated outputs
- `out/*_report.md`  readable reports
- `out/*_summary.json`  structured outputs for analysis

---

## Linear Path (Milestones) + Gates

### M1  Tooling Reliability (DONE)
**Goal:** the pipeline runs cleanly every time.
**Gate:**
- `python -m unittest discover -s tests -p "test_*.py" -v` passes
- `python -m src.cli run --all` generates outputs

### M2  Assumptions Become Real (CURRENT)
**Goal:** replace placeholders/hand-waves with sourced defaults.
**Deliverables:**
- assumptions filled with realistic Huntsville defaults
- `docs/SOURCES.md` updated with citations
- `docs/ASSUMPTIONS_CATALOG.md` created/updated
**Gate:** no placeholder assumptions; reports look sane; big drivers are sourced.

### M3  Operating Model Logic (Hours + Staffing + Late-Night Mode)
**Goal:** stop lying to ourselves about labor/security/late-night.
**Deliverables:**
- standard mode vs late-night mode model logic
- staffing templates by time block
- late-night incremental profitability threshold output
**Gate:** model explicitly answers when late-night is worth it.

### M4  CAPEX + Financing Realism
**Goal:** convert monthly profitability into bankable feasibility.
**Deliverables:**
- CAPEX for 12-table opening + 24-table expansion
- debt service + DSCR outputs
- can it carry the debt? result in reports
**Gate:** finance feasibility is explicit and testable.

### M5  Site + Rent Comps + Space Program Lock-In
**Goal:** site choice doesnt silently sabotage the plan.
**Deliverables:**
- rent/CAM/utilities assumptions integrated
- space program constraints summarized (sqft + layout rules)
**Gate:** you can compare sites apples-to-apples.

### M6  Decision Pack (Final)
**Goal:** produce a defendable, shareable decision packet.
**Deliverables:**
- scenario reports (S12/S24 + conservative/base/upside)
- sensitivity checks on rent/labor/utilization/check size
- go/no-go summary: break-even guests/day + revenue/day + membership base needed
**Gate:** can be handed to a banker/partner without embarrassment.

---

## Scope Control Rules (Anti-Sauce)
1) If it doesnt change a decision, its backlog.
2) No new feature unless it supports a milestone gate.
3) Every new assumption must have:
   - a value in `model/assumptions.yaml`
   - a rationale + source in `docs/SOURCES.md`
   - an entry in `docs/ASSUMPTIONS_CATALOG.md` if its a top-20 driver
4) Any change that affects outputs must be paired with:
   - updated tests (or confirmation existing tests cover it)
   - regenerated `out/` (optional to commit, but must be reproducible)

---

## Definition of Done (per PR)
- Tests green:
  - `python -m unittest discover -s tests -p "test_*.py" -v`
- CLI run succeeds:
  - `python -m src.cli run --all`
- If assumptions changed:
  - `docs/SOURCES.md` updated
  - `docs/ASSUMPTIONS_CATALOG.md` updated (if major driver)

---

## Standard Commands
- Run tests:
  - `python -m unittest discover -s tests -p "test_*.py" -v`
- Run all scenarios:
  - `python -m src.cli run --all`
- Create a fresh zip bundle:
  - `Compress-Archive -Path @("README.md","requirements.txt","docs","model","src","tests","deep_research") -DestinationPath $zip -Force`

---

## Backlog Parking Lot (Allowed, but not blocking)
- Screen/kiosk mode, UX polish, charts
- Fancy Monte Carlo simulations
- Multi-location scaling
- Anything not required to clear the next milestone gate
