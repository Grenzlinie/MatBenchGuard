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


def run_review(package: Path, valid_output: Path) -> subprocess.CompletedProcess[str]:
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
            self.assertGreaterEqual(
                positive["observed_score"], checker["pass_threshold"]
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

    def test_rejected_oracle_mock_is_only_solution_completeness_evidence(
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
            self.assertIn("SOLUTION_POSITIVE_MOCK_REJECTED", finding_codes)
            self.assertNotIn("KNOWN_VALID_OUTPUT_REJECTED", finding_codes)
            solution_dimension = next(
                item
                for item in report["dimension_scores"]
                if item["dimension"] == "solution_completeness"
            )
            self.assertTrue(solution_dimension["finding_ids"])

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

    def test_missing_checker_publishes_repairable_static_bundle(self) -> None:
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
                gates["CHECKER_CORE_ALIGNMENT"], "PASS"
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
