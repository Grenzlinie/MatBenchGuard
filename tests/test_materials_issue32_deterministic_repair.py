from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]

def external_audit_dir(package: Path) -> Path:
    paper_id = (
        package.name[len("paper-"):]
        if package.name.startswith("paper-")
        else package.name
    )
    path = package.parent / "review_outputs" / paper_id / "benchmark_audit"
    path.mkdir(parents=True, exist_ok=True)
    return path


def external_reaudit_dir(package: Path) -> Path:
    paper_id = package.name.removeprefix("paper-")
    path = (
        package.parent
        / "review_outputs"
        / paper_id
        / "repair_reaudit"
        / "benchmark_audit"
    )
    path.mkdir(parents=True, exist_ok=True)
    return path


REVIEW_SCRIPTS = (
    REPO_ROOT / ".cursor/skills/materials-benchmark-review/scripts"
)
REPAIR_SCRIPTS = (
    REPO_ROOT / ".cursor/skills/materials-benchmark-repair/scripts"
)
sys.path.insert(0, str(REVIEW_SCRIPTS))
sys.path.insert(0, str(REPAIR_SCRIPTS))

import canonical_status  # noqa: E402
import deterministic_contract  # noqa: E402
import run_repair  # noqa: E402


HARD_GATE_CODES = (
    "NON_MATERIALS_TASK",
    "SCIENTIFIC_TARGET_INVALID",
    "CHECKER_CORE_TASK_UNASSESSED",
    "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE",
)


def required_contract() -> dict[str, Any]:
    return deterministic_contract.evaluate_deterministic_contract(
        normalized_instruction_contract={},
        grading_contract={},
        checker_analysis={},
        package_roles={},
        findings=[
            {
                "finding_id": "F1",
                "title": "ZERO_WEIGHT_SCORING_COMPONENT",
                "status": "OPEN",
                "repairable": True,
                "evidence": {},
            }
        ],
    )


def clean_contract() -> dict[str, Any]:
    return deterministic_contract.evaluate_deterministic_contract(
        normalized_instruction_contract={},
        grading_contract={},
        checker_analysis={
            "d6_core_output_scoring": {"status": "PROVEN"}
        },
        package_roles={},
        findings=[],
    )


def required_d6_contract() -> dict[str, Any]:
    return deterministic_contract.evaluate_deterministic_contract(
        normalized_instruction_contract={},
        grading_contract={},
        checker_analysis={
            "d6_core_output_scoring": {
                "status": "FAILED",
                "schema_version": "materials-d6-core-output-scoring/1.0",
            }
        },
        package_roles={},
        findings=[
            {
                "finding_id": "F6",
                "title": "CORE_RUNTIME_ORACLE_REJECTED",
                "status": "OPEN",
                "repairable": True,
                "lane": "deterministic_core",
                "evidence": {"deterministic_core": True},
            }
        ],
    )


def authoritative_pass_fields(contract: dict[str, Any]) -> dict[str, Any]:
    return {
        "summary": {
            "scoring_version": "materials-review-scoring/2.0",
            "final_verdict": "PASS",
            "publication_route": "PUBLISH_CANDIDATE",
            "scoring_version": "materials-review-scoring/2.0",
            "total_score": 90,
            "hard_gate_triggered": False,
        },
        "publishability": "PUBLISH_CANDIDATE",
        "evidence_contract": {"fail_closed": True, "gaps": []},
        "hard_gates": [
            {
                "code": code,
                "status": "PASS",
                "evidence": [{"fact": "source-bound gate evidence"}],
            }
            for code in HARD_GATE_CODES
        ],
        "deterministic_contract": contract,
        "findings": [],
    }


def deterministic_plan(
    contract: dict[str, Any],
    *,
    findings: list[dict[str, Any]] | None = None,
    binding_overrides: dict[str, Any] | None = None,
) -> dict[str, Any]:
    binding = {
        "schema_version": contract["schema_version"],
        "registry_version": contract["registry_version"],
        "contract_digest": contract["contract_digest"],
        "audit_id": "A1",
        "required_finding_ids": contract["repair_summary"][
            "required_finding_ids"
        ],
    }
    binding.update(binding_overrides or {})
    return {
        "schema_version": deterministic_contract.DETERMINISTIC_REPAIR_PLAN_SCHEMA_VERSION,
        "audit_id": "A1",
        "deterministic_contract": binding,
        "source_audit": {
            "audit_id": "A1",
            "deterministic_contract": binding,
        },
        "findings": findings
        if findings is not None
        else [
            {
                "finding_id": "F1",
                "deterministic_check": "D4",
                "finding_code": "ZERO_WEIGHT_SCORING_COMPONENT",
                "repair_class": "ASSISTED_FIX",
            }
        ],
    }


def published_bundle(
    *,
    comparison_overrides: dict[str, Any] | None = None,
    source_binding: dict[str, Any] | None = None,
) -> dict[str, Any]:
    identity = {"package_id": "P1", "package_hash": "sha256:package"}
    binding = {
        "schema_version": deterministic_contract.DETERMINISTIC_SCHEMA_VERSION,
        "registry_version": deterministic_contract.DETERMINISTIC_REGISTRY_VERSION,
        "contract_digest": "sha256:contract",
        "audit_id": "A1",
        "required_finding_ids": ["F1"],
    }
    operation = {
        "id": "op1",
        "type": "text_replace",
        "file": "instruction.md",
    }
    change = {
        "operation_id": "op1",
        "file": "instruction.md",
        "operation": "text_replace",
        "before_hash": None,
        "after_hash": "sha256:after",
        "evidence_ids": ["EV1"],
    }
    regression = {
        "id": "R1",
        "type": "file_contains",
        "finding_id": "F1",
        "file": "instruction.md",
        "expected": "fixed",
        "causal_operation_ids": ["op1"],
    }
    plan = {
        "schema_version": deterministic_contract.DETERMINISTIC_REPAIR_PLAN_SCHEMA_VERSION,
        "review_verdict": "PASS",
        "publishability": "PUBLISH_CANDIDATE",
        "repair_decision": "AUTO_FIX",
        "repair_status": "REPAIRED",
        "audit_id": "A1",
        "package_identity": identity,
        "deterministic_contract": binding,
        "source_audit": {
            "audit_id": "A1",
            "deterministic_contract": source_binding
            if source_binding is not None
            else binding,
        },
        "findings": [
            {
                "finding_id": "F1",
                "operations": [operation],
                "regression_tests": [regression],
            }
        ],
    }
    comparison = {
        "audit_id": "A1",
        "package_identity": identity,
        "target_resolved": True,
        "source_finding": {
            "audit_id": "A1",
            "package_identity": identity,
        },
        "source_configuration": {"review_lane": "dual"},
        "reaudit_configuration": {"review_lane": "dual"},
        "reaudit_audit_id": "A2",
        "reaudit_count": 1,
        "reaudit_verdict": "PASS",
        "publication_route": "PUBLISH_CANDIDATE",
        "score": 90,
        "evidence_contract_fail_closed": True,
        "evidence_contract_gaps": [],
        "hard_gate_codes": list(HARD_GATE_CODES),
        "hard_gate_statuses": ["PASS"] * len(HARD_GATE_CODES),
        "hard_gate_evidence": True,
        "deterministic_state": "CLEAN",
        "hard_gate_free": True,
        "identity_preserved": True,
        "mutation_scope_allowed": True,
        "residual_blocking_finding_ids": [],
    }
    comparison.update(comparison_overrides or {})
    history = {
        "audit_id": "A1",
        "package_identity": identity,
        "review_verdict": "PASS",
        "publishability": "PUBLISH_CANDIDATE",
        "repair_decision": "AUTO_FIX",
        "repair_status": "REPAIRED",
        "bundle_complete": True,
        "bundle_files": list(canonical_status.REPAIR_BUNDLE_FILES),
        "root_cause": "deterministic finding",
        "attempt_number": 1,
        "decision": "AUTO_FIX",
        "status": "REPAIRED",
    }
    evidence = [
        {
            "id": "EV1",
            "source": "benchmark_audit/audit_report.json",
            "audit_id": "A1",
            "package_identity": identity,
        }
    ]
    return {
        "repair_plan.json": plan,
        "changes.json": [change],
        "unresolved.json": [],
        "regression_results.json": [
            {
                "specification": regression,
                "before_passed": False,
                "after_passed": True,
            }
        ],
        "re_audit_comparison.json": comparison,
        "patch.json": {
            "schema_version": "0.1",
            "files": [change],
            "atomic_publish": True,
        },
        "evidence.json": evidence,
        "repair.log": "decision=AUTO_FIX status=REPAIRED",
        "history.json": history,
    }


class MaterialsIssue32DeterministicRepairTests(unittest.TestCase):
    def test_batch_fplan_preserves_finding_code_for_repair_gate(self) -> None:
        contract = required_contract()
        plan = deterministic_plan(
            contract,
            findings=[
                {
                    "finding_id": "F1",
                    "deterministic_check": "D4",
                    "finding_code": "WEIGHTS_NOT_ONE",
                    "repair_class": "AUTO_FIX",
                    "justification": "Normalize proven ratios.",
                    "operations": [],
                    "regression_tests": [],
                    "evidence": [],
                }
            ],
        )

        fplan = run_repair.build_fplan(plan, plan["findings"][0])

        self.assertEqual(fplan["finding_code"], "WEIGHTS_NOT_ONE")

    def test_complete_plan_binds_schema_queue_and_finding_owner(self) -> None:
        contract = required_contract()
        plan = deterministic_plan(contract)

        deterministic_contract.validate_deterministic_plan_binding(
            {"audit_id": "A1", "deterministic_contract": contract},
            plan,
        )

    def test_incomplete_plan_omits_open_blocker(self) -> None:
        contract = required_contract()
        with self.assertRaisesRegex(ValueError, "complete source queue"):
            deterministic_contract.validate_deterministic_plan_binding(
                {"audit_id": "A1", "deterministic_contract": contract},
                deterministic_plan(contract, findings=[]),
            )

    def test_stale_and_unknown_plan_bindings_fail_closed(self) -> None:
        contract = required_contract()
        stale = deterministic_plan(
            contract,
            binding_overrides={"contract_digest": "sha256:stale"},
        )
        with self.assertRaisesRegex(ValueError, "binding is stale"):
            deterministic_contract.validate_deterministic_plan_binding(
                {"audit_id": "A1", "deterministic_contract": contract},
                stale,
            )

        unknown = deterministic_plan(
            contract,
            findings=[
                {
                    "finding_id": "F1",
                    "deterministic_check": "D9",
                    "finding_code": "ZERO_WEIGHT_SCORING_COMPONENT",
                    "repair_class": "ASSISTED_FIX",
                }
            ],
        )
        with self.assertRaisesRegex(ValueError, "target check is unknown"):
            deterministic_contract.validate_deterministic_plan_binding(
                {"audit_id": "A1", "deterministic_contract": contract},
                unknown,
            )

    def test_active_ingress_rejects_legacy_plan_versions_without_history(self) -> None:
        for version in ("0.1", "0.2"):
            with self.subTest(version=version), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary) / "package"
                root.mkdir()
                (root / "instruction.md").write_text("task", encoding="utf-8")
                (root / "tests").mkdir()
                plan_path = Path(temporary) / "legacy-plan.json"
                repair_output = Path(temporary) / "repair"
                plan_path.write_text(
                    json.dumps(
                        {
                            "schema_version": version,
                            "audit_id": "paper-867767-audit",
                            "finding_id": "FINDING-001",
                            "repair_class": "ABANDON",
                            "justification": "legacy D6 abandonment",
                            "operations": [],
                            "regression_tests": [],
                            "evidence": [],
                            "repair_output_dir": str(repair_output),
                        }
                    ),
                    encoding="utf-8",
                )
                with self.assertRaisesRegex(
                    ValueError, "active Repair requires schema_version"
                ):
                    run_repair.repair(
                        root,
                        plan_path,
                        Path(temporary) / "missing-attestation.json",
                    )
                self.assertFalse(repair_output.exists())

    def test_current_ingress_requires_batch_contract_binding(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "package"
            root.mkdir()
            plan_path = Path(temporary) / "plan.json"
            plan_path.write_text(
                json.dumps(
                    {
                        "schema_version": (
                            deterministic_contract
                            .DETERMINISTIC_REPAIR_PLAN_SCHEMA_VERSION
                        ),
                        "audit_id": "A1",
                        "findings": [
                            {
                                "finding_id": "F1",
                                "deterministic_check": "D4",
                                "repair_class": "ABANDON",
                                "justification": "No admissible repair.",
                                "operations": [],
                                "regression_tests": [],
                                "evidence": [],
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "source contract binding"):
                run_repair.validate_external_plan(root, plan_path)

    def test_complete_d6_plan_may_explicitly_abandon(self) -> None:
        contract = required_d6_contract()
        plan = deterministic_plan(
            contract,
            findings=[
                {
                    "finding_id": "F6",
                    "deterministic_check": "D6",
                    "finding_code": "CORE_RUNTIME_ORACLE_REJECTED",
                    "repair_class": "ABANDON",
                    "justification": "No admissible implementation is available.",
                    "operations": [],
                    "regression_tests": [],
                    "evidence": [],
                }
            ],
        )

        deterministic_contract.validate_deterministic_plan_binding(
            {"audit_id": "A1", "deterministic_contract": contract},
            plan,
        )

    def test_complete_d6_abandon_is_nonsemantic_and_package_immutable(self) -> None:
        contract = required_d6_contract()
        plan = deterministic_plan(
            contract,
            findings=[
                {
                    "finding_id": "F6",
                    "deterministic_check": "D6",
                    "finding_code": "CORE_RUNTIME_ORACLE_REJECTED",
                    "repair_class": "ABANDON",
                    "justification": "No admissible implementation is available.",
                    "operations": [],
                    "regression_tests": [],
                    "evidence": [],
                }
            ],
        )
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            root = workspace / "paper-fixture"
            (root / "tests").mkdir(parents=True)
            (root / "instruction.md").write_text("task\n", encoding="utf-8")
            (root / "tests/checker.py").write_text("pass\n", encoding="utf-8")
            plan["repair_output_dir"] = str(
                workspace / "review_outputs/fixture/repair"
            )
            before = run_repair.package_hashes(root)
            report = {
                "audit_id": "A1",
                "review_verdict": "CONDITIONAL",
                "summary": {"final_verdict": "CONDITIONAL"},
                "findings": [
                    {
                        "finding_id": "F6",
                        "status": "OPEN",
                        "title": "CORE_RUNTIME_ORACLE_REJECTED",
                    }
                ],
            }
            with mock.patch.object(
                run_repair,
                "validate_fresh_audit_batch",
                return_value=(report, {}, {"F6": report["findings"][0]}),
            ):
                result = run_repair.repair_batch(
                    root,
                    plan,
                    workspace / "unused-attestation.json",
                    workspace / "plan.json",
                )

            self.assertEqual(result["status"], "ABANDONED")
            self.assertEqual(result["attempt_kind"], "CONTROL")
            self.assertFalse(result["attempt_consumed"])
            self.assertFalse(result["package_mutated"])
            self.assertEqual(run_repair.package_hashes(root), before)



    def test_residual_deterministic_blocker_cannot_pass_reaudit(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            candidate = Path(temporary)
            audit = external_reaudit_dir(candidate)
            audit.mkdir(parents=True, exist_ok=True)
            (audit / "audit_manifest.json").write_text(
                json.dumps({"input_hashes": {}}), encoding="utf-8"
            )
            report = {
                "audit_id": "A2",
                "configuration": {
                    "review_lane": "dual",
                },
                **authoritative_pass_fields(required_contract()),
            }
            with self.assertRaisesRegex(ValueError, "deterministic CLEAN"):
                run_repair.validate_reaudit(
                    candidate,
                    report,
                    {"finding_id": "F1"},
                    {
                        "configuration": {
                            "review_lane": "dual",
                        }
                    },
                    {},
                )



    def test_reaudit_is_equal_depth_and_exactly_one(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            candidate = Path(temporary)
            audit = external_reaudit_dir(candidate)
            audit.mkdir(parents=True, exist_ok=True)
            (audit / "audit_manifest.json").write_text(
                json.dumps({"input_hashes": {}}), encoding="utf-8"
            )
            reaudit = {
                "audit_id": "A2",
                "configuration": {
                    "review_lane": "dual",
                },
                **authoritative_pass_fields(clean_contract()),
            }
            comparison = run_repair.validate_reaudit(
                candidate,
                reaudit,
                {"finding_id": "F1"},
                {
                    "configuration": {
                        "review_lane": "dual",
                    }
                },
                {},
            )

        self.assertEqual(comparison["reaudit_count"], 1)
        self.assertEqual(comparison["reaudit_configuration"]["review_lane"], "dual")



    def test_reaudit_rejects_historical_scoring_schema(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            candidate = Path(temporary)
            audit = external_reaudit_dir(candidate)
            audit.mkdir(parents=True, exist_ok=True)
            (audit / "audit_manifest.json").write_text(
                json.dumps({"input_hashes": {}}), encoding="utf-8"
            )
            reaudit = {
                "audit_id": "A2",
                "configuration": {
                    "review_lane": "dual",
                },
                **authoritative_pass_fields(clean_contract()),
            }
            reaudit["summary"]["scoring_version"] = "materials-review-scoring/1.0"
            with self.assertRaisesRegex(ValueError, "scoring schema is stale"):
                run_repair.validate_reaudit(
                    candidate,
                    reaudit,
                    {"finding_id": "F1"},
                    {
                        "configuration": {
                            "review_lane": "dual",
                        }
                    },
                    {},
                )

    def test_atomic_publication_requires_every_invariant(self) -> None:
        values = published_bundle()
        self.assertEqual(
            canonical_status.validate_repair_bundle_semantics(
                values, repair_log=values["repair.log"]
            )["repair_status"],
            "REPAIRED",
        )

        residual = published_bundle(
            comparison_overrides={
                "residual_blocking_finding_ids": ["F1"],
                "deterministic_state": "REQUIRED",
            }
        )
        with self.assertRaisesRegex(ValueError, "atomic publication invariant"):
            canonical_status.validate_repair_bundle_semantics(
                residual, repair_log=residual["repair.log"]
            )

        missing_binding = published_bundle(source_binding=None)
        missing_binding["repair_plan.json"]["source_audit"].pop(
            "deterministic_contract"
        )
        with self.assertRaisesRegex(ValueError, "source binding is stale"):
            canonical_status.validate_repair_bundle_semantics(
                missing_binding, repair_log=missing_binding["repair.log"]
            )


if __name__ == "__main__":
    unittest.main()
