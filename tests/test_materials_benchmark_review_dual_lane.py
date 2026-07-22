from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

REVIEW_SCRIPTS = REPO_ROOT / ".cursor/skills/materials-benchmark-review/scripts"
sys.path.insert(0, str(REVIEW_SCRIPTS))
import run_context  # noqa: E402


def review_run_dir(package: Path) -> Path:
    """Build an isolated public-CLI run for a fixture package."""
    run = package.parent / ".review_records" / package.name / "runs" / "test"
    if run.exists():
        return run
    (run / "agent_contract").mkdir(parents=True)
    (run / "agent_contract/assessment.json").write_text("{}\n", encoding="utf-8")
    (run / "regressions").mkdir()
    (run / "roots").mkdir()
    run_context.write_json_atomic(
        run / "context.json",
        {
            "schema_version": run_context.RUN_CONTEXT_SCHEMA,
            "run_id": "test",
            "package_id": f"fixture/theme/{package.name}",
            "package_path": str(package.resolve()),
            "corpus_root": str(package.parent.resolve()),
            "review_contract_version": run_context.REVIEW_CONTRACT_VERSION,
            "created_at": run_context.now(),
        },
    )
    run_context.write_json_atomic(
        run / "status.json",
        {"schema_version": run_context.STATUS_SCHEMA, "state": "ASSIGNED", "updated_at": run_context.now()},
    )
    return run


def external_audit_dir(package: Path) -> Path:
    return review_run_dir(package) / "audit" / "benchmark_audit"


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


def sanitize_dual_lane_assessment(value: dict[str, object]) -> dict[str, object]:
    return dict(value)


def assessment() -> dict[str, object]:
    return sanitize_dual_lane_assessment({
        "schema_version": "0.1",
        "materials_qualification": {
            "classification": "MAT_CORE",
            "rationale": "The task evaluates a materials lattice-dynamics endpoint.",
            "evidence": [
                {
                    "axis": axis,
                    "package_file": "instruction.md",
                    "package_quote": quote,
                }
                for axis, quote in (
                    ("object", "face-centred cubic copper (Cu)"),
                    ("data", "c11 = 1.68×10¹² dynes/cm²"),
                    ("operation", "evaluate the corresponding analytical formula"),
                    ("endpoint", "dispersion_curves.csv"),
                    ("domain_dependence", "phonon spectrum"),
                )
            ],
        },
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
    })


def dual_lane_assessment() -> dict[str, object]:
    value = assessment()
    return sanitize_dual_lane_assessment({
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
    })


def run_dual_lane(
    package: Path,
    assessment_path: Path,
    *,
    audit_output_dir: Path | None = None,
    extra_args: list[str] | None = None,
    **_ignored,
) -> subprocess.CompletedProcess[str]:
    del audit_output_dir, extra_args
    if assessment_path.resolve().is_relative_to(package.resolve()):
        # Keep the public fixture helper honest: the CLI receives a run-local
        # copy only after enforcing the external-evidence boundary.
        return subprocess.CompletedProcess([], 2, "", "agent assessment must be outside the Harbor 题包")
    existing = package.parent / ".review_records" / package.name / "runs" / "test"
    if existing.exists():
        shutil.rmtree(existing)
    run = review_run_dir(package)
    shutil.copy2(assessment_path, run / "agent_assessment.json")
    command = [
        "python3",
        str(RUNNER),
        "--run-dir",
        str(run),
    ]
    return subprocess.run(command, capture_output=True, text=True, check=False)


def assert_assessment_pending(
    test: unittest.TestCase,
    completed: subprocess.CompletedProcess[str],
    *,
    needle: str,
    package: Path,
) -> None:
    """Invalid paper assessments pause the same run without a formal audit."""

    test.assertEqual(
        completed.returncode,
        0,
        msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
    )
    payload = json.loads(completed.stdout)
    test.assertEqual(payload.get("status"), "AGENT_ASSESSMENT_PENDING")
    test.assertIn(needle, payload.get("message", ""))
    test.assertFalse((external_audit_dir(package) / "audit_report.json").exists())
    run = review_run_dir(package)
    status = json.loads((run / "status.json").read_text(encoding="utf-8"))
    test.assertEqual(status["state"], "AGENT_ASSESSMENT_PENDING")
    test.assertFalse((run / "roots/A0.json").exists())



def run_dual_lane_with_taxonomy(
    package: Path,
    assessment_path: Path,
    *,
    audit_output_dir: Path | None = None,
    **_ignored,
) -> subprocess.CompletedProcess[str]:
    return run_dual_lane(
        package,
        assessment_path,
        audit_output_dir=audit_output_dir,
    )



class MaterialsBenchmarkDualLaneTests(unittest.TestCase):
    def test_oracle_probe_is_not_a_public_fixture(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            value = assessment()
            public_assessment = dual_lane_assessment()
            value["materials_qualification"] = public_assessment[
                "materials_qualification"
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

            completed = run_dual_lane(package, assessment_path)

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            report = json.loads(
                (
                    external_audit_dir(package) / "audit_report.json"
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





    def test_paper_grounded_review_publishes_fidelity_and_taxonomy(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            original_manifest = (package / "manifest.json").read_bytes()
            assessment_path = workspace / "assessment.json"
            assessment_path.write_text(
                json.dumps(sanitize_dual_lane_assessment(assessment()), ensure_ascii=False),
                encoding="utf-8",
            )

            completed = run_dual_lane(package, assessment_path)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            audit_dir = external_audit_dir(package)
            report = json.loads(
                (audit_dir / "audit_report.json").read_text(encoding="utf-8")
            )
            self.assertEqual(report["configuration"]["review_lane"], "dual")
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
                report["summary"]["final_verdict"], "CONDITIONAL"
            )
            self.assertEqual(
                report["summary"]["publication_route"], "REPAIR_QUEUE"
            )
            self.assertIn(
                "PAPER_DATA_FIDELITY_WARNING",
                {finding["title"] for finding in report["findings"]},
            )
            self.assertTrue(report.get("repair_findings"))
            self.assertEqual(
                report["agent_quality"].get("repair_findings"),
                report["repair_findings"],
            )
            paper_queue = [
                item
                for item in report["repair_findings"]
                if item["title"] == "PAPER_DATA_FIDELITY_WARNING"
            ]
            self.assertEqual(len(paper_queue), 1)
            self.assertEqual(paper_queue[0]["lane"], "agent_quality")
            self.assertIsNone(paper_queue[0].get("deterministic_check"))
            self.assertEqual(
                paper_queue[0]["repair_scope"], "SCIENCE_SEMANTICS"
            )
            self.assertEqual(
                report["deterministic_contract"]["repair_summary"]["state"],
                report["repair_queue"]["deterministic_state"],
            )
            self.assertFalse(
                any(
                    (package / name).exists()
                    for name in (
                        "benchmark_audit",
                        ".benchmark_audit_tmp",
                        "audit_report.json",
                    )
                )
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
            self.assertIn("dual-lane", scope_section)



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

            completed = run_dual_lane(package, assessment_path)

            assert_assessment_pending(
                self,
                completed,
                needle="unknown computation_task labels",
                package=package,
            )

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

            completed = run_dual_lane(package, assessment_path)

            assert_assessment_pending(
                self,
                completed,
                needle="missing taxonomy evidence for computation_task",
                package=package,
            )

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

            completed = run_dual_lane(package, assessment_path)

            assert_assessment_pending(
                self,
                completed,
                needle="unsupported package evidence file",
                package=package,
            )

    def test_agent_assessment_cannot_come_from_solution(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            assessment_path = package / "solution/assessment.json"
            assessment_path.write_text(
                json.dumps(sanitize_dual_lane_assessment(assessment()), ensure_ascii=False),
                encoding="utf-8",
            )

            completed = run_dual_lane(package, assessment_path)

            self.assertNotEqual(completed.returncode, 0)
            self.assertIn(
                "agent assessment must be outside the Harbor 题包",
                completed.stderr,
            )
            self.assertFalse((external_audit_dir(package) / "audit_report.json").exists())

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
                json.dumps(sanitize_dual_lane_assessment(assessment()), ensure_ascii=False),
                encoding="utf-8",
            )

            completed = run_dual_lane(package, assessment_path)

            assert_assessment_pending(
                self,
                completed,
                needle="paper role routes through a symlink",
                package=package,
            )
            self.assertFalse((external_audit_dir(package) / "audit_report.json").exists())

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

            completed = run_dual_lane(package, assessment_path)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            report = json.loads(
                (
                    external_audit_dir(package) / "audit_report.json"
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

                    completed = run_dual_lane(package, assessment_path)

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
                            external_audit_dir(package) / "audit_report.json"
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

            completed = run_dual_lane(package, assessment_path)

            assert_assessment_pending(
                self,
                completed,
                needle="checker_fidelity requires at least one evidence item",
                package=package,
            )

    def test_failed_paper_dimension_is_scored_without_inventing_hard_gate(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            value = assessment()
            public_assessment = dual_lane_assessment()
            value["materials_qualification"] = public_assessment[
                "materials_qualification"
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

            completed = run_dual_lane(package, assessment_path)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            report = json.loads(
                (
                    external_audit_dir(package) / "audit_report.json"
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
            self.assertLess(
                checker_alignment["points_earned"],
                checker_alignment["max_points"],
            )
            self.assertTrue(checker_alignment["deductions"])
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

            method_run = run_dual_lane(method_package, method_path)
            exact_run = run_dual_lane(exact_package, exact_path)

            self.assertEqual(method_run.returncode, 0, msg=method_run.stderr)
            self.assertEqual(exact_run.returncode, 0, msg=exact_run.stderr)
            method_report = json.loads(
                (
                    external_audit_dir(method_package) / "audit_report.json"
                ).read_text(encoding="utf-8")
            )
            exact_report = json.loads(
                (
                    external_audit_dir(exact_package) / "audit_report.json"
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

            completed = run_dual_lane(package, assessment_path)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            report = json.loads(
                (
                    external_audit_dir(package) / "audit_report.json"
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

            completed = run_dual_lane(package, assessment_path)

            assert_assessment_pending(
                self,
                completed,
                needle="NOT_ASSESSABLE requires an empty evidence list",
                package=package,
            )


if __name__ == "__main__":
    unittest.main()
