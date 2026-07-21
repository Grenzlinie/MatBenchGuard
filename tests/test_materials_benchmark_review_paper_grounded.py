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
    )
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
        "paper_triggers": ["EXPLICIT_REPRODUCTION_CLAIM"],
        "paper_trigger_adjudication": [
            {
                "trigger": trigger,
                "status": (
                    "TRIGGERED"
                    if trigger == "EXPLICIT_REPRODUCTION_CLAIM"
                    else "NOT_TRIGGERED"
                ),
                "rationale": (
                    "The instruction explicitly claims a scoped reproduction."
                    if trigger == "EXPLICIT_REPRODUCTION_CLAIM"
                    else "The public package evidence does not trigger this condition."
                ),
                "evidence": [
                    {
                        "package_file": "instruction.md",
                        "package_quote": "This computation reproduces a key prediction",
                    }
                ],
            }
            for trigger in (
                "SCIENTIFIC_CONFLICT",
                "NECESSARY_INFORMATION_MISSING",
                "GOLD_PROVENANCE_UNCERTAIN",
                "EXPLICIT_REPRODUCTION_CLAIM",
            )
        ],
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
                        "package_file": "instruction.md",
                        "package_quote": "only nearest-neighbour interactions (α=β=0)",
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


def no_paper_assessment() -> dict[str, object]:
    value = assessment()
    return {
        "schema_version": value["schema_version"],
        "taxonomy": value["taxonomy"],
        "taxonomy_evidence": value["taxonomy_evidence"],
        "materials_qualification": {
            "classification": "MAT_CORE",
            "rationale": (
                "The public task fixes a copper material, numerical inputs, "
                "lattice-dynamics operation, and phonon-dispersion endpoint."
            ),
            "evidence": [
                {
                    "axis": "object",
                    "package_file": "instruction.md",
                    "package_quote": "face-centred cubic copper (Cu)",
                },
                {
                    "axis": "data",
                    "package_file": "instruction.md",
                    "package_quote": "c11 = 1.68×10¹² dynes/cm²",
                },
                {
                    "axis": "operation",
                    "package_file": "instruction.md",
                    "package_quote": "evaluate the corresponding analytical formula",
                },
                {
                    "axis": "endpoint",
                    "package_file": "instruction.md",
                    "package_quote": "dispersion_curves.csv",
                },
                {
                    "axis": "domain_dependence",
                    "package_file": "instruction.md",
                    "package_quote": "phonon spectrum",
                },
            ],
        },
        "paper_trigger_adjudication": [
            {
                "trigger": "SCIENTIFIC_CONFLICT",
                "status": "NOT_TRIGGERED",
                "rationale": (
                    "The instruction and checker both define the same "
                    "dispersion-curve endpoint."
                ),
                "evidence": [
                    {
                        "package_file": "instruction.md",
                        "package_quote": "independently recomputes the expected frequencies",
                    }
                ],
            },
            {
                "trigger": "NECESSARY_INFORMATION_MISSING",
                "status": "NOT_TRIGGERED",
                "rationale": (
                    "The instruction supplies formulas, constants, units, "
                    "sampling, and the output schema."
                ),
                "evidence": [
                    {
                        "package_file": "instruction.md",
                        "package_quote": "The required inputs are",
                    }
                ],
            },
            {
                "trigger": "GOLD_PROVENANCE_UNCERTAIN",
                "status": "NOT_TRIGGERED",
                "rationale": (
                    "The public contract says the checker independently "
                    "recomputes the target from disclosed formulas and inputs."
                ),
                "evidence": [
                    {
                        "package_file": "instruction.md",
                        "package_quote": "metric_recompute",
                    }
                ],
            },
            {
                "trigger": "EXPLICIT_REPRODUCTION_CLAIM",
                "status": "TRIGGERED",
                "rationale": (
                    "The instruction explicitly calls the task a scoped "
                    "reproduction of a lattice-dynamical prediction."
                ),
                "evidence": [
                    {
                        "package_file": "instruction.md",
                        "package_quote": "This computation reproduces a key prediction",
                    }
                ],
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
    def test_oracle_probe_is_not_a_public_fixture(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            value = assessment()
            public_assessment = no_paper_assessment()
            value["materials_qualification"] = public_assessment[
                "materials_qualification"
            ]
            value["paper_trigger_adjudication"] = public_assessment[
                "paper_trigger_adjudication"
            ]
            for dimension in value["dimensions"].values():
                dimension["status"] = "PASS"
            value["dimensions"]["gold_provenance"]["evidence"][0][
                "package_quote"
            ] = "_paper_test_rows"
            value["dimensions"]["checker_fidelity"]["evidence"][0][
                "package_quote"
            ] = "_paper_test_rows"
            assessment_path = workspace / "assessment.json"
            assessment_path.write_text(
                json.dumps(value, ensure_ascii=False),
                encoding="utf-8",
            )

            completed = run_paper_grounded(package, assessment_path)

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            report = json.loads(
                (
                    package / "benchmark_audit/audit_report.json"
                ).read_text(encoding="utf-8")
            )
            self.assertEqual(
                report["deterministic_core"]["probe_results"]["probe_origin"],
                "SCHEMA_DERIVED_DETERMINISTIC",
            )
            self.assertNotIn("fixture_hashes", json.dumps(report))
            self.assertNotIn("repair_reaudit_lineage", json.dumps(report))
            positive = next(
                item
                for item in report["checker_tests"]
                if item["test_type"] == "positive_oracle"
            )
            self.assertEqual(
                report["deterministic_core"]["probe_results"]["probe_origin"],
                "SCHEMA_DERIVED_DETERMINISTIC",
            )
            self.assertNotEqual(
                positive["probe_origin"], "INDEPENDENT_PUBLIC_FIXTURE"
            )

    def test_no_paper_report_records_trigger_adjudication_and_blocks_pass(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            assessment_path = workspace / "assessment.json"
            assessment_path.write_text(
                json.dumps(no_paper_assessment(), ensure_ascii=False),
                encoding="utf-8",
            )

            completed = run_no_paper_with_taxonomy(package, assessment_path)

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            report = json.loads(
                (package / "benchmark_audit/audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(
                {
                    item["trigger"]
                    for item in report["paper_trigger_adjudication"]
                },
                {
                    "SCIENTIFIC_CONFLICT",
                    "NECESSARY_INFORMATION_MISSING",
                    "GOLD_PROVENANCE_UNCERTAIN",
                    "EXPLICIT_REPRODUCTION_CLAIM",
                },
            )
            self.assertEqual(
                report["summary"]["final_verdict"], "NOT_ASSESSABLE"
            )
            self.assertIn(
                "triggered_paper_review",
                report["evidence_contract"]["gaps"],
            )
            for dimension in report["dimensions_v11"]:
                self.assertIn("status", dimension, msg=dimension["dimension"])

    def test_no_paper_assessment_requires_per_trigger_adjudication(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            value = assessment()
            taxonomy_only = {
                "schema_version": value["schema_version"],
                "taxonomy": value["taxonomy"],
                "taxonomy_evidence": value["taxonomy_evidence"],
            }
            assessment_path = workspace / "assessment.json"
            assessment_path.write_text(
                json.dumps(taxonomy_only, ensure_ascii=False),
                encoding="utf-8",
            )

            completed = run_no_paper_with_taxonomy(package, assessment_path)

            self.assertNotEqual(completed.returncode, 0)
            self.assertIn(
                "paper_trigger_adjudication must cover exactly",
                completed.stderr,
            )

    def test_paper_review_requires_a_confirmed_trigger_and_defaults_to_method(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            value = assessment()
            del value["reproduction_type"]
            assessment_path = workspace / "assessment.json"
            assessment_path.write_text(
                json.dumps(value, ensure_ascii=False), encoding="utf-8"
            )

            completed = run_paper_grounded(package, assessment_path)

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
                report["paper_consistency"]["reproduction_type"],
                "METHOD_REIMPLEMENTATION",
            )
            self.assertEqual(
                report["paper_consistency"]["triggers"],
                ["EXPLICIT_REPRODUCTION_CLAIM"],
            )

    def test_paper_grounded_report_preserves_trigger_adjudication(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            value = assessment()
            no_paper_value = no_paper_assessment()
            value["materials_qualification"] = no_paper_value[
                "materials_qualification"
            ]
            value["paper_trigger_adjudication"] = no_paper_value[
                "paper_trigger_adjudication"
            ]
            assessment_path = workspace / "assessment.json"
            assessment_path.write_text(
                json.dumps(value, ensure_ascii=False),
                encoding="utf-8",
            )

            completed = run_paper_grounded(package, assessment_path)

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            report = json.loads(
                (package / "benchmark_audit/audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            adjudication = {
                item["trigger"]: item["status"]
                for item in report["paper_trigger_adjudication"]
            }
            self.assertEqual(
                adjudication,
                {
                    "SCIENTIFIC_CONFLICT": "NOT_TRIGGERED",
                    "NECESSARY_INFORMATION_MISSING": "NOT_TRIGGERED",
                    "GOLD_PROVENANCE_UNCERTAIN": "NOT_TRIGGERED",
                    "EXPLICIT_REPRODUCTION_CLAIM": "TRIGGERED",
                },
            )
            self.assertNotIn(
                "triggered_paper_review",
                report["evidence_contract"]["gaps"],
            )

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
                report["gold_provenance"]["mode"], "paper_grounded"
            )
            self.assertFalse(report["gold_provenance"]["oracle_used"])
            self.assertTrue(
                report["gold_provenance"]["provenance"]["evidence"]
            )
            self.assertIsNotNone(
                report["audit_binding"]["implementation_hash"]
            )
            self.assertTrue(report["audit_binding"]["source_hashes"])
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
                report["summary"]["final_verdict"], "NOT_ASSESSABLE"
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
            self.assertEqual(
                report["summary"]["final_verdict"], "NOT_ASSESSABLE"
            )
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
            taxonomy_only = no_paper_assessment()
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

    def test_failed_paper_dimension_is_scored_without_inventing_hard_gate(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            value = assessment()
            public_assessment = no_paper_assessment()
            value["materials_qualification"] = public_assessment[
                "materials_qualification"
            ]
            value["paper_trigger_adjudication"] = public_assessment[
                "paper_trigger_adjudication"
            ]
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
            self.assertFalse(report["summary"]["hard_gate_triggered"])
            self.assertEqual(
                report["summary"]["final_verdict"], "CONDITIONAL"
            )
            self.assertIsInstance(
                report["summary"]["total_score"], (int, float)
            )
            checker_alignment = next(
                item
                for item in report["dimensions_v11"]
                if item["dimension"] == "C04"
            )
            self.assertEqual(checker_alignment["points_earned"], 0)
            self.assertEqual(
                [
                    deduction["points"]
                    for deduction in checker_alignment["deductions"]
                ],
                [8, 8, 8],
            )
            self.assertIn(
                "PAPER_GOLD_PROVENANCE_FAIL",
                {finding["title"] for finding in report["findings"]},
            )
            self.assertTrue(
                all(
                    item["code"] != "PAPER_GOLD_PROVENANCE_FAIL"
                    for item in report["hard_gates"]
                )
            )

    def test_reproduction_classification_never_changes_score(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            method_package = workspace / "method"
            exact_package = workspace / "exact"
            copy_source_package(method_package)
            copy_source_package(exact_package)
            method_value = assessment()
            exact_value = assessment()
            exact_value["reproduction_type"] = "EXACT_REPRODUCTION"
            method_path = workspace / "method-assessment.json"
            exact_path = workspace / "exact-assessment.json"
            method_path.write_text(
                json.dumps(method_value, ensure_ascii=False), encoding="utf-8"
            )
            exact_path.write_text(
                json.dumps(exact_value, ensure_ascii=False), encoding="utf-8"
            )

            method_run = run_paper_grounded(method_package, method_path)
            exact_run = run_paper_grounded(exact_package, exact_path)

            self.assertEqual(method_run.returncode, 0, msg=method_run.stderr)
            self.assertEqual(exact_run.returncode, 0, msg=exact_run.stderr)
            method_report = json.loads(
                (
                    method_package / "benchmark_audit/audit_report.json"
                ).read_text(encoding="utf-8")
            )
            exact_report = json.loads(
                (
                    exact_package / "benchmark_audit/audit_report.json"
                ).read_text(encoding="utf-8")
            )
            self.assertEqual(
                method_report["summary"]["total_score"],
                exact_report["summary"]["total_score"],
            )
            self.assertEqual(
                method_report["summary"]["final_verdict"],
                exact_report["summary"]["final_verdict"],
            )

    def test_unrecoverable_task_definition_skips_paper_assessment(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            (package / "instruction.md").unlink()

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
                "UNRECOVERABLE_TASK_DEFINITION",
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
                gates["SCIENTIFIC_VALIDITY"], "NOT_ASSESSABLE"
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
