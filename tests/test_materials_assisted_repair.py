from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from typing import Any

from tests.test_materials_safe_repair import (
    initial_repair_context,
    external_audit_dir,
    external_repair_dir,
    repair_module,
    run_repair,
    safe_plan,
    sha256_file,
    write_audit_attestation,
    write_plan,
)


def assisted_plan(audit_id: str, finding_id: str) -> dict[str, Any]:
    value = safe_plan(audit_id, finding_id)
    value["repair_class"] = "ASSISTED_FIX"
    value["justification"] = (
        "Correct a transcription error using the bundled paper quote."
    )
    value["evidence"] = [
        {
            "id": "paper-method",
            "source_kind": "PACKAGE_PAPER",
            "source": "paper/paper.md",
            "exact_quote": "The exact public replacement is paper-supported quantity.",
            "applicability": "The package claims the published method's public quantity.",
            "derivation": "The exact quoted replacement supplies the corrected public wording.",
            "core_science_change": False,
            "kind": "scientific_method",
            "precision": {
                "kind": "scientific_method",
                "claim": "paper-supported quantity",
                "replacement": "paper-supported quantity",
            },
        }
    ]
    value["operations"] = [
        {
            "id": "correct-instruction",
            "type": "replace_text",
            "file": "instruction.md",
            "old": "evidence-backed quantity",
            "new": "paper-supported quantity",
            "evidence_ids": ["paper-method"],
        }
    ]
    value["regression_tests"] = [
        {
            "id": "instruction-correction",
            "finding_id": finding_id,
            "causal_operation_ids": ["correct-instruction"],
            "type": "text_contains",
            "file": "instruction.md",
            "expected": "paper-supported quantity",
        }
    ]
    return value


def web_assisted_plan(audit_id: str, finding_id: str) -> dict[str, Any]:
    value = assisted_plan(audit_id, finding_id)
    value["evidence"] = [
        {
            "id": "primary-web",
            "source_kind": "AUTHORITATIVE_PRIMARY_WEB",
            "source": "https://example.org/primary-method",
            "url": "https://example.org/primary-method",
            "exact_quote": "The exact public replacement is paper-supported quantity.",
            "source_hash": "sha256:" + "a" * 64,
            "retrieved_at": "2026-07-21T03:00:00Z",
            "retrieval_metadata": {
                "retrieved_at": "2026-07-21T03:00:00Z",
                "content_hash": "sha256:" + "a" * 64,
            },
            "approval": {
                "approved": True,
                "primary": True,
                "authority": "PEER_REVIEWED_PRIMARY",
                "reference": "approval-record-1",
            },
            "applicability": "The primary source defines this exact public quantity.",
            "derivation": "The quoted source determines the replacement wording.",
            "core_science_change": False,
            "kind": "scientific_method",
            "precision": {
                "kind": "scientific_method",
                "claim": "paper-supported quantity",
                "replacement": "paper-supported quantity",
            },
        }
    ]
    value["operations"][0]["evidence_ids"] = ["primary-web"]
    return value


class MaterialsAssistedRepairTests(unittest.TestCase):
    def test_evidence_backed_assisted_fix_runs_without_per_fix_approval(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(
                workspace, review_lane="dual"
            )
            plan = workspace / "assisted-plan.json"
            value = assisted_plan(report["audit_id"], finding_id)
            value["approval"] = {"approved": False}
            write_plan(plan, value)

            completed = run_repair(package, plan, runner)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            result = json.loads(completed.stdout)
            self.assertEqual(result["status"], "REPAIRED")
            self.assertEqual(result["repair_state"], "REPAIRED")
            self.assertTrue(result["publishable"])
            self.assertIn(
                "paper-supported quantity",
                (package / "instruction.md").read_text(encoding="utf-8"),
            )
            manifest = json.loads(
                ((external_repair_dir(package) / "benchmark_repair") / "repair_manifest.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(manifest["repair_class"], "ASSISTED_FIX")
            self.assertEqual(manifest["evidence"][0]["id"], "paper-method")

    def test_assisted_fix_without_operation_evidence_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(
                workspace, review_lane="dual"
            )
            plan = workspace / "assisted-plan.json"
            value = assisted_plan(report["audit_id"], finding_id)
            value["operations"][0]["evidence_ids"] = []
            write_plan(plan, value)
            before = sha256_file(package / "instruction.md")

            completed = run_repair(package, plan, runner)

            self.assertEqual(completed.returncode, 3)
            result = json.loads(completed.stdout)
            self.assertEqual(result["status"], "BLOCKED_EVIDENCE")
            self.assertEqual(sha256_file(package / "instruction.md"), before)
            self.assertFalse((package / "benchmark_repair").exists())

    def test_assisted_fix_requires_exact_typed_provenance_fields(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(
                workspace, review_lane="dual"
            )
            plan = workspace / "assisted-plan.json"
            value = assisted_plan(report["audit_id"], finding_id)
            value["evidence"][0].pop("exact_quote")
            write_plan(plan, value)

            completed = run_repair(package, plan, runner)

            self.assertEqual(completed.returncode, 3)
            result = json.loads(completed.stdout)
            self.assertEqual(result["status"], "BLOCKED_EVIDENCE")
            self.assertFalse((package / "benchmark_repair").exists())

    def test_approved_primary_web_evidence_can_drive_assisted_fix(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(
                workspace, review_lane="dual"
            )
            plan = workspace / "web-assisted-plan.json"
            write_plan(
                plan, web_assisted_plan(report["audit_id"], finding_id)
            )

            completed = run_repair(package, plan, runner)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            result = json.loads(completed.stdout)
            self.assertEqual(result["status"], "REPAIRED")

    def test_source_score_below_repair_gate_is_abandoned(self) -> None:
        module = repair_module()
        with self.assertRaises(module.PolicyStop) as context:
            module.enforce_source_score_gate(
                {"summary": {"total_score": 59}}
            )
        self.assertEqual(context.exception.status, "ABANDONED")

    def test_agent_quality_finding_cannot_be_auto_fix(self) -> None:
        module = repair_module()
        with self.assertRaises(module.PolicyStop) as context:
            module.enforce_repair_lane_boundary(
                {
                    "finding_id": "quality-1",
                    "repair_class": "AUTO_FIX",
                },
                {
                    "finding_id": "quality-1",
                    "lane": "agent_quality",
                    "judgment_type": "AGENT_JUDGMENT",
                },
                {"agent_quality": {"finding_ids": ["quality-1"]}},
            )
        self.assertEqual(context.exception.status, "POLICY_VIOLATION")

    def test_plan_cannot_redefine_core_science(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(
                workspace, review_lane="dual"
            )
            plan = workspace / "assisted-plan.json"
            value = assisted_plan(report["audit_id"], finding_id)
            value["core_science_change"] = True
            write_plan(plan, value)

            completed = run_repair(package, plan, runner)

            self.assertEqual(completed.returncode, 3)
            self.assertEqual(
                json.loads(completed.stdout)["status"], "POLICY_VIOLATION"
            )



    def test_solution_content_cannot_be_copied_into_instruction(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(
                workspace, review_lane="dual"
            )
            secret = "hidden_answer = 7.314159265"
            (package / "solution/answer.py").write_text(
                secret + "\n", encoding="utf-8"
            )
            audit_manifest = external_audit_dir(package) / "audit_manifest.json"
            manifest = json.loads(audit_manifest.read_text(encoding="utf-8"))
            manifest["input_hashes"]["solution/answer.py"] = sha256_file(
                package / "solution/answer.py"
            )
            manifest["core_contract_digest"] = repair_module().core_contract_digest(
                package
            )
            write_plan(audit_manifest, manifest)
            write_audit_attestation(package)
            plan = workspace / "assisted-plan.json"
            value = assisted_plan(report["audit_id"], finding_id)
            value["operations"][0]["new"] = secret
            value["regression_tests"][0]["expected"] = secret
            write_plan(plan, value)

            completed = run_repair(package, plan, runner)

            self.assertEqual(completed.returncode, 3)
            self.assertEqual(
                json.loads(completed.stdout)["status"], "POLICY_VIOLATION"
            )
            self.assertNotIn(
                secret,
                (package / "instruction.md").read_text(encoding="utf-8"),
            )

    def test_threshold_lowering_requires_linked_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(
                workspace, review_lane="dual"
            )
            plan = workspace / "assisted-plan.json"
            value = assisted_plan(report["audit_id"], finding_id)
            value["operations"] = [
                {
                    "id": "lower-threshold",
                    "type": "json_set",
                    "file": "tests/grading_spec.json",
                    "path": ["pass_threshold"],
                    "value": 0.5,
                    "evidence_ids": [],
                }
            ]
            value["regression_tests"] = [
                {
                    "id": "threshold",
                    "finding_id": finding_id,
                    "causal_operation_ids": ["lower-threshold"],
                    "type": "json_path_equals",
                    "file": "tests/grading_spec.json",
                    "path": ["pass_threshold"],
                    "expected": 0.5,
                }
            ]
            write_plan(plan, value)
            before = sha256_file(package / "tests/grading_spec.json")

            completed = run_repair(package, plan, runner)

            self.assertEqual(completed.returncode, 3)
            self.assertEqual(
                json.loads(completed.stdout)["status"], "BLOCKED_EVIDENCE"
            )
            self.assertEqual(
                sha256_file(package / "tests/grading_spec.json"), before
            )

    def test_failed_control_attempts_remain_rolled_back(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(
                workspace, review_lane="dual"
            )
            plan = workspace / "failing-plan.json"
            value = safe_plan(report["audit_id"], finding_id)
            value["regression_tests"] = [
                value["regression_tests"][0],
                {
                    "id": "forced-failure",
                    "finding_id": finding_id,
                    "causal_operation_ids": ["restore-solve"],
                    "type": "command",
                    "command": ["sh", "solution/solve.sh"],
                    "expected_returncode": 1,
                },
            ]
            write_plan(plan, value)
            instruction_before = sha256_file(package / "instruction.md")

            first = run_repair(package, plan, runner)
            second = run_repair(package, plan, runner)
            third = run_repair(package, plan, runner)

            self.assertEqual(
                [first.returncode, second.returncode, third.returncode],
                [3, 3, 3],
            )
            results = [
                json.loads(item.stdout) for item in (first, second, third)
            ]
            self.assertEqual(
                [item["status"] for item in results],
                ["ROLLED_BACK", "ROLLED_BACK", "ROLLED_BACK"],
            )
            self.assertEqual(
                sha256_file(package / "instruction.md"), instruction_before
            )
            self.assertFalse((package / "solution/solve.sh").exists())
            history_root = Path(results[0]["history_root"])
            manifests = [
                json.loads(path.read_text(encoding="utf-8"))
                for path in history_root.glob("*/attempt_manifest.json")
            ]
            attempts = sorted(
                (
                    item
                    for item in manifests
                    if item["root_cause"] == results[0]["root_cause"]
                ),
                key=lambda item: item["attempt_number"],
            )
            self.assertEqual(
                [item["status"] for item in attempts],
                ["ROLLED_BACK", "ROLLED_BACK", "ROLLED_BACK"],
            )
            for path in history_root.glob("*/attempt_manifest.json"):
                attempt = json.loads(path.read_text(encoding="utf-8"))
                if attempt["root_cause"] == results[0]["root_cause"]:
                    self.assertTrue((path.parent / "snapshot").is_dir())
                    self.assertTrue((path.parent / "candidate").is_dir())


if __name__ == "__main__":
    unittest.main()
