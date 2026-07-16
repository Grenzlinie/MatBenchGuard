from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tests.test_materials_benchmark_review_e1 import (
    REPO_ROOT,
    RUNNER,
    copy_source_package,
    run_review,
    write_public_valid_dispersion,
)


class MaterialsCheckerScientificProbeTests(unittest.TestCase):
    def test_missing_public_valid_fixture_is_scored_as_a_limitation(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / "paper-fixture"
            copy_source_package(package)

            completed = subprocess.run(
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

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            checker = json.loads(
                (package / "benchmark_audit/checker_tests.json").read_text(
                    encoding="utf-8"
                )
            )
            coverage = checker["probe_coverage"]
            self.assertEqual(coverage["negative"]["status"], "ASSESSED")
            self.assertEqual(
                coverage["discrimination"]["status"], "NOT_ASSESSABLE"
            )
            self.assertEqual(
                coverage["equivalence"]["status"], "NOT_ASSESSABLE"
            )
            self.assertFalse(
                coverage["discrimination"]["provenance"]["oracle_used"]
            )
            report = json.loads(
                (package / "benchmark_audit/audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            robustness = next(
                item
                for item in report["dimension_scores"]
                if item["dimension"] == "robustness_discrimination"
            )
            self.assertIn(
                robustness["status"], {"PASS", "WARNING", "FAIL"}
            )
            self.assertIsInstance(
                robustness["points_earned"], (int, float)
            )
            self.assertTrue(robustness["evidence"])
            self.assertIn(
                "INDEPENDENT_PUBLIC_FIXTURE_UNAVAILABLE",
                {finding["title"] for finding in report["findings"]},
            )

    def test_public_audit_runs_gaming_gradient_and_invariance_probes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / "paper-fixture"
            copy_source_package(package)
            valid_output = workspace / "known-valid-output"
            write_public_valid_dispersion(valid_output)

            completed = run_review(package, valid_output)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            audit = json.loads(
                (package / "benchmark_audit/checker_tests.json").read_text(
                    encoding="utf-8"
                )
            )
            tests = {item["test_type"]: item for item in audit["tests"]}
            self.assertTrue(
                {
                    "missing_outputs",
                    "empty_valid_shape",
                    "malformed_outputs",
                    "random_baseline",
                    "minimal_gold_shape",
                    "duplicate_gold_rows",
                    "nonfinite_values",
                    "known_valid_public",
                    "quality_gradient_small_error",
                    "quality_gradient_large_error",
                    "metamorphic_equivalent_representation",
                }.issubset(tests)
            )
            valid_score = tests["known_valid_public"]["observed_score"]
            small_score = tests["quality_gradient_small_error"]["observed_score"]
            large_score = tests["quality_gradient_large_error"]["observed_score"]
            equivalent_score = tests[
                "metamorphic_equivalent_representation"
            ]["observed_score"]
            self.assertGreaterEqual(valid_score, small_score)
            self.assertGreaterEqual(small_score, large_score)
            self.assertAlmostEqual(valid_score, equivalent_score, places=9)
            self.assertFalse(
                {
                    "SCIENTIFIC_QUALITY_GRADIENT_VIOLATION",
                    "SCIENTIFIC_INVARIANCE_VIOLATION",
                }
                & {item["code"] for item in audit["findings"]}
            )
            self.assertFalse(audit["solution_content_inspected"])
            self.assertEqual(
                {item["probe_class"] for item in audit["tests"]},
                {"positive", "negative", "discrimination", "equivalence"},
            )

    def test_equivalent_representation_defect_is_repairable(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / "paper-fixture"
            copy_source_package(package)
            valid_output = workspace / "known-valid-output"
            write_public_valid_dispersion(valid_output)

            checker_path = package / "tests/checker.py"
            checker_path.write_text(
                """
import csv
import json
import os

output = "/app/outputs/dispersion_curves.csv"
reward = 0.0
if os.path.isfile(output):
    try:
        with open(output, newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            rows = list(reader)
        if rows and reader.fieldnames == ["direction", "mode", "k", "frequency"]:
            reward = 1.0
    except (csv.Error, UnicodeError):
        reward = 0.0
os.makedirs("/logs/verifier", exist_ok=True)
with open("/logs/verifier/reward.txt", "w", encoding="utf-8") as handle:
    handle.write(str(reward))
with open("/logs/verifier/breakdown.json", "w", encoding="utf-8") as handle:
    json.dump({"order_sensitive_fixture": reward}, handle)
""",
                encoding="utf-8",
            )

            completed = run_review(package, valid_output)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            report = json.loads(
                (package / "benchmark_audit/audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            findings = {
                item["title"]: item for item in report["findings"]
            }
            self.assertEqual(
                report["summary"]["final_verdict"], "NOT_ASSESSABLE"
            )
            self.assertFalse(report["summary"]["hard_gate_triggered"])
            self.assertEqual(
                findings["SCIENTIFIC_INVARIANCE_VIOLATION"]["severity"],
                "HIGH",
            )


if __name__ == "__main__":
    unittest.main()
