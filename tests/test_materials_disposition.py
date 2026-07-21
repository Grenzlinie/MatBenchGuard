from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tests.test_materials_benchmark_review_dual_lane import (
    REPO_ROOT,
    RUNNER,
    assessment,
    copy_source_package,
    dual_lane_assessment,
    external_audit_dir,
    run_dual_lane,
)


def run_dual_review(package: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(RUNNER),
            str(package),
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=120,
        check=False,
    )


def read_bundle(package: Path) -> tuple[dict[str, object], dict[str, object]]:
    audit = external_audit_dir(package)
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


def install_passing_oracle(package: Path) -> None:
    (package / "solution/solve.sh").chmod(0o755)
    (package / "tests/checker.py").write_text(
        "import csv, json, math\n"
        "from pathlib import Path\n"
        "output = Path('/app/outputs/dispersion_curves.csv')\n"
        "reward = 0.0\n"
        "try:\n"
        "    with output.open(newline='', encoding='utf-8') as handle:\n"
        "        rows = list(csv.DictReader(handle))\n"
        "    keys = [(r['direction'], r['mode'], r['k']) for r in rows]\n"
        "    if len(rows) == 180 and len(set(keys)) == 180 and all("
        "math.isfinite(float(r['frequency'])) for r in rows):\n"
        "        reward = 1.0\n"
        "except (OSError, KeyError, TypeError, ValueError):\n"
        "    pass\n"
        "logs = Path('/logs/verifier')\n"
        "logs.mkdir(parents=True, exist_ok=True)\n"
        "(logs / 'reward.txt').write_text(str(reward), encoding='utf-8')\n"
        "(logs / 'breakdown.json').write_text("
        "json.dumps({'scientific_contract': reward}), encoding='utf-8')\n",
        encoding="utf-8",
    )


class MaterialsDispositionTests(unittest.TestCase):
    def test_quality_score_uses_only_the_confirmed_five_dimensions(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "paper-fixture"
            copy_source_package(package)
            (package / "solution/solve.sh").unlink()

            completed = run_dual_review(package)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            report, index = read_bundle(package)
            dimensions = report["dimensions_v11"]
            self.assertEqual(
                {item["dimension"] for item in dimensions},
                {"C01", "C02", "C03", "C04", "C05", "C06", "C07"},
            )
            for dimension in dimensions:
                self.assertIn("points_earned", dimension)
                self.assertIn("normalized", dimension)
                self.assertIn("deductions", dimension)
                self.assertIn("finding_ids", dimension)
            self.assertEqual(
                {item["code"] for item in report["hard_gates"]},
                {
                    "NON_MATERIALS_TASK",
                    "SCIENTIFIC_TARGET_INVALID",
                    "CHECKER_CORE_TASK_UNASSESSED",
                    "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE",
                },
            )
            for gate in report["hard_gates"]:
                self.assertIn(gate["status"], {"PASS", "FAIL", "NOT_ASSESSABLE"})
                self.assertIn("evidence", gate)
                self.assertIn("affected_locations", gate)
            self.assertEqual(
                report["summary"]["scoring_version"],
                "materials-review-scoring/2.0",
            )
            self.assertEqual(
                [item["dimension"] for item in report["dimensions_v11"]],
                ["C01", "C02", "C03", "C04", "C05", "C06", "C07"],
            )
            self.assertEqual(
                {item["dimension"]: item["weight"]
                 for item in report["dimensions_v11"]},
                {
                    "C01": 10,
                    "C02": 20,
                    "C03": 20,
                    "C04": 20,
                    "C05": 10,
                    "C06": 10,
                    "C07": 10,
                },
            )
            for gate in report["hard_gates"]:
                self.assertIn(
                    gate["dimension"], {"C01", "C03", "C04", "C06"}
                )
            self.assertEqual(
                index["dimensions_v11"], report["dimensions_v11"]
            )
            self.assertEqual(
                index["dimensions_v11"], report["dimensions_v11"]
            )
            self.assertEqual(index["hard_gates"], report["hard_gates"])
            self.assertEqual(
                index["total_score"], report["summary"]["total_score"]
            )

    def test_metadata_environment_and_resource_roles_do_not_change_quality(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            baseline = workspace / "baseline"
            stripped = workspace / "stripped"
            copy_source_package(baseline)
            copy_source_package(stripped)
            for relative in (
                "task.toml",
                "manifest.json",
                "steps.json",
                "resources.json",
                "environment/Dockerfile",
            ):
                (stripped / relative).unlink()

            baseline_run = run_dual_review(baseline)
            stripped_run = run_dual_review(stripped)

            self.assertEqual(baseline_run.returncode, 0, msg=baseline_run.stderr)
            self.assertEqual(stripped_run.returncode, 0, msg=stripped_run.stderr)
            baseline_report, _ = read_bundle(baseline)
            stripped_report, _ = read_bundle(stripped)
            self.assertEqual(
                stripped_report["summary"]["final_verdict"],
                baseline_report["summary"]["final_verdict"],
            )
            self.assertEqual(
                stripped_report["summary"]["total_score"],
                baseline_report["summary"]["total_score"],
            )
            self.assertFalse(
                {
                    "task.toml",
                    "manifest.json",
                    "steps.json",
                    "resources.json",
                    "environment/Dockerfile",
                }
                & set(stripped_report["scope"]["quality_evidence_files"])
            )

    def test_missing_solution_oracle_is_repairable_completeness_not_hard_gate(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "paper-fixture"
            copy_source_package(package)

            completed = run_dual_review(package)

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            report, index = read_bundle(package)
            self.assertTrue(
                any(
                    item["status"] == "NOT_ASSESSABLE"
                    for item in report["dimensions_v11"]
                )
            )
            self.assertIsNone(report["summary"]["total_score"])
            self.assertEqual(
                report["summary"]["final_verdict"], "NOT_ASSESSABLE"
            )
            self.assertFalse(report["summary"]["hard_gate_triggered"])
            self.assertEqual(index["route"], "EVIDENCE_PENDING")
            self.assertIn(
                "CORE_RUNTIME_ORACLE_REJECTED",
                {item["title"] for item in report["findings"]},
            )

    def test_assessable_clean_report_passes_above_score_gate(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "paper-fixture"
            copy_source_package(package)
            clear_external_resources(package)
            install_passing_oracle(package)
            assessment_value = assessment()
            assessment_value["materials_qualification"] = (
                dual_lane_assessment()["materials_qualification"]
            )
            assessment_value["dimensions"]["data_fidelity"]["status"] = "PASS"
            assessment_value["dimensions"]["checker_fidelity"]["evidence"][0][
                "package_quote"
            ] = "scientific_contract"
            assessment_value["dimensions"]["gold_provenance"]["evidence"][0][
                "package_quote"
            ] = "reward = 1.0"
            assessment_path = Path(temporary) / "assessment.json"
            assessment_path.write_text(
                json.dumps(assessment_value, ensure_ascii=False),
                encoding="utf-8",
            )

            completed = subprocess.run(
                [
                    sys.executable,
                    str(RUNNER),
                    str(package),
                    "--agent-assessment",
                    str(assessment_path),
                ],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                timeout=120,
                check=False,
            )

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            report, index = read_bundle(package)
            summary = report["summary"]
            self.assertEqual(summary["final_verdict"], "PASS")
            self.assertGreaterEqual(summary["total_score"], 80)
            self.assertEqual(summary["disposition"], "PASS")
            self.assertTrue(summary["publishable"])
            self.assertEqual(summary["publication_route"], "PUBLISH_CANDIDATE")
            v11 = {item["dimension"]: item for item in report["dimensions_v11"]}
            self.assertTrue(
                all(
                    v11[name]["points_earned"] is not None
                    for name in ("C01", "C02", "C03", "C04", "C05", "C06", "C07")
                )
            )
            self.assertFalse(summary["hard_gate_triggered"])
            self.assertTrue(
                all(
                    item["points_earned"] is not None
                    for item in report["dimensions_v11"]
                )
            )
            self.assertEqual(index["route"], "PUBLISH_CANDIDATE")
            self.assertTrue(index["publishable"])
            self.assertEqual(index["review_lane"], "dual")
            self.assertIn("taxonomy_labels", index)
            self.assertIn("finding_summary", index)
            self.assertTrue(
                (external_audit_dir(package) / "disposition.json").is_file()
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

            completed = run_dual_lane(package, assessment_path)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            report, index = read_bundle(package)
            self.assertEqual(
                report["summary"]["final_verdict"], "CONDITIONAL"
            )
            self.assertEqual(
                report["summary"]["disposition"], "CONDITIONAL"
            )
            self.assertFalse(report["summary"]["publishable"])
            self.assertFalse(index["publishable"])
            self.assertEqual(
                index["taxonomy_labels"]["computation_task"],
                ["声子与晶格动力学"],
            )

    def test_repairable_paper_fidelity_failure_is_not_a_hard_gate(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / "paper-fixture"
            copy_source_package(package)
            clear_external_resources(package)
            paper_assessment = assessment()
            for dimension in paper_assessment["dimensions"].values():
                dimension["status"] = "PASS"
            paper_assessment["dimensions"]["checker_fidelity"]["status"] = "FAIL"
            paper_assessment["dimensions"]["checker_fidelity"]["rationale"] = (
                "The checker has a repairable paper-fidelity defect."
            )
            assessment_path = workspace / "assessment.json"
            assessment_path.write_text(
                json.dumps(paper_assessment, ensure_ascii=False),
                encoding="utf-8",
            )

            completed = run_dual_lane(package, assessment_path)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            report, index = read_bundle(package)
            self.assertEqual(
                report["summary"]["final_verdict"], "CONDITIONAL"
            )
            self.assertFalse(report["summary"]["hard_gate_triggered"])
            self.assertEqual(index["route"], "REPAIR_QUEUE")
            finding = next(
                item
                for item in report["findings"]
                if item["title"] == "PAPER_CHECKER_FIDELITY_FAIL"
            )
            self.assertEqual(finding["category"], "PAPER_FIDELITY")

    def test_reject_routes_non_destructively_to_quarantine(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "paper-fixture"
            copy_source_package(package)
            checker_path = package / "tests/checker.py"
            # A checker that never evaluates the declared core output is a
            # confirmed CHECKER_CORE_TASK_UNASSESSED Hard Gate (C04) and must
            # REJECT deterministically without an agent classification.
            checker_path.write_text("raise SystemExit(0)\n", encoding="utf-8")
            instruction = package / "instruction.md"
            before = hashlib.sha256(instruction.read_bytes()).hexdigest()

            completed = run_dual_review(package)

            self.assertEqual(completed.returncode, 0)
            report, index = read_bundle(package)
            disposition = json.loads(
                (
                    external_audit_dir(package) / "disposition.json"
                ).read_text(encoding="utf-8")
            )
            self.assertEqual(report["summary"]["final_verdict"], "REJECT")
            self.assertEqual(report["summary"]["disposition"], "REJECT")
            self.assertFalse(report["summary"]["publishable"])
            self.assertEqual(disposition["route"], "QUARANTINE")
            self.assertEqual(index["route"], "QUARANTINE")
            self.assertFalse(index["publishable"])
            self.assertTrue(disposition["non_destructive"])
            self.assertTrue(disposition["original_preserved"])
            self.assertTrue(package.is_dir())
            self.assertEqual(
                before, hashlib.sha256(instruction.read_bytes()).hexdigest()
            )

    def test_checker_that_ignores_core_output_routes_to_quarantine(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "paper-fixture"
            copy_source_package(package)
            clear_external_resources(package)
            (package / "tests/checker.py").write_text(
                "raise SystemExit(0)\n", encoding="utf-8"
            )

            completed = run_dual_review(package)

            self.assertEqual(completed.returncode, 0)
            report, index = read_bundle(package)
            self.assertEqual(
                report["summary"]["final_verdict"], "REJECT"
            )
            self.assertEqual(
                report["summary"]["disposition"], "REJECT"
            )
            self.assertEqual(index["route"], "QUARANTINE")
            self.assertFalse(index["publishable"])
            self.assertIn(
                "CHECKER_CORE_TASK_UNASSESSED",
                {item["title"] for item in report["findings"]},
            )

    def test_findings_publish_exact_locations_and_actionable_repairs(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "paper-fixture"
            copy_source_package(package)
            (package / "tests/checker.py").unlink()

            completed = run_dual_review(package)

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            report, _ = read_bundle(package)
            finding = next(
                item
                for item in report["findings"]
                if item["title"] == "MISSING_FILE"
            )
            self.assertEqual(
                finding["affected_locations"],
                [
                    {
                        "file": "tests/checker.py",
                        "line": None,
                        "quote": None,
                    }
                ],
            )
            self.assertNotIn("may be invalid", finding["impact"])
            self.assertNotIn("Resolve the observed", finding["minimal_repair"])
            self.assertNotIn("Re-run the failing", finding["retest"])


if __name__ == "__main__":
    unittest.main()
