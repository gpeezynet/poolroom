# Poolroom ROI Model

This project turns the Deep Research notes into a deterministic ROI calculator and report generator for the Huntsville poolroom concept.

- Project guardrails: `docs/PROJECT_GUARDRAILS.md`

## Setup

1) Create and activate a virtual environment.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2) Install dependencies.

```powershell
pip install -r requirements.txt
```

## Run scenarios

```powershell
python -m src.cli run --scenario S12
python -m src.cli run --scenario S24
python -m src.cli run --all
```

Outputs land in `out/` as `{SCENARIO}_report.md` and `{SCENARIO}_summary.json`.

## Assumptions that drive results

All defaults live in `model/assumptions.yaml` and are sourced from the Deep Research docs in `docs/`:

- Rent, CAM, utilities, and lease norms
- Alcohol hour constraints and late-hours permit risk flag
- Space program rules (sf per table, bar/kitchen/restrooms/storage allocations)
- Bar COGS targets, labor % targets, staffing roles by time block, security cost ranges
- Pricing and utilization assumptions for tables and average check sizes

Scenario sizing and startup cost estimates live in `model/scenarios.yaml`.

## How to edit assumptions safely

1) Keep the numeric defaults tied to the docs unless you label a value as a placeholder.
2) Update one category at a time (rent/CAM, utilization, checks, labor, etc.) and rerun the scenario.
3) If you change table pricing style to `wristband`, review the `wristband_count_method` in `model/assumptions.yaml` to avoid double-counting guests.
4) If you change square footage or tables, review rent, CAM, and utilization assumptions for consistency.

## How to run Deep Research in this repo

1) Open a `docs/DR-XX_*.md` file, copy the Prompt block, and run the research.
2) Paste results into the FINDINGS section and update `model/assumptions.yaml` per the YAML Mapping.
3) Run `python -m src.cli run --all` to refresh outputs.

## Deep Research sources

The canonical inputs are stored in `docs/` with a URL list in `docs/SOURCES.md`.
