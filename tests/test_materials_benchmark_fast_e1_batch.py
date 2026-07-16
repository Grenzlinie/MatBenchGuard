from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
RUNNER = (
    REPO_ROOT
    / ".cursor"
    / "skills"
    / "materials-benchmark-review"
    / "scripts"
    / "run_fast_e1_batch.py"
)
SCHEMA_VERSION = "materials-fast-e1-index/0.2"


def package_root(corpus: Path, cluster: str, theme: str, paper: str) -> Path:
    root = corpus / cluster / theme / paper
    root.mkdir(parents=True)
    return root


def write_reviewable_package(root: Path) -> None:
    (root / "environment").mkdir()
    (root / "tests").mkdir()
    (root / "solution").mkdir()
    (root / "solution" / "do-not-read.txt").write_text(
        "private", encoding="utf-8"
    )
    (root / "task.toml").write_text('name = "fixture"\n', encoding="utf-8")
    (root / "manifest.json").write_text(
        json.dumps({"discipline": "materials science"}), encoding="utf-8"
    )
    (root / "instruction.md").write_text(
        "Compute the energy of a crystal material and write "
        "/app/outputs/result.json.",
        encoding="utf-8",
    )
    (root / "steps.json").write_text(
        json.dumps(
            [
                {
                    "id": "compute",
                    "output_file": "result.json",
                    "evidence": "",
                }
            ]
        ),
        encoding="utf-8",
    )
    (root / "resources.json").write_text(
        json.dumps(
            {
                "version": 1,
                "resources": [
                    {
                        "id": "constants",
                        "required": True,
                        "access": {
                            "method": "inline",
                            "notes": "A crystal energy constant is in the task.",
                        },
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    (root / "environment" / "Dockerfile").write_text(
        "FROM python:3.11\n", encoding="utf-8"
    )
    grading_spec = {
        "pass_threshold": 0.8,
        "output_contract": {
            "outputs": [
                {
                    "file": "result.json",
                    "format": "json",
                    "schema": {"required": {"energy": "number"}},
                    "target_policy": "metric_recompute",
                }
            ]
        },
        "steps": [{"output_file": "result.json", "weight": 1.0}],
    }
    (root / "tests" / "grading_spec.json").write_text(
        json.dumps(grading_spec), encoding="utf-8"
    )
    (root / "tests" / "checker.py").write_text(
        "from pathlib import Path\n"
        "logs = Path('/logs/verifier')\n"
        "logs.mkdir(parents=True, exist_ok=True)\n"
        "(logs / 'reward.txt').write_text('0.0')\n"
        "(logs / 'breakdown.json').write_text('{\"_errors\": {}}')\n",
        encoding="utf-8",
    )
    (root / "tests" / "test.sh").write_text(
        "python /tests/checker.py\n", encoding="utf-8"
    )


def run_cli(
    corpus: Path, output: Path, *extra: str
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(RUNNER),
            str(corpus),
            "--output-dir",
            str(output),
            *extra,
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=120,
        check=False,
    )


def source_role_hashes(package: Path) -> dict[str, str]:
    paths = [package / "instruction.md"]
    paths.extend(
        path for path in (package / "tests").rglob("*") if path.is_file()
    )
    return {
        path.relative_to(package).as_posix(): (
            "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()
        )
        for path in sorted(paths)
    }


class FastE1BatchTests(unittest.TestCase):
    def test_candidate_manifest_contains_sample_identities_only(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            corpus = base / "corpus"
            source = package_root(
                corpus, "cluster-1", "materials-energy", "paper-1"
            )
            write_reviewable_package(source)
            output = base / "artifacts"

            completed = run_cli(
                corpus,
                output,
                "--workers",
                "1",
                "--max-packages",
                "1",
                "--target",
                "1",
            )

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            manifest = json.loads(
                (output / "candidate_manifest.json").read_text(encoding="utf-8")
            )
            self.assertEqual(
                set(manifest),
                {
                    "schema_version",
                    "manifest_role",
                    "identity_set_authoritative",
                    "sample_count",
                    "ordering",
                    "package_ids",
                },
            )
            self.assertEqual(
                manifest["manifest_role"], "AUTHORITATIVE_SAMPLE_IDENTITY"
            )
            self.assertEqual(
                manifest["package_ids"],
                ["cluster-1/materials-energy/paper-1"],
            )

    def test_frozen_identity_baseline_blocks_repair_until_all_are_reviewed(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            corpus = base / "corpus"
            identities = [
                "cluster-2/theme/paper-2",
                "cluster-1/theme/paper-1",
            ]
            for package_id in identities:
                root = corpus.joinpath(*package_id.split("/"))
                root.mkdir(parents=True)
                write_reviewable_package(root)
            extra = package_root(corpus, "cluster-3", "theme", "paper-3")
            write_reviewable_package(extra)
            frozen = base / "frozen.json"
            frozen.write_text(
                json.dumps(
                    {
                        "schema_version": (
                            "materials-fast-e1-sample-identities/1.0"
                        ),
                        "manifest_role": "AUTHORITATIVE_SAMPLE_IDENTITY",
                        "identity_set_authoritative": True,
                        "sample_count": 2,
                        "ordering": "fixture",
                        "package_ids": identities,
                    }
                ),
                encoding="utf-8",
            )
            output = base / "artifacts"

            first = run_cli(
                corpus,
                output,
                "--identity-manifest",
                str(frozen),
                "--workers",
                "1",
                "--max-packages",
                "1",
                "--target",
                "2",
            )
            self.assertEqual(first.returncode, 0, msg=first.stderr)
            first_index = json.loads(
                (output / "index.json").read_text(encoding="utf-8")
            )
            self.assertEqual(
                first_index["repair_gate"],
                "BLOCKED_REVIEW_BASELINE_INCOMPLETE",
            )

            second = run_cli(
                corpus,
                output,
                "--identity-manifest",
                str(frozen),
                "--workers",
                "1",
                "--max-packages",
                "2",
                "--target",
                "2",
            )
            self.assertEqual(second.returncode, 0, msg=second.stderr)
            second_index = json.loads(
                (output / "index.json").read_text(encoding="utf-8")
            )
            self.assertEqual(second_index["repair_gate"], "READY_FOR_REPAIR")
            manifest = json.loads(
                (output / "candidate_manifest.json").read_text(encoding="utf-8")
            )
            self.assertEqual(manifest["package_ids"], identities)

    def test_parallel_jsonl_preserves_frozen_identity_order(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            corpus = base / "corpus"
            identities = [
                "cluster-1/theme/paper-slow",
                "cluster-2/theme/paper-fast",
            ]
            for package_id in identities:
                root = corpus.joinpath(*package_id.split("/"))
                root.mkdir(parents=True)
                write_reviewable_package(root)
            slow_checker = corpus / identities[0] / "tests/checker.py"
            slow_checker.write_text(
                "import time\ntime.sleep(0.05)\n"
                + slow_checker.read_text(encoding="utf-8"),
                encoding="utf-8",
            )
            frozen = base / "frozen.json"
            frozen.write_text(
                json.dumps(
                    {
                        "schema_version": (
                            "materials-fast-e1-sample-identities/1.0"
                        ),
                        "manifest_role": "AUTHORITATIVE_SAMPLE_IDENTITY",
                        "identity_set_authoritative": True,
                        "sample_count": 2,
                        "ordering": "fixture",
                        "package_ids": identities,
                    }
                ),
                encoding="utf-8",
            )
            output = base / "artifacts"

            completed = run_cli(
                corpus,
                output,
                "--identity-manifest",
                str(frozen),
                "--workers",
                "2",
                "--max-packages",
                "2",
                "--target",
                "2",
            )

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            records = [
                json.loads(line)
                for line in (output / "results.jsonl")
                .read_text(encoding="utf-8")
                .splitlines()
            ]
            self.assertEqual(
                [record["package_id"] for record in records],
                identities,
            )

    def test_discovery_is_deterministic_and_cluster_round_robin(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            corpus = base / "corpus"
            for cluster in ("cluster-2", "cluster-1"):
                for paper in ("paper-2", "paper-1"):
                    package_root(corpus, cluster, "theme", paper)
            output = base / "artifacts"

            first = run_cli(corpus, output, "--discover-only")
            self.assertEqual(first.returncode, 0, msg=first.stderr)
            first_index = (output / "index.json").read_bytes()
            second = run_cli(corpus, output, "--discover-only")
            self.assertEqual(second.returncode, 0, msg=second.stderr)
            self.assertEqual(first_index, (output / "index.json").read_bytes())

            index = json.loads(first_index)
            self.assertEqual(
                [item["package_id"] for item in index["records"]],
                [
                    "cluster-1/theme/paper-1",
                    "cluster-2/theme/paper-1",
                    "cluster-1/theme/paper-2",
                    "cluster-2/theme/paper-2",
                ],
            )

    def test_public_cli_index_schema_and_solution_exclusion(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            corpus = base / "corpus"
            source = package_root(
                corpus, "cluster-1", "materials-energy", "paper-1"
            )
            write_reviewable_package(source)
            output = base / "artifacts"

            completed = run_cli(
                corpus,
                output,
                "--workers",
                "2",
                "--max-packages",
                "1",
                "--target",
                "1",
            )
            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            index = json.loads(
                (output / "index.json").read_text(encoding="utf-8")
            )
            manifest = json.loads(
                (output / "candidate_manifest.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(index["schema_version"], SCHEMA_VERSION)
            self.assertFalse(index["solution_content_inspected"])
            self.assertEqual(index["counts"]["screened"], 1)
            self.assertEqual(
                index["records"][0]["state"], "E1_EXCLUDED"
            )
            self.assertIn(
                "PAPER_GROUNDED_STAGE_REQUIRED",
                index["records"][0]["exclusion_reasons"],
            )
            self.assertEqual(
                manifest["manifest_role"], "AUTHORITATIVE_SAMPLE_IDENTITY"
            )
            self.assertEqual(
                manifest["package_ids"],
                ["cluster-1/materials-energy/paper-1"],
            )
            record = index["records"][0]
            hashes = record["evidence"]["input_hashes"]
            self.assertFalse(
                any(name.startswith("solution/") for name in hashes)
            )
            checker_tests = record["evidence"]["checker"]["tests"]
            self.assertTrue(checker_tests)
            self.assertEqual(
                record["evidence"]["checker"]["runtime"][
                    "verifier_entrypoint"
                ],
                "tests/test.sh",
            )
            self.assertEqual(
                record["evidence"]["checker"]["runtime"][
                    "runtime_provenance"
                ],
                "audit-host-copy",
            )
            self.assertTrue(
                all(
                    item["runtime_package_contains_solution"] is False
                    for item in checker_tests
                )
            )
            report_path = (
                output
                / record["evidence"]["cli_evidence"]["report_path"]
            )
            report = json.loads(report_path.read_text(encoding="utf-8"))
            self.assertEqual(
                set(record["evidence"]["qa_axes"]),
                {
                    "factual_accuracy",
                    "answer_leakage",
                    "instruction_completeness",
                    "checker_instruction_consistency",
                },
            )
            self.assertEqual(
                record["evidence"]["qa_axes"], report["qa_axes"]
            )
            self.assertEqual(
                record["evidence"]["cli_evidence"]["qa_axes"],
                report["qa_axes"],
            )
            scoring = record["evidence"]["cli_scoring"]
            self.assertEqual(
                scoring["scoring_version"], "materials-review-scoring/1.0"
            )
            self.assertIsNone(scoring["total_score"])
            self.assertTrue(
                any(
                    item["points_earned"] is None
                    for item in scoring["dimension_scores"]
                )
            )
            self.assertEqual(len(scoring["hard_gates"]), 4)
            evidence_snapshot = index["records"][0]["evidence"][
                "cli_evidence"
            ]
            self.assertEqual(
                evidence_snapshot["contract_version"],
                "materials-evidence-contract/1.0",
            )
            self.assertEqual(
                evidence_snapshot["checker_tests_path"],
                "cli_reports/cluster-1/materials-energy/paper-1/checker_tests.json",
            )
            self.assertTrue(evidence_snapshot["snapshot_hash"].startswith("sha256:"))
            implementation = evidence_snapshot["review_implementation"]
            self.assertEqual(
                implementation["root"],
                ".cursor/skills/materials-benchmark-review",
            )
            self.assertTrue(
                implementation["aggregate_hash"].startswith("sha256:")
            )
            self.assertTrue(
                all(
                    not Path(relative).is_absolute()
                    for relative in implementation["files"]
                )
            )
            persisted_manifest = json.loads(
                (output / evidence_snapshot["manifest_path"]).read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(
                persisted_manifest["review_implementation"],
                implementation,
            )
            self.assertTrue(
                (output / evidence_snapshot["checker_tests_path"]).is_file()
            )
            self.assertFalse((source / "benchmark_audit").exists())
            self.assertFalse((source / ".benchmark_audit_tmp").exists())

    def test_public_cli_accepts_source_bound_external_taxonomy_assessment(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            corpus = base / "corpus"
            source = package_root(
                corpus, "cluster-1", "materials-energy", "paper-1"
            )
            write_reviewable_package(source)
            instruction = source / "instruction.md"
            instruction.write_text(
                instruction.read_text(encoding="utf-8")
                + "\nCompute the electronic structure of a metal alloy.\n",
                encoding="utf-8",
            )
            assessments = base / "assessments"
            assessment = assessments / "cluster-1/materials-energy/paper-1.json"
            assessment.parent.mkdir(parents=True)
            assessment.write_text(
                json.dumps(
                    {
                        "schema_version": "0.1",
                        "taxonomy": {
                            "computation_task": ["电子结构"],
                            "research_domain": ["基础材料研究与材料发现"],
                            "material_system": {
                                "primary": "金属与合金",
                                "secondary": [],
                            },
                        },
                        "taxonomy_evidence": [
                            {
                                "dimension": "computation_task",
                                "label": "电子结构",
                                "package_file": "instruction.md",
                                "package_quote": "electronic structure",
                            },
                            {
                                "dimension": "research_domain",
                                "label": "基础材料研究与材料发现",
                                "package_file": "instruction.md",
                                "package_quote": "Compute the electronic structure",
                            },
                            {
                                "dimension": "material_system.primary",
                                "label": "金属与合金",
                                "package_file": "instruction.md",
                                "package_quote": "metal alloy",
                            },
                        ],
                        "materials_qualification": {
                            "classification": "MAT_WRAPPER",
                            "rationale": (
                                "The instruction names a material and a "
                                "domain-specific electronic-structure operation."
                            ),
                            "evidence": [
                                {
                                    "axis": "object",
                                    "package_file": "instruction.md",
                                    "package_quote": "metal alloy",
                                },
                                {
                                    "axis": "operation",
                                    "package_file": "instruction.md",
                                    "package_quote": "electronic structure",
                                },
                                {
                                    "axis": "endpoint",
                                    "package_file": "instruction.md",
                                    "package_quote": "result.json",
                                },
                                {
                                    "axis": "domain_dependence",
                                    "package_file": "instruction.md",
                                    "package_quote": "electronic structure of a metal alloy",
                                },
                            ],
                        },
                        "paper_trigger_adjudication": [
                            {
                                "trigger": trigger,
                                "status": (
                                    "TRIGGERED"
                                    if trigger == "NECESSARY_INFORMATION_MISSING"
                                    else "NOT_TRIGGERED"
                                ),
                                "rationale": (
                                    "The minimal fixture omits scientific "
                                    "definitions needed for a real calculation."
                                    if trigger == "NECESSARY_INFORMATION_MISSING"
                                    else "The public fixture supplies no evidence "
                                    "for this trigger."
                                ),
                                "evidence": [
                                    {
                                        "package_file": "instruction.md",
                                        "package_quote": "Compute the energy",
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
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            output = base / "artifacts"

            completed = run_cli(
                corpus,
                output,
                "--workers",
                "1",
                "--max-packages",
                "1",
                "--target",
                "1",
                "--assessment-dir",
                str(assessments),
            )

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            report = json.loads(
                next((output / "cli_reports").rglob("audit_report.json")).read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(report["taxonomy_labels"]["computation_task"], ["电子结构"])
            self.assertEqual(report["taxonomy_source"]["revision"], 85)
            assessment.write_text(
                assessment.read_text(encoding="utf-8") + "\n",
                encoding="utf-8",
            )
            resumed = run_cli(
                corpus,
                output,
                "--workers",
                "1",
                "--max-packages",
                "1",
                "--target",
                "1",
                "--assessment-dir",
                str(assessments),
            )
            self.assertNotEqual(resumed.returncode, 0)
            self.assertIn("taxonomy assessment is missing or stale", resumed.stderr)

    def test_public_cli_runs_triggered_paper_assessment_source_bound(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            corpus = base / "corpus"
            source = package_root(
                corpus, "cluster-1", "materials-energy", "paper-1"
            )
            write_reviewable_package(source)
            (source / "paper").mkdir()
            (source / "paper/paper.md").write_text(
                "A crystal energy model is reproduced.",
                encoding="utf-8",
            )
            (source / "paper/images_manifest.json").write_text(
                "[]\n",
                encoding="utf-8",
            )
            assessments = base / "assessments"
            assessment = assessments / "cluster-1/materials-energy/paper-1.json"
            assessment.parent.mkdir(parents=True)
            assessment.write_text(
                json.dumps(
                    {
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
                                "rationale": "The package evidence adjudicates this trigger.",
                                "evidence": [
                                    {
                                        "package_file": "instruction.md",
                                        "package_quote": "Compute the energy",
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
                            name: {
                                "status": "PASS",
                                "rationale": "The paper and package define the same scoped model.",
                                "evidence": [
                                    {
                                        "paper_quote": "A crystal energy model is reproduced.",
                                        "package_file": (
                                            "tests/checker.py"
                                            if name == "checker_fidelity"
                                            else "tests/grading_spec.json"
                                            if name == "gold_provenance"
                                            else "instruction.md"
                                        ),
                                        "package_quote": (
                                            "logs = Path('/logs/verifier')"
                                            if name == "checker_fidelity"
                                            else '"pass_threshold": 0.8'
                                            if name == "gold_provenance"
                                            else "Compute the energy"
                                        ),
                                    }
                                ],
                            }
                            for name in (
                                "instruction_fidelity",
                                "data_fidelity",
                                "method_fidelity",
                                "gold_provenance",
                                "checker_fidelity",
                            )
                        },
                        "taxonomy": {
                            "computation_task": ["电子结构"],
                            "research_domain": ["基础材料研究与材料发现"],
                            "material_system": {
                                "primary": "金属与合金",
                                "secondary": [],
                            },
                        },
                        "taxonomy_evidence": [
                            {
                                "dimension": "computation_task",
                                "label": "电子结构",
                                "package_file": "instruction.md",
                                "package_quote": "Compute the energy",
                            },
                            {
                                "dimension": "research_domain",
                                "label": "基础材料研究与材料发现",
                                "package_file": "instruction.md",
                                "package_quote": "crystal material",
                            },
                            {
                                "dimension": "material_system.primary",
                                "label": "金属与合金",
                                "package_file": "instruction.md",
                                "package_quote": "crystal material",
                            },
                        ],
                        "materials_qualification": {
                            "classification": "MAT_WRAPPER",
                            "rationale": "The task evaluates a material-energy endpoint.",
                            "evidence": [
                                {
                                    "axis": axis,
                                    "package_file": "instruction.md",
                                    "package_quote": quote,
                                }
                                for axis, quote in (
                                    ("object", "crystal material"),
                                    ("operation", "Compute the energy"),
                                    ("endpoint", "result.json"),
                                    ("domain_dependence", "energy of a crystal material"),
                                )
                            ],
                        },
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            output = base / "artifacts"

            completed = run_cli(
                corpus,
                output,
                "--workers",
                "1",
                "--max-packages",
                "1",
                "--target",
                "1",
                "--assessment-dir",
                str(assessments),
            )

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            report = json.loads(
                next((output / "cli_reports").rglob("audit_report.json")).read_text(
                    encoding="utf-8"
                )
            )
            record = json.loads(
                (output / "results.jsonl").read_text(encoding="utf-8")
            )
            self.assertEqual(
                report["configuration"]["paper_mode"], "paper_grounded"
            )
            self.assertIn(
                "paper/paper.md",
                record["evidence"]["source_binding"]["source_role_hashes"],
            )
            self.assertEqual(
                record["paper_grounded_status"],
                report["paper_consistency"]["status"],
            )
            self.assertEqual(
                report["audit_binding"]["parent_audit_id"],
                record["evidence"]["stage_binding"]["no_paper_audit_id"],
            )
            self.assertEqual(
                record["evidence"]["stage_binding"]["paper_grounded_audit_id"],
                report["audit_id"],
            )
            self.assertEqual(
                record["evidence"]["stage_binding"]["status"],
                "PAPER_GROUNDED_BOUND_TO_NO_PAPER",
            )

    def test_resume_does_not_review_completed_package_again(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            corpus = base / "corpus"
            source = package_root(
                corpus, "cluster-1", "materials-energy", "paper-1"
            )
            write_reviewable_package(source)
            output = base / "artifacts"
            arguments = (
                "--workers",
                "1",
                "--max-packages",
                "1",
                "--target",
                "1",
            )

            first = run_cli(corpus, output, *arguments)
            self.assertEqual(first.returncode, 0, msg=first.stderr)
            ledger_before = (output / "results.jsonl").read_bytes()
            second = run_cli(corpus, output, *arguments)
            self.assertEqual(second.returncode, 0, msg=second.stderr)
            self.assertEqual(
                ledger_before, (output / "results.jsonl").read_bytes()
            )
            index = json.loads(
                (output / "index.json").read_text(encoding="utf-8")
            )
            self.assertEqual(index["counts"]["screened"], 1)

    def test_public_cli_rejects_source_misbound_completed_record(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            corpus = base / "corpus"
            source = package_root(
                corpus, "cluster-1", "materials-energy", "paper-1"
            )
            write_reviewable_package(source)
            output = base / "artifacts"
            arguments = (
                "--workers",
                "1",
                "--max-packages",
                "1",
                "--target",
                "1",
            )
            first = run_cli(corpus, output, *arguments)
            self.assertEqual(first.returncode, 0, msg=first.stderr)
            ledger = output / "results.jsonl"
            record = json.loads(ledger.read_text(encoding="utf-8"))
            binding = record["evidence"]["source_binding"]
            self.assertEqual(binding["package_id"], record["package_id"])
            self.assertEqual(
                binding["source_role_hashes"], source_role_hashes(source)
            )
            self.assertEqual(
                binding["cli_audit_identity"]["audit_id"],
                binding["cli_audit_identity"]["manifest_audit_id"],
            )

            other = package_root(
                corpus, "cluster-2", "other-materials", "paper-2"
            )
            write_reviewable_package(other)
            (other / "instruction.md").write_text(
                "Compute a different material property and write "
                "/app/outputs/result.json.",
                encoding="utf-8",
            )
            other_hashes = source_role_hashes(other)
            record["evidence"]["input_hashes"] = other_hashes
            record["evidence"]["source_binding"][
                "source_role_hashes"
            ] = other_hashes
            record["evidence"]["source_binding"]["cli_audit_identity"][
                "package_id"
            ] = "cluster-2/other-materials/paper-2"
            ledger.write_text(
                json.dumps(record, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )

            resumed = run_cli(
                corpus,
                output,
                "--identity-manifest",
                str(output / "candidate_manifest.json"),
                *arguments,
            )

            self.assertEqual(resumed.returncode, 2)
            self.assertIn("source binding validation failed", resumed.stderr)

    def test_public_cli_rejects_manual_score_or_verdict_fields(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            corpus = base / "corpus"
            source = package_root(
                corpus, "cluster-1", "materials-energy", "paper-1"
            )
            write_reviewable_package(source)
            output = base / "artifacts"
            arguments = (
                "--workers",
                "1",
                "--max-packages",
                "1",
                "--target",
                "1",
            )
            first = run_cli(corpus, output, *arguments)
            self.assertEqual(first.returncode, 0, msg=first.stderr)
            ledger = output / "results.jsonl"
            record = json.loads(ledger.read_text(encoding="utf-8"))
            record["total_score"] = 100
            record["verdict"] = "PASS"
            ledger.write_text(
                json.dumps(record, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )

            resumed = run_cli(
                corpus,
                output,
                "--identity-manifest",
                str(output / "candidate_manifest.json"),
                *arguments,
            )

            self.assertEqual(resumed.returncode, 2)
            self.assertIn(
                "manual score/verdict fields are forbidden", resumed.stderr
            )

    def test_public_cli_rejects_overridden_cli_scoring_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            corpus = base / "corpus"
            source = package_root(
                corpus, "cluster-1", "materials-energy", "paper-1"
            )
            write_reviewable_package(source)
            output = base / "artifacts"
            arguments = (
                "--workers",
                "1",
                "--max-packages",
                "1",
                "--target",
                "1",
            )
            first = run_cli(corpus, output, *arguments)
            self.assertEqual(first.returncode, 0, msg=first.stderr)
            ledger = output / "results.jsonl"
            record = json.loads(ledger.read_text(encoding="utf-8"))
            scoring = record["evidence"]["cli_scoring"]
            scoring["total_score"] = 100
            unhashed = {
                key: value
                for key, value in scoring.items()
                if key != "snapshot_hash"
            }
            scoring["snapshot_hash"] = "sha256:" + hashlib.sha256(
                json.dumps(
                    unhashed,
                    ensure_ascii=False,
                    sort_keys=True,
                    separators=(",", ":"),
                ).encode("utf-8")
            ).hexdigest()
            record["evidence"]["source_binding"]["cli_audit_identity"][
                "scoring_snapshot_hash"
            ] = scoring["snapshot_hash"]
            ledger.write_text(
                json.dumps(record, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )

            resumed = run_cli(
                corpus,
                output,
                "--identity-manifest",
                str(output / "candidate_manifest.json"),
                *arguments,
            )

            self.assertEqual(resumed.returncode, 2)
            self.assertIn(
                "scoring snapshot differs from persisted report",
                resumed.stderr,
            )

    def test_public_cli_rejects_tampered_persisted_checker_evidence(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            corpus = base / "corpus"
            source = package_root(
                corpus, "cluster-1", "materials-energy", "paper-1"
            )
            write_reviewable_package(source)
            output = base / "artifacts"
            arguments = (
                "--workers",
                "1",
                "--max-packages",
                "1",
                "--target",
                "1",
            )
            first = run_cli(corpus, output, *arguments)
            self.assertEqual(first.returncode, 0, msg=first.stderr)
            record = json.loads(
                (output / "results.jsonl").read_text(encoding="utf-8")
            )
            checker_path = (
                output
                / record["evidence"]["cli_evidence"]["checker_tests_path"]
            )
            checker_path.write_text("{}\n", encoding="utf-8")

            resumed = run_cli(
                corpus,
                output,
                "--identity-manifest",
                str(output / "candidate_manifest.json"),
                *arguments,
            )

            self.assertEqual(resumed.returncode, 2)
            self.assertIn(
                "persisted CLI evidence snapshot differs",
                resumed.stderr,
            )

    def test_canonical_calibration_reconciliation_is_source_bound(self) -> None:
        artifacts = (
            REPO_ROOT
            / "review_artifacts"
            / "materials_fast_e1_100"
            / "calibration_review_v2_20260715"
        )
        canonical = json.loads(
            (artifacts / "canonical_reconciliation.json").read_text(
                encoding="utf-8"
            )
        )
        frozen = json.loads(
            (artifacts.parent / "candidate_manifest.json").read_text(
                encoding="utf-8"
            )
        )
        source_validation = json.loads(
            (artifacts / "source_hash_validation.json").read_text(
                encoding="utf-8"
            )
        )
        expected_verdicts = [
            "CONDITIONAL",
            "REJECT",
            "PASS",
            "CONDITIONAL",
            "PASS",
            "REJECT",
            "PASS",
            "REJECT",
            "CONDITIONAL",
            "REJECT",
        ]
        expected_reproduction = [
            "METHOD_REIMPLEMENTATION",
            "METHOD_REIMPLEMENTATION",
            "EXACT_REPRODUCTION",
            "EXACT_REPRODUCTION",
            "EXACT_REPRODUCTION",
            "METHOD_REIMPLEMENTATION",
            "EXACT_REPRODUCTION",
            "METHOD_REIMPLEMENTATION",
            "EXACT_REPRODUCTION",
            "METHOD_REIMPLEMENTATION",
        ]
        records = canonical["records"]
        self.assertTrue(canonical["authoritative"])
        self.assertEqual(
            [item["package_id"] for item in records],
            frozen["package_ids"][:10],
        )
        self.assertEqual(
            [item["verdict"] for item in records], expected_verdicts
        )
        self.assertEqual(
            [item["reproduction_type"] for item in records],
            expected_reproduction,
        )
        self.assertEqual(
            dict(Counter(expected_verdicts)),
            {
                key: value
                for key, value in canonical["verdict_totals"].items()
                if value
            },
        )

        corpus = REPO_ROOT / "materials_science_questions"
        for record in records:
            package_id = record["package_id"]
            source = corpus / package_id
            audit = artifacts / record["source_binding"]["cli_audit"]
            manifest = json.loads(
                (audit / "audit_manifest.json").read_text(encoding="utf-8")
            )
            report = json.loads(
                (audit / "audit_report.json").read_text(encoding="utf-8")
            )
            self.assertEqual(
                record["source_binding"]["audit_id"], manifest["audit_id"]
            )
            self.assertEqual(report["audit_id"], manifest["audit_id"])
            actual_hashes = {
                role: "sha256:"
                + hashlib.sha256((source / role).read_bytes()).hexdigest()
                for role in manifest["input_hashes"]
            }
            self.assertEqual(manifest["input_hashes"], actual_hashes)
            self.assertEqual(
                manifest["input_hashes"],
                {
                    role: source_validation["after"][package_id][role]
                    for role in manifest["input_hashes"]
                },
            )

        revised = REPO_ROOT / "review_artifacts/materials_revised_calibration_10"
        invalid = json.loads(
            (revised / "INVALID_NON_AUTHORITATIVE.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(invalid["status"], "INVALID")
        self.assertFalse(invalid["authoritative"])
        self.assertTrue(invalid["evidence_preserved"])

    def test_discovery_index_has_required_identity_schema(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            corpus = base / "corpus"
            package_root(
                corpus, "cluster-9", "compute-band-gap", "paper-42"
            )
            output = base / "artifacts"

            completed = run_cli(corpus, output, "--discover-only")
            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            record = json.loads(
                (output / "index.json").read_text(encoding="utf-8")
            )["records"][0]
            self.assertEqual(
                {
                    "package_id",
                    "cluster",
                    "theme",
                    "paper",
                    "source_relative_path",
                    "discovery_rank",
                    "schema_version",
                    "state",
                    "solution_content_inspected",
                },
                set(record),
            )
            self.assertEqual(record["cluster"], "cluster-9")
            self.assertEqual(record["theme"], "compute-band-gap")
            self.assertEqual(record["paper"], "paper-42")


if __name__ == "__main__":
    unittest.main()
