"""Ticket 03: Agent repair assessment + materials-repair-plan/2.0 fail-closed tests."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from typing import Any

from tests.test_materials_safe_repair import (
    FINDING_ID,
    build_agent_repair_assessment_for_plan,
    external_audit_dir,
    fixture_paper_assessment,
    initial_repair_context,
    repair_module,
    safe_plan,
    sha256_file,
    write_json,
    write_plan,
)


class MaterialsAgentRepairAssessmentTests(unittest.TestCase):
    def test_archival_plan_1_0_cannot_enter_execution(self) -> None:
        module = repair_module()
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, _runner = initial_repair_context(
                workspace, review_lane="dual"
            )
            plan = safe_plan(report["audit_id"], finding_id)
            plan["schema_version"] = (
                "materials-deterministic-repair-plan/1.0"
            )
            plan_path = workspace / "legacy-plan.json"
            write_json(plan_path, plan)
            with self.assertRaisesRegex(ValueError, "archival-only"):
                module.validate_external_plan(package, plan_path)

    def test_plan_omitting_agent_finding_is_rejected(self) -> None:
        module = repair_module()
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, _runner = initial_repair_context(
                workspace, review_lane="dual"
            )
            agent_id = "agent-quality-checker-fairness"
            audit = external_audit_dir(package)
            payload = json.loads(
                (audit / "audit_report.json").read_text(encoding="utf-8")
            )
            payload["findings"].append(
                {
                    "finding_id": agent_id,
                    "status": "OPEN",
                    "title": "CHECKER_NONFINITE_BYPASS",
                    "severity": "HIGH",
                    "lane": "agent_quality",
                    "repairable": True,
                    "repair_lane": "agent_quality",
                    "repair_scope": "CHECKER_ROBUSTNESS",
                    "dimension": "C07",
                }
            )
            payload["agent_quality"]["finding_ids"] = [agent_id]
            payload["repair_queue"] = {
                "schema_version": "materials-repair-findings/1.0",
                "open_finding_ids": sorted([finding_id, agent_id]),
                "open_findings": [
                    {
                        "finding_id": finding_id,
                        "lane": "deterministic_core",
                        "status": "OPEN",
                        "repairable": True,
                    },
                    {
                        "finding_id": agent_id,
                        "lane": "agent_quality",
                        "status": "OPEN",
                        "repairable": True,
                        "repair_scope": "CHECKER_ROBUSTNESS",
                    },
                ],
                "deterministic_finding_ids": [finding_id],
                "agent_quality_finding_ids": [agent_id],
            }
            write_json(audit / "audit_report.json", payload)
            plan = safe_plan(report["audit_id"], finding_id)
            write_plan(workspace / "plan.json", plan)
            with self.assertRaisesRegex(ValueError, "complete dual-lane"):
                from deterministic_contract import validate_repair_plan_binding

                validate_repair_plan_binding(payload, plan)

    def test_missing_assessment_is_rejected(self) -> None:
        module = repair_module()
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, _runner = initial_repair_context(
                workspace, review_lane="dual"
            )
            plan = safe_plan(report["audit_id"], finding_id)
            write_plan(workspace / "plan.json", plan)
            plan.pop("agent_repair_assessment", None)
            with self.assertRaisesRegex(
                ValueError, "agent_repair_assessment"
            ):
                module.validate_batch_plan(package, plan)

    def test_stale_assessment_hash_is_rejected(self) -> None:
        module = repair_module()
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, _runner = initial_repair_context(
                workspace, review_lane="dual"
            )
            plan = safe_plan(report["audit_id"], finding_id)
            write_plan(workspace / "plan.json", plan)
            plan["agent_repair_assessment"]["assessment_hash"] = (
                "sha256:" + "f" * 64
            )
            audit = json.loads(
                (external_audit_dir(package) / "audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            with self.assertRaises(module.PolicyStop) as context:
                module.load_and_bind_agent_repair_assessment(
                    package, plan, audit, plan_path=workspace / "plan.json"
                )
            self.assertEqual(context.exception.status, "BLOCKED_EVIDENCE")
            self.assertIn("stale", context.exception.reason)

    def test_unapproved_operation_is_rejected(self) -> None:
        module = repair_module()
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, _runner = initial_repair_context(
                workspace, review_lane="dual"
            )
            plan = safe_plan(report["audit_id"], finding_id)
            write_plan(workspace / "plan.json", plan)
            assessment = build_agent_repair_assessment_for_plan(package, plan)
            assessment["findings"][0]["approved_operation_ids"] = [
                "not-the-real-op"
            ]
            path = workspace / "agent_repair_assessment.json"
            write_json(path, assessment)
            plan["agent_repair_assessment"] = {
                "schema_version": "materials-agent-repair-assessment/1.0",
                "path": str(path),
                "assessment_hash": sha256_file(path),
            }
            audit = json.loads(
                (external_audit_dir(package) / "audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            with self.assertRaisesRegex(ValueError, "not approved"):
                module.load_and_bind_agent_repair_assessment(
                    package, plan, audit, plan_path=workspace / "plan.json"
                )

    def test_d_finding_may_take_evidence_bound_assisted_fix(self) -> None:
        module = repair_module()
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, _runner = initial_repair_context(
                workspace, review_lane="dual"
            )
            plan = safe_plan(report["audit_id"], finding_id)
            plan["repair_class"] = "ASSISTED_FIX"
            plan["findings"][0]["repair_class"] = "ASSISTED_FIX"
            plan["findings"][0]["repair_scope"] = "INSTRUCTION_CONTRACT"
            plan["findings"][0]["evidence"] = [
                {
                    "id": "paper-method",
                    "source_kind": "PACKAGE_PAPER",
                    "source": "paper/paper.md",
                    "exact_quote": (
                        "The exact public replacement is paper-supported quantity."
                    ),
                    "source_hash": sha256_file(package / "paper/paper.md"),
                    "applicability": "paper-backed public wording",
                    "derivation": "quote supplies replacement",
                    "core_science_change": False,
                }
            ]
            plan["evidence"] = plan["findings"][0]["evidence"]
            plan["findings"][0]["operations"] = [
                {
                    "id": "correct-instruction",
                    "type": "replace_text",
                    "file": "instruction.md",
                    "old": "evidence-backed quantity",
                    "new": "paper-supported quantity",
                    "evidence_ids": ["paper-method"],
                    "publication_class": "REAUDIT_REQUIRED",
                }
            ]
            plan["operations"] = plan["findings"][0]["operations"]
            plan["findings"][0]["regression_tests"] = [
                {
                    "id": "instruction-correction",
                    "finding_id": finding_id,
                    "causal_operation_ids": ["correct-instruction"],
                    "type": "text_contains",
                    "file": "instruction.md",
                    "expected": "paper-supported quantity",
                }
            ]
            plan["regression_tests"] = plan["findings"][0]["regression_tests"]
            write_plan(workspace / "assisted.json", plan)
            assessment = build_agent_repair_assessment_for_plan(package, plan)
            self.assertEqual(
                assessment["findings"][0]["decision"], "ASSISTED_FIX"
            )
            self.assertEqual(
                assessment["findings"][0]["lane"], "deterministic_core"
            )
            path = workspace / "agent_repair_assessment.json"
            write_json(path, assessment)
            plan["agent_repair_assessment"] = {
                "schema_version": "materials-agent-repair-assessment/1.0",
                "path": str(path),
                "assessment_hash": sha256_file(path),
            }
            audit = json.loads(
                (external_audit_dir(package) / "audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            bound = module.load_and_bind_agent_repair_assessment(
                package, plan, audit, plan_path=workspace / "assisted.json"
            )
            self.assertEqual(
                bound["findings"][0]["approved_operation_ids"],
                ["correct-instruction"],
            )

    def test_unsupported_science_change_blocks_or_abandons(self) -> None:
        from agent_repair_assessment import (
            validate_agent_repair_assessment_payload,
        )

        with self.assertRaisesRegex(ValueError, "core science"):
            validate_agent_repair_assessment_payload(
                {
                    "schema_version": "materials-agent-repair-assessment/1.0",
                    "audit_id": "audit-1",
                    "a0_content_root": "sha256:" + "a" * 64,
                    "package_identity": {"directory_name": "paper-fixture"},
                    "findings": [
                        {
                            "finding_id": FINDING_ID,
                            "lane": "deterministic_core",
                            "decision": "ASSISTED_FIX",
                            "agent_verdict": "APPROVE_REPAIR",
                            "repair_scope": "SCIENCE_SEMANTICS",
                            "core_science_change": True,
                            "rationale": "invented science",
                            "evidence": [
                                {
                                    "source_kind": "PACKAGE_PAPER",
                                    "exact_quote": "quote",
                                    "source_hash": "sha256:" + "b" * 64,
                                }
                            ],
                            "approved_operation_ids": ["op-1"],
                        }
                    ],
                }
            )

    def test_source_audit_without_paper_assessment_is_rejected(self) -> None:
        module = repair_module()
        with self.assertRaises(module.PolicyStop) as context:
            module.require_validated_paper_assessment(
                {
                    "agent_quality": {"assessment": {}},
                    "evidence_contract": {
                        "gaps": [
                            "paper_assessment",
                            "authoritative_materials_qualification",
                        ]
                    },
                }
            )
        self.assertEqual(context.exception.status, "BLOCKED_EVIDENCE")

    def test_fixture_has_validated_paper_assessment(self) -> None:
        from agent_repair_assessment import report_has_validated_paper_assessment

        self.assertTrue(
            report_has_validated_paper_assessment(
                {
                    "agent_quality": {
                        "assessment": fixture_paper_assessment()
                    }
                }
            )
        )

    def test_direct_deterministic_publisher_is_live(self) -> None:
        source = (
            Path(__file__).resolve().parents[1]
            / ".codex/skills/materials-benchmark-repair/scripts/run_repair.py"
        ).read_text(encoding="utf-8")
        self.assertIn("verification_mode", source)
        self.assertIn("publish_direct_deterministic_batch", source)
        self.assertIn("evaluate_direct_deterministic_eligibility", source)


if __name__ == "__main__":
    unittest.main()
