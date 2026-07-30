from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


review_test = load(
    "lifecycle_review_builder",
    ROOT / "tests/test_materials_agent_final_decision.py",
)
lifecycle = load(
    "lifecycle_validator",
    ROOT
    / ".cursor/skills/materials-benchmark-orchestration/scripts/validate_lifecycle.py",
)


def screened_out_decision() -> tuple[dict, dict]:
    value = review_test.decision()
    parameter = review_test.parameter_item(
        "loading_rate",
        source_status="MISSING",
        resolution="UNRESOLVED",
        scoring_sensitive=True,
    )
    value["parameter_assessment"]["fixed_or_source_required"].update(
        {"status": "FAIL", "items": [parameter]}
    )
    value["criteria"]["2.3"]["status"] = "FAIL"
    value["scientific_risk_patterns"]["SIMULATION_CONTRACT_UNDERDETERMINED"][
        "status"
    ] = "FAIL"
    gate = next(
        item
        for item in value["hard_gates"]
        if item["code"] == "ESSENTIAL_SIMULATION_PARAMETER_UNAVAILABLE"
    )
    gate.update({"status": "FAIL", "disposition": "ABANDON"})
    value["open_confirmed_findings"] = [
        {
            "finding_id": "F-ESSENTIAL",
            "title": "Essential simulation parameter is unavailable.",
            "pattern_id": "SIMULATION_CONTRACT_UNDERDETERMINED",
            "severity": "FATAL",
            "dimension": "C03",
            "repairable": False,
            "hard_gate": True,
            "hard_gate_code": "ESSENTIAL_SIMULATION_PARAMETER_UNAVAILABLE",
            "disposition": "ABANDON",
            "failure_modes": [],
            "evidence": review_test.evidence("paper does not define it"),
        }
    ]
    value["verdict"] = "REJECT"
    matrix_parameter = {**parameter, "bucket": "fixed_or_source_required"}
    matrix = {
        "schema_version": lifecycle.MATRIX_SCHEMA,
        "package_id": value["package_id"],
        "parameters": [matrix_parameter],
    }
    return value, matrix


class OrchestrationLifecycleTests(unittest.TestCase):
    def write_screened_out(self, output: Path) -> None:
        decision, matrix = screened_out_decision()
        (output / "evidence").mkdir(parents=True)
        (output / "agent_final_decision.json").write_text(
            json.dumps(decision), encoding="utf-8"
        )
        (output / "evidence/simulation_parameter_matrix.json").write_text(
            json.dumps(matrix), encoding="utf-8"
        )

    def test_valid_screened_out_lifecycle_has_no_repair_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            self.write_screened_out(output)
            self.assertEqual(
                lifecycle.validate_package_lifecycle(output), "SCREENED_OUT"
            )

            (output / "candidate").mkdir()
            with self.assertRaisesRegex(ValueError, "must not contain candidate"):
                lifecycle.validate_package_lifecycle(output)

    def test_simulation_lifecycle_requires_matching_parameter_matrix(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            self.write_screened_out(output)
            (output / "evidence/simulation_parameter_matrix.json").unlink()
            with self.assertRaisesRegex(ValueError, "required JSON"):
                lifecycle.validate_package_lifecycle(output)

            _, matrix = screened_out_decision()
            matrix["parameters"][0]["value_or_rule"] = "silently changed"
            (output / "evidence/simulation_parameter_matrix.json").write_text(
                json.dumps(matrix), encoding="utf-8"
            )
            with self.assertRaisesRegex(ValueError, "differs between matrix"):
                lifecycle.validate_package_lifecycle(output)


if __name__ == "__main__":
    unittest.main()
