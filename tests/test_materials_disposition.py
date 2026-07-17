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
    no_paper_assessment,
    run_paper_grounded,
)
from tests.test_materials_benchmark_review_e1 import (
    bind_public_fixture,
    write_public_valid_dispersion,
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


def install_passing_oracle(package: Path) -> None:
    oracle_output = package / "solution/oracle-output"
    write_public_valid_dispersion(oracle_output)
    (package / "solution/solve.sh").write_text(
        "#!/bin/sh\n"
        "mkdir -p \"${OUTPUT_DIR}\"\n"
        "cp \"$(dirname \"$0\")/oracle-output/dispersion_curves.csv\" "
        "\"${OUTPUT_DIR}/dispersion_curves.csv\"\n",
        encoding="utf-8",
    )
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

            completed = run_no_paper(package)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            report, index = read_bundle(package)
            self.assertEqual(
                {
                    item["dimension"]: item["max_points"]
                    for item in report["dimension_scores"]
                },
                {
                    "scientific_validity": 35,
                    "instruction_answerability": 20,
                    "checker_gold_alignment": 25,
                    "robustness_discrimination": 15,
                    "solution_completeness": 5,
                },
            )
            for dimension in report["dimension_scores"]:
                self.assertIn("points_earned", dimension)
                self.assertIn("normalized_score", dimension)
                self.assertIn("deduction_ids", dimension)
                self.assertIn("finding_ids", dimension)
                self.assertIn("evidence", dimension)
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
                "materials-review-scoring/1.1",
            )
            self.assertEqual(
                report["summary"]["legacy_scoring_version"],
                "materials-review-scoring/1.0",
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
                index["dimension_scores"], report["dimension_scores"]
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

            baseline_run = run_no_paper(baseline)
            stripped_run = run_no_paper(stripped)

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

            completed = run_no_paper(package)

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            report, index = read_bundle(package)
            dimensions = {
                item["dimension"]: item for item in report["dimension_scores"]
            }
            self.assertEqual(
                dimensions["solution_completeness"]["points_earned"], 0
            )
            self.assertEqual(
                dimensions["solution_completeness"]["normalized_score"], 0.0
            )
            self.assertIsNone(report["summary"]["total_score"])
            self.assertEqual(
                report["summary"]["final_verdict"], "NOT_ASSESSABLE"
            )
            self.assertFalse(report["summary"]["hard_gate_triggered"])
            self.assertEqual(index["route"], "EVIDENCE_PENDING")
            self.assertIn(
                "SOLUTION_ORACLE_MISSING",
                {item["title"] for item in report["findings"]},
            )

    def test_pass_routes_to_publish_candidate_with_weighted_index(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "paper-fixture"
            copy_source_package(package)
            clear_external_resources(package)
            install_passing_oracle(package)
            valid_output = Path(temporary) / "known-valid-output"
            write_public_valid_dispersion(valid_output)
            bind_public_fixture(package, valid_output)
            assessment_value = assessment()
            assessment_value["materials_qualification"] = (
                no_paper_assessment()["materials_qualification"]
            )
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
                    "--paper-mode",
                    "paper_grounded",
                    "--execution-level",
                    "E1",
                    "--agent-assessment",
                    str(assessment_path),
                    "--known-valid-output",
                    str(valid_output),
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
            dimensions = {
                item["dimension"]: item
                for item in report["dimension_scores"]
            }
            self.assertEqual(summary["final_verdict"], "PASS")
            self.assertGreaterEqual(summary["total_score"], 80)
            self.assertEqual(summary["disposition"], "PASS")
            self.assertTrue(summary["publishable"])
            self.assertEqual(summary["repair_state"], "NOT_REQUIRED")
            self.assertEqual(summary["publication_route"], "PUBLISH_CANDIDATE")
            v11 = {item["dimension"]: item for item in report["dimensions_v11"]}
            self.assertTrue(
                all(
                    v11[name]["points_earned"] is not None
                    for name in ("C01", "C02", "C03", "C04", "C05", "C06", "C07")
                )
            )
            self.assertFalse(summary["hard_gate_triggered"])
            self.assertEqual(
                {
                    "scientific_validity",
                    "instruction_answerability",
                    "checker_gold_alignment",
                    "robustness_discrimination",
                    "solution_completeness",
                },
                set(dimensions),
            )
            self.assertTrue(
                all(
                    item["normalized_score"] is None
                    or not item["critical"]
                    or item["normalized_score"] >= 0.5
                    for item in dimensions.values()
                )
            )
            self.assertEqual(index["route"], "PUBLISH_CANDIDATE")
            self.assertTrue(index["publishable"])
            self.assertEqual(index["paper_mode"], "paper_grounded")
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
                report["summary"]["final_verdict"], "NOT_ASSESSABLE"
            )
            self.assertEqual(
                report["summary"]["disposition"], "NOT_ASSESSABLE"
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

            completed = run_paper_grounded(package, assessment_path)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            report, index = read_bundle(package)
            self.assertEqual(
                report["summary"]["final_verdict"], "NOT_ASSESSABLE"
            )
            self.assertFalse(report["summary"]["hard_gate_triggered"])
            self.assertEqual(index["route"], "EVIDENCE_PENDING")
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

            completed = run_no_paper(package)

            self.assertEqual(completed.returncode, 0)
            report, index = read_bundle(package)
            disposition = json.loads(
                (
                    package / "benchmark_audit/disposition.json"
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

            completed = run_no_paper(package)

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

            completed = run_no_paper(package)

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
