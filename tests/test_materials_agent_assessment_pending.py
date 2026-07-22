from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
REVIEW_SCRIPTS = REPO_ROOT / ".cursor/skills/materials-benchmark-review/scripts"
REPAIR_SCRIPTS = REPO_ROOT / ".cursor/skills/materials-benchmark-repair/scripts"
sys.path.insert(0, str(REVIEW_SCRIPTS))
sys.path.insert(0, str(REPAIR_SCRIPTS))

import migrate_legacy_assessment_pending as migrate  # noqa: E402
import prepare_audit_output  # noqa: E402
import run_context  # noqa: E402
import run_repair  # noqa: E402
import run_review  # noqa: E402


def minimal_non_mat_assessment() -> dict[str, object]:
    return {
        "schema_version": "materials-agent-assessment/2.0",
        "materials_qualification": {
            "classification": "NON_MAT",
            "rationale": "The task is a pure arithmetic exercise without materials content.",
            "evidence": [
                {
                    "axis": axis,
                    "package_file": "instruction.md",
                    "package_quote": "pure arithmetic",
                }
                for axis in (
                    "object",
                    "data",
                    "operation",
                    "endpoint",
                    "domain_dependence",
                )
            ],
        },
        "taxonomy": {
            "computation_task": ["其他"],
            "research_domain": ["其他"],
            "material_system": {"primary": "其他", "secondary": []},
        },
        "taxonomy_evidence": [
            {
                "dimension": "computation_task",
                "label": "其他",
                "package_file": "instruction.md",
                "package_quote": "pure arithmetic",
            },
            {
                "dimension": "research_domain",
                "label": "其他",
                "package_file": "instruction.md",
                "package_quote": "pure arithmetic",
            },
            {
                "dimension": "material_system.primary",
                "label": "其他",
                "package_file": "instruction.md",
                "package_quote": "pure arithmetic",
            },
        ],
    }


class MaterialsAgentAssessmentPendingTests(unittest.TestCase):
    def package(self, root: Path) -> Path:
        package = root / "corpus" / "cluster-1" / "theme" / "paper-1"
        (package / "tests").mkdir(parents=True)
        (package / "instruction.md").write_text(
            "## Problem background\npure arithmetic\n",
            encoding="utf-8",
        )
        (package / "tests/checker.py").write_text("pass\n", encoding="utf-8")
        return package

    def test_missing_assessment_pauses_without_a0_or_formal_audit(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.package(root)
            run = run_context.create_run(
                root / "corpus", "cluster-1/theme/paper-1", "run-1"
            )
            result = run_review.run_review_context(run)
            self.assertEqual(
                result["status"], prepare_audit_output.AGENT_ASSESSMENT_PENDING
            )
            status = run_context.status(run)
            self.assertEqual(
                status["state"], prepare_audit_output.AGENT_ASSESSMENT_PENDING
            )
            self.assertFalse((run / "roots/A0.json").exists())
            self.assertFalse(
                (run / "audit/benchmark_audit/audit_report.json").exists()
            )
            self.assertFalse((run / "snapshot").exists())

    def test_supplying_assessment_resumes_same_run_into_reviewing(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = self.package(root)
            run = run_context.create_run(
                root / "corpus", "cluster-1/theme/paper-1", "run-1"
            )
            pending = run_review.run_review_context(run)
            self.assertEqual(
                pending["status"], prepare_audit_output.AGENT_ASSESSMENT_PENDING
            )

            def reviewed(_package: Path, **kwargs: object) -> dict[str, object]:
                self.assertEqual(
                    Path(str(kwargs["agent_assessment_path"])).resolve(),
                    (run / "agent_assessment.json").resolve(),
                )
                self.assertTrue(kwargs.get("require_agent_assessment"))
                audit = Path(str(kwargs["audit_output_dir"]))
                audit.mkdir(parents=True, exist_ok=True)
                (audit / "benchmark_audit").mkdir(parents=True, exist_ok=True)
                (audit / "benchmark_audit/audit_report.json").write_text(
                    "{}", encoding="utf-8"
                )
                return {
                    "review_verdict": "PASS",
                    "audit_id": "audit-1",
                    "summary": {"final_verdict": "PASS"},
                }

            (run / "agent_assessment.json").write_text(
                json.dumps(minimal_non_mat_assessment()),
                encoding="utf-8",
            )
            # Bypass full schema validation against taxonomy labels for this
            # lifecycle unit test; the resume path still requires a file.
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
            self.assertTrue((run / "snapshot").is_dir())
            self.assertEqual(
                (run / "snapshot/instruction.md").read_text(encoding="utf-8"),
                (package / "instruction.md").read_text(encoding="utf-8"),
            )

    def test_reaudit_requires_inherited_assessment_no_deterministic_fallback(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            candidate = root / "candidate"
            candidate.mkdir()
            (candidate / "instruction.md").write_text("task\n", encoding="utf-8")
            report = {
                "configuration": {"review_lane": "dual"},
                "agent_quality": {"assessment": {}},
            }
            plan = {"audit_id": "audit-1", "findings": []}
            result = run_repair.run_equal_depth_review(
                candidate,
                report,
                plan,
            )
            self.assertEqual(
                result["status"], prepare_audit_output.AGENT_ASSESSMENT_PENDING
            )
            self.assertFalse(result.get("attempt_consumed", True))
            self.assertIn("inherited paper Agent assessment", result["message"])

    def test_reaudit_inherits_source_assessment_when_plan_omits_path(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            candidate = root / "candidate"
            candidate.mkdir()
            (candidate / "instruction.md").write_text("task\n", encoding="utf-8")
            assessment = {"materials_qualification": {"classification": "MAT_CORE"}}
            report = {
                "configuration": {"review_lane": "dual"},
                "agent_quality": {"assessment": assessment},
            }
            plan = {"audit_id": "audit-1", "findings": []}
            captured: dict[str, object] = {}

            def fake_review(_candidate: Path, **kwargs: object) -> dict[str, object]:
                captured.update(kwargs)
                return {
                    "status": "ok",
                    "audit_id": "reaudit-1",
                    "configuration": {"review_lane": "dual"},
                    "summary": {"final_verdict": "PASS"},
                }

            with patch.object(run_repair, "external_binding_hashes", return_value=({}, {})), patch(
                "run_review.run_review", side_effect=fake_review
            ), patch.object(
                run_repair,
                "reaudit_output_root",
                return_value=root / "reaudit_out",
            ), patch.object(
                run_repair,
                "reaudit_audit_dir",
                return_value=root / "reaudit_out" / "benchmark_audit",
            ), patch.object(
                run_repair,
                "read_json",
                return_value={
                    "audit_id": "reaudit-1",
                    "configuration": {"review_lane": "dual"},
                },
            ):
                # Force the production engine branch by ensuring run_review source
                # contains def run_review(.
                result = run_repair.run_equal_depth_review(
                    candidate,
                    report,
                    plan,
                    audit_output_dir=root / "reaudit_out",
                )
            self.assertEqual(result.get("audit_id"), "reaudit-1")
            assessment_path = Path(str(captured["agent_assessment_path"]))
            self.assertTrue(assessment_path.is_file())
            self.assertTrue(captured.get("require_agent_assessment"))
            self.assertEqual(
                json.loads(assessment_path.read_text(encoding="utf-8")),
                assessment,
            )

    def test_batch_finalizer_rejects_both_pending_states(self) -> None:
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            "finalize_materials_review_batch",
            REPO_ROOT / "tools/finalize_materials_review_batch.py",
        )
        assert spec and spec.loader
        finalizer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(finalizer)

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.package(root)
            tracking = root / "corpus/corpus_review_tracking.json"
            tracking.write_text(
                json.dumps({"records": [{"package_id": "cluster-1/theme/paper-1"}]}),
                encoding="utf-8",
            )
            for state in (
                prepare_audit_output.AGENT_ASSESSMENT_PENDING,
                prepare_audit_output.AGENT_CONTRACT_PENDING,
            ):
                run = run_context.create_run(
                    root / "corpus",
                    "cluster-1/theme/paper-1",
                    f"run-{state.lower()}",
                )
                if state == prepare_audit_output.AGENT_ASSESSMENT_PENDING:
                    run_context.transition(run, state)
                else:
                    run_context.transition(run, "REVIEWING")
                    run_context.transition(run, state)
                with self.assertRaisesRegex(
                    run_context.RunContextError, "not terminal"
                ):
                    finalizer.tracking_update([run], tracking)

    def test_legacy_migration_is_idempotent_and_preserves_diagnostics(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            records = root / ".review_records"
            package_id = "cluster-1/theme/paper-1"
            run_id = "run-legacy"
            run = records.joinpath(*package_id.split("/")) / "runs" / run_id
            self.package(root)
            created = run_context.create_run(
                root / "corpus", package_id, run_id
            )
            # Point inventory at the temporary run while keeping create_run layout.
            self.assertEqual(created, run)
            run_context.transition(run, "REVIEWING")
            audit = run / "audit" / "benchmark_audit"
            audit.mkdir(parents=True)
            report = {
                "agent_quality": {"assessment": {}},
                "evidence_contract": {
                    "gaps": [
                        "authoritative_materials_qualification",
                        "paper_assessment",
                    ]
                },
                "summary": {
                    "final_verdict": "NOT_ASSESSABLE",
                    "agent_contract_status": "NOT_SUPPLIED",
                },
            }
            (audit / "audit_report.json").write_text(
                json.dumps(report), encoding="utf-8"
            )
            (audit / "diagnostic.txt").write_text("keep-me\n", encoding="utf-8")
            run_context.transition(
                run,
                "REVIEWED",
                review_result={"review_verdict": "NOT_ASSESSABLE"},
            )
            inventory = {
                "schema_version": "materials-legacy-assessment-pending-inventory/1.0",
                "runs": [{"package_id": package_id, "run_id": run_id}],
            }
            first = migrate.migrate_inventory(records, inventory=inventory)
            self.assertEqual(first["results"][0]["action"], "migrated")
            self.assertEqual(
                run_context.status(run)["state"],
                prepare_audit_output.AGENT_ASSESSMENT_PENDING,
            )
            self.assertTrue((audit / "diagnostic.txt").is_file())
            self.assertTrue((run / migrate.MIGRATION_MARKER).is_file())
            second = migrate.migrate_inventory(records, inventory=inventory)
            self.assertEqual(second["results"][0]["action"], "already_migrated")
            self.assertFalse(first["tracking_updated"])
            self.assertFalse(second["tracking_updated"])

    def test_inventory_lists_exactly_ten_known_runs(self) -> None:
        inventory = migrate.load_inventory()
        self.assertEqual(len(inventory["runs"]), 10)
        ids = {
            (item["package_id"], item["run_id"]) for item in inventory["runs"]
        }
        self.assertEqual(len(ids), 10)


if __name__ == "__main__":
    unittest.main()
