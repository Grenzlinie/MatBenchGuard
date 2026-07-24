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


review_test = load("review_test_builder", ROOT / "tests/test_materials_agent_final_decision.py")
repair = load("repair_validator", ROOT / ".cursor/skills/materials-benchmark-repair/scripts/validate_repair_report.py")


class RepairReportTests(unittest.TestCase):
    def test_repaired_requires_valid_pass_reaudit_and_causal_regression(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            decision = review_test.decision()
            decision["mode"] = "REPAIR_REAUDIT"
            (root / "decision.json").write_text(json.dumps(decision), encoding="utf-8")
            source_decision = review_test.decision()
            source_decision["criteria"]["2.2"]["status"] = "FAIL"
            source_decision["verdict"] = "CONDITIONAL"
            (root / "source-decision.json").write_text(json.dumps(source_decision), encoding="utf-8")
            report = {
                "schema_version": repair.SCHEMA,
                "source_package": "source", "candidate_package": "candidate",
                "source_decision": "source-decision.json", "reaudit_decision": "decision.json",
                "reaudit_verdict": "PASS", "outcome": "REPAIRED", "publishable": True,
                "targets": [{"finding_id": "F-1", "decision": "AUTO_FIX", "rationale": "Unique wiring fix.", "resolved": True}],
                "changes": [{"finding_id": "F-1", "path": "tests/checker.py", "before_sha256": "sha256:before", "after_sha256": "sha256:after", "evidence": "Scorer binding restored."}],
                "regressions": [{"finding_id": "F-1", "specification": "valid output is scored", "before_passed": False, "after_passed": True}],
                "unresolved_findings": [], "limitations": [],
            }
            self.assertEqual(repair.validate(report, report_path=root / "report.json")["outcome"], "REPAIRED")

            report["regressions"][0]["before_passed"] = True
            with self.assertRaisesRegex(ValueError, "fail before"):
                repair.validate(report, report_path=root / "report.json")

    def test_conditional_candidate_is_never_publishable(self) -> None:
        report = {
            "schema_version": repair.SCHEMA,
            "source_package": "source", "candidate_package": "candidate",
            "source_decision": "source.json", "reaudit_decision": "reaudit.json",
            "reaudit_verdict": "CONDITIONAL", "outcome": "PARTIALLY_REPAIRED", "publishable": False,
                "targets": [{"finding_id": "F-1", "decision": "ASSISTED_FIX", "rationale": "Evidence-backed attempt.", "resolved": False}],
                "changes": [], "regressions": [], "unresolved_findings": ["F-1"], "limitations": [],
        }
        self.assertEqual(repair.validate(report)["outcome"], "PARTIALLY_REPAIRED")
        report["publishable"] = True
        with self.assertRaisesRegex(ValueError, "publishable"):
            repair.validate(report)


if __name__ == "__main__":
    unittest.main()
