from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

def external_audit_dir(package: Path) -> Path:
    paper_id = (
        package.name[len("paper-"):]
        if package.name.startswith("paper-")
        else package.name
    )
    path = package.parent / "review_outputs" / paper_id / "benchmark_audit"
    path.mkdir(parents=True, exist_ok=True)
    return path


RUNNER = (
    REPO_ROOT
    / ".cursor"
    / "skills"
    / "materials-benchmark-review"
    / "scripts"
    / "run_review.py"
)
SCRIPTS_DIR = RUNNER.parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import audit_package  # noqa: E402
import dynamic_checker_probe  # noqa: E402
import finalize_audit_output  # noqa: E402
import prepare_audit_output  # noqa: E402
SOURCE_PACKAGE = (
    REPO_ROOT
    / "materials_science_questions"
    / "cluster-18137"
    / "compute-sound-velocities-and-debye-temperature-from-elastic-data"
    / "paper-814614162100453378"
)


def copy_source_package(destination: Path) -> None:
    shutil.copytree(
        SOURCE_PACKAGE,
        destination,
    )


def run_review(
    package: Path,
    *,
    audit_output_dir: Path | None = None,
    agent_assessment: Path | None = None,
    extra_args: list[str] | None = None,
    **_ignored,
) -> subprocess.CompletedProcess[str]:
    output = audit_output_dir or (
        package.parent / "review_outputs" / package.name.removeprefix("paper-")
    )
    command = [
        "python3",
        str(RUNNER),
        str(package),
        "--audit-output-dir",
        str(output),
    ]
    if agent_assessment is not None:
        command.extend(["--agent-assessment", str(agent_assessment)])
    if extra_args:
        command.extend(extra_args)
    return subprocess.run(command, capture_output=True, text=True, check=False)



class MaterialsBenchmarkReviewCoreTests(unittest.TestCase):
    def test_review_implementation_digest_covers_every_canonical_dependency(
        self,
    ) -> None:
        canonical = prepare_audit_output.review_implementation_files()
        self.assertIn("scripts/probe_resources.py", canonical)
        self.assertIn("references/materials-taxonomy.json", canonical)
        with tempfile.TemporaryDirectory() as temporary:
            copied = Path(temporary) / "materials-benchmark-review"
            shutil.copytree(RUNNER.parent.parent, copied)
            baseline = prepare_audit_output.collect_review_implementation_hashes(
                copied
            )
            for relative in canonical:
                with self.subTest(relative=relative):
                    path = copied / relative
                    original = path.read_bytes()
                    path.write_bytes(original + b"\n")
                    changed = (
                        prepare_audit_output.collect_review_implementation_hashes(
                            copied
                        )
                    )
                    self.assertNotEqual(
                        changed["aggregate_hash"],
                        baseline["aggregate_hash"],
                    )
                    path.write_bytes(original)

    def test_instruction_role_scope_ends_at_any_later_heading(self) -> None:
        contract = audit_package.instruction_contract_map(
            """
### Step 1: Compute result
- Role: scored (load-bearing)
- Action: Compute the scientific result.
- Output file: `/app/outputs/result.json`

### result.json
- Role: process
- path: `/app/outputs/result.json`
"""
        )

        self.assertEqual(len(contract["requirements"]), 1)
        self.assertEqual(
            contract["requirements"][0]["role"], "scored (load-bearing)"
        )
        self.assertEqual(contract["scored_outputs"], ["result.json"])
        self.assertEqual(contract["process_evidence"], [])

    def test_instruction_output_reference_ignores_sentence_punctuation(self) -> None:
        contract = audit_package.instruction_contract_map(
            """
### Step 5: Compute lambda
- Role: scored (load-bearing)
- Action: Compute the scientific result.
  Write lambda values to /app/outputs/lambda.csv.
  Also retain /app/outputs/archive.tar.gz.
- Output file: `/app/outputs/lambda.csv`
"""
        )

        self.assertEqual(
            contract["requirements"][0]["declared_outputs"],
            ["lambda.csv", "archive.tar.gz"],
        )
        self.assertEqual(
            contract["instruction_outputs"],
            ["archive.tar.gz", "lambda.csv"],
        )
        self.assertNotIn("lambda.csv.", contract["core_outputs"])

    def test_missing_checker_cannot_claim_runtime_binding(self) -> None:
        contract = audit_package.instruction_contract_map(
            """
### Step 1: Compute result
- Role: scored
- Action: Compute it.
- Output file: `/app/outputs/result.json`
"""
        )
        issues: list[dict[str, object]] = []
        analysis = audit_package.checker_contract_analysis(
            "",
            {
                "steps": [
                    {
                        "id": "result",
                        "output_file": "result.json",
                        "weight": 1.0,
                    }
                ]
            },
            contract,
            issues,
        )

        self.assertEqual(analysis["parse_status"], "NOT_RUN")
        self.assertFalse(analysis["all_scoring_items_runtime_bound"])
        self.assertFalse(analysis["all_scoring_items_source_bound"])
        runtime_status = analysis["outputs"][0]["checker_scoring"][
            "runtime_status"
        ]
        self.assertIsInstance(runtime_status, str)
        self.assertEqual(runtime_status, "RUNTIME_NOT_PROVEN")

    def test_static_scorer_analysis_handles_none_and_partial_returns(self) -> None:
        contract = audit_package.instruction_contract_map(
            """
### Step 1: A
- Role: scored
- Action: Compute A.
- Output file: `/app/outputs/a.json`
### Step 2: B
- Role: scored
- Action: Compute B.
- Output file: `/app/outputs/b.json`
"""
        )
        checker = """
def score_a(artifact, step, ctx):
    return None

def score_b(artifact, step, ctx):
    if artifact:
        return 1.0

_SCORERS = {"a": score_a, "b": score_b}
"""
        issues: list[dict[str, object]] = []
        analysis = audit_package.checker_contract_analysis(
            checker,
            {
                "steps": [
                    {"id": "a", "output_file": "a.json", "weight": 0.5},
                    {"id": "b", "output_file": "b.json", "weight": 0.5},
                ]
            },
            contract,
            issues,
        )

        self.assertEqual(
            analysis["scorer_status"]["a"]["return_status"],
            "ALWAYS_RETURNS_NONE",
        )
        self.assertEqual(
            analysis["scorer_status"]["b"]["return_status"],
            "PARTIAL_RETURN_PATHS",
        )
        self.assertIn("SCORER_RETURN_NOT_TOTAL", {item["code"] for item in issues})
        for output in analysis["outputs"]:
            scoring = output["checker_scoring"]
            self.assertIsNone(scoring["effective_weight"])
            self.assertFalse(scoring["runtime_score_proven"])

    def test_pass_probe_coverage_rejects_invalid_unavailable_provenance(
        self,
    ) -> None:
        coverage = {
            "positive": {"status": "ASSESSED"},
            "negative": {
                "status": "ASSESSED",
                "subcoverage": {
                    "task_family_attacks": {
                        "constant_or_all_zero": {
                            "status": "NOT_APPLICABLE",
                            "reason": "not applicable to this fixture",
                            "provenance": {
                                "source_kind": "NONE",
                                "oracle_used": False,
                            },
                        },
                    },
                },
            },
            "discrimination": {
                "status": "NOT_ASSESSABLE",
                "provenance": {
                    "source_kind": "NONE",
                    "oracle_used": False,
                    "external_result_directory_accepted": False,
                },
            },
            "equivalence": {
                "status": "NOT_ASSESSABLE",
                "provenance": {
                    "source_kind": "NONE",
                    "oracle_used": False,
                    "external_result_directory_accepted": False,
                },
            },
            "component_isolation": {
                "status": "NOT_APPLICABLE",
                "reason": "not part of deterministic core",
                "provenance": {
                    "source_kind": "NONE",
                    "oracle_used": False,
                    "external_result_directory_accepted": False,
                    "source_bindings_verified": False,
                    "runtime_bindings_verified": False,
                    "cases_planned": 0,
                    "cases_executed": 0,
                },
            },
        }
        finalize_audit_output.validate_pass_probe_coverage(coverage)

        dishonest = json.loads(json.dumps(coverage))
        dishonest["discrimination"]["provenance"]["source_kind"] = (
            "ORACLE_POSITIVE_MOCK"
        )
        with self.assertRaisesRegex(
            ValueError, "invalid unavailable discrimination probe state"
        ):
            finalize_audit_output.validate_pass_probe_coverage(dishonest)

        invalid_status = json.loads(json.dumps(coverage))
        invalid_status["equivalence"]["status"] = "SKIPPED"
        with self.assertRaisesRegex(
            ValueError, "invalid unavailable equivalence probe state"
        ):
            finalize_audit_output.validate_pass_probe_coverage(invalid_status)

        for label, provenance_update in (
            ("oracle_used", {"oracle_used": True}),
            ("source_kind", {"source_kind": "ORACLE_POSITIVE_MOCK"}),
            (
                "external_result_directory",
                {"external_result_directory_accepted": True},
            ),
        ):
            with self.subTest(label=label):
                oracle_component = json.loads(json.dumps(coverage))
                oracle_component["component_isolation"]["status"] = (
                    "NOT_ASSESSABLE"
                )
                oracle_component["component_isolation"]["reason"] = (
                    "runtime failed"
                )
                oracle_component["component_isolation"]["provenance"].update(
                    provenance_update
                )
                with self.assertRaisesRegex(
                    ValueError, "provenance"
                ):
                    finalize_audit_output.validate_pass_probe_coverage(
                        oracle_component
                    )

    def test_output_free_requirement_has_complete_unknown_chain(self) -> None:
        contract = audit_package.instruction_contract_map(
            """
### Step 1: Inspect convergence
- Role: process
- Action: Inspect convergence before computing the final result.
"""
        )
        checker = audit_package.checker_contract_analysis(
            "",
            {},
            contract,
            [],
        )
        chains = audit_package._requirement_chains(
            contract, checker["outputs"]
        )

        self.assertEqual(len(contract["requirements"]), 1)
        self.assertEqual(len(chains), 1)
        self.assertIsNone(chains[0]["core_output"])
        self.assertEqual(chains[0]["output_role"], "unclassified")
        self.assertEqual(
            chains[0]["checker_read"], "UNKNOWN_NO_DECLARED_OUTPUT"
        )
        self.assertEqual(
            chains[0]["checker_score"]["checker_scores"],
            "UNKNOWN_NO_DECLARED_OUTPUT",
        )

    def test_component_isolation_requires_source_and_runtime_bindings(
        self,
    ) -> None:
        self.assertFalse(
            hasattr(dynamic_checker_probe, "component_isolation_plan")
        )
        self.assertFalse(
            hasattr(dynamic_checker_probe, "component_isolation_coverage")
        )

    def test_usable_probe_result_rejects_swallowed_errors_across_classes(
        self,
    ) -> None:
        def result(
            case: str,
            reward: float,
            errors: object = None,
        ) -> dict[str, object]:
            breakdown: dict[str, object] = {}
            if errors is not None:
                breakdown["_errors"] = errors
            return {
                "case": case,
                "reward": reward,
                "breakdown": breakdown,
                "crashed": False,
                "returncode": 0,
                "stderr": "",
                "runtime_package_contains_solution": False,
            }

        self.assertTrue(
            dynamic_checker_probe.usable_probe_result(
                result("clean", 1.0)
            )
        )
        for errors in (
            {"scorer": "swallowed"},
            ["swallowed"],
            "swallowed",
            17,
            [],
        ):
            with self.subTest(errors=errors):
                self.assertFalse(
                    dynamic_checker_probe.usable_probe_result(
                        result("malformed", 1.0, errors)
                    )
                )

        positive = [result("positive_oracle", 1.0, "positive swallowed")]
        self.assertFalse(
            dynamic_checker_probe.probe_assessment_flags(positive)["positive"]
        )
        self.assertIn(
            "CORE_RUNTIME_RESULT_UNUSABLE",
            {
                item["code"]
                for item in dynamic_checker_probe.evaluate_results(
                    positive, 0.8
                )
            },
        )

        discrimination = [
            result("positive_oracle", 0.8),
            result(
                "quality_gradient_small_error",
                0.9,
                ["gradient swallowed"],
            ),
            result("quality_gradient_large_error", 0.7),
        ]
        self.assertFalse(
            dynamic_checker_probe.probe_assessment_flags(discrimination)[
                "discrimination"
            ]
        )
        discrimination_findings = dynamic_checker_probe.evaluate_results(
            discrimination, 0.8
        )
        self.assertNotIn(
            "SCIENTIFIC_QUALITY_GRADIENT_VIOLATION",
            {item["code"] for item in discrimination_findings},
        )

        equivalence = [
            result("positive_oracle", 1.0),
            result(
                "metamorphic_equivalent_representation",
                0.5,
                {"equivalence": "swallowed"},
            ),
        ]
        self.assertFalse(
            dynamic_checker_probe.probe_assessment_flags(equivalence)[
                "equivalence"
            ]
        )
        equivalence_findings = dynamic_checker_probe.evaluate_results(
            equivalence, 0.8
        )
        self.assertNotIn(
            "SCIENTIFIC_INVARIANCE_VIOLATION",
            {item["code"] for item in equivalence_findings},
        )

        self.assertFalse(
            hasattr(dynamic_checker_probe, "component_isolation_coverage")
        )

    def test_repeated_runtime_failure_signature_shares_deduction_root(
        self,
    ) -> None:
        def result(
            case: str, source_line: int, terminal_error: str
        ) -> dict[str, object]:
            return {
                "case": case,
                "runtime_package_contains_solution": False,
                "crashed": True,
                "stderr": (
                    "Traceback\n"
                    f'  File "/tmp/run/checker_patched.py", line '
                    f"{source_line}, in main\n"
                    f"{terminal_error}\n"
                ),
                "returncode": 1,
                "reward": None,
            }

        findings = dynamic_checker_probe.evaluate_results(
            [
                result("missing_outputs", 12, "RuntimeError: same defect"),
                result("random_baseline", 12, "RuntimeError: same defect"),
                result("malformed_outputs", 27, "RuntimeError: same defect"),
            ],
            0.6,
        )
        crash_roots = [
            item["evidence"]["root_cause"]
            for item in findings
            if item["code"] in {"CHECKER_CRASH", "CORE_RUNTIME_CHECKER_CRASH"}
        ]
        self.assertEqual(crash_roots[0], crash_roots[1])
        self.assertNotEqual(crash_roots[0], crash_roots[2])

        first = result(
            "missing_outputs",
            12,
            "RuntimeError: /tmp/run-a/value-"
            "123e4567-e89b-12d3-a456-426614174000 at 0xabc123",
        )
        second = result(
            "random_baseline",
            12,
            "RuntimeError: /private/var/folders/zz/run-b/value-"
            "f47ac10b-58cc-4372-a567-0e02b2c3d479 at 0xdef456",
        )
        first_root = dynamic_checker_probe.runtime_failure_root(first)[0]
        second_root = dynamic_checker_probe.runtime_failure_root(second)[0]
        self.assertEqual(first_root, second_root)

        pid_space = result(
            "missing_outputs", 12, "RuntimeError: worker pid 123 failed"
        )
        pid_equals = result(
            "random_baseline", 12, "RuntimeError: worker PID=9876 failed"
        )
        self.assertEqual(
            dynamic_checker_probe.runtime_failure_root(pid_space)[0],
            dynamic_checker_probe.runtime_failure_root(pid_equals)[0],
        )

        list_error = result(
            "missing_outputs", 12, "RuntimeError: scorer failed"
        )
        list_error["breakdown"] = {"_errors": ["same failure"]}
        string_error = result(
            "random_baseline", 12, "RuntimeError: scorer failed"
        )
        string_error["breakdown"] = {"_errors": "same failure"}
        self.assertNotEqual(
            dynamic_checker_probe.runtime_failure_root(list_error)[0],
            dynamic_checker_probe.runtime_failure_root(string_error)[0],
        )
        scalar_error = result(
            "missing_outputs", 12, "RuntimeError: scorer failed"
        )
        scalar_error["breakdown"] = {"_errors": 17}
        scalar_root = dynamic_checker_probe.runtime_failure_root(scalar_error)[
            0
        ]
        self.assertEqual(
            scalar_root,
            dynamic_checker_probe.runtime_failure_root(scalar_error)[0],
        )
        self.assertNotIn(
            scalar_root,
            {
                dynamic_checker_probe.runtime_failure_root(list_error)[0],
                dynamic_checker_probe.runtime_failure_root(string_error)[0],
            },
        )

    def test_deduction_groups_require_explicit_shared_root_cause(self) -> None:
        oracle = finalize_audit_output.normalized_finding(
            Path("."),
            {
                "severity": "HIGH",
                "code": "ORACLE_POSITIVE_MOCK_REJECTED",
                "message": "Oracle mock rejected.",
                "affected_files": ["tests/checker.py"],
            },
            "FINDING-001",
            "EV1",
            "CHECKER_ROBUSTNESS",
        )
        missing_return = finalize_audit_output.normalized_finding(
            Path("."),
            {
                "severity": "HIGH",
                "code": "SCORER_MISSING_RETURN",
                "message": "Scorer has no return.",
                "affected_files": ["tests/checker.py"],
                "evidence": {
                    "root_cause": "checker_scorer_return_contract"
                },
            },
            "FINDING-002",
            "E0",
            "PACKAGE_STATIC",
        )
        self.assertNotEqual(
            oracle["deduction_group"], missing_return["deduction_group"]
        )

        shared = []
        for finding_id, severity in (
            ("FINDING-003", "MEDIUM"),
            ("FINDING-004", "HIGH"),
        ):
            shared.append(
                {
                    "finding_id": finding_id,
                    "title": "CHECKER_CRASH",
                    "severity": severity,
                    "category": "CHECKER_ROBUSTNESS",
                    "affected_files": ["tests/checker.py"],
                    "affected_locations": [],
                    "observed_fact": "same runtime root",
                    "deduction_group": "checker_case_runtime:case",
                }
            )
        dimensions = finalize_audit_output.dimension_scores(
            {"tests": [], "probe_coverage": {}},
            shared,
            {"status": "NOT_ASSESSED"},
        )
        robustness = next(
            item
            for item in dimensions
            if item["dimension"] == "robustness_discrimination"
        )
        applied = [
            item
            for item in robustness["deductions"]
            if item["deduction_applied"]
        ]
        self.assertEqual(len(applied), 1)
        self.assertEqual(applied[0]["finding_id"], "FINDING-004")
        self.assertEqual(applied[0]["points"], 6.0)

    def test_v11_dimension_metadata_matches_plan(self) -> None:
        self.assertEqual(
            finalize_audit_output.V11_DIMENSION_TITLES,
            {
                "C01": "domain_admission",
                "C02": "task_design_and_file_consistency",
                "C03": "scientific_validity_and_solvability",
                "C04": "scoring_semantics",
                "C05": "answer_leakage",
                "C06": "reproducibility",
                "C07": "difficulty_and_auditability",
            },
        )
        self.assertEqual(
            finalize_audit_output.V11_DIMENSION_WEIGHTS,
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
        self.assertEqual(
            finalize_audit_output.V11_KEY_DIMENSIONS,
            {"C01", "C03", "C04", "C06"},
        )
        self.assertEqual(
            finalize_audit_output.V11_HARD_GATE_DIMENSION[
                "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE"
            ],
            "C06",
        )
        self.assertEqual(
            finalize_audit_output.V11_HARD_GATE_DIMENSION["NON_MATERIALS_TASK"],
            "C01",
        )

    def test_v11_finding_attribution_c05_c06_c07(self) -> None:
        def finding(code: str, category: str = "") -> dict[str, object]:
            return {
                "title": code,
                "category": category,
                "affected_files": [],
            }

        attribute = finalize_audit_output.scored_dimension_v11_for
        for code in (
            "SOLUTION_BOUNDARY_VIOLATION",
            "ANSWER_LEAKAGE",
            "ORACLE_VALUE_LEAKED",
            "PAPER_ANSWER_LEAK",
            "PAPER_IDENTITY_MISMATCH",
        ):
            self.assertEqual(attribute(finding(code)), "C05", msg=code)
        for code in (
            "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE",
            "INDISPENSABLE_DIRECT_INPUT_TRANSIENT",
            "PAPER_REPRODUCIBILITY_GAP",
        ):
            self.assertEqual(attribute(finding(code)), "C06", msg=code)
        self.assertEqual(
            attribute(finding("RESOURCE_MISSING", "RESOURCE_USABILITY")),
            "C06",
        )
        for code in (
            "SCIENTIFIC_QUALITY_GRADIENT_VIOLATION",
            "SCIENTIFIC_INVARIANCE_VIOLATION",
        ):
            self.assertEqual(attribute(finding(code)), "C07", msg=code)

    def test_pass_is_blocked_without_authoritative_materials_qualification(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            completed = run_review(package)

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            report = json.loads(
                (external_audit_dir(package) / "audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(
                report["summary"]["final_verdict"], "NOT_ASSESSABLE"
            )
            self.assertIsNone(report["summary"]["total_score"])
            self.assertFalse(
                report["materials_qualification"]["authoritative"]
            )
            self.assertIn(
                "authoritative_materials_qualification",
                report["evidence_contract"]["gaps"],
            )

    def test_solution_oracle_timeout_reports_the_failed_stage(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            (package / "solution/solve.sh").write_text(
                "#!/bin/sh\nsleep 1\n", encoding="utf-8"
            )
            output = workspace / "checker.json"
            environment = {
                **os.environ,
                "MATERIALS_ORACLE_SOLVE_TIMEOUT_SECONDS": "0.05",
            }

            completed = subprocess.run(
                [
                    sys.executable,
                    str(
                        RUNNER.parent / "dynamic_checker_probe.py"
                    ),
                    str(package),
                    "--output",
                    str(output),
                ],
                cwd=REPO_ROOT,
                env=environment,
                capture_output=True,
                text=True,
                timeout=30,
                check=False,
            )

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            oracle = json.loads(output.read_text(encoding="utf-8"))[
                "solution_oracle"
            ]
            self.assertEqual(oracle["status"], "BROKEN")
            self.assertEqual(oracle["failure_stage"], "solve")
            self.assertEqual(oracle["failure_reason"], "TIMEOUT")
            self.assertEqual(oracle["timeout_seconds"], 0.05)
            self.assertTrue(oracle["attempted"])
            self.assertTrue(oracle["setup_prepared"])
            self.assertTrue(oracle["producer_started"])
            self.assertTrue(oracle["executed"])

    def test_oracle_venv_failure_is_not_reported_as_executed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            (package / "solution/solve.sh").write_text(
                "#!/bin/sh\nexit 0\n", encoding="utf-8"
            )
            specification = json.loads(
                (package / "tests/grading_spec.json").read_text(
                    encoding="utf-8"
                )
            )
            with (
                mock.patch.object(
                    dynamic_checker_probe.shutil,
                    "which",
                    return_value=None,
                ),
                mock.patch.object(
                    dynamic_checker_probe.subprocess,
                    "run",
                    side_effect=subprocess.TimeoutExpired(
                        [sys.executable, "-m", "venv"], 0.05
                    ),
                ),
            ):
                temporary_oracle, oracle_output, oracle = (
                    dynamic_checker_probe.prepare_solution_oracle(
                        package, specification
                    )
                )
            try:
                self.assertIsNone(oracle_output)
                self.assertEqual(oracle["failure_stage"], "venv")
                self.assertTrue(oracle["attempted"])
                self.assertTrue(oracle["setup_attempted"])
                self.assertFalse(oracle["setup_prepared"])
                self.assertFalse(oracle["producer_started"])
                self.assertFalse(oracle["executed"])
            finally:
                if temporary_oracle is not None:
                    temporary_oracle.cleanup()

    def test_solution_oracle_supplies_an_isolated_positive_mock_only(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            (package / "solution/solve.sh").write_text(
                "#!/bin/sh\n"
                "mkdir -p \"$OUTPUT_DIR\"\n"
                "printf 'direction,mode,k,frequency\\n100,L,0,0\\n' "
                "> \"$OUTPUT_DIR/dispersion_curves.csv\"\n",
                encoding="utf-8",
            )

            completed = subprocess.run(
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

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            audit_dir = external_audit_dir(package)
            checker = json.loads(
                (audit_dir / "checker_tests.json").read_text(encoding="utf-8")
            )
            positive = next(
                item
                for item in checker["tests"]
                if item["test_type"] == "positive_oracle"
            )
            self.assertEqual(positive["probe_class"], "positive")
            self.assertIsNone(positive["observed_score"])
            self.assertTrue(
                positive["evidence"]["contracted_outputs_generated"]
            )
            self.assertTrue(checker["solution_oracle"]["used"])
            self.assertFalse(checker["solution_oracle"]["scientific_evidence"])
            serialized = json.dumps(checker, ensure_ascii=False)
            self.assertNotIn("1.68e12", serialized)
            self.assertNotIn("oracle-output", serialized)
            report = json.loads(
                (audit_dir / "audit_report.json").read_text(encoding="utf-8")
            )
            self.assertTrue(report["scope"]["solution_oracle_executed"])
            self.assertFalse(report["scope"]["solution_content_inspected"])
            manifest = json.loads(
                (audit_dir / "audit_manifest.json").read_text(encoding="utf-8")
            )
            self.assertTrue(manifest["solution_oracle_executed"])
            self.assertFalse(
                any(path.startswith("solution/") for path in manifest["input_hashes"])
            )

    def test_static_unknown_process_evidence_is_not_claimed_unverified(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            instruction = package / "instruction.md"
            instruction.write_text(
                instruction.read_text(encoding="utf-8")
                + "\n\n### Step 2: Audit process evidence\n"
                "- Role: process\n"
                "- Evidence: `/app/outputs/process_trace.json`\n",
                encoding="utf-8",
            )
            completed = run_review(package)

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            report = json.loads(
                (external_audit_dir(package) / "audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            process_findings = [
                item
                for item in report["findings"]
                if item["title"] == "PROCESS_EVIDENCE_NOT_VERIFIED"
            ]
            self.assertEqual(process_findings, [])
            mapped_process = next(
                item
                for item in report["contract_map"]["checker_analysis"]["outputs"]
                if item["file"] == "process_trace.json"
            )
            self.assertEqual(mapped_process["role"], "process_evidence")
            self.assertEqual(
                mapped_process["checker_reads"], "UNKNOWN_NOT_ESTABLISHED"
            )
            self.assertFalse(
                any(
                    item["title"] == "INSTRUCTION_ONLY_OUTPUT"
                    and "process_trace.json" in item["observed_fact"]
                    for item in report["findings"]
                )
            )

    def test_static_process_read_candidate_remains_conservative(self) -> None:
        instruction = """
### Step 1: Record trace
- Role: process
- Action: Record the convergence trace.
- Evidence: `/app/outputs/process_trace.json`
"""
        contract = audit_package.instruction_contract_map(instruction)
        issues: list[dict[str, object]] = []
        checker = audit_package.checker_contract_analysis(
            "def inspect():\n"
            "    return open('/app/outputs/process_trace.json').read()\n",
            {},
            contract,
            issues,
        )
        contract["checker_analysis"] = checker
        sets = audit_package.cross_file_checks(
            instruction, [], {}, "", issues, contract
        )

        self.assertEqual(
            checker["outputs"][0]["checker_reads"],
            "STATIC_EXPLICIT_READ_CANDIDATE",
        )
        self.assertEqual(
            sets["process_evidence_status"]["process_trace.json"],
            "CONTRACT_MAP_ONLY",
        )
        self.assertEqual(sets["unverified_process_evidence"], [])
        self.assertNotIn(
            "PROCESS_EVIDENCE_NOT_VERIFIED",
            {item["code"] for item in issues},
        )

    def test_process_artifacts_never_create_dynamic_findings_or_tests(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            instruction = package / "instruction.md"
            instruction.write_text(
                instruction.read_text(encoding="utf-8")
                + "\n\n### Step 2: Record process evidence\n"
                "- Role: process\n"
                "- Action: Record both convergence artifacts.\n"
                "- Evidence: `/app/outputs/process_trace.json`\n"
                "- Evidence: `/app/outputs/training.log`\n",
                encoding="utf-8",
            )
            completed = run_review(package)

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            report = json.loads(
                (external_audit_dir(package) / "audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            findings = [
                item
                for item in report["findings"]
                if item["title"] == "PROCESS_EVIDENCE_NOT_VERIFIED"
            ]
            self.assertEqual(findings, [])
            process_tests = [
                item
                for item in report["checker_tests"]
                if item["probe_class"] == "process_evidence"
            ]
            self.assertEqual(process_tests, [])
            mapped = {
                item["file"]: item
                for item in report["contract_map"]["checker_analysis"][
                    "outputs"
                ]
            }
            for filename in ("process_trace.json", "training.log"):
                self.assertEqual(mapped[filename]["role"], "process_evidence")
            checker = json.loads(
                (
                    external_audit_dir(package) / "checker_tests.json"
                ).read_text(encoding="utf-8")
            )
            self.assertEqual(
                set(checker["probe_coverage"]),
                {
                    "positive",
                    "negative",
                    "discrimination",
                    "equivalence",
                    "component_isolation",
                },
            )
            self.assertEqual(
                checker["probe_coverage"]["discrimination"]["provenance"][
                    "source_kind"
                ],
                "NONE",
            )

    def test_process_access_tracer_is_out_of_scope(self) -> None:
        self.assertFalse(
            hasattr(dynamic_checker_probe, "process_evidence_coverage")
        )

    def test_component_weight_reaching_threshold_is_a_risk_not_a_proven_bypass(
        self,
    ) -> None:
        self.assertFalse(
            hasattr(dynamic_checker_probe, "component_isolation_plan")
        )
        self.assertFalse(
            hasattr(dynamic_checker_probe, "component_isolation_coverage")
        )

    def test_oracle_positive_mock_is_never_component_isolation_fixture(
        self,
    ) -> None:
        self.assertFalse(
            hasattr(dynamic_checker_probe, "component_isolation_plan")
        )
        self.assertFalse(
            hasattr(dynamic_checker_probe, "component_isolation_coverage")
        )

    def test_source_bound_component_isolation_executes_and_can_prove_bypass(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            completed = run_review(package)

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            report = json.loads(
                (external_audit_dir(package) / "audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertFalse(
                any(
                    item["probe_class"] == "component_isolation"
                    for item in report["checker_tests"]
                )
            )
            self.assertNotIn(
                "SINGLE_COMPONENT_CAN_PASS",
                {item["title"] for item in report["findings"]},
            )

    def test_report_publishes_instruction_to_checker_contract_mapping(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            instruction = package / "instruction.md"
            instruction.write_text(
                instruction.read_text(encoding="utf-8")
                + "\n\n### Step 2: Inspect convergence\n"
                "- Role: process\n"
                "- Action: Inspect convergence before finalizing results.\n",
                encoding="utf-8",
            )
            completed = run_review(package)

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            report = json.loads(
                (external_audit_dir(package) / "audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            contract_map = report["contract_map"]
            self.assertIn(
                "dispersion_curves.csv",
                contract_map["scored_outputs"],
            )
            mapped = next(
                item
                for item in contract_map["checker_analysis"]["outputs"]
                if item["file"] == "dispersion_curves.csv"
            )
            self.assertEqual(mapped["role"], "scored_output")
            self.assertTrue(mapped["instruction_declared"])
            self.assertTrue(mapped["structured_contract"])
            self.assertEqual(
                mapped["checker_reads"], "STATIC_GENERIC_LOADER_CANDIDATE"
            )
            self.assertFalse(mapped["checker_read_runtime_proven"])
            self.assertIsNotNone(mapped["checker_scoring"])
            self.assertTrue(
                mapped["checker_scoring"]["scorer_bound"]
            )
            self.assertIsInstance(
                mapped["checker_scoring"]["runtime_status"], str
            )
            chain = next(
                item
                for item in contract_map["requirement_chains"]
                if item["core_output"] == "dispersion_curves.csv"
            )
            self.assertIn("compute the angular frequency", chain["agent_work"])
            self.assertEqual(
                chain["checker_read"], "STATIC_GENERIC_LOADER_CANDIDATE"
            )
            markdown = (
                external_audit_dir(package) / "audit_report.md"
            ).read_text(encoding="utf-8")
            self.assertIn("agent_work=Using the Born", markdown)
            self.assertIn("core_output=dispersion_curves.csv", markdown)
            output_free_chain = next(
                item
                for item in contract_map["requirement_chains"]
                if item["core_output"] is None
            )
            self.assertEqual(
                output_free_chain["checker_read"],
                "UNKNOWN_NO_DECLARED_OUTPUT",
            )
            self.assertIn(
                "[requirement=1; declaration=None]", markdown
            )
            finalize_audit_output.validate_requirement_chains(
                contract_map, markdown
            )

    def test_missing_scorer_return_is_reported_as_checker_contract_bug(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            checker_path = package / "tests/checker.py"
            checker_source = checker_path.read_text(encoding="utf-8")
            broken_scorer = (
                "\ndef broken_score(artifact, step, ctx):\n"
                "    computed = 1.0\n"
                "    computed\n\n"
                "_SCORERS = {'step_dispersion': broken_score}\n"
            )
            checker_path.write_text(
                checker_source.replace(
                    '\nif __name__ == "__main__":',
                    broken_scorer + '\nif __name__ == "__main__":',
                ),
                encoding="utf-8",
            )
            completed = run_review(package)

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            report = json.loads(
                (external_audit_dir(package) / "audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            finding = next(
                item
                for item in report["findings"]
                if item["title"] == "SCORER_MISSING_RETURN"
            )
            self.assertIn("step_dispersion", finding["observed_fact"])
            self.assertIn(
                finding["finding_id"],
                {item["finding_id"] for item in report["findings"]},
            )

    def test_rejected_oracle_mock_is_attributed_to_checker_alignment(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            (package / "solution/solve.sh").write_text(
                "#!/bin/sh\n"
                "mkdir -p /app/outputs\n"
                "printf 'direction,mode,k,frequency\\n100,L,0,999\\n' "
                "> /app/outputs/dispersion_curves.csv\n",
                encoding="utf-8",
            )

            completed = subprocess.run(
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

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            report = json.loads(
                (external_audit_dir(package) / "audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            finding_codes = {item["title"] for item in report["findings"]}
            self.assertIn("CORE_RUNTIME_ORACLE_REJECTED", finding_codes)
            self.assertNotIn("SOLUTION_POSITIVE_MOCK_REJECTED", finding_codes)
            oracle_finding = next(
                item
                for item in report["findings"]
                if item["title"] == "CORE_RUNTIME_ORACLE_REJECTED"
            )
            self.assertIn("checker", oracle_finding["minimal_repair"].lower())
            self.assertNotIn("solution/solve.sh", oracle_finding["minimal_repair"])


    def test_public_report_cites_evidence_for_every_hard_gate(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            checker_path = package / "tests/checker.py"
            checker_path.write_text(
                "raise RuntimeError('forced checker evidence gap')\n"
                + checker_path.read_text(encoding="utf-8"),
                encoding="utf-8",
            )

            completed = run_review(package)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            report = json.loads(
                (external_audit_dir(package) / "audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(len(report["hard_gates"]), 4)
            self.assertIn(
                "NOT_ASSESSABLE",
                {gate["status"] for gate in report["hard_gates"]},
            )
            for gate in report["hard_gates"]:
                self.assertTrue(gate["evidence"], msg=gate["code"])
                self.assertTrue(gate["affected_locations"], msg=gate["code"])
                for item in gate["evidence"]:
                    self.assertTrue(item["observed_fact"])
                    self.assertEqual(
                        set(item["source_evidence"]),
                        {"file", "line", "quote"},
                    )
                for location in gate["affected_locations"]:
                    self.assertEqual(set(location), {"file", "line", "quote"})
                    self.assertTrue(location["file"])
                    self.assertIsInstance(location["line"], int)
                    self.assertGreater(location["line"], 0)
                    self.assertTrue(location["quote"])

    def test_missing_checker_is_structural_and_gate_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            (package / "tests/checker.py").unlink()
            completed = run_review(package)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            audit_dir = external_audit_dir(package)
            report = json.loads(
                (audit_dir / "audit_report.json").read_text(encoding="utf-8")
            )
            checker = json.loads(
                (audit_dir / "checker_tests.json").read_text(encoding="utf-8")
            )
            self.assertEqual(
                report["summary"]["final_verdict"], "NOT_ASSESSABLE"
            )
            self.assertIn(
                "MISSING_FILE",
                {finding["title"] for finding in report["findings"]},
            )
            self.assertEqual(checker["tests"], [])
            gates = {
                gate["gate_id"]: gate["status"]
                for gate in report["gate_results"]
            }
            self.assertEqual(
                gates["CHECKER_CORE_ALIGNMENT"], "NOT_ASSESSABLE"
            )
            self.assertNotIn(
                "checker_gold_alignment",
                report["evidence_contract"]["gaps"],
            )
            checker_gate = next(
                gate
                for gate in report["hard_gates"]
                if gate["code"] == "CHECKER_CORE_TASK_UNASSESSED"
            )
            self.assertIn(
                "repairable structural defect",
                checker_gate["evidence"][0]["observed_fact"],
            )
            markdown = (audit_dir / "audit_report.md").read_text(
                encoding="utf-8"
            )
            checker_section = markdown.split(
                "## 10. Checker Assessment", 1
            )[1].split("## 11.", 1)[0]
            self.assertIn("Status: NOT_ASSESSED", checker_section)

    def test_malformed_grading_schema_is_repairable(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            specification_path = package / "tests/grading_spec.json"
            specification = json.loads(
                specification_path.read_text(encoding="utf-8")
            )
            specification["output_contract"] = [{"outputs": []}]
            specification["steps"] = {}
            specification_path.write_text(
                json.dumps(specification), encoding="utf-8"
            )
            completed = run_review(package)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            report = json.loads(
                (external_audit_dir(package) / "audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(
                report["summary"]["final_verdict"], "NOT_ASSESSABLE"
            )
            self.assertIn(
                "INVALID_GRADING_SPEC_SCHEMA",
                {finding["title"] for finding in report["findings"]},
            )

    def test_bundle_validation_rejects_semantic_cross_artifact_tampering(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            (package / "tests/checker.py").unlink()
            completed = run_review(package)
            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            audit = external_audit_dir(package)
            finalize_audit_output.validate_bundle(audit)

            report_path = audit / "audit_report.json"
            original_report = report_path.read_text(encoding="utf-8")
            report = json.loads(original_report)
            report["summary"]["final_verdict"] = "CONDITIONAL"
            report_path.write_text(json.dumps(report), encoding="utf-8")
            with self.assertRaisesRegex(
                ValueError, "inconsistent"
            ):
                finalize_audit_output.validate_bundle(audit)
            report_path.write_text(original_report, encoding="utf-8")

            findings_path = audit / "findings.jsonl"
            original_findings = findings_path.read_text(encoding="utf-8")
            finding_lines = [
                json.loads(line)
                for line in original_findings.splitlines()
                if line.strip()
            ]
            self.assertTrue(finding_lines)
            finding_lines[0]["impact"] = "tampered with the same count"
            findings_path.write_text(
                "\n".join(json.dumps(item) for item in finding_lines) + "\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(
                ValueError, "JSONL content differs"
            ):
                finalize_audit_output.validate_bundle(audit)
            findings_path.write_text(original_findings, encoding="utf-8")

            checker_path = audit / "checker_tests.json"
            original_checker = checker_path.read_text(encoding="utf-8")
            checker = json.loads(original_checker)
            checker["probe_coverage"]["component_isolation"]["status"] = (
                "NOT_RUN"
            )
            checker_path.write_text(json.dumps(checker), encoding="utf-8")
            with self.assertRaisesRegex(
                ValueError, "invalid component_isolation probe coverage"
            ):
                finalize_audit_output.validate_bundle(audit)
            checker_path.write_text(original_checker, encoding="utf-8")

    def test_nonfinite_pass_threshold_is_a_repairable_static_finding(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            specification_path = package / "tests/grading_spec.json"
            specification = json.loads(
                specification_path.read_text(encoding="utf-8")
            )
            specification["pass_threshold"] = "NaN"
            specification_path.write_text(
                json.dumps(specification), encoding="utf-8"
            )
            completed = run_review(package)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            report = json.loads(
                (external_audit_dir(package) / "audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(
                report["summary"]["final_verdict"], "NOT_ASSESSABLE"
            )
            self.assertIn(
                "INVALID_PASS_THRESHOLD",
                {finding["title"] for finding in report["findings"]},
            )

    def test_required_role_cannot_route_through_solution_symlink(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            solution_tests = package / "solution/tests"
            shutil.copytree(package / "tests", solution_tests)
            shutil.rmtree(package / "tests")
            os.symlink(
                solution_tests,
                package / "tests",
                target_is_directory=True,
            )
            completed = run_review(package)

            self.assertNotEqual(completed.returncode, 0)
            self.assertIn(
                "routes through a symlink", completed.stderr
            )
            self.assertFalse((external_audit_dir(package) / "audit_report.json").exists())

    def test_failed_reaudit_preserves_previous_authoritative_bundle(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            previous_audit = external_audit_dir(package)
            previous_audit.mkdir(exist_ok=True)
            marker = previous_audit / "previous-result.txt"
            marker.write_text("authoritative", encoding="utf-8")

            package.rename(workspace / "package-hidden")
            failed = run_review(package)
            (workspace / "package-hidden").rename(package)
            self.assertNotEqual(failed.returncode, 0)
            self.assertEqual(marker.read_text(encoding="utf-8"), "authoritative")

            completed = run_review(package)
            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            self.assertTrue((external_audit_dir(package)).is_dir())
            archived_markers = list(
                (external_audit_dir(package).parent / "benchmark_audit_history").rglob(
                    "previous-result.txt"
                )
            )
            self.assertEqual(len(archived_markers), 1)
            self.assertEqual(
                archived_markers[0].read_text(encoding="utf-8"),
                "authoritative",
            )


if __name__ == "__main__":
    unittest.main()
