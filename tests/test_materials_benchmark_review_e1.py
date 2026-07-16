from __future__ import annotations

import csv
import hashlib
import json
import math
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
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
        ignore=shutil.ignore_patterns("solution"),
    )
    (destination / "solution").mkdir()


def write_public_valid_dispersion(output_dir: Path) -> None:
    c11 = 1.68e12
    c12 = 1.21e12
    c44 = 0.75e12
    rho = 8.96
    a_angstrom = 3.61
    a_cm = a_angstrom * 1e-8
    epsilon = c11 - c12 - 2 * c44
    factor8 = 8.0 / (rho * a_cm * a_cm)
    factor2 = 2.0 / (rho * a_cm * a_cm)

    def frequency(direction: str, mode: str, k_value: float) -> float:
        if direction == "100":
            sin_sq = math.sin(a_angstrom * k_value / (2 * math.sqrt(2))) ** 2
            bracket = c11 if mode == "L" else c44
            omega_sq = factor8 * sin_sq * bracket
        elif direction == "110":
            sin_sq = math.sin(a_angstrom * k_value / 4) ** 2
            if mode == "L":
                bracket = (
                    2 * c11
                    - epsilon
                    - (2 * c11 - c44 - epsilon) * sin_sq
                )
            elif mode == "T1":
                bracket = epsilon + 2 * c44 - (c44 + epsilon) * sin_sq
            else:
                bracket = 2 * c44 - (2 * c44 - c11) * sin_sq
            omega_sq = factor8 * sin_sq * bracket
        else:
            sin_sq = math.sin(a_angstrom * k_value / math.sqrt(6)) ** 2
            bracket = 3 * c11 - 2 * epsilon if mode == "L" else 3 * c44 + epsilon
            omega_sq = factor2 * sin_sq * bracket
        return math.sqrt(max(omega_sq, 0.0)) / 1e13

    limits = {
        "100": math.sqrt(2) * math.pi / a_angstrom,
        "110": math.sqrt(5) * math.pi / a_angstrom,
        "111": math.sqrt(3 / 2) * math.pi / a_angstrom,
    }
    output_dir.mkdir(parents=True)
    with (output_dir / "dispersion_curves.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(
            handle, fieldnames=["direction", "mode", "k", "frequency"]
        )
        writer.writeheader()
        for direction, k_max in limits.items():
            for mode in ("L", "T1", "T2"):
                for index in range(20):
                    k_value = k_max * index / 19
                    writer.writerow(
                        {
                            "direction": direction,
                            "mode": mode,
                            "k": f"{k_value:.12g}",
                            "frequency": f"{frequency(direction, mode, k_value):.12g}",
                        }
                    )


def bind_public_fixture(package: Path, output_dir: Path) -> None:
    package = package.resolve()
    output_dir = output_dir.resolve()
    if output_dir == package or output_dir.is_relative_to(package):
        return
    if not output_dir.is_dir():
        return
    source_roles = (
        "instruction.md",
        "tests/checker.py",
        "tests/grading_spec.json",
        "tests/test.sh",
    )
    source_hashes = {
        role: "sha256:"
        + hashlib.sha256((package / role).read_bytes()).hexdigest()
        for role in source_roles
        if (package / role).is_file()
    }
    specification = json.loads(
        (package / "tests/grading_spec.json").read_text(encoding="utf-8")
    )
    output_contract = specification.get("output_contract", {})
    if not isinstance(output_contract, dict):
        return
    output_names = {
        str(item.get("file", "")).replace("\\", "/").split("/")[-1]
        for item in output_contract.get("outputs", [])
        if isinstance(item, dict)
    }
    output_files = [
        output_dir / name
        for name in sorted(output_names)
        if name and (output_dir / name).is_file()
    ]
    fixture_hashes = {
        path.name: "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(output_files)
    }
    (output_dir / "fixture_manifest.json").write_text(
        json.dumps(
            {
                "schema_version": "materials-known-valid-fixture/1.0",
                "source_kind": "INDEPENDENT_PUBLIC_FIXTURE",
                "public": True,
                "oracle_used": False,
                "source_role_hashes": source_hashes,
                "fixture_hashes": fixture_hashes,
            },
            indent=2,
        ),
        encoding="utf-8",
    )


def run_review(package: Path, valid_output: Path) -> subprocess.CompletedProcess[str]:
    bind_public_fixture(package, valid_output)
    return subprocess.run(
        [
            sys.executable,
            str(RUNNER),
            str(package),
            "--paper-mode",
            "no_paper",
            "--execution-level",
            "E1",
            "--known-valid-output",
            str(valid_output),
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=120,
        check=False,
    )


class MaterialsBenchmarkReviewE1Tests(unittest.TestCase):
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
            "negative": {"status": "ASSESSED"},
            "discrimination": {
                "status": "NOT_ASSESSABLE",
                "provenance": {
                    "source_kind": "NONE",
                    "fixture_hashes": {},
                    "oracle_used": False,
                },
            },
            "equivalence": {
                "status": "NOT_ASSESSABLE",
                "provenance": {
                    "source_kind": "NONE",
                    "fixture_hashes": {},
                    "oracle_used": False,
                },
            },
            "component_isolation": {
                "status": "NOT_RUN",
                "reason": "no independent fixture",
                "provenance": {
                    "source_kind": "NONE",
                    "oracle_used": False,
                    "source_bindings_verified": False,
                    "runtime_bindings_verified": False,
                    "cases_planned": 0,
                    "cases_executed": 0,
                },
            },
            "process_evidence": {
                "status": "NOT_APPLICABLE",
                "reason": "instruction declares no process-evidence outputs",
                "files": {},
                "instrumentation": "PYTHON_FILE_ACCESS_TRACE",
                "provenance": {
                    "source_kind": "NONE",
                    "oracle_used": False,
                },
            },
        }
        finalize_audit_output.validate_pass_probe_coverage(coverage)

        dishonest = json.loads(json.dumps(coverage))
        dishonest["discrimination"]["provenance"]["source_kind"] = (
            "ORACLE_POSITIVE_MOCK"
        )
        with self.assertRaisesRegex(
            ValueError, "dishonest unavailable discrimination provenance"
        ):
            finalize_audit_output.validate_pass_probe_coverage(dishonest)

        invalid_status = json.loads(json.dumps(coverage))
        invalid_status["equivalence"]["status"] = "SKIPPED"
        with self.assertRaisesRegex(
            ValueError, "invalid equivalence probe status"
        ):
            finalize_audit_output.validate_pass_probe_coverage(invalid_status)

        for label, provenance_update in (
            ("oracle_used", {"oracle_used": True}),
            ("source_kind", {"source_kind": "ORACLE_POSITIVE_MOCK"}),
            (
                "equivalent_marker",
                {"fixture_provenance": {"kind": "oracle_generated"}},
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
                    ValueError, "must be non-Oracle"
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
        specification = {
            "output_contract": {
                "outputs": [{"file": "a.json"}, {"file": "b.json"}]
            },
            "steps": [
                {"id": "a", "output_file": "a.json", "weight": 0.5},
                {"id": "b", "output_file": "b.json", "weight": 0.5},
            ],
        }
        with tempfile.TemporaryDirectory() as temporary:
            fixture = Path(temporary)
            (fixture / "a.json").write_text("{}", encoding="utf-8")
            (fixture / "b.json").write_text("{}", encoding="utf-8")
            plan, reason = dynamic_checker_probe.component_isolation_plan(
                specification,
                fixture,
                "def score(value, step, ctx):\n"
                "    return 1.0\n"
                "_SCORERS = {'a': score}\n",
            )
        self.assertEqual(plan, [])
        self.assertIn("verified checker source bindings", reason)

        failed = dynamic_checker_probe.component_isolation_coverage(
            [
                {"step_id": "a", "file": "a.json", "scorer_function": "score"},
                {"step_id": "b", "file": "b.json", "scorer_function": "score"},
            ],
            None,
            [
                {
                    "case": "known_valid_public",
                    "crashed": True,
                    "reward": None,
                    "breakdown": None,
                },
                {
                    "case": "component_isolation__a",
                    "crashed": True,
                    "reward": None,
                },
                {
                    "case": "component_isolation__b",
                    "crashed": True,
                    "reward": None,
                },
            ],
        )
        self.assertEqual(failed["status"], "NOT_ASSESSABLE")
        self.assertFalse(
            failed["provenance"]["runtime_bindings_verified"]
        )

        swallowed = dynamic_checker_probe.component_isolation_coverage(
            [
                {"step_id": "a", "file": "a.json", "scorer_function": "score"},
                {"step_id": "b", "file": "b.json", "scorer_function": "score"},
            ],
            None,
            [
                {
                    "case": "known_valid_public",
                    "crashed": False,
                    "reward": 1.0,
                    "breakdown": {
                        "a": {"score": 1.0},
                        "b": {"score": 1.0},
                    },
                },
                {
                    "case": "component_isolation__a",
                    "crashed": False,
                    "reward": 0.5,
                    "breakdown": {
                        "a": {"score": 1.0},
                        "b": {"score": 0.0},
                        "_errors": {"b": "ValueError('swallowed')"},
                    },
                },
                {
                    "case": "component_isolation__b",
                    "crashed": False,
                    "reward": 0.5,
                    "breakdown": {
                        "a": {"score": 0.0},
                        "b": {"score": 1.0},
                    },
                },
            ],
        )
        self.assertEqual(swallowed["status"], "NOT_ASSESSABLE")
        self.assertFalse(
            swallowed["provenance"]["runtime_bindings_verified"]
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

        positive = [result("known_valid_public", 1.0, "positive swallowed")]
        self.assertFalse(
            dynamic_checker_probe.probe_assessment_flags(positive)["positive"]
        )
        self.assertIn(
            "CHECKER_RESULT_UNUSABLE",
            {
                item["code"]
                for item in dynamic_checker_probe.evaluate_results(
                    positive, 0.8
                )
            },
        )

        discrimination = [
            result("known_valid_public", 0.8),
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
            result("known_valid_public", 1.0),
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

        isolation = [
            result("known_valid_public", 1.0),
            {
                **result(
                    "component_isolation__a",
                    1.0,
                    {"a": "swallowed"},
                ),
                "isolated_component": {"step_id": "a", "file": "a.json"},
            },
        ]
        isolation[0]["breakdown"] = {"a": {"score": 1.0}}
        isolation_findings = dynamic_checker_probe.evaluate_results(
            isolation, 0.8
        )
        isolation_coverage = (
            dynamic_checker_probe.component_isolation_coverage(
                [
                    {
                        "step_id": "a",
                        "file": "a.json",
                        "scorer_function": "score",
                    }
                ],
                None,
                isolation,
            )
        )
        self.assertEqual(isolation_coverage["status"], "NOT_ASSESSABLE")
        self.assertNotIn(
            "SINGLE_COMPONENT_CAN_PASS",
            {item["code"] for item in isolation_findings},
        )
        self.assertIn(
            "CHECKER_RESULT_UNUSABLE",
            {item["code"] for item in isolation_findings},
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
            if item["code"] == "CHECKER_CRASH"
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
            "E1",
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

    def test_pass_is_blocked_without_authoritative_materials_qualification(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            valid_output = workspace / "known-valid-output"
            write_public_valid_dispersion(valid_output)

            completed = run_review(package, valid_output)

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            report = json.loads(
                (package / "benchmark_audit/audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(
                report["summary"]["final_verdict"], "NOT_ASSESSABLE"
            )
            self.assertIsNone(report["summary"]["total_score"])
            scientific_validity = next(
                item
                for item in report["dimension_scores"]
                if item["dimension"] == "scientific_validity"
            )
            self.assertEqual(
                scientific_validity["status"], "NOT_ASSESSABLE"
            )
            self.assertIsNone(scientific_validity["points_earned"])
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
            with mock.patch.object(
                dynamic_checker_probe.subprocess,
                "run",
                side_effect=subprocess.TimeoutExpired(
                    [sys.executable, "-m", "venv"], 0.05
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
            oracle_output = package / "solution/oracle-output"
            write_public_valid_dispersion(oracle_output)
            oracle_csv = oracle_output / "dispersion_curves.csv"
            with oracle_csv.open(newline="", encoding="utf-8") as handle:
                rows = list(csv.DictReader(handle))
            with oracle_csv.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=list(rows[-1]))
                writer.writeheader()
                writer.writerow(rows[-1])
            (package / "solution/generate.py").write_text(
                "from pathlib import Path\n"
                "assert '/solutionary' == '/solutionary'\n"
                "Path('/app/outputs').mkdir(parents=True, exist_ok=True)\n"
                "source = Path('/solution/oracle-output/dispersion_curves.csv')\n"
                "Path('/app/outputs/dispersion_curves.csv').write_bytes(source.read_bytes())\n",
                encoding="utf-8",
            )
            (package / "solution/solve.sh").write_text(
                "#!/bin/sh\n"
                "python3 -c \"import sys; assert sys.prefix != sys.base_prefix\"\n"
                "python3 /solution/generate.py\n",
                encoding="utf-8",
            )

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

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            audit_dir = package / "benchmark_audit"
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
                positive["evidence"]["positive_mock_accepted"]
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
            valid_output = workspace / "known-valid-output"
            write_public_valid_dispersion(valid_output)

            completed = run_review(package, valid_output)

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            report = json.loads(
                (package / "benchmark_audit/audit_report.json").read_text(
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
            "CANDIDATE_READ_NOT_RUNTIME_PROVEN",
        )
        self.assertEqual(sets["unverified_process_evidence"], [])
        self.assertNotIn(
            "PROCESS_EVIDENCE_NOT_VERIFIED",
            {item["code"] for item in issues},
        )

    def test_dynamic_process_nonverification_is_grouped_after_safe_trace(
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
            valid_output = workspace / "known-valid-output"
            write_public_valid_dispersion(valid_output)
            (valid_output / "process_trace.json").write_text(
                '{"converged": true}', encoding="utf-8"
            )
            (valid_output / "training.log").write_text(
                "converged\n", encoding="utf-8"
            )

            completed = run_review(package, valid_output)

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            report = json.loads(
                (package / "benchmark_audit/audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            findings = [
                item
                for item in report["findings"]
                if item["title"] == "PROCESS_EVIDENCE_NOT_VERIFIED"
            ]
            self.assertEqual(len(findings), 1)
            self.assertEqual(
                findings[0]["evidence"]["unverified_process_evidence"],
                ["process_trace.json", "training.log"],
            )
            process_tests = [
                item
                for item in report["checker_tests"]
                if item["probe_class"] == "process_evidence"
            ]
            self.assertEqual(len(process_tests), 1)
            mapped = {
                item["file"]: item
                for item in report["contract_map"]["checker_analysis"][
                    "outputs"
                ]
            }
            for filename in ("process_trace.json", "training.log"):
                self.assertEqual(
                    mapped[filename]["checker_reads"],
                    "DYNAMIC_NOT_VERIFIED",
                )

    def test_process_directory_listing_does_not_prove_file_access(self) -> None:
        coverage, findings = dynamic_checker_probe.process_evidence_coverage(
            ["process_trace.json"],
            None,
            [
                {
                    "case": "process_evidence_read_trace",
                    "reward": 1.0,
                    "breakdown": {"_errors": {}},
                    "crashed": False,
                    "read_trace_enabled": True,
                    "runtime_outputs_dir": "/tmp/runtime/app/outputs",
                    "read_trace": [
                        {
                            "operation": "listdir",
                            "path": "/tmp/runtime/app/outputs",
                        },
                        {
                            "operation": "scandir",
                            "path": "/tmp/runtime/app/outputs",
                        },
                    ],
                }
            ],
        )

        self.assertEqual(coverage["status"], "ASSESSED")
        self.assertEqual(
            coverage["files"]["process_trace.json"],
            "DYNAMIC_NOT_ACCESSED",
        )
        self.assertEqual(
            [item["code"] for item in findings],
            ["PROCESS_EVIDENCE_NOT_VERIFIED"],
        )

    def test_component_weight_reaching_threshold_is_a_risk_not_a_proven_bypass(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            spec_path = package / "tests/grading_spec.json"
            specification = json.loads(spec_path.read_text(encoding="utf-8"))
            specification["steps"][0]["weight"] = 0.8
            specification["steps"].append(
                {
                    "id": "supporting_structure",
                    "output_file": "dispersion_curves.csv",
                    "kind": "structural_audit",
                    "weight": 0.2,
                }
            )
            spec_path.write_text(
                json.dumps(specification, indent=2), encoding="utf-8"
            )
            valid_output = workspace / "known-valid-output"
            write_public_valid_dispersion(valid_output)

            completed = run_review(package, valid_output)

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            report = json.loads(
                (package / "benchmark_audit/audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            findings = {
                item["title"]: item for item in report["findings"]
            }
            self.assertNotIn("SINGLE_COMPONENT_CAN_PASS", findings)
            self.assertEqual(
                findings["SINGLE_COMPONENT_THRESHOLD_REACHABLE"]["severity"],
                "MEDIUM",
            )
            self.assertIn(
                "requires a component-isolation probe",
                findings["SINGLE_COMPONENT_THRESHOLD_REACHABLE"][
                    "observed_fact"
                ],
            )
            component_check = next(
                item
                for item in report["contract_map"]["checker_analysis"][
                    "dynamic_checks_required"
                ]
                if item["check"] == "component_isolation"
            )
            self.assertEqual(component_check["status"], "NOT_RUN")
            self.assertNotIn("SINGLE_COMPONENT_CAN_PASS", findings)

    def test_oracle_positive_mock_is_never_component_isolation_fixture(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            spec_path = package / "tests/grading_spec.json"
            specification = json.loads(spec_path.read_text(encoding="utf-8"))
            support_contract = dict(
                specification["output_contract"]["outputs"][0]
            )
            support_contract["file"] = "support.csv"
            specification["output_contract"]["outputs"].append(
                support_contract
            )
            specification["steps"][0]["weight"] = 0.5
            specification["steps"].append(
                {
                    "id": "step_support",
                    "output_file": "support.csv",
                    "weight": 0.5,
                }
            )
            spec_path.write_text(
                json.dumps(specification, indent=2), encoding="utf-8"
            )
            checker_path = package / "tests/checker.py"
            checker = checker_path.read_text(encoding="utf-8").replace(
                "_SCORERS = {\n    'step_dispersion': score_0,\n}",
                "_SCORERS = {\n"
                "    'step_dispersion': score_0,\n"
                "    'step_support': score_0,\n"
                "}",
            )
            checker_path.write_text(checker, encoding="utf-8")
            oracle_output = workspace / "oracle-positive"
            write_public_valid_dispersion(oracle_output)
            shutil.copy2(
                oracle_output / "dispersion_curves.csv",
                oracle_output / "support.csv",
            )
            output = workspace / "checker.json"

            with mock.patch.object(
                dynamic_checker_probe,
                "prepare_solution_oracle",
                return_value=(
                    None,
                    oracle_output,
                    {
                        "used": True,
                        "status": "PASS",
                        "positive_mock_available": True,
                        "scientific_evidence": False,
                    },
                ),
            ):
                checker_result = dynamic_checker_probe.dynamic_checker_probe(
                    package, output, known_valid_output=None
                )

            isolation = checker_result["probe_coverage"][
                "component_isolation"
            ]
            self.assertEqual(isolation["status"], "NOT_RUN")
            self.assertEqual(
                isolation["provenance"]["source_kind"], "NONE"
            )
            self.assertFalse(isolation["provenance"]["oracle_used"])
            self.assertEqual(isolation["provenance"]["cases_executed"], 0)
            self.assertFalse(
                any(
                    item["probe_class"] == "component_isolation"
                    for item in checker_result["tests"]
                )
            )
            self.assertTrue(
                any(
                    "component isolation requires an independent" in item
                    for item in checker_result["limitations"]
                )
            )

    def test_source_bound_component_isolation_executes_and_can_prove_bypass(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            instruction = package / "instruction.md"
            instruction.write_text(
                instruction.read_text(encoding="utf-8")
                + "\n\n### Step 2: Supporting result\n"
                "- Role: scored (load-bearing)\n"
                "- Action: Compute the supporting dispersion result.\n"
                "- Output file: `/app/outputs/support.csv`\n",
                encoding="utf-8",
            )
            spec_path = package / "tests/grading_spec.json"
            specification = json.loads(spec_path.read_text(encoding="utf-8"))
            support_contract = dict(
                specification["output_contract"]["outputs"][0]
            )
            support_contract["file"] = "support.csv"
            specification["output_contract"]["outputs"].append(
                support_contract
            )
            specification["steps"][0]["weight"] = 0.6
            specification["steps"].append(
                {
                    "id": "step_support",
                    "output_file": "support.csv",
                    "kind": "recompute_metric",
                    "weight": 0.4,
                }
            )
            spec_path.write_text(
                json.dumps(specification, indent=2), encoding="utf-8"
            )
            checker_path = package / "tests/checker.py"
            checker = checker_path.read_text(encoding="utf-8")
            checker = checker.replace(
                "    _ff_contract_gate()\n    with open",
                "    # Component isolation must reach aggregation.\n    with open",
            )
            checker = checker.replace(
                "_SCORERS = {\n    'step_dispersion': score_0,\n}",
                "def isolation_score(artifact, step, ctx):\n"
                "    return 1.0 if artifact else 0.0\n\n"
                "_SCORERS = {\n"
                "    'step_dispersion': isolation_score,\n"
                "    'step_support': isolation_score,\n"
                "}",
            )
            checker_path.write_text(checker, encoding="utf-8")
            valid_output = workspace / "known-valid-output"
            write_public_valid_dispersion(valid_output)
            shutil.copy2(
                valid_output / "dispersion_curves.csv",
                valid_output / "support.csv",
            )

            completed = run_review(package, valid_output)

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            report = json.loads(
                (package / "benchmark_audit/audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            isolation_tests = [
                item
                for item in report["checker_tests"]
                if item["probe_class"] == "component_isolation"
            ]
            self.assertEqual(len(isolation_tests), 2)
            finding = next(
                item
                for item in report["findings"]
                if item["title"] == "SINGLE_COMPONENT_CAN_PASS"
            )
            self.assertEqual(
                finding["evidence"]["component_id"], "step_dispersion"
            )
            component_check = next(
                item
                for item in report["contract_map"]["checker_analysis"][
                    "dynamic_checks_required"
                ]
                if item["check"] == "component_isolation"
            )
            self.assertEqual(component_check["status"], "ASSESSED")
            self.assertTrue(
                component_check["provenance"]["source_bindings_verified"]
            )
            self.assertTrue(
                component_check["provenance"]["runtime_bindings_verified"]
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
            valid_output = workspace / "known-valid-output"
            write_public_valid_dispersion(valid_output)

            completed = run_review(package, valid_output)

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            report = json.loads(
                (package / "benchmark_audit/audit_report.json").read_text(
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
                package / "benchmark_audit/audit_report.md"
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
            valid_output = workspace / "known-valid-output"
            write_public_valid_dispersion(valid_output)

            completed = run_review(package, valid_output)

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            report = json.loads(
                (package / "benchmark_audit/audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            finding = next(
                item
                for item in report["findings"]
                if item["title"] == "SCORER_MISSING_RETURN"
            )
            self.assertIn("step_dispersion", finding["observed_fact"])
            checker_dimension = next(
                item
                for item in report["dimension_scores"]
                if item["dimension"] == "checker_gold_alignment"
            )
            self.assertIn(
                finding["finding_id"], checker_dimension["finding_ids"]
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
            report = json.loads(
                (package / "benchmark_audit/audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            finding_codes = {item["title"] for item in report["findings"]}
            self.assertIn("ORACLE_POSITIVE_MOCK_REJECTED", finding_codes)
            self.assertNotIn("SOLUTION_POSITIVE_MOCK_REJECTED", finding_codes)
            self.assertNotIn("KNOWN_VALID_OUTPUT_REJECTED", finding_codes)
            solution_dimension = next(
                item
                for item in report["dimension_scores"]
                if item["dimension"] == "solution_completeness"
            )
            checker_dimension = next(
                item
                for item in report["dimension_scores"]
                if item["dimension"] == "checker_gold_alignment"
            )
            self.assertEqual(solution_dimension["points_earned"], 5)
            self.assertFalse(solution_dimension["finding_ids"])
            self.assertTrue(checker_dimension["finding_ids"])
            oracle_finding = next(
                item
                for item in report["findings"]
                if item["title"] == "ORACLE_POSITIVE_MOCK_REJECTED"
            )
            self.assertIn("checker", oracle_finding["minimal_repair"].lower())
            self.assertNotIn("solution/solve.sh", oracle_finding["minimal_repair"])

    def test_no_paper_e1_review_publishes_real_checker_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            valid_output = workspace / "known-valid-output"
            write_public_valid_dispersion(valid_output)

            checker_path = package / "tests/checker.py"
            checker_path.write_text(
                "from pathlib import Path as _AuditPath\n"
                "assert not (_AuditPath.cwd() / 'solution').exists(), "
                "'checker runtime exposed solution/'\n"
                "assert not (_AuditPath.cwd() / 'paper').exists(), "
                "'no-paper runtime exposed paper/'\n"
                + checker_path.read_text(encoding="utf-8"),
                encoding="utf-8",
            )
            solution_dir = package / "solution"
            original_mode = solution_dir.stat().st_mode
            os.chmod(solution_dir, 0)
            try:
                completed = run_review(package, valid_output)
            finally:
                os.chmod(solution_dir, original_mode)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )

            audit_dir = package / "benchmark_audit"
            required = {
                "audit_report.md",
                "audit_report.json",
                "findings.jsonl",
                "resource_checks.json",
                "checker_tests.json",
                "audit_manifest.json",
                "logs/audit.log",
            }
            self.assertTrue(audit_dir.is_dir())
            self.assertEqual(
                required,
                {
                    path.relative_to(audit_dir).as_posix()
                    for path in audit_dir.rglob("*")
                    if path.is_file()
                    and path.relative_to(audit_dir).as_posix() in required
                },
            )

            report = json.loads(
                (audit_dir / "audit_report.json").read_text(encoding="utf-8")
            )
            self.assertEqual(report["configuration"]["paper_mode"], "no_paper")
            self.assertEqual(report["configuration"]["execution_level"], "E1")
            self.assertEqual(report["summary"]["materials_class"], "MAT_CORE")
            self.assertEqual(
                report["summary"]["final_verdict"], "NOT_ASSESSABLE"
            )
            self.assertIsNone(report["summary"]["total_score"])
            report_findings = {
                finding["title"] for finding in report["findings"]
            }
            self.assertTrue(
                {
                    "KNOWN_VALID_OUTPUT_REJECTED",
                    "ADVERSARIAL_OUTPUT_PASSES",
                }.issubset(report_findings)
            )
            self.assertEqual(
                report["paper_consistency"]["status"], "NOT_ASSESSED"
            )
            self.assertFalse(report["scope"]["solution_content_inspected"])

            checker = json.loads(
                (audit_dir / "checker_tests.json").read_text(encoding="utf-8")
            )
            scores = {
                case["test_type"]: case["observed_score"]
                for case in checker["tests"]
            }
            self.assertLess(
                scores["known_valid_public"], checker["pass_threshold"]
            )
            self.assertIn(
                "KNOWN_VALID_OUTPUT_REJECTED",
                {finding["code"] for finding in checker["findings"]},
            )
            self.assertGreaterEqual(
                scores["sparse_known_valid"], checker["pass_threshold"]
            )
            self.assertIn(
                "ADVERSARIAL_OUTPUT_PASSES",
                {finding["code"] for finding in checker["findings"]},
            )
            for case in (
                "missing_outputs",
                "empty_valid_shape",
                "random_baseline",
                "minimal_gold_shape",
            ):
                self.assertLess(scores[case], checker["pass_threshold"])
            self.assertFalse(
                any(
                    case["evidence"]["runtime_package_contains_solution"]
                    for case in checker["tests"]
                )
            )
            self.assertFalse(checker["solution_content_inspected"])

            manifest = json.loads(
                (audit_dir / "audit_manifest.json").read_text(encoding="utf-8")
            )
            self.assertEqual(
                manifest["auditor_version"], "materials-benchmark-review/0.1"
            )
            self.assertFalse(
                any(path.startswith("solution/") for path in manifest["input_hashes"])
            )
            self.assertFalse(
                any(path.startswith("paper/") for path in manifest["input_hashes"])
            )
            for relative, expected_hash in manifest["output_hashes"].items():
                digest = hashlib.sha256(
                    (audit_dir / relative).read_bytes()
                ).hexdigest()
                self.assertEqual(expected_hash, f"sha256:{digest}")

    def test_public_report_cites_evidence_for_every_hard_gate(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            valid_output = workspace / "known-valid-output"
            write_public_valid_dispersion(valid_output)
            checker_path = package / "tests/checker.py"
            checker_path.write_text(
                "raise RuntimeError('forced checker evidence gap')\n"
                + checker_path.read_text(encoding="utf-8"),
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
            valid_output = workspace / "known-valid-output"
            write_public_valid_dispersion(valid_output)

            completed = run_review(package, valid_output)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            audit_dir = package / "benchmark_audit"
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
            dimensions = {
                item["dimension"]: item
                for item in report["dimension_scores"]
            }
            self.assertEqual(
                dimensions["checker_gold_alignment"]["points_earned"], 15
            )
            self.assertEqual(
                dimensions["checker_gold_alignment"]["status"],
                "WARNING",
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
            valid_output = workspace / "known-valid-output"
            write_public_valid_dispersion(valid_output)

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
            valid_output = workspace / "known-valid-output"
            write_public_valid_dispersion(valid_output)
            completed = run_review(package, valid_output)
            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            audit = package / "benchmark_audit"
            finalize_audit_output.validate_bundle(audit)

            report_path = audit / "audit_report.json"
            original_report = report_path.read_text(encoding="utf-8")
            report = json.loads(original_report)
            report["summary"]["final_verdict"] = "CONDITIONAL"
            report_path.write_text(json.dumps(report), encoding="utf-8")
            with self.assertRaisesRegex(
                ValueError, "verdict is inconsistent"
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
                ValueError, "component-isolation contract/probe mismatch"
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
            valid_output = workspace / "known-valid-output"
            write_public_valid_dispersion(valid_output)

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
            valid_output = workspace / "known-valid-output"
            write_public_valid_dispersion(valid_output)

            completed = run_review(package, valid_output)

            self.assertNotEqual(completed.returncode, 0)
            self.assertIn(
                "routes through a symlink", completed.stderr
            )
            self.assertFalse((package / "benchmark_audit").exists())

    def test_failed_reaudit_preserves_previous_authoritative_bundle(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            previous_audit = package / "benchmark_audit"
            previous_audit.mkdir()
            marker = previous_audit / "previous-result.txt"
            marker.write_text("authoritative", encoding="utf-8")

            failed = run_review(package, workspace / "missing-valid-output")
            self.assertNotEqual(failed.returncode, 0)
            self.assertEqual(marker.read_text(encoding="utf-8"), "authoritative")

            valid_output = workspace / "known-valid-output"
            write_public_valid_dispersion(valid_output)
            completed = run_review(package, valid_output)
            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            self.assertTrue((package / "benchmark_audit").is_dir())
            archived_markers = list(
                (package / "benchmark_audit_history").rglob(
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
