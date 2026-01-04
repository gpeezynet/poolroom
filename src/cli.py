from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict

import yaml

from .model import compute_scenario
from .matrix import write_scenario_matrix
from .report import render_report
from .sensitivity import run_sensitivity


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

    results = []
    for scenario_id in ids:
        if scenario_id not in scenarios:
            raise SystemExit(f"Unknown scenario '{scenario_id}'.")
        result = compute_scenario(assumptions, scenario_id, scenarios[scenario_id])
        results.append(result)

    results_by_id = {result["scenario_id"]: result for result in results}

    for result in results:
        scenario_id = result["scenario_id"]
        report_path = out_dir / f"{scenario_id}_report.md"
        summary_path = out_dir / f"{scenario_id}_summary.json"

        report_path.write_text(render_report(result, results_by_id), encoding="utf-8")
        write_json(summary_path, result)
        print(
            f"Generated {report_path.as_posix()} and {summary_path.as_posix()}"
        )
    write_scenario_matrix(results, out_dir)


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

    sensitivity_parser = subparsers.add_parser(
        "sensitivity", help="Run program driver sensitivity sweep"
    )
    sensitivity_parser.add_argument(
        "--scenario",
        required=True,
        help="Scenario ID to sweep (ex: S12_BASE_PLUS_PROGRAMS2)",
    )
    sensitivity_parser.add_argument(
        "--assumptions",
        default="model/assumptions.yaml",
        help="Path to assumptions.yaml",
    )
    sensitivity_parser.add_argument(
        "--scenarios",
        default="model/scenarios.yaml",
        help="Path to scenarios.yaml",
    )
    sensitivity_parser.add_argument(
        "--out-dir",
        default="out",
        help="Output directory for sensitivity results",
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
    elif args.command == "sensitivity":
        assumptions_path = Path(args.assumptions)
        scenarios_path = Path(args.scenarios)
        out_dir = Path(args.out_dir)
        run_sensitivity(assumptions_path, scenarios_path, out_dir, args.scenario)


if __name__ == "__main__":
    main()
