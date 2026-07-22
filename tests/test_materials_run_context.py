from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(
    0,
    str(
        REPO_ROOT
        / ".cursor/skills/materials-benchmark-review/scripts"
    ),
)
import run_context  # noqa: E402
import run_review  # noqa: E402


class MaterialsRunContextTests(unittest.TestCase):
    def package(self, root: Path) -> Path:
        package = root / "corpus" / "cluster-1" / "theme" / "paper-1"
        (package / "tests").mkdir(parents=True)
        (package / "instruction.md").write_text("task\n", encoding="utf-8")
        (package / "tests/checker.py").write_text("pass\n", encoding="utf-8")
        return package

    def test_run_transitions_are_atomic_and_reject_skips(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.package(root)
            run = run_context.create_run(
                root / "corpus", "cluster-1/theme/paper-1", "run-1"
            )
            self.assertTrue((run / "agent_contract/assessment.json").is_file())
            with self.assertRaisesRegex(run_context.RunContextError, "illegal"):
                run_context.transition(run, "REVIEWED")
            run_context.transition(run, "REVIEWING")
            status = run_context.transition(run, "REVIEWED")
            self.assertEqual(status["state"], "REVIEWED")
            self.assertEqual(
                json.loads((run / "status.json").read_text())["state"],
                "REVIEWED",
            )

    def test_content_root_detects_snapshot_and_audit_changes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = self.package(root)
            run = run_context.create_run(
                root / "corpus", "cluster-1/theme/paper-1", "run-1"
            )
            run_context.snapshot_package(package, run)
            (run / "audit").mkdir()
            (run / "audit/audit_report.json").write_text("{}\n", encoding="utf-8")
            first = run_context.write_content_root(run, "A0")
            self.assertEqual(first, run_context.verify_content_root(run, "A0"))
            (run / "audit/audit_report.json").write_text("{\"changed\": true}\n", encoding="utf-8")
            with self.assertRaisesRegex(run_context.RunContextError, "does not match"):
                run_context.verify_content_root(run, "A0")

    def test_r0_covers_plan_candidate_regressions_and_result(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = self.package(root)
            run = run_context.create_run(
                root / "corpus", "cluster-1/theme/paper-1", "run-1"
            )
            run_context.snapshot_package(package, run)
            (run / "audit").mkdir()
            (run / "audit/audit_report.json").write_text("{}", encoding="utf-8")
            (run / "plan.json").write_text("{}", encoding="utf-8")
            (run / "candidate").mkdir()
            (run / "candidate/instruction.md").write_text("candidate\n", encoding="utf-8")
            (run / "regressions/result.json").write_text("{}", encoding="utf-8")
            (run / "repair_result.json").write_text("{}", encoding="utf-8")
            run_context.write_content_root(run, "R0")
            self.assertEqual(run_context.verify_content_root(run, "R0"), run_context.content_root(run, run_context.PHASE_CONTENT["R0"]))
            (run / "plan.json").write_text('{"changed": true}', encoding="utf-8")
            with self.assertRaisesRegex(run_context.RunContextError, "does not match"):
                run_context.verify_content_root(run, "R0")

    def test_same_package_lock_fails_fast_but_other_packages_are_independent(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.package(root)
            other = root / "corpus" / "cluster-2" / "theme" / "paper-2"
            (other / "tests").mkdir(parents=True)
            (other / "instruction.md").write_text("task\n", encoding="utf-8")
            first = run_context.create_run(root / "corpus", "cluster-1/theme/paper-1", "run-1")
            second = run_context.create_run(root / "corpus", "cluster-2/theme/paper-2", "run-2")
            with run_context.PackageRunLock(first):
                with self.assertRaises(run_context.RunLockHeld):
                    with run_context.PackageRunLock(first):
                        pass
                with run_context.PackageRunLock(second):
                    pass

    def test_contract_version_mismatch_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.package(root)
            run = run_context.create_run(
                root / "corpus", "cluster-1/theme/paper-1", "run-1"
            )
            context_path = run / "context.json"
            context = json.loads(context_path.read_text(encoding="utf-8"))
            context["review_contract_version"] = "materials-review-contract/old"
            context_path.write_text(json.dumps(context), encoding="utf-8")
            with self.assertRaisesRegex(run_context.RunContextError, "incompatible"):
                run_context.load_context(run)

    def test_direct_pass_completes_with_not_required_outcome(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = self.package(root)
            run = run_context.create_run(root / "corpus", "cluster-1/theme/paper-1", "run-1")
            (run / "agent_assessment.json").write_text("{}", encoding="utf-8")

            def reviewed(_package: Path, **kwargs: object) -> dict[str, object]:
                audit = Path(str(kwargs["audit_output_dir"]))
                audit.mkdir()
                (audit / "audit_report.json").write_text("{}", encoding="utf-8")
                return {"review_verdict": "PASS", "audit_id": "audit-1"}

            with patch.object(
                run_review,
                "try_load_agent_assessment",
                return_value=({"paper_skipped": True}, None),
            ), patch.object(run_review, "run_review", side_effect=reviewed):
                result = run_review.run_review_context(run)
            self.assertEqual(result["review_verdict"], "PASS")
            final = run_context.status(run)
            self.assertEqual(final["state"], "COMPLETED")
            self.assertEqual(final["outcome"], "NOT_REQUIRED")
            self.assertTrue((run / "roots/A0.json").is_file())

    def test_contract_pending_returns_to_same_review_lifecycle(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.package(root)
            run = run_context.create_run(root / "corpus", "cluster-1/theme/paper-1", "run-1")
            (run / "agent_assessment.json").write_text("{}", encoding="utf-8")

            def pending(_package: Path, **kwargs: object) -> dict[str, object]:
                audit = Path(str(kwargs["audit_output_dir"]))
                request = audit / "agent_contract/request.json"
                request.parent.mkdir(parents=True)
                request.write_text("{}", encoding="utf-8")
                return {"status": "AGENT_CONTRACT_PENDING"}

            with patch.object(
                run_review,
                "try_load_agent_assessment",
                return_value=({"paper_skipped": True}, None),
            ), patch.object(run_review, "run_review", side_effect=pending):
                run_review.run_review_context(run)
            self.assertEqual(run_context.status(run)["state"], "AGENT_CONTRACT_PENDING")
            self.assertTrue((run / "agent_contract/request.json").is_file())
            run_context.transition(run, "REVIEWING")
            self.assertEqual(run_context.status(run)["state"], "REVIEWING")

    def test_live_package_change_after_a0_requires_fresh_run(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = self.package(root)
            run = run_context.create_run(root / "corpus", "cluster-1/theme/paper-1", "run-1")
            run_context.snapshot_package(package, run)
            (package / "instruction.md").write_text("changed\n", encoding="utf-8")
            with self.assertRaisesRegex(run_context.RunContextError, "changed after A0"):
                run_context.verify_live_package_matches_snapshot(run)
