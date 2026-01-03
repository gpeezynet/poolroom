from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict

import yaml

from .model import compute_scenario
from .report import render_report


def load_yaml(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8-sig") as handle:
        return yaml.safe_load(handle)


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")


def run_scenarios(assumptions_path: Path, scenarios_path: Path, out_dir: Path, ids: list[str]) -> None:
    assumptions = load_yaml(assumptions_path)
    scenarios = load_yaml(scenarios_path)["scenarios"]

    out_dir.mkdir(parents=True, exist_ok=True)

    for scenario_id in ids:
        if scenario_id not in scenarios:
            raise SystemExit(f"Unknown scenario '{scenario_id}'.")
        result = compute_scenario(assumptions, scenario_id, scenarios[scenario_id])

        report_path = out_dir / f"{scenario_id}_report.md"
        summary_path = out_dir / f"{scenario_id}_summary.json"

        report_path.write_text(render_report(result), encoding="utf-8")
        write_json(summary_path, result)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Poolroom ROI model")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Run scenario models")
    run_parser.add_argument("--scenario", help="Scenario ID to run")
    run_parser.add_argument("--all", action="store_true", help="Run all scenarios")
    run_parser.add_argument(
        "--assumptions",
        default="model/assumptions.yaml",
        help="Path to assumptions.yaml",
    )
    run_parser.add_argument(
        "--scenarios",
        default="model/scenarios.yaml",
        help="Path to scenarios.yaml",
    )
    run_parser.add_argument(
        "--out-dir",
        default="out",
        help="Output directory for reports",
    )

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "run":
        if not args.all and not args.scenario:
            raise SystemExit("Provide --scenario or --all")

        assumptions_path = Path(args.assumptions)
        scenarios_path = Path(args.scenarios)
        out_dir = Path(args.out_dir)

        scenarios_data = load_yaml(scenarios_path)
        scenario_ids = list(scenarios_data["scenarios"].keys())

        if args.all:
            ids = scenario_ids
        else:
            ids = [args.scenario]

        run_scenarios(assumptions_path, scenarios_path, out_dir, ids)


if __name__ == "__main__":
    main()
