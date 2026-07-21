from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = (
    REPO_ROOT
    / ".cursor"
    / "skills"
    / "materials-benchmark-review"
    / "scripts"
)
sys.path.insert(0, str(SCRIPTS))

import deterministic_contract  # noqa: E402
import dynamic_checker_probe  # noqa: E402


class MaterialsCheckerScientificProbeTests(unittest.TestCase):
    def test_schema_derived_cases_include_malformed_full_partial_and_wrong(self) -> None:
        specification = {
            "output_contract": {
                "outputs": [
                    {
                        "file": "result.json",
                        "format": "json",
                        "schema": {"required": {"prediction": {"type": "number"}}},
                    },
                    {
                        "file": "support.csv",
                        "format": "csv",
                        "schema": {
                            "required_columns": [
                                {"name": "x"},
                                {"name": "y"},
                            ]
                        },
                    },
                ]
            },
            "steps": [
                {"id": "result", "output_file": "result.json", "weight": 0.6},
                {"id": "support", "output_file": "support.csv", "weight": 0.4},
            ],
        }
        with tempfile.TemporaryDirectory() as temporary:
            oracle = Path(temporary) / "oracle"
            oracle.mkdir()
            dynamic_checker_probe.write_synthetic_outputs(
                oracle, specification, "full"
            )
            plan, reason = dynamic_checker_probe.schema_derived_probe_plan(
                specification, oracle
            )

        self.assertIsNone(reason)
        self.assertEqual(plan[0]["case"], "all_wrong")
        self.assertEqual(
            [item["case"] for item in plan[1:]],
            ["partial__result", "partial__support"],
        )
        self.assertTrue(
            all(
                item["probe_origin"] == "SCHEMA_DERIVED_DETERMINISTIC"
                for item in plan
            )
        )

    def test_malformed_outputs_are_generated_from_declared_contract(self) -> None:
        specification = {
            "output_contract": {
                "outputs": [
                    {
                        "file": "result.json",
                        "format": "json",
                        "schema": {"required": {"prediction": {"type": "number"}}},
                    }
                ]
            }
        }
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            created = dynamic_checker_probe.write_malformed_outputs(
                output, specification
            )
            self.assertEqual(created, ["result.json"])
            self.assertEqual(
                (output / "result.json").read_text(encoding="utf-8"),
                '{"malformed": ',
            )

    def test_quality_findings_have_no_deterministic_ownership(self) -> None:
        findings = deterministic_contract.annotate_findings(
            [
                {
                    "finding_id": "quality-1",
                    "title": "SCIENTIFIC_QUALITY_GRADIENT_VIOLATION",
                    "status": "OPEN",
                    "repairable": True,
                    "evidence": {"probe_class": "discrimination"},
                },
                {
                    "finding_id": "core-1",
                    "title": "CORE_RUNTIME_ORDERING_VIOLATION",
                    "status": "OPEN",
                    "repairable": True,
                    "evidence": {"deterministic_core": True},
                },
            ]
        )
        by_id = {item["finding_id"]: item for item in findings}
        self.assertEqual(by_id["quality-1"]["lane"], "quality_results")
        self.assertIsNone(by_id["quality-1"]["deterministic_check"])
        self.assertFalse(by_id["quality-1"]["blocking"])
        self.assertEqual(by_id["core-1"]["deterministic_check"], "D6")
        self.assertTrue(by_id["core-1"]["blocking"])

    def test_oracle_is_the_only_positive_probe_source(self) -> None:
        specification = {
            "output_contract": {
                "outputs": [{"file": "result.json", "format": "json"}]
            },
            "steps": [{"id": "result", "output_file": "result.json", "weight": 1.0}],
        }
        plan, reason = dynamic_checker_probe.schema_derived_probe_plan(
            specification, None
        )
        self.assertEqual(plan, [])
        self.assertIn("isolated Oracle", reason or "")



if __name__ == "__main__":
    unittest.main()
