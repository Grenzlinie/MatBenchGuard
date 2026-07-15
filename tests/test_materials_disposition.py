from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tests.test_materials_benchmark_review_paper_grounded import (
    REPO_ROOT,
    RUNNER,
    assessment,
    copy_source_package,
    run_paper_grounded,
)


def run_no_paper(package: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(RUNNER),
            str(package),
            "--paper-mode",
            "no_paper",
            "--execution-level",
            "E1",
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=120,
        check=False,
    )


def read_bundle(package: Path) -> tuple[dict[str, object], dict[str, object]]:
    audit = package / "benchmark_audit"
    report = json.loads(
        (audit / "audit_report.json").read_text(encoding="utf-8")
    )
    index = json.loads(
        (audit / "corpus_index_entry.json").read_text(encoding="utf-8")
    )
    return report, index


def clear_external_resources(package: Path) -> None:
    (package / "resources.json").write_text(
        json.dumps({"version": 1, "resources": []}),
        encoding="utf-8",
    )


class MaterialsDispositionTests(unittest.TestCase):
    def test_pass_routes_to_publish_candidate_with_weighted_index(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "paper-fixture"
            copy_source_package(package)
            clear_external_resources(package)

            completed = run_no_paper(package)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            report, index = read_bundle(package)
            summary = report["summary"]
            dimensions = {
                item["dimension"]: item
                for item in report["dimension_scores"]
            }
            self.assertEqual(summary["final_verdict"], "PASS")
            self.assertGreaterEqual(summary["total_score"], 0.8)
            self.assertEqual(summary["disposition"], "PUBLISH_CANDIDATE")
            self.assertFalse(summary["hard_gate_triggered"])
            self.assertEqual(
                {
                    "materials_admission",
                    "core_scientific_contract",
                    "resource_availability",
                    "task_answerability",
                    "checker_validity",
                    "paper_consistency",
                },
                set(dimensions),
            )
            self.assertTrue(
                all(
                    item["score"] is None
                    or not item["critical"]
                    or item["score"] >= 0.5
                    for item in dimensions.values()
                )
            )
            self.assertEqual(index["route"], "PUBLISH_CANDIDATE")
            self.assertTrue(index["publishable"])
            self.assertEqual(index["paper_mode"], "no_paper")
            self.assertEqual(index["execution_level"], "E1")
            self.assertIn("taxonomy_labels", index)
            self.assertIn("finding_summary", index)
            self.assertTrue(
                (package / "benchmark_audit/disposition.json").is_file()
            )

    def test_conditional_routes_to_repair_queue_with_taxonomy(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / "paper-fixture"
            copy_source_package(package)
            clear_external_resources(package)
            assessment_path = workspace / "assessment.json"
            assessment_path.write_text(
                json.dumps(assessment(), ensure_ascii=False),
                encoding="utf-8",
            )

            completed = run_paper_grounded(package, assessment_path)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            report, index = read_bundle(package)
            self.assertEqual(
                report["summary"]["final_verdict"], "CONDITIONAL"
            )
            self.assertEqual(report["summary"]["disposition"], "REPAIR_QUEUE")
            self.assertFalse(index["publishable"])
            self.assertEqual(
                index["taxonomy_labels"]["computation_task"],
                ["声子与晶格动力学"],
            )

    def test_reject_routes_non_destructively_to_quarantine(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "paper-fixture"
            copy_source_package(package)
            checker_path = package / "tests/checker.py"
            checker_path.write_text(
                """
from pathlib import Path
import json

logs = Path("/logs/verifier")
logs.mkdir(parents=True, exist_ok=True)
(logs / "reward.txt").write_text("1.0", encoding="utf-8")
(logs / "breakdown.json").write_text(json.dumps({"gaming": 1.0}), encoding="utf-8")
""",
                encoding="utf-8",
            )
            instruction = package / "instruction.md"
            before = hashlib.sha256(instruction.read_bytes()).hexdigest()

            completed = run_no_paper(package)

            self.assertEqual(completed.returncode, 0)
            report, index = read_bundle(package)
            disposition = json.loads(
                (
                    package / "benchmark_audit/disposition.json"
                ).read_text(encoding="utf-8")
            )
            self.assertEqual(report["summary"]["final_verdict"], "REJECT")
            self.assertEqual(report["summary"]["disposition"], "QUARANTINE")
            self.assertEqual(index["route"], "QUARANTINE")
            self.assertFalse(index["publishable"])
            self.assertTrue(disposition["non_destructive"])
            self.assertTrue(disposition["original_preserved"])
            self.assertTrue(package.is_dir())
            self.assertEqual(
                before, hashlib.sha256(instruction.read_bytes()).hexdigest()
            )

    def test_missing_checker_evidence_routes_to_evidence_pending(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "paper-fixture"
            copy_source_package(package)
            clear_external_resources(package)
            (package / "tests/checker.py").write_text(
                "raise SystemExit(0)\n", encoding="utf-8"
            )

            completed = run_no_paper(package)

            self.assertEqual(completed.returncode, 0)
            report, index = read_bundle(package)
            self.assertEqual(
                report["summary"]["final_verdict"], "NOT_ASSESSABLE"
            )
            self.assertEqual(
                report["summary"]["disposition"], "EVIDENCE_PENDING"
            )
            self.assertEqual(index["route"], "EVIDENCE_PENDING")
            self.assertFalse(index["publishable"])
            self.assertTrue(index["evidence_gaps"])


if __name__ == "__main__":
    unittest.main()
