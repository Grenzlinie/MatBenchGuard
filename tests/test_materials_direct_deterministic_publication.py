"""Ticket 04: DIRECT_DETERMINISTIC publication eligibility and routing."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from typing import Any

from tests.test_materials_safe_repair import (
    FINDING_ID,
    external_reaudit_dir,
    external_repair_dir,
    initial_repair_context,
    repair_module,
    run_repair,
    safe_plan,
    write_plan,
)


def _base_direct_plan() -> dict[str, Any]:
    return {
        "core_science_change": False,
        "findings": [
            {
                "finding_id": FINDING_ID,
                "repair_class": "AUTO_FIX",
                "core_science_change": False,
                "deterministic_check": "D5",
                "repair_scope": "DETERMINISTIC_WIRING",
                "lane": "deterministic_core",
                "justification": "restore entrypoint",
                "operations": [
                    {
                        "id": "op-1",
                        "type": "write_file",
                        "file": "solution/solve.sh",
                        "publication_class": "DIRECT_DETERMINISTIC",
                    }
                ],
            }
        ],
    }


def _report() -> dict[str, Any]:
    return {
        "findings": [{"finding_id": FINDING_ID, "status": "OPEN"}],
        "agent_quality": {"finding_ids": []},
        "configuration": {"review_lane": "dual"},
        "summary": {"total_score": 70, "final_verdict": "CONDITIONAL"},
    }


class DirectDeterministicEligibilityTests(unittest.TestCase):
    def test_eligible_d_only_auto_fix(self) -> None:
        module = repair_module()
        ok, reason = module.evaluate_direct_deterministic_eligibility(
            _base_direct_plan(), _report()
        )
        self.assertTrue(ok)
        self.assertIn("DIRECT_DETERMINISTIC", reason)

    def test_assisted_fix_requires_reaudit(self) -> None:
        module = repair_module()
        plan = _base_direct_plan()
        plan["findings"][0]["repair_class"] = "ASSISTED_FIX"
        ok, reason = module.evaluate_direct_deterministic_eligibility(
            plan, _report()
        )
        self.assertFalse(ok)
        self.assertIn("AUTO_FIX", reason)

    def test_agent_quality_requires_reaudit(self) -> None:
        module = repair_module()
        plan = _base_direct_plan()
        plan["findings"][0]["lane"] = "agent_quality"
        plan["findings"][0]["deterministic_check"] = None
        ok, reason = module.evaluate_direct_deterministic_eligibility(
            plan, _report()
        )
        self.assertFalse(ok)

    def test_checker_robustness_scope_requires_reaudit(self) -> None:
        module = repair_module()
        plan = _base_direct_plan()
        plan["findings"][0]["repair_scope"] = "CHECKER_ROBUSTNESS"
        ok, reason = module.evaluate_direct_deterministic_eligibility(
            plan, _report()
        )
        self.assertFalse(ok)
        self.assertIn("CHECKER_ROBUSTNESS", reason)

    def test_instruction_contract_requires_reaudit(self) -> None:
        module = repair_module()
        plan = _base_direct_plan()
        plan["findings"][0]["repair_scope"] = "INSTRUCTION_CONTRACT"
        ok, _reason = module.evaluate_direct_deterministic_eligibility(
            plan, _report()
        )
        self.assertFalse(ok)

    def test_direct_input_scope_requires_reaudit(self) -> None:
        module = repair_module()
        plan = _base_direct_plan()
        plan["findings"][0]["repair_scope"] = "DIRECT_INPUT_REFERENCE"
        ok, _reason = module.evaluate_direct_deterministic_eligibility(
            plan, _report()
        )
        self.assertFalse(ok)

    def test_mixed_publication_class_requires_reaudit(self) -> None:
        module = repair_module()
        plan = _base_direct_plan()
        plan["findings"][0]["operations"].append(
            {
                "id": "op-2",
                "type": "replace_text",
                "file": "tests/checker.py",
                "publication_class": "REAUDIT_REQUIRED",
            }
        )
        ok, reason = module.evaluate_direct_deterministic_eligibility(
            plan, _report()
        )
        self.assertFalse(ok)
        self.assertIn("DIRECT_DETERMINISTIC", reason)

    def test_unresolved_blocks_direct(self) -> None:
        module = repair_module()
        ok, reason = module.evaluate_direct_deterministic_eligibility(
            _base_direct_plan(),
            _report(),
            unresolved_findings=[{"finding_id": "x", "reason": "blocked"}],
        )
        self.assertFalse(ok)
        self.assertIn("unresolved", reason)


class DirectDeterministicPublicationIntegrationTests(unittest.TestCase):
    def test_direct_path_skips_equal_depth_review(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(
                workspace
            )
            plan_path = workspace / "repair-plan.json"
            write_plan(plan_path, safe_plan(report["audit_id"], finding_id))

            completed = run_repair(package, plan_path, runner)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            result = json.loads(completed.stdout)
            self.assertEqual(result["status"], "REPAIRED")
            self.assertEqual(result.get("verification_mode"), "DIRECT_DETERMINISTIC")
            self.assertFalse(result.get("attempt_consumed", True))
            self.assertFalse(external_reaudit_dir(package).is_dir())
            self.assertFalse((package / "benchmark_repair").exists())
            comparison = json.loads(
                (
                    external_repair_dir(package)
                    / "benchmark_repair"
                    / "re_audit_comparison.json"
                ).read_text(encoding="utf-8")
            )
            self.assertEqual(
                comparison["verification_mode"], "DIRECT_DETERMINISTIC"
            )
            self.assertIs(comparison["reaudit_performed"], False)
            self.assertTrue(comparison.get("regression_evidence"))

    def test_reaudit_required_still_invokes_review(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(
                workspace
            )
            plan_payload = safe_plan(report["audit_id"], finding_id)
            for operation in plan_payload.get("operations", []):
                if isinstance(operation, dict):
                    operation["publication_class"] = "REAUDIT_REQUIRED"
            for finding in plan_payload.get("findings", []):
                for operation in finding.get("operations", []):
                    if isinstance(operation, dict):
                        operation["publication_class"] = "REAUDIT_REQUIRED"
            plan_path = workspace / "repair-plan.json"
            write_plan(plan_path, plan_payload)

            completed = run_repair(package, plan_path, runner)
            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            result = json.loads(completed.stdout)
            self.assertEqual(result["status"], "REPAIRED")
            self.assertNotEqual(
                result.get("verification_mode"), "DIRECT_DETERMINISTIC"
            )
            self.assertTrue(external_reaudit_dir(package).is_dir())
            comparison = json.loads(
                (
                    external_repair_dir(package)
                    / "benchmark_repair"
                    / "re_audit_comparison.json"
                ).read_text(encoding="utf-8")
            )
            self.assertNotEqual(
                comparison.get("verification_mode"), "DIRECT_DETERMINISTIC"
            )
            self.assertTrue(comparison.get("reaudit_performed", True))
            self.assertFalse((package / "benchmark_repair").exists())


if __name__ == "__main__":
    unittest.main()
