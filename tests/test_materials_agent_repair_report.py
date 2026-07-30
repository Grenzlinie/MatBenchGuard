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
    "review_test_builder", ROOT / "tests/test_materials_agent_final_decision.py"
)
repair = load(
    "repair_validator",
    ROOT
    / ".cursor/skills/materials-benchmark-repair/scripts/validate_repair_report.py",
)


class RepairReportTests(unittest.TestCase):
    def test_repaired_requires_valid_pass_reaudit_and_causal_regression(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            decision = review_test.decision()
            decision["mode"] = "REPAIR_REAUDIT"
            observations = []
            for name in review_test.module.PROBES:
                observations.append(
                    {
                        "case_id": name,
                        "probe_class": name,
                        "status": "OBSERVED",
                        "reward": 0.0,
                        "breakdown": {},
                    }
                )
                decision["checker_probes"][name]["evidence"] = [
                    {
                        "source_kind": "PROBE",
                        "path": "candidate-observations.json",
                        "locator": name,
                        "quote_or_result": "executed",
                    }
                ]
            (root / "decision.json").write_text(json.dumps(decision), encoding="utf-8")
            source_decision = review_test.decision()
            source_decision["criteria"]["2.2"]["status"] = "FAIL"
            source_decision["verdict"] = "CONDITIONAL"
            source_decision["open_confirmed_findings"] = [
                {
                    "finding_id": "F-1",
                    "title": "The public contract and checker disagree.",
                    "pattern_id": None,
                    "severity": "HIGH",
                    "dimension": "C02",
                    "repairable": True,
                    "hard_gate": False,
                    "hard_gate_code": None,
                    "disposition": "REPAIR",
                    "failure_modes": [],
                    "evidence": review_test.evidence("contract/checker mismatch"),
                }
            ]
            for name in review_test.module.PROBES:
                source_decision["checker_probes"][name]["evidence"] = [
                    {
                        "source_kind": "PROBE",
                        "path": "source-observations.json",
                        "locator": name,
                        "quote_or_result": "executed",
                    }
                ]
            (root / "source-decision.json").write_text(
                json.dumps(source_decision), encoding="utf-8"
            )
            (root / "source-observations.json").write_text(
                json.dumps({"observations": observations}),
                encoding="utf-8",
            )
            (root / "candidate-observations.json").write_text(
                json.dumps({"observations": observations}),
                encoding="utf-8",
            )
            report = {
                "schema_version": repair.SCHEMA,
                "source_package": "source",
                "candidate_package": "candidate",
                "source_decision": "source-decision.json",
                "reaudit_decision": "decision.json",
                "source_probe_observations": ["source-observations.json"],
                "candidate_probe_observations": ["candidate-observations.json"],
                "reaudit_verdict": "PASS",
                "outcome": "REPAIRED",
                "publishable": True,
                "targets": [
                    {
                        "finding_id": "F-1",
                        "decision": "AUTO_FIX",
                        "rationale": "Unique wiring fix.",
                        "resolved": True,
                    }
                ],
                "changes": [
                    {
                        "finding_id": "F-1",
                        "path": "tests/checker.py",
                        "before_sha256": "sha256:before",
                        "after_sha256": "sha256:after",
                        "evidence": "Scorer binding restored.",
                    }
                ],
                "regressions": [
                    {
                        "finding_id": "F-1",
                        "specification": "valid output is scored",
                        "before_passed": False,
                        "after_passed": True,
                    }
                ],
                "impact_matrix": [
                    {
                        "finding_id": "F-1",
                        "affected_paths": ["instruction.md", "tests/checker.py"],
                        "rationale": "Public contract and scorer were checked together.",
                        "synchronized": True,
                    }
                ],
                "fresh_review": {"status": "COMPLETE", "evidence": "All phases rerun."},
                "unresolved_findings": [],
                "limitations": [],
            }
            self.assertEqual(
                repair.validate(report, report_path=root / "report.json")["outcome"],
                "REPAIRED",
            )

            with_self_check = json.loads(json.dumps(report))
            with_self_check["author_self_check"] = {
                "status": "PASS",
                "evidence": "Forbidden.",
            }
            with self.assertRaisesRegex(ValueError, "author_self_check is forbidden"):
                repair.validate(with_self_check)

            solution_change = json.loads(json.dumps(report))
            solution_change["changes"][0]["path"] = "solution/solve.sh"
            with self.assertRaisesRegex(ValueError, "must not reference solution"):
                repair.validate(solution_change)

            report["regressions"][0]["before_passed"] = True
            with self.assertRaisesRegex(ValueError, "fail before"):
                repair.validate(report, report_path=root / "report.json")

    def test_controlling_abandon_source_cannot_create_repair_report(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = review_test.decision()
            source["parameter_assessment"]["fixed_or_source_required"].update(
                {
                    "status": "FAIL",
                    "items": [
                        review_test.parameter_item(
                            "loading_rate",
                            source_status="MISSING",
                            resolution="UNRESOLVED",
                            scoring_sensitive=True,
                        )
                    ],
                }
            )
            source["criteria"]["2.3"]["status"] = "FAIL"
            source["scientific_risk_patterns"][
                "SIMULATION_CONTRACT_UNDERDETERMINED"
            ]["status"] = "FAIL"
            gate = next(
                item
                for item in source["hard_gates"]
                if item["code"] == "ESSENTIAL_SIMULATION_PARAMETER_UNAVAILABLE"
            )
            gate.update({"status": "FAIL", "disposition": "ABANDON"})
            source["open_confirmed_findings"] = [
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
            source["verdict"] = "REJECT"
            (root / "source.json").write_text(json.dumps(source), encoding="utf-8")

            report = {
                "schema_version": repair.SCHEMA,
                "source_package": "source",
                "candidate_package": "candidate",
                "source_decision": "source.json",
                "reaudit_decision": "never-read.json",
                "source_probe_observations": ["never-read-source.json"],
                "candidate_probe_observations": ["never-read-candidate.json"],
                "reaudit_verdict": "REJECT",
                "outcome": "ABANDONED",
                "publishable": False,
                "targets": [
                    {
                        "finding_id": "F-ESSENTIAL",
                        "decision": "ABANDON",
                        "rationale": "Unavailable evidence cannot be repaired.",
                        "resolved": False,
                    }
                ],
                "changes": [],
                "regressions": [],
                "impact_matrix": [],
                "fresh_review": {
                    "status": "COMPLETE",
                    "evidence": "Entry gate should stop before candidate creation.",
                },
                "unresolved_findings": ["F-ESSENTIAL"],
                "limitations": [],
            }
            with self.assertRaisesRegex(ValueError, "SCREENED_OUT"):
                repair.validate(report, report_path=root / "report.json")

    def test_conditional_candidate_is_never_publishable(self) -> None:
        report = {
            "schema_version": repair.SCHEMA,
            "source_package": "source",
            "candidate_package": "candidate",
            "source_decision": "source.json",
            "reaudit_decision": "reaudit.json",
            "source_probe_observations": ["source-observations.json"],
            "candidate_probe_observations": ["candidate-observations.json"],
            "reaudit_verdict": "CONDITIONAL",
            "outcome": "PARTIALLY_REPAIRED",
            "publishable": False,
            "targets": [
                {
                    "finding_id": "F-1",
                    "decision": "ASSISTED_FIX",
                    "rationale": "Evidence-backed attempt.",
                    "resolved": False,
                }
            ],
            "changes": [],
            "regressions": [],
            "impact_matrix": [],
            "fresh_review": {
                "status": "INCOMPLETE",
                "evidence": "Blocked by missing evidence.",
            },
            "unresolved_findings": ["F-1"],
            "limitations": [],
        }
        self.assertEqual(repair.validate(report)["outcome"], "PARTIALLY_REPAIRED")
        report["publishable"] = True
        with self.assertRaisesRegex(ValueError, "publishable"):
            repair.validate(report)


if __name__ == "__main__":
    unittest.main()
