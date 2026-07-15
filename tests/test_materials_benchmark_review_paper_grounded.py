from __future__ import annotations

import json
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
    checker_path = destination / "tests/checker.py"
    original_checker = checker_path.read_text(encoding="utf-8")
    checker_path.write_text(
        """
from pathlib import Path as _PaperTestPath
import csv as _paper_test_csv
import json as _paper_test_json
import math as _paper_test_math

_paper_test_output = _PaperTestPath("/app/outputs/dispersion_curves.csv")
_paper_test_valid = False
if _paper_test_output.is_file():
    try:
        with _paper_test_output.open(newline="", encoding="utf-8") as _handle:
            _paper_test_rows = list(_paper_test_csv.DictReader(_handle))
        _paper_test_keys = [
            (row["direction"], row["mode"], row["k"])
            for row in _paper_test_rows
        ]
        _paper_test_valid = (
            len(_paper_test_rows) >= 180
            and len(set(_paper_test_keys)) == len(_paper_test_keys)
            and all(
                _paper_test_math.isfinite(float(row["frequency"]))
                for row in _paper_test_rows
            )
        )
    except (KeyError, TypeError, ValueError):
        _paper_test_valid = False
if not _paper_test_valid:
    _paper_test_logs = _PaperTestPath("/logs/verifier")
    _paper_test_logs.mkdir(parents=True, exist_ok=True)
    (_paper_test_logs / "reward.txt").write_text("0.0", encoding="utf-8")
    (_paper_test_logs / "breakdown.json").write_text(
        _paper_test_json.dumps({"fixture_integrity_gate": 0.0}),
        encoding="utf-8",
    )
    raise SystemExit(0)
"""
        + original_checker,
        encoding="utf-8",
    )


def assessment() -> dict[str, object]:
    return {
        "schema_version": "0.1",
        "reproduction_type": "METHOD_REIMPLEMENTATION",
        "dimensions": {
            "instruction_fidelity": {
                "status": "PASS",
                "rationale": "The scoped task implements a dispersion result described by the paper.",
                "evidence": [
                    {
                        "paper_quote": "The dispersion relations for Cu are calculated along the (100), (110), and (111) directions",
                        "package_file": "instruction.md",
                        "package_quote": "This task focuses on face-centred cubic copper (Cu).",
                    }
                ],
            },
            "data_fidelity": {
                "status": "WARNING",
                "rationale": "The paper identifies room-temperature elastic constants but the bundled text does not enumerate every task constant.",
                "evidence": [
                    {
                        "paper_quote": "Using room-temperature values of the elastic constants",
                        "package_file": "instruction.md",
                        "package_quote": "c11 = 1.68×10¹² dynes/cm²",
                    }
                ],
            },
            "method_fidelity": {
                "status": "PASS",
                "rationale": "The nearest-neighbor Born-Begbie specialization is explicitly discussed by the paper.",
                "evidence": [
                    {
                        "paper_quote": "If one confines oneself to nearest neighbors only, the three force constants may be determined from the experimental values of the three elastic constants.",
                        "package_file": "steps.json",
                        "package_quote": "nearest‑neighbor interactions (α=β=0)",
                    }
                ],
            },
            "gold_provenance": {
                "status": "PASS",
                "rationale": "The checker recomputes the published analytical branch rather than copying solution output.",
                "evidence": [
                    {
                        "paper_quote": "#### 100 Direction",
                        "package_file": "tests/checker.py",
                        "package_quote": "c11 = 1.68e12",
                    }
                ],
            },
            "checker_fidelity": {
                "status": "PASS",
                "rationale": "The checker evaluates the longitudinal and transverse branch frequencies.",
                "evidence": [
                    {
                        "paper_quote": "The symbols $L$ and $T$ refer to the three (longitudinal and transverse) branches.",
                        "package_file": "tests/checker.py",
                        "package_quote": "def expected_freq(direction, mode, k):",
                    }
                ],
            },
        },
        "taxonomy": {
            "computation_task": ["声子与晶格动力学"],
            "research_domain": ["基础材料研究与材料发现"],
            "material_system": {
                "primary": "金属与合金",
                "secondary": ["铜", "面心立方金属"],
            },
        },
        "taxonomy_evidence": [
            {
                "dimension": "computation_task",
                "label": "声子与晶格动力学",
                "package_file": "instruction.md",
                "package_quote": "dispersion relations—angular frequency ω as a function of wave vector k—describe the phonon spectrum",
            },
            {
                "dimension": "research_domain",
                "label": "基础材料研究与材料发现",
                "package_file": "instruction.md",
                "package_quote": "Understanding the vibrational properties of crystals is essential for predicting their thermal and elastic behaviour.",
            },
            {
                "dimension": "material_system.primary",
                "label": "金属与合金",
                "package_file": "instruction.md",
                "package_quote": "This task focuses on face-centred cubic copper (Cu).",
            },
            {
                "dimension": "material_system.secondary",
                "label": "铜",
                "package_file": "instruction.md",
                "package_quote": "This task focuses on face-centred cubic copper (Cu).",
            },
            {
                "dimension": "material_system.secondary",
                "label": "面心立方金属",
                "package_file": "instruction.md",
                "package_quote": "This task focuses on face-centred cubic copper (Cu).",
            },
        ],
    }


def run_paper_grounded(
    package: Path, assessment_path: Path
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
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
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=120,
        check=False,
    )


def run_no_paper_with_taxonomy(
    package: Path, assessment_path: Path
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(RUNNER),
            str(package),
            "--paper-mode",
            "no_paper",
            "--execution-level",
            "E1",
            "--agent-assessment",
            str(assessment_path),
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=120,
        check=False,
    )


class MaterialsBenchmarkPaperGroundedTests(unittest.TestCase):
    def test_paper_grounded_review_publishes_fidelity_and_taxonomy(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            original_manifest = (package / "manifest.json").read_bytes()
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
            audit_dir = package / "benchmark_audit"
            report = json.loads(
                (audit_dir / "audit_report.json").read_text(encoding="utf-8")
            )
            self.assertEqual(
                report["configuration"]["paper_mode"], "paper_grounded"
            )
            self.assertEqual(
                report["paper_consistency"]["reproduction_type"],
                "METHOD_REIMPLEMENTATION",
            )
            self.assertEqual(report["paper_consistency"]["status"], "WARNING")
            self.assertEqual(
                set(report["paper_consistency"]["dimensions"]),
                {
                    "instruction_fidelity",
                    "data_fidelity",
                    "method_fidelity",
                    "gold_provenance",
                    "checker_fidelity",
                },
            )
            self.assertEqual(
                report["taxonomy_labels"],
                assessment()["taxonomy"],
            )
            self.assertEqual(
                report["taxonomy_evidence"],
                assessment()["taxonomy_evidence"],
            )
            self.assertEqual(report["taxonomy_source"]["revision"], 85)
            self.assertEqual(
                report["taxonomy_source"]["url"],
                "https://dptechnology.feishu.cn/docx/RclxdULMcoH4cUxALk4cd8EgnDe",
            )
            self.assertEqual(
                report["summary"]["final_verdict"], "CONDITIONAL"
            )
            self.assertNotIn(
                "no-paper",
                report["summary"]["core_reason"].lower(),
            )
            self.assertIn(
                "PAPER_DATA_FIDELITY_WARNING",
                {finding["title"] for finding in report["findings"]},
            )
            manifest = json.loads(
                (audit_dir / "audit_manifest.json").read_text(encoding="utf-8")
            )
            self.assertIn("paper/paper.md", manifest["input_hashes"])
            self.assertIn(
                "paper/images_manifest.json", manifest["input_hashes"]
            )
            self.assertEqual(
                (package / "manifest.json").read_bytes(), original_manifest
            )
            markdown = (audit_dir / "audit_report.md").read_text(
                encoding="utf-8"
            )
            gold_section = markdown.split(
                "## 11. Gold Standard Assessment", 1
            )[1].split("## 12.", 1)[0]
            self.assertIn("Status: PASS", gold_section)
            self.assertNotIn("NOT_ASSESSED", gold_section)
            scope_section = markdown.split(
                "## 19. Audit Scope and Limitations", 1
            )[1].split("## 20.", 1)[0]
            self.assertIn("paper-grounded E1", scope_section)
            self.assertNotIn("no-paper E1 behavior only", scope_section)

    def test_repairable_e1_fatal_does_not_suppress_paper_review(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            shutil.copy2(
                SOURCE_PACKAGE / "tests/checker.py",
                package / "tests/checker.py",
            )
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
            report = json.loads(
                (
                    package / "benchmark_audit/audit_report.json"
                ).read_text(encoding="utf-8")
            )
            self.assertEqual(report["summary"]["final_verdict"], "REJECT")
            self.assertEqual(
                report["paper_consistency"]["reproduction_type"],
                "METHOD_REIMPLEMENTATION",
            )
            self.assertNotEqual(
                report["paper_consistency"]["status"], "NOT_ASSESSED"
            )

    def test_no_paper_review_can_publish_evidence_backed_taxonomy(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            original_manifest = (package / "manifest.json").read_bytes()
            value = assessment()
            taxonomy_only = {
                "schema_version": value["schema_version"],
                "taxonomy": value["taxonomy"],
                "taxonomy_evidence": value["taxonomy_evidence"],
            }
            assessment_path = workspace / "taxonomy-assessment.json"
            assessment_path.write_text(
                json.dumps(taxonomy_only, ensure_ascii=False),
                encoding="utf-8",
            )

            completed = run_no_paper_with_taxonomy(package, assessment_path)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            audit_dir = package / "benchmark_audit"
            report = json.loads(
                (audit_dir / "audit_report.json").read_text(encoding="utf-8")
            )
            self.assertEqual(report["configuration"]["paper_mode"], "no_paper")
            self.assertEqual(
                report["paper_consistency"]["status"], "NOT_ASSESSED"
            )
            self.assertEqual(report["taxonomy_labels"], value["taxonomy"])
            self.assertEqual(
                report["taxonomy_evidence"], value["taxonomy_evidence"]
            )
            self.assertEqual(report["taxonomy_source"]["revision"], 85)
            manifest = json.loads(
                (audit_dir / "audit_manifest.json").read_text(encoding="utf-8")
            )
            self.assertNotIn("paper/paper.md", manifest["input_hashes"])
            self.assertEqual(
                (package / "manifest.json").read_bytes(), original_manifest
            )

    def test_paper_grounded_review_rejects_unknown_taxonomy_label(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            value = assessment()
            value["taxonomy"]["computation_task"] = ["不存在的计算任务"]
            assessment_path = workspace / "assessment.json"
            assessment_path.write_text(
                json.dumps(value, ensure_ascii=False),
                encoding="utf-8",
            )

            completed = run_paper_grounded(package, assessment_path)

            self.assertNotEqual(completed.returncode, 0)
            self.assertIn(
                "unknown computation_task labels", completed.stderr
            )
            self.assertFalse((package / "benchmark_audit").exists())

    def test_paper_grounded_review_requires_evidence_for_every_taxonomy_label(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            value = assessment()
            value["taxonomy_evidence"] = [
                item
                for item in value["taxonomy_evidence"]
                if item["label"] != "声子与晶格动力学"
            ]
            assessment_path = workspace / "assessment.json"
            assessment_path.write_text(
                json.dumps(value, ensure_ascii=False),
                encoding="utf-8",
            )

            completed = run_paper_grounded(package, assessment_path)

            self.assertNotEqual(completed.returncode, 0)
            self.assertIn(
                "missing taxonomy evidence for computation_task",
                completed.stderr,
            )
            self.assertFalse((package / "benchmark_audit").exists())

    def test_paper_evidence_cannot_use_paper_as_the_package_side(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            value = assessment()
            evidence = value["dimensions"]["instruction_fidelity"]["evidence"][0]
            evidence["package_file"] = "paper/paper.md"
            evidence["package_quote"] = evidence["paper_quote"]
            assessment_path = workspace / "assessment.json"
            assessment_path.write_text(
                json.dumps(value, ensure_ascii=False),
                encoding="utf-8",
            )

            completed = run_paper_grounded(package, assessment_path)

            self.assertNotEqual(completed.returncode, 0)
            self.assertIn(
                "unsupported package evidence file",
                completed.stderr,
            )
            self.assertFalse((package / "benchmark_audit").exists())

    def test_agent_assessment_cannot_come_from_solution(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            assessment_path = package / "solution/assessment.json"
            assessment_path.write_text(
                json.dumps(assessment(), ensure_ascii=False),
                encoding="utf-8",
            )

            completed = run_paper_grounded(package, assessment_path)

            self.assertNotEqual(completed.returncode, 0)
            self.assertIn(
                "agent assessment must be outside the Harbor 题包",
                completed.stderr,
            )
            self.assertFalse((package / "benchmark_audit").exists())

    def test_bundled_paper_cannot_route_through_solution_symlink(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            paper_path = package / "paper/paper.md"
            hidden_paper = package / "solution/paper.md"
            hidden_paper.write_bytes(paper_path.read_bytes())
            paper_path.unlink()
            paper_path.symlink_to(hidden_paper)
            assessment_path = workspace / "assessment.json"
            assessment_path.write_text(
                json.dumps(assessment(), ensure_ascii=False),
                encoding="utf-8",
            )

            completed = run_paper_grounded(package, assessment_path)

            self.assertNotEqual(completed.returncode, 0)
            self.assertIn(
                "paper role routes through a symlink",
                completed.stderr,
            )
            self.assertFalse((package / "benchmark_audit").exists())

    def test_paper_grounded_review_accepts_multiple_pinned_task_labels(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            value = assessment()
            value["taxonomy"]["computation_task"] = [
                "声子与晶格动力学",
                "热学性质",
            ]
            value["taxonomy_evidence"].append(
                {
                    "dimension": "computation_task",
                    "label": "热学性质",
                    "package_file": "instruction.md",
                    "package_quote": "thermal and elastic behaviour",
                }
            )
            assessment_path = workspace / "assessment.json"
            assessment_path.write_text(
                json.dumps(value, ensure_ascii=False),
                encoding="utf-8",
            )

            completed = run_paper_grounded(package, assessment_path)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            report = json.loads(
                (
                    package / "benchmark_audit/audit_report.json"
                ).read_text(encoding="utf-8")
            )
            self.assertEqual(
                report["taxonomy_labels"]["computation_task"],
                ["声子与晶格动力学", "热学性质"],
            )

    def test_paper_grounded_review_records_each_reproduction_type(self) -> None:
        for reproduction_type in (
            "EXACT_REPRODUCTION",
            "SCIENTIFIC_EXTENSION",
        ):
            with self.subTest(reproduction_type=reproduction_type):
                with tempfile.TemporaryDirectory() as temporary:
                    workspace = Path(temporary)
                    package = workspace / SOURCE_PACKAGE.name
                    copy_source_package(package)
                    value = assessment()
                    value["reproduction_type"] = reproduction_type
                    if reproduction_type == "SCIENTIFIC_EXTENSION":
                        value["dimensions"]["gold_provenance"]["status"] = (
                            "WARNING"
                        )
                        value["dimensions"]["gold_provenance"]["rationale"] = (
                            "An extension must not use exact paper values as "
                            "its sole Gold."
                        )
                    assessment_path = workspace / "assessment.json"
                    assessment_path.write_text(
                        json.dumps(value, ensure_ascii=False),
                        encoding="utf-8",
                    )

                    completed = run_paper_grounded(package, assessment_path)

                    self.assertEqual(
                        completed.returncode,
                        0,
                        msg=(
                            f"stdout:\n{completed.stdout}\n"
                            f"stderr:\n{completed.stderr}"
                        ),
                    )
                    report = json.loads(
                        (
                            package / "benchmark_audit/audit_report.json"
                        ).read_text(encoding="utf-8")
                    )
                    self.assertEqual(
                        report["paper_consistency"]["reproduction_type"],
                        reproduction_type,
                    )

    def test_paper_grounded_review_requires_evidence_for_every_dimension(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            value = assessment()
            value["dimensions"]["checker_fidelity"]["evidence"] = []
            assessment_path = workspace / "assessment.json"
            assessment_path.write_text(
                json.dumps(value, ensure_ascii=False),
                encoding="utf-8",
            )

            completed = run_paper_grounded(package, assessment_path)

            self.assertNotEqual(completed.returncode, 0)
            self.assertIn(
                "checker_fidelity requires at least one evidence item",
                completed.stderr,
            )
            self.assertFalse((package / "benchmark_audit").exists())

    def test_failed_paper_dimension_triggers_hard_gate(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            value = assessment()
            value["dimensions"]["gold_provenance"]["status"] = "FAIL"
            value["dimensions"]["gold_provenance"]["rationale"] = (
                "The checker target contradicts the paper evidence."
            )
            assessment_path = workspace / "assessment.json"
            assessment_path.write_text(
                json.dumps(value, ensure_ascii=False),
                encoding="utf-8",
            )

            completed = run_paper_grounded(package, assessment_path)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            report = json.loads(
                (
                    package / "benchmark_audit/audit_report.json"
                ).read_text(encoding="utf-8")
            )
            self.assertEqual(report["paper_consistency"]["status"], "FAIL")
            self.assertTrue(report["summary"]["hard_gate_triggered"])
            self.assertEqual(report["summary"]["final_verdict"], "REJECT")
            self.assertIn(
                "PAPER_GOLD_PROVENANCE_FAIL",
                {finding["title"] for finding in report["findings"]},
            )
            gates = {
                item["gate_id"]: item["status"]
                for item in report["gate_results"]
            }
            self.assertEqual(gates["PAPER_CONSISTENCY"], "FAIL")

    def test_fatal_no_paper_gate_skips_paper_grounded_assessment(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            (package / "tests/checker.py").unlink()

            completed = run_paper_grounded(
                package, workspace / "missing-assessment.json"
            )

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            report = json.loads(
                (
                    package / "benchmark_audit/audit_report.json"
                ).read_text(encoding="utf-8")
            )
            self.assertEqual(report["summary"]["final_verdict"], "REJECT")
            self.assertEqual(
                report["paper_consistency"]["status"], "NOT_ASSESSED"
            )
            self.assertIn(
                "skipped",
                report["paper_consistency"]["reason"].lower(),
            )
            self.assertIn(
                "MISSING_FILE",
                {finding["title"] for finding in report["findings"]},
            )

    def test_unavailable_paper_evidence_is_not_assessable(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            value = assessment()
            value["dimensions"]["checker_fidelity"] = {
                "status": "NOT_ASSESSABLE",
                "rationale": "The bundled paper does not expose enough checker-grounding evidence.",
                "evidence": [],
            }
            assessment_path = workspace / "assessment.json"
            assessment_path.write_text(
                json.dumps(value, ensure_ascii=False),
                encoding="utf-8",
            )

            completed = run_paper_grounded(package, assessment_path)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            report = json.loads(
                (
                    package / "benchmark_audit/audit_report.json"
                ).read_text(encoding="utf-8")
            )
            self.assertEqual(
                report["paper_consistency"]["status"], "NOT_ASSESSABLE"
            )
            gates = {
                item["gate_id"]: item["status"]
                for item in report["gate_results"]
            }
            self.assertEqual(
                gates["PAPER_CONSISTENCY"], "WARNING"
            )

    def test_not_assessable_dimension_rejects_conflicting_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            value = assessment()
            value["dimensions"]["checker_fidelity"]["status"] = (
                "NOT_ASSESSABLE"
            )
            value["dimensions"]["checker_fidelity"]["rationale"] = (
                "Evidence is unavailable."
            )
            assessment_path = workspace / "assessment.json"
            assessment_path.write_text(
                json.dumps(value, ensure_ascii=False),
                encoding="utf-8",
            )

            completed = run_paper_grounded(package, assessment_path)

            self.assertNotEqual(completed.returncode, 0)
            self.assertIn(
                "NOT_ASSESSABLE requires an empty evidence list",
                completed.stderr,
            )


if __name__ == "__main__":
    unittest.main()
