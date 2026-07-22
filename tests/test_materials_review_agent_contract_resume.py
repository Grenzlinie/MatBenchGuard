from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / ".cursor/skills/materials-benchmark-review/scripts"
sys.path.insert(0, str(SCRIPTS))

import agent_contract_wiring  # noqa: E402
import deterministic_contract  # noqa: E402
import run_review  # noqa: E402


def unavailable_machine_contract() -> dict[str, object]:
    return deterministic_contract.evaluate_deterministic_contract(
        normalized_instruction_contract={},
        grading_contract={},
        checker_analysis={
            "d6_core_output_scoring": {"status": "UNKNOWN"},
        },
        package_roles={},
        findings=[],
    )


def valid_contract_assessment(
    machine: dict[str, object],
    *,
    d6_status: str = "PASS",
) -> dict[str, object]:
    checks = {
        check_id: {
            "status": d6_status if check_id == "D6" else "NOT_PROVEN",
            "rationale": f"{check_id} contract wiring is established",
            "evidence": (
                [
                    {
                        "source_kind": "DETERMINISTIC_PROBE_ARTIFACT",
                        "path": "deterministic_core/probe_results.json",
                        "scope": "CONTRACT_WIRING",
                        "claim": claim,
                        "quote": f'"{claim}": "PROVEN"',
                        "artifact_digest": "sha256:" + "1" * 64,
                    }
                    for claim in agent_contract_wiring.D6_CHAIN_STATES
                ]
                if check_id == "D6"
                else []
            ),
            **(
                {
                    "chain_states": {
                        name: "PROVEN"
                        for name in agent_contract_wiring.D6_CHAIN_STATES
                    }
                }
                if check_id == "D6" and d6_status == "PASS"
                else {}
            ),
        }
        for check_id in deterministic_contract.CHECK_IDS
    }
    return agent_contract_wiring.make_agent_contract_assessment(
        machine, checks
    )


class MaterialsReviewAgentContractResumeTests(unittest.TestCase):
    def test_pending_requires_only_unavailable_wiring_gaps(self) -> None:
        machine = unavailable_machine_contract()
        clean_context = {"hard_gates": [], "findings": []}
        self.assertTrue(
            run_review.agent_contract_pending_eligible(
                machine, clean_context
            )
        )
        quality_context = {
            "hard_gates": [],
            "findings": [
                {
                    "lane": "agent_quality",
                    "status": "OPEN",
                    "severity": "HIGH",
                    "repairable": True,
                }
            ],
        }
        self.assertTrue(
            run_review.agent_contract_pending_eligible(
                machine, quality_context
            )
        )

        cases = {
            "machine_fail": (
                {**machine, "checks": [
                    {**check, "status": "FAIL"}
                    if check["check_id"] == "D1"
                    else check
                    for check in machine["checks"]
                ]},
                clean_context,
            ),
            "blocking_finding": (
                {**machine, "checks": [
                    {**check, "blocking_finding_ids": ["finding-1"]}
                    if check["check_id"] == "D1"
                    else check
                    for check in machine["checks"]
                ]},
                clean_context,
            ),
            "required_queue": (
                {**machine, "repair_summary": {
                    **machine["repair_summary"], "state": "REQUIRED"
                }},
                clean_context,
            ),
            "hard_gate": (
                machine,
                {"hard_gates": [{"code": "C04", "status": "FAIL"}],
                 "findings": []},
            ),
            "runtime_contradiction": (
                {**machine, "checks": [
                    {**check, "usable_runtime_contradiction": True}
                    if check["check_id"] == "D6"
                    else check
                    for check in machine["checks"]
                ]},
                clean_context,
            ),
            "other_real_defect": (
                machine,
                {"hard_gates": [], "findings": [
                    {
                        "lane": "deterministic_core",
                        "proven_defect": True,
                        "blocking": False,
                        "advisory": False,
                    }
                ]},
            ),
        }
        for name, (candidate, report) in cases.items():
            with self.subTest(name=name):
                self.assertFalse(
                    run_review.agent_contract_pending_eligible(
                        candidate, report
                    )
                )

    def _package(self, root: Path) -> Path:
        package = root / "topic/paper-1"
        (package / "tests").mkdir(parents=True)
        (package / "instruction.md").write_text(
            "# Task\n\nPredict a materials property.\n",
            encoding="utf-8",
        )
        (package / "tests/grading_spec.json").write_text(
            "{}\n", encoding="utf-8"
        )
        (package / "tests/checker.py").write_text(
            "def check():\n    return 0\n", encoding="utf-8"
        )
        (package / "tests/test.sh").write_text(
            "#!/bin/sh\n", encoding="utf-8"
        )
        return package

    def test_pending_request_and_resume_reuse_persisted_probes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = self._package(root)
            output = root / "topic/review_outputs/1"
            machine = unavailable_machine_contract()
            calls = {"static": 0, "dynamic": 0, "resources": 0}

            def fake_static(
                _root: Path, destination: Path
            ) -> dict[str, object]:
                calls["static"] += 1
                value = {
                    "issues": [],
                    "parse_status": {
                        "tests/checker.py": "ok",
                        "tests/grading_spec.json": "ok",
                        "tests/test.sh": "ok",
                    },
                    "contract_map": {
                        "checker_analysis": {"parse_status": "OK"}
                    },
                }
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_text(json.dumps(value), encoding="utf-8")
                return value

            def fake_dynamic(
                _root: Path, destination: Path
            ) -> dict[str, object]:
                calls["dynamic"] += 1
                value = {"tests": [], "findings": []}
                destination.write_text(json.dumps(value), encoding="utf-8")
                return value

            def fake_resources(
                _root: Path, destination: Path, **_kwargs: object
            ) -> dict[str, object]:
                calls["resources"] += 1
                value = {"resources": [], "findings": [], "limitations": []}
                destination.write_text(json.dumps(value), encoding="utf-8")
                return value

            def fake_synthesize(
                _root: Path,
                temp_dir: Path,
                _static: dict[str, object],
                _checker: dict[str, object],
                **_kwargs: object,
            ) -> dict[str, object]:
                effective = _kwargs.get("agent_contract_assessment")
                report = {
                    "deterministic_contract": machine,
                    "effective_deterministic_contract": effective,
                }
                artifact = {
                    "schema_version": (
                        "materials-deterministic-core/2.0"
                    ),
                    "lane": "deterministic_core",
                    "contract": machine,
                }
                (temp_dir / "deterministic_core/report.json").write_text(
                    json.dumps(artifact), encoding="utf-8"
                )
                (temp_dir / "deterministic_core/probe_results.json").write_text(
                    json.dumps({"probe": "stable"}), encoding="utf-8"
                )
                (temp_dir / "agent_quality/assessment.json").write_text(
                    json.dumps(
                        {
                            "schema_version": (
                                "materials-agent-quality-assessment/1.0"
                            ),
                            "assessment": {},
                        }
                    ),
                    encoding="utf-8",
                )
                return report

            def fake_finalize(
                _root: Path, *, output_dir: Path, **_kwargs: object
            ) -> dict[str, object]:
                return {
                    "benchmark_root": str(package),
                    "audit_dir": str(output_dir / "benchmark_audit"),
                    "audit_id": "audit-resumed",
                    "verdict": "PASS",
                }

            with patch.object(run_review.sandbox_runtime, "ensure_env"), patch.object(
                run_review, "static_audit", side_effect=fake_static
            ), patch.object(
                run_review, "dynamic_checker_probe", side_effect=fake_dynamic
            ), patch.object(
                run_review, "probe_resources", side_effect=fake_resources
            ), patch.object(
                run_review, "synthesize_report", side_effect=fake_synthesize
            ), patch.object(
                run_review, "finalize_audit", side_effect=fake_finalize
            ):
                pending = run_review.run_review(
                    package, audit_output_dir=output
                )
                self.assertEqual(
                    pending["status"], "AGENT_CONTRACT_PENDING"
                )
                request_path = output / "agent_contract/request.json"
                self.assertTrue(request_path.is_file())
                request = json.loads(request_path.read_text(encoding="utf-8"))
                self.assertEqual(
                    request["assessment_statuses"]["D6"],
                    ["PASS", "REPAIR_REQUIRED", "NOT_PROVEN"],
                )
                self.assertIn(
                    "tests/checker.py", request["d6_evidence_sources"]
                )
                self.assertEqual(
                    request["d6_chain_state_claims"],
                    list(agent_contract_wiring.D6_CHAIN_STATES),
                )
                self.assertEqual(
                    request["d6_evidence_contract"][
                        "pass_required_claims"
                    ],
                    "ALL_FIVE_PROVEN_STATES",
                )
                self.assertEqual(calls, {"static": 1, "dynamic": 1, "resources": 1})

                not_proven_path = root / "not-proven-assessment.json"
                not_proven_path.write_text(
                    json.dumps(
                        valid_contract_assessment(
                            machine, d6_status="NOT_PROVEN"
                        )
                    ),
                    encoding="utf-8",
                )
                inconclusive = run_review.run_review(
                    package,
                    audit_output_dir=output,
                    agent_contract_assessment_path=not_proven_path,
                )
                self.assertEqual(
                    inconclusive["status"], "AGENT_CONTRACT_PENDING"
                )
                self.assertEqual(
                    inconclusive["agent_contract_status"], "NOT_PROVEN"
                )
                self.assertEqual(
                    inconclusive["publishability"], "EVIDENCE_PENDING"
                )
                self.assertTrue(request_path.is_file())
                self.assertEqual(
                    calls, {"static": 1, "dynamic": 1, "resources": 1}
                )

                assessment_path = root / "contract-assessment.json"
                assessment_path.write_text(
                    json.dumps(valid_contract_assessment(machine)),
                    encoding="utf-8",
                )
                resumed = run_review.run_review(
                    package,
                    audit_output_dir=output,
                    agent_contract_assessment_path=assessment_path,
                )

            self.assertEqual(resumed["agent_contract_status"], "APPLIED")
            self.assertEqual(calls, {"static": 1, "dynamic": 1, "resources": 1})
            self.assertFalse(request_path.exists())
            self.assertTrue(
                (output / "agent_contract/history/audit-resumed.json").is_file()
            )

    def test_tampered_pending_request_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = self._package(root)
            output = root / "topic/review_outputs/1"
            machine = unavailable_machine_contract()

            def fake_static(
                _root: Path, destination: Path
            ) -> dict[str, object]:
                value = {
                    "issues": [],
                    "parse_status": {
                        "tests/checker.py": "ok",
                        "tests/grading_spec.json": "ok",
                        "tests/test.sh": "ok",
                    },
                    "contract_map": {
                        "checker_analysis": {"parse_status": "OK"}
                    },
                }
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_text(json.dumps(value), encoding="utf-8")
                return value

            def fake_dynamic(
                _root: Path, destination: Path
            ) -> dict[str, object]:
                destination.write_text("{}", encoding="utf-8")
                return {}

            def fake_resources(
                _root: Path, destination: Path, **_kwargs: object
            ) -> dict[str, object]:
                value = {"resources": [], "findings": [], "limitations": []}
                destination.write_text(json.dumps(value), encoding="utf-8")
                return value

            def fake_synthesize(
                _root: Path,
                temp_dir: Path,
                _static: dict[str, object],
                _checker: dict[str, object],
                **_kwargs: object,
            ) -> dict[str, object]:
                artifact = {
                    "schema_version": "materials-deterministic-core/2.0",
                    "lane": "deterministic_core",
                    "contract": machine,
                }
                (temp_dir / "deterministic_core/report.json").write_text(
                    json.dumps(artifact), encoding="utf-8"
                )
                (temp_dir / "deterministic_core/probe_results.json").write_text(
                    json.dumps({"probe": "stable"}), encoding="utf-8"
                )
                (temp_dir / "agent_quality/assessment.json").write_text(
                    json.dumps(
                        {
                            "schema_version": (
                                "materials-agent-quality-assessment/1.0"
                            ),
                            "assessment": {},
                        }
                    ),
                    encoding="utf-8",
                )
                return {"deterministic_contract": machine}

            with patch.object(run_review.sandbox_runtime, "ensure_env"), patch.object(
                run_review, "static_audit", side_effect=fake_static
            ), patch.object(
                run_review, "dynamic_checker_probe", side_effect=fake_dynamic
            ), patch.object(
                run_review, "probe_resources", side_effect=fake_resources
            ), patch.object(
                run_review, "synthesize_report", side_effect=fake_synthesize
            ):
                run_review.run_review(package, audit_output_dir=output)
                request_path = output / "agent_contract/request.json"
                request = json.loads(request_path.read_text(encoding="utf-8"))
                temp_dir = Path(request["audit_temp_dir"])
                probe_path = temp_dir / "deterministic_core/probe_results.json"
                quality_path = temp_dir / "agent_quality/assessment.json"
                original_probe = probe_path.read_text(encoding="utf-8")
                original_quality = quality_path.read_text(encoding="utf-8")
                quality_path.write_text(
                    original_quality + "tampered",
                    encoding="utf-8",
                )
                with self.assertRaisesRegex(ValueError, "quality assessment"):
                    run_review.run_review(
                        package, audit_output_dir=output
                    )
                quality_path.write_text(original_quality, encoding="utf-8")
                probe_path.write_text('{"probe":"tampered"}', encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "probe hash"):
                    run_review.run_review(
                        package, audit_output_dir=output
                    )
                probe_path.write_text(original_probe, encoding="utf-8")
                request = json.loads(request_path.read_text(encoding="utf-8"))
                request["probe_hash"] = "sha256:tampered"
                request_path.write_text(
                    json.dumps(request), encoding="utf-8"
                )
                with self.assertRaisesRegex(ValueError, "request digest"):
                    run_review.run_review(
                        package, audit_output_dir=output
                    )


if __name__ == "__main__":
    unittest.main()
