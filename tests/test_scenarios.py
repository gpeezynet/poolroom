import json
import subprocess
import sys
import tempfile
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def run_cli(args):
    cmd = [sys.executable, "-m", "src.cli", "run"] + args
    result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    if result.returncode != 0:
        raise AssertionError(result.stderr or result.stdout)


class ScenarioSmokeTests(unittest.TestCase):
    def _assert_outputs(self, scenario_id: str) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            out_dir = Path(tmpdir)
            run_cli(["--scenario", scenario_id, "--out-dir", str(out_dir)])

            report = out_dir / f"{scenario_id}_report.md"
            summary = out_dir / f"{scenario_id}_summary.json"

            self.assertTrue(report.exists(), f"Missing report for {scenario_id}")
            self.assertTrue(summary.exists(), f"Missing summary for {scenario_id}")

            self.assertTrue(report.read_text(encoding="utf-8").strip())
            data = json.loads(summary.read_text(encoding="utf-8"))
            self.assertEqual(data.get("scenario_id"), scenario_id)

    def test_s12_outputs(self):
        self._assert_outputs("S12")

    def test_s24_outputs(self):
        self._assert_outputs("S24")


if __name__ == "__main__":
    unittest.main()
