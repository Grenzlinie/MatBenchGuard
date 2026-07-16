from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tests.test_materials_benchmark_review_e1 import (
    SOURCE_PACKAGE,
    copy_source_package,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
RUNNER_SCRIPTS = (
    REPO_ROOT
    / ".cursor"
    / "skills"
    / "materials-benchmark-review"
    / "scripts"
)
if str(RUNNER_SCRIPTS) not in __import__("sys").path:
    __import__("sys").path.insert(0, str(RUNNER_SCRIPTS))
REPAIR_SCRIPTS = (
    REPO_ROOT
    / ".cursor"
    / "skills"
    / "materials-benchmark-repair"
    / "scripts"
)
if str(REPAIR_SCRIPTS) not in __import__("sys").path:
    __import__("sys").path.insert(0, str(REPAIR_SCRIPTS))

import dynamic_checker_probe  # noqa: E402
import finalize_audit_output  # noqa: E402
import run_review  # noqa: E402
from run_repair import report_configuration, run_equal_depth_review  # noqa: E402


def usable_result(case: str) -> dict[str, object]:
    return {
        "case": case,
        "crashed": False,
        "reward": 1.0,
        "breakdown": {"score": 1.0, "_errors": {}},
    }


class MaterialsIssue20Tests(unittest.TestCase):
    def test_authoritative_review_rejects_non_e1_execution(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / SOURCE_PACKAGE.name
            copy_source_package(package)

            with self.assertRaisesRegex(ValueError, "E1-only"):
                run_review.run_review(
                    package,
                    known_valid_output=None,
                    execution_level="E2",
                )

    def test_authoritative_report_publishes_checker_runtime_provenance(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / SOURCE_PACKAGE.name
            copy_source_package(package)

            run_review.run_review(package, known_valid_output=None)
            report = json.loads(
                (
                    package / "benchmark_audit/audit_report.json"
                ).read_text(encoding="utf-8")
            )

            self.assertEqual(
                report["checker_runtime"]["verifier_entrypoint"],
                "tests/test.sh",
            )
            self.assertEqual(
                report["checker_runtime"]["runtime_provenance"],
                "audit-host-copy",
            )
            self.assertFalse(
                report["checker_runtime"]["direct_checker_harness"]
            )
            self.assertFalse(
                report["execution_evidence"]["scientific_reproduction"]
            )

    def test_repair_reaudit_configuration_is_e1_only(self) -> None:
        with self.assertRaisesRegex(ValueError, "E1-only"):
            report_configuration(
                {
                    "configuration": {
                        "paper_mode": "no_paper",
                        "execution_level": "E2",
                    }
                }
            )

    def test_repair_reaudit_rejects_future_execution_plan(self) -> None:
        with self.assertRaisesRegex(ValueError, "cannot enter"):
            run_equal_depth_review(
                Path("."),
                {
                    "configuration": {
                        "paper_mode": "no_paper",
                        "execution_level": "E1",
                    }
                },
                {"e2_smoke_plan": "/tmp/future-plan.json"},
            )

    def test_public_fixture_is_not_the_positive_control(self) -> None:
        results = [
            usable_result("known_valid_public"),
            usable_result("quality_gradient_small_error"),
            usable_result("quality_gradient_large_error"),
            usable_result("metamorphic_equivalent_representation"),
        ]

        flags = dynamic_checker_probe.probe_assessment_flags(results)

        self.assertFalse(flags["positive"])
        self.assertTrue(flags["discrimination"])
        self.assertTrue(flags["equivalence"])

    def test_checker_cases_record_test_sh_audit_host_provenance(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / SOURCE_PACKAGE.name
            copy_source_package(package)
            output = Path(temporary) / "checker.json"
            source_before = {
                path.relative_to(package): path.read_bytes()
                for path in package.rglob("*")
                if path.is_file()
            }

            result = dynamic_checker_probe.dynamic_checker_probe(
                package, output, known_valid_output=None
            )

            self.assertTrue(result["tests"])
            self.assertEqual(
                result["runtime"]["verifier_entrypoint"],
                "tests/test.sh",
            )
            self.assertEqual(
                result["runtime"]["runtime_provenance"],
                "audit-host-copy",
            )
            self.assertFalse(result["runtime"]["direct_checker_harness"])
            for case in result["tests"]:
                self.assertEqual(
                    case["evidence"]["verifier_entrypoint"],
                    "tests/test.sh",
                )
                self.assertEqual(
                    case["evidence"]["runtime_provenance"],
                    "audit-host-copy",
                )
            self.assertEqual(
                source_before,
                {
                    path.relative_to(package): path.read_bytes()
                    for path in package.rglob("*")
                    if path.is_file()
                },
            )

    def test_audit_host_missing_dependency_is_not_a_package_defect(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / SOURCE_PACKAGE.name
            copy_source_package(package)
            checker = package / "tests/checker.py"
            checker.write_text(
                "import issue20_missing_audit_host_dependency\n"
                + checker.read_text(encoding="utf-8"),
                encoding="utf-8",
            )
            dockerfile = package / "environment/Dockerfile"
            dockerfile.write_text(
                dockerfile.read_text(encoding="utf-8")
                + "\n# Harbor image supplies the checker dependency.\n",
                encoding="utf-8",
            )

            result = dynamic_checker_probe.dynamic_checker_probe(
                package,
                Path(temporary) / "checker.json",
                known_valid_output=None,
            )

            self.assertEqual(result["runtime"]["status"], "NOT_ASSESSABLE")
            self.assertEqual(
                result["runtime"]["runtime_provenance"], "not-assessable"
            )
            self.assertFalse(
                {"CHECKER_CRASH", "CHECKER_RESULT_UNUSABLE"}
                & {finding["code"] for finding in result["findings"]}
            )

    def test_verifier_dependency_install_failure_is_not_a_package_defect(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / SOURCE_PACKAGE.name
            copy_source_package(package)
            (package / "tests/test.sh").write_text(
                "#!/usr/bin/env bash\n"
                "echo 'Could not find a version that satisfies the requirement' >&2\n"
                "exit 1\n",
                encoding="utf-8",
            )

            result = dynamic_checker_probe.dynamic_checker_probe(
                package,
                Path(temporary) / "checker.json",
                known_valid_output=None,
            )

            self.assertEqual(result["runtime"]["status"], "NOT_ASSESSABLE")
            self.assertFalse(
                {"CHECKER_CRASH", "CHECKER_RESULT_UNUSABLE"}
                & {finding["code"] for finding in result["findings"]}
            )

    def test_report_contains_unweighted_first_class_qa_axes(self) -> None:
        findings = [
            {
                "title": "INSTRUCTION_ONLY_OUTPUT",
                "severity": "MEDIUM",
                "observed_fact": "The final output is not contracted.",
                "affected_locations": [
                    {"file": "instruction.md", "line": 4, "quote": "result"}
                ],
            },
            {
                "title": "OUTPUT_NOT_CONTRACTED",
                "severity": "HIGH",
                "observed_fact": "The checker output is not contracted.",
                "affected_locations": [
                    {
                        "file": "tests/grading_spec.json",
                        "line": 8,
                        "quote": "outputs",
                    }
                ],
            },
        ]
        axes = finalize_audit_output.derive_qa_axes(
            Path("."),
            findings,
            checker_result={
                "tests": [],
                "solution_content_inspected": False,
                "solution_oracle": {"executed": False},
            },
            contract_map={"requirements": []},
            paper_result={"status": "NOT_ASSESSED"},
            materials_assessment=None,
        )

        self.assertEqual(
            set(axes),
            {
                "factual_accuracy",
                "answer_leakage",
                "instruction_completeness",
                "checker_instruction_consistency",
            },
        )
        for axis in axes.values():
            self.assertEqual(
                set(axis),
                {"status", "evidence", "locations", "limitations"},
            )
            self.assertNotIn("points_earned", axis)
            self.assertIsInstance(axis["evidence"], list)
            self.assertIsInstance(axis["locations"], list)
            self.assertIsInstance(axis["limitations"], list)
        self.assertEqual(
            axes["instruction_completeness"]["status"], "FAIL"
        )
        self.assertEqual(
            axes["checker_instruction_consistency"]["status"], "FAIL"
        )
        self.assertEqual(
            axes["factual_accuracy"]["status"], "NOT_ASSESSABLE"
        )
        self.assertEqual(axes["answer_leakage"]["status"], "NOT_ASSESSABLE")

    def test_factual_uncertainty_has_its_own_qa_axis(self) -> None:
        axes = finalize_audit_output.derive_qa_axes(
            Path("."),
            [
                {
                    "title": "SCIENTIFIC_TARGET_INVALID",
                    "observed_fact": "The scientific target is contradictory.",
                    "affected_locations": [
                        {"file": "instruction.md", "line": 3, "quote": "target"}
                    ],
                }
            ],
            checker_result={"tests": [], "solution_oracle": {}},
            contract_map={"requirements": []},
            paper_result={"status": "NOT_ASSESSED"},
            materials_assessment=None,
        )

        self.assertEqual(axes["factual_accuracy"]["status"], "FAIL")
        self.assertNotIn("points_earned", axes["factual_accuracy"])

    def test_external_accessibility_is_not_factual_inaccuracy(self) -> None:
        axes = finalize_audit_output.derive_qa_axes(
            Path("."),
            [
                {
                    "title": "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE",
                    "observed_fact": "A fixed non-equivalent input is unavailable.",
                    "affected_locations": [
                        {"file": "instruction.md", "line": 7, "quote": "dataset"}
                    ],
                }
            ],
            checker_result={"tests": [], "solution_oracle": {}},
            contract_map={"requirements": []},
            paper_result={"status": "NOT_ASSESSED"},
            materials_assessment=None,
        )

        self.assertEqual(
            axes["factual_accuracy"]["status"], "NOT_ASSESSABLE"
        )

    def test_answer_leakage_has_its_own_qa_axis(self) -> None:
        axes = finalize_audit_output.derive_qa_axes(
            Path("."),
            [
                {
                    "title": "SOLUTION_BOUNDARY_VIOLATION",
                    "observed_fact": "Solution content entered checker runtime.",
                    "affected_locations": [
                        {"file": "solution/", "line": None, "quote": None}
                    ],
                }
            ],
            checker_result={"tests": [], "solution_oracle": {}},
            contract_map={"requirements": []},
            paper_result={"status": "NOT_ASSESSED"},
            materials_assessment=None,
        )

        self.assertEqual(axes["answer_leakage"]["status"], "FAIL")
        self.assertNotIn("points_earned", axes["answer_leakage"])

    def test_instruction_incompleteness_has_its_own_qa_axis(self) -> None:
        axes = finalize_audit_output.derive_qa_axes(
            Path("."),
            [
                {
                    "title": "INSTRUCTION_ONLY_OUTPUT",
                    "observed_fact": "A required final output lacks a contract.",
                    "affected_locations": [
                        {"file": "instruction.md", "line": 4, "quote": "output"}
                    ],
                }
            ],
            checker_result={"tests": [], "solution_oracle": {}},
            contract_map={"requirements": []},
            paper_result={"status": "NOT_ASSESSED"},
            materials_assessment=None,
        )

        self.assertEqual(axes["instruction_completeness"]["status"], "FAIL")
        self.assertNotIn("points_earned", axes["instruction_completeness"])

    def test_checker_instruction_mismatch_has_its_own_qa_axis(self) -> None:
        axes = finalize_audit_output.derive_qa_axes(
            Path("."),
            [
                {
                    "title": "OUTPUT_NOT_CONTRACTED",
                    "observed_fact": "The checker reads an undeclared output.",
                    "affected_locations": [
                        {
                            "file": "tests/grading_spec.json",
                            "line": 8,
                            "quote": "output_file",
                        }
                    ],
                }
            ],
            checker_result={"tests": [], "solution_oracle": {}},
            contract_map={"requirements": []},
            paper_result={"status": "NOT_ASSESSED"},
            materials_assessment=None,
        )

        self.assertEqual(
            axes["checker_instruction_consistency"]["status"], "FAIL"
        )
        self.assertNotIn(
            "points_earned", axes["checker_instruction_consistency"]
        )


if __name__ == "__main__":
    unittest.main()
