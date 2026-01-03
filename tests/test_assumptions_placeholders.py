import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def get_path(d: dict, path: str):
    cur = d
    for part in path.split("."):
        if not isinstance(cur, dict) or part not in cur:
            raise KeyError(path)
        cur = cur[part]
    return cur


class AssumptionsNoPlaceholders(unittest.TestCase):
    def test_required_assumptions_are_not_placeholders(self):
        a = yaml.safe_load((ROOT / "model" / "assumptions.yaml").read_text(encoding="utf-8-sig"))

        required_paths = [
            "facility.hvac.service_contract_per_year",
            "facility.hvac.filter_replacement_per_month",
            "facility.hvac.hvac_maintenance_reserve_per_year",
            "music_licensing.total_music_licenses_per_year",
            "pos_stack.monthly_software_fee",
            "pos_stack.payment_processing_pct",
            "pos_stack.card_mix_pct",
            "marketing.monthly_budget",
            "maintenance.annual_budget_12_tables.total_high",
            "maintenance.annual_budget_24_tables.total_high",
        ]

        for p in required_paths:
            v = get_path(a, p)
            self.assertNotEqual(str(v).strip().upper(), "PLACEHOLDER", f"{p} is PLACEHOLDER")


if __name__ == "__main__":
    unittest.main()
