from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from tests.test_materials_safe_repair import (
    EVIDENCE,
    initial_repair_context,
    run_repair,
    write_plan,
)


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class MaterialsAssistedRepairTests(unittest.TestCase):
    def test_assisted_fix_waits_for_approval_without_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id = initial_repair_context(workspace)
            plan = workspace / "assisted-plan.json"
            write_plan(plan, report["audit_id"], finding_id)
            value = json.loads(plan.read_text(encoding="utf-8"))
            value["repair_class"] = "ASSISTED_FIX"
            value["approval"] = {
                "approved": False,
                "approved_by": None,
                "approved_at": None,
                "evidence": [],
            }
            plan.write_text(json.dumps(value), encoding="utf-8")
            resources = package / "resources.json"
            before = file_hash(resources)

            completed = run_repair(package, plan)

            self.assertEqual(completed.returncode, 3)
            result = json.loads(completed.stdout)
            self.assertEqual(result["status"], "AWAITING_APPROVAL")
            self.assertEqual(file_hash(resources), before)
            self.assertFalse((package / "benchmark_repair").exists())

    def test_sensitive_scoring_change_requires_approval_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id = initial_repair_context(workspace)
            plan = workspace / "sensitive-plan.json"
            value = {
                "schema_version": "0.1",
                "audit_id": report["audit_id"],
                "finding_id": finding_id,
                "repair_class": "ASSISTED_FIX",
                "justification": "Change the pass threshold.",
                "approval": {
                    "approved": True,
                    "approved_by": "materials-owner",
                    "approved_at": "2026-07-15T12:00:00Z",
                    "evidence": [],
                },
                "operations": [
                    {
                        "type": "json_set",
                        "file": "tests/grading_spec.json",
                        "path": ["pass_threshold"],
                        "value": 0.5,
                    }
                ],
                "regression_tests": [
                    {
                        "type": "json_path_equals",
                        "file": "tests/grading_spec.json",
                        "path": ["pass_threshold"],
                        "expected": 0.5,
                    }
                ],
            }
            plan.write_text(json.dumps(value), encoding="utf-8")
            grading = package / "tests/grading_spec.json"
            before = file_hash(grading)

            completed = run_repair(package, plan)

            self.assertEqual(completed.returncode, 3)
            result = json.loads(completed.stdout)
            self.assertEqual(result["status"], "BLOCKED_EVIDENCE")
            self.assertEqual(file_hash(grading), before)

    def test_two_failed_attempts_roll_back_then_abandon_root_cause(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id = initial_repair_context(workspace)
            plan = workspace / "failing-plan.json"
            write_plan(plan, report["audit_id"], finding_id)
            value = json.loads(plan.read_text(encoding="utf-8"))
            value["regression_tests"][0]["expected"] = [
                {"file": "instruction.md", "quote": "not the applied evidence"}
            ]
            plan.write_text(json.dumps(value), encoding="utf-8")
            resources = package / "resources.json"
            before = file_hash(resources)

            first = run_repair(package, plan)
            second = run_repair(package, plan)
            third = run_repair(package, plan)

            self.assertEqual(first.returncode, 3)
            self.assertEqual(second.returncode, 3)
            self.assertEqual(third.returncode, 3)
            first_result = json.loads(first.stdout)
            second_result = json.loads(second.stdout)
            third_result = json.loads(third.stdout)
            self.assertEqual(first_result["status"], "ROLLED_BACK")
            self.assertEqual(second_result["status"], "ABANDONED")
            self.assertEqual(third_result["status"], "ABANDONED")
            self.assertEqual(file_hash(resources), before)
            history_root = Path(first_result["history_root"])
            manifests = sorted(history_root.glob("*/attempt_manifest.json"))
            attempts = [
                json.loads(path.read_text(encoding="utf-8"))
                for path in manifests
                if json.loads(path.read_text(encoding="utf-8"))[
                    "root_cause"
                ]
                == first_result["root_cause"]
            ]
            attempts.sort(key=lambda item: item["attempt_number"])
            self.assertEqual(
                [item["status"] for item in attempts],
                ["ROLLED_BACK", "ABANDONED"],
            )
            self.assertEqual([item["attempt_number"] for item in attempts], [1, 2])
            for path in manifests:
                attempt = json.loads(path.read_text(encoding="utf-8"))
                if attempt["root_cause"] == first_result["root_cause"]:
                    attempt_dir = path.parent
                    self.assertTrue((attempt_dir / "snapshot").is_dir())
                    self.assertTrue((attempt_dir / "candidate").is_dir())
                    self.assertTrue(
                        (attempt_dir / "snapshot/solution").is_dir()
                    )
            current_resources = json.loads(resources.read_text(encoding="utf-8"))
            self.assertNotIn(
                "evidence",
                current_resources["resources"][0]["access"],
            )
            self.assertNotEqual(EVIDENCE, [])


if __name__ == "__main__":
    unittest.main()
