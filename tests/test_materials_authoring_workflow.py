from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "tests") not in sys.path:
    sys.path.insert(0, str(ROOT / "tests"))
from test_materials_core_workflow_v3 import baseline_review

AUTHORING = ROOT / ".cursor/skills/materials-benchmark-authoring"
VALIDATE_RECORD = AUTHORING / "scripts/validate_authoring_record.py"
INIT_WORKSPACE = AUTHORING / "scripts/init_authoring_workspace.py"
VALIDATE_PACKAGE = AUTHORING / "scripts/validate_package.py"


def enhanced_record() -> dict:
    return {
        "schema_version": "materials-benchmark-authoring/1.1",
        "authoring_id": "author-test-paper",
        "status": "REVIEW_PASSED_ENHANCED",
        "source": {
            "pdf_path": "source/paper.pdf",
            "pdf_sha256": "a" * 64,
            "markdown_path": "candidate/paper/paper.md",
        },
        "parse_quality": {"status": "PASS"},
        "candidate_records": [
            {
                "candidate_id": "candidate-1",
                "decision": "SELECTED",
                "q0_status": "PASS",
                "checkpoint_ids": ["checkpoint-1"],
            }
        ],
        "selected_candidate_id": "candidate-1",
        "parameter_records": [],
        "condition_group_records": [
            {
                "condition_group_id": "condition-1",
                "condition_signature": "composition=A; temperature=300 K",
                "required_target_ids": ["target-1"],
            }
        ],
        "resource_records": [],
        "gold_records": [
            {
                "target_id": "target-1",
                "policy": "PAPER_DIRECT",
                "condition_group_ids": ["condition-1"],
                "provenance": ["paper.md: Results, paragraph 2"],
                "independent_check": "manual source cross-check",
            }
        ],
        "tolerance_records": [
            {
                "target_id": "target-1",
                "basis": "reported_precision",
                "boundary_policy": "inclusive",
                "boundary_evidence": ["T-epsilon fails", "T passes", "T+epsilon fails"],
            }
        ],
        "workflow_records": [
            {
                "workflow_id": "workflow-1",
                "producer": "solver computation",
                "consumer": "result checker",
            }
        ],
        "output_contract": [
            {
                "output_id": "result-1",
                "path": "/app/outputs/result.json",
                "target_ids": ["target-1"],
            }
        ],
        "enhancement": {
            "status": "PASS",
            "gold_weight": 0.7,
            "result_weight": 0.3,
            "result_checks": ["checkpoint-1"],
        },
        "probe_records": [
            {"probe_type": probe_type, "status": "PASS"}
            for probe_type in (
                "valid_positive",
                "tolerance_boundary",
                "missing_or_malformed",
                "non_finite_and_duplicate",
                "wrong_science",
                "quality_gradient",
            )
        ],
        "checker_cost_record": {
            "hardware_class": "CPU",
            "cpu_cores": 1,
            "gpu_count": 0,
            "gpu_type": None,
            "measured_wall_seconds": 0.1,
            "peak_memory_mb": 16,
            "input_bytes_read": 1024,
            "uses_full_trajectory": False,
            "performs_new_simulation": False,
            "real_scale_input": True,
            "cost_rationale": "measured on expected full-size result.json",
            "status": "PASS",
        },
        "oracle_validation": {
            "purpose": "CHECKER_FULL_SCORE_FIXTURE",
            "scientific_execution_performed": False,
            "status": "PASS",
            "command": "harbor run -p candidate -a oracle",
            "expected_reward": 1.0,
            "actual_reward": 1.0,
            "all_components_full_score": True,
            "evidence": ["jobs/oracle/trial/result.json: reward=1"],
            "notes": [],
        },
        "package_path": "candidate",
        "independent_review": {
            "schema_version": "materials-core-review/3.3",
            "verdict": "PASS",
            "quality_tier": "RESULT_ENHANCED",
            "publishable": True,
            "artifact_path": "independent_review/core_review.json",
        },
        "blockers": [],
    }


class AuthoringRecordContractTests(unittest.TestCase):
    def validate(
        self,
        record: dict,
        stage: str = "publish",
        artifact_overrides: dict | None = None,
        write_artifact: bool = True,
        artifact_stub: bool = False,
        package_legacy_tier: bool = False,
    ) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "authoring_record.json"
            path.write_text(json.dumps(record), encoding="utf-8")
            package_tests = Path(directory) / "candidate" / "tests"
            package_tests.mkdir(parents=True)
            tier_fields = (
                {"scoring_tier": "result_enhanced"}
                if package_legacy_tier
                else {"quality_tier": "RESULT_ENHANCED"}
            )
            (package_tests / "grading_spec.json").write_text(
                json.dumps(
                    {
                        **tier_fields,
                        "weights": {"gold": 0.7, "result_checks": 0.3},
                        "tolerance_contract": {"result": 0.01},
                    }
                ),
                encoding="utf-8",
            )
            if stage == "publish" and write_artifact:
                artifact_path = Path(directory) / record["independent_review"]["artifact_path"]
                artifact_path.parent.mkdir(parents=True, exist_ok=True)
                artifact = (
                    {
                        key: record["independent_review"][key]
                        for key in ("schema_version", "verdict", "quality_tier", "publishable")
                        if key in record["independent_review"]
                    }
                    if artifact_stub
                    else baseline_review(enhanced=True)
                )
                artifact.update(artifact_overrides or {})
                artifact_path.write_text(json.dumps(artifact), encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(VALIDATE_RECORD), str(path), "--stage", stage],
                check=False,
                capture_output=True,
                text=True,
            )

    def test_publish_consumes_review_v33_quality_tier(self) -> None:
        result = self.validate(enhanced_record())
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

        legacy = enhanced_record()
        legacy["independent_review"]["correctness_level"] = legacy[
            "independent_review"
        ].pop("quality_tier")
        result = self.validate(legacy)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("quality_tier", result.stdout)

    def test_publish_rejects_non_v33_review_artifact(self) -> None:
        record = enhanced_record()
        record["independent_review"]["schema_version"] = "materials-core-review/3.2"
        result = self.validate(record)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("materials-core-review/3.3", result.stdout)

    def test_publish_rejects_review_summary_artifact_mismatch(self) -> None:
        result = self.validate(
            enhanced_record(), artifact_overrides={"quality_tier": "BASELINE_CORRECT"}
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("artifact quality_tier", result.stdout)

    def test_publish_rejects_four_field_review_stub(self) -> None:
        result = self.validate(enhanced_record(), artifact_stub=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Review 3.3 validation failed", result.stdout)

    def test_publish_rejects_legacy_lowercase_scoring_tier(self) -> None:
        result = self.validate(enhanced_record(), package_legacy_tier=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("grading_spec.quality_tier", result.stdout)

    def test_publish_requires_readable_review_artifact(self) -> None:
        result = self.validate(enhanced_record(), write_artifact=False)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("review artifact", result.stdout)

    def test_publish_keeps_review_artifact_outside_candidate_package(self) -> None:
        record = enhanced_record()
        record["independent_review"]["artifact_path"] = "candidate/core_review.json"
        result = self.validate(record)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("outside the candidate package", result.stdout)

    def test_review_ready_record_passes_before_independent_review(self) -> None:
        record = enhanced_record()
        record["status"] = "READY_FOR_REVIEW"
        record["independent_review"] = {
            "schema_version": None,
            "verdict": None,
            "quality_tier": None,
            "publishable": False,
            "artifact_path": None,
        }
        result = self.validate(record, stage="review-ready")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_review_ready_requires_passing_oracle_evidence(self) -> None:
        record = enhanced_record()
        record["status"] = "READY_FOR_REVIEW"
        record["oracle_validation"] = {
            "purpose": "CHECKER_FULL_SCORE_FIXTURE",
            "scientific_execution_performed": False,
            "status": "PENDING",
            "command": "harbor run -p candidate -a oracle",
            "expected_reward": 1.0,
            "actual_reward": 0.0,
            "all_components_full_score": False,
            "evidence": [],
            "notes": [],
        }
        result = self.validate(record, stage="review-ready")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("oracle_validation.status must be PASS", result.stdout)
        self.assertIn("oracle_validation.actual_reward must be 1.0", result.stdout)
        self.assertIn("oracle_validation.all_components_full_score", result.stdout)
        self.assertIn("oracle_validation.evidence", result.stdout)

    def test_review_ready_requires_fixture_purpose_and_no_scientific_execution(self) -> None:
        record = enhanced_record()
        record["status"] = "READY_FOR_REVIEW"
        record["oracle_validation"]["purpose"] = "REFERENCE_EXECUTION"
        record["oracle_validation"]["scientific_execution_performed"] = True
        result = self.validate(record, stage="review-ready")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("purpose must be CHECKER_FULL_SCORE_FIXTURE", result.stdout)
        self.assertIn("scientific_execution_performed must be false", result.stdout)

    def test_package_path_may_have_solution_as_an_external_parent_name(self) -> None:
        record = enhanced_record()
        record["package_path"] = "solution/candidate"
        result = self.validate(record, stage="draft")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_output_path_cannot_escape_app_outputs(self) -> None:
        record = enhanced_record()
        record["output_contract"][0]["path"] = "/app/outputs/../escaped.json"
        result = self.validate(record, stage="draft")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("canonical path under /app/outputs", result.stdout)

    def test_checker_cost_hardware_fields_are_consistent(self) -> None:
        record = enhanced_record()
        record["checker_cost_record"].update(
            {"hardware_class": "GPU", "gpu_count": 1, "gpu_type": None}
        )
        result = self.validate(record, stage="review-ready")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("hardware_class", result.stdout)

        record["checker_cost_record"].update(
            {
                "hardware_class": "SINGLE_GPU",
                "gpu_type": "H100",
                "h100_equivalent_or_less": True,
            }
        )
        result = self.validate(record, stage="review-ready")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_checker_cost_measurements_must_be_complete_nonnegative_numbers(self) -> None:
        invalid_cases = (
            ("measured_wall_seconds", -1),
            ("measured_wall_seconds", True),
            ("peak_memory_mb", None),
            ("input_bytes_read", -1),
            ("cost_rationale", ""),
        )
        for field, value in invalid_cases:
            with self.subTest(field=field, value=value):
                record = enhanced_record()
                record["checker_cost_record"][field] = value
                result = self.validate(record, stage="review-ready")
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(field, result.stdout)


class AuthoringWorkspaceAndPackageTests(unittest.TestCase):
    def init_workspace(self, root: Path) -> Path:
        pdf = root / "paper.pdf"
        pdf.write_bytes(b"%PDF-1.4\n% authoring smoke fixture\n%%EOF\n")
        result = subprocess.run(
            [
                sys.executable,
                str(INIT_WORKSPACE),
                "--pdf",
                str(pdf),
                "--output-root",
                str(root / "processing"),
                "--paper-id",
                "paper-test",
                "--task-name",
                "org/test-task",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return root / "processing" / "paper-test"

    def run_init(self, root: Path, paper_id: str) -> subprocess.CompletedProcess[str]:
        pdf = root / "paper.pdf"
        pdf.write_bytes(b"%PDF-1.4\n%%EOF\n")
        return subprocess.run(
            [
                sys.executable,
                str(INIT_WORKSPACE),
                "--pdf",
                str(pdf),
                "--output-root",
                str(root / "processing"),
                "--paper-id",
                paper_id,
                "--task-name",
                "org/test-task",
            ],
            check=False,
            capture_output=True,
            text=True,
        )

    def make_complete_package(self, workspace: Path) -> Path:
        package = workspace / "candidate"
        headings = (
            "Problem background",
            "Approach",
            "Reproduction target",
            "Assets",
            "Workflow steps",
            "Output files",
            "Output contract",
            "How you are scored",
        )
        sections = ["# Scientific task"]
        for heading in headings:
            body = "Self-contained scientific contract."
            if heading == "Assets":
                body = "Use the bundled input.csv dataset."
            if heading in {"Output files", "Output contract"}:
                body = "Write result.json under /app/outputs."
            sections.extend((f"## {heading}", "", body))
        (package / "instruction.md").write_text("\n".join(sections) + "\n", encoding="utf-8")
        (package / "paper" / "paper.md").write_text("paper evidence " * 100, encoding="utf-8")
        (package / "steps.json").write_text(
            json.dumps([{"id": "step-1", "role": "scored"}]), encoding="utf-8"
        )
        resources_dir = package / "resources"
        resources_dir.mkdir()
        (resources_dir / "input.csv").write_text("x,y\n0,1\n", encoding="utf-8")
        (package / "resources.json").write_text(
            json.dumps(
                {
                    "version": 1,
                    "resources": [
                        {
                            "id": "input-data",
                            "name": "Input data",
                            "type": "dataset",
                            "access": {"method": "bundled", "filename": "input.csv"},
                        }
                    ],
                    "resources_mapping": [
                        {
                            "resource_type": "dataset",
                            "resource_unique_key": "authoring-test-input",
                        }
                    ],
                }
            ),
            encoding="utf-8",
        )
        (package / "tests" / "grading_spec.json").write_text(
            json.dumps(
                {
                    "quality_tier": "RESULT_ENHANCED",
                    "output_contract": [{"path": "/app/outputs/result.json"}],
                }
            ),
            encoding="utf-8",
        )
        record_path = workspace / "authoring_record.json"
        record = json.loads(record_path.read_text(encoding="utf-8"))
        record["resource_records"] = [
            {
                "resource_id": "input-data",
                "indispensable": True,
                "availability": "READY",
                "filename": "input.csv",
                "resource_type": "dataset",
            }
        ]
        record_path.write_text(json.dumps(record), encoding="utf-8")
        (package / "tests" / "checker.py").write_text(
            "#!/usr/bin/env python3\nprint(1.0)\n", encoding="utf-8"
        )
        solve_sh = package / "solution" / "solve.sh"
        solve_sh.write_text(
            "#!/usr/bin/env bash\n"
            "set -euo pipefail\n"
            "readonly OUTDIR=/app/outputs\n"
            "mkdir -p \"$OUTDIR\"\n"
            "# CHECKER_FULL_SCORE_FIXTURE\n"
            "python3 - \"$OUTDIR\" <<'PYEOF'\n"
            "import json, sys\n"
            "from pathlib import Path\n"
            "outdir = Path(sys.argv[1])\n"
            "(outdir / 'result.json').write_text(json.dumps({}) + '\\n')\n"
            "PYEOF\n",
            encoding="utf-8",
        )
        solve_sh.chmod(solve_sh.stat().st_mode | 0o100)
        return package

    def validate_package(self, package: Path, record: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(VALIDATE_PACKAGE),
                str(package),
                "--authoring-record",
                str(record),
            ],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_init_workspace_includes_oracle_solution_and_uses_v33_review_bridge(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            workspace = self.init_workspace(Path(directory))
            solve_sh = workspace / "candidate" / "solution" / "solve.sh"
            self.assertTrue(solve_sh.is_file())
            self.assertTrue(solve_sh.stat().st_mode & 0o100)
            self.assertEqual(
                sorted(path.name for path in solve_sh.parent.iterdir()),
                ["solve.sh"],
            )
            solve_text = solve_sh.read_text(encoding="utf-8")
            self.assertIn("CHECKER_FULL_SCORE_FIXTURE", solve_text)
            self.assertIn("python3 -", solve_text)
            record = json.loads((workspace / "authoring_record.json").read_text())
            self.assertIn("quality_tier", record["independent_review"])
            self.assertNotIn("correctness_level", record["independent_review"])
            self.assertTrue((workspace / "candidate" / "tests" / "test.sh").stat().st_mode & 0o100)

    def test_bundled_resource_mapping_passes_and_missing_key_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            workspace = self.init_workspace(Path(directory))
            package = self.make_complete_package(workspace)
            record = workspace / "authoring_record.json"
            result = self.validate_package(package, record)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

            resources_path = package / "resources.json"
            resources = json.loads(resources_path.read_text())
            resources["resources_mapping"][0].pop("resource_unique_key")
            resources_path.write_text(json.dumps(resources), encoding="utf-8")
            result = self.validate_package(package, record)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("mapping missing resource_unique_key", result.stdout)

    def test_inherited_assets_package_locator_is_accepted_and_safe(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            workspace = self.init_workspace(Path(directory))
            package = self.make_complete_package(workspace)
            source = package / "resources" / "input.csv"
            asset = package / "assets" / "source" / "input.csv"
            asset.parent.mkdir(parents=True)
            source.replace(asset)
            resources_path = package / "resources.json"
            resources = json.loads(resources_path.read_text())
            resources["resources"][0]["access"]["package"] = "assets/source/input.csv"
            resources_path.write_text(json.dumps(resources), encoding="utf-8")
            result = self.validate_package(package, workspace / "authoring_record.json")
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

            resources["resources"][0]["access"]["package"] = "../input.csv"
            resources_path.write_text(json.dumps(resources), encoding="utf-8")
            result = self.validate_package(package, workspace / "authoring_record.json")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("package locator is invalid or missing", result.stdout)

    def test_package_validator_requires_solution_script(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            workspace = self.init_workspace(Path(directory))
            package = self.make_complete_package(workspace)
            (package / "solution" / "solve.sh").unlink()
            result = self.validate_package(package, workspace / "authoring_record.json")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("missing required file: solution/solve.sh", result.stdout)

    def test_package_validator_rejects_placeholder_solution(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            workspace = self.init_workspace(Path(directory))
            package = self.make_complete_package(workspace)
            (package / "solution" / "solve.sh").write_text(
                "#!/usr/bin/env bash\n"
                "set -euo pipefail\n"
                "# CHECKER_FULL_SCORE_FIXTURE\n"
                "python3 - <<'PYEOF'\n"
                "raise SystemExit('TODO: materialize every declared standard correct output')\n"
                "PYEOF\n",
                encoding="utf-8",
            )
            result = self.validate_package(package, workspace / "authoring_record.json")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("solution/solve.sh is still the placeholder", result.stdout)

    def test_package_validator_requires_single_file_inline_python_fixture(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            workspace = self.init_workspace(Path(directory))
            package = self.make_complete_package(workspace)
            helper = package / "solution" / "generate.py"
            helper.write_text("print('not allowed')\n", encoding="utf-8")
            result = self.validate_package(package, workspace / "authoring_record.json")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("must contain exactly one entry", result.stdout)

            helper.unlink()
            solve_sh = package / "solution" / "solve.sh"
            solve_sh.write_text(
                "#!/usr/bin/env bash\n"
                "set -euo pipefail\n"
                "# CHECKER_FULL_SCORE_FIXTURE\n"
                "mkdir -p /app/outputs\n"
                "printf '{}\\n' > /app/outputs/result.json\n",
                encoding="utf-8",
            )
            result = self.validate_package(package, workspace / "authoring_record.json")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("must generate outputs with inline Python", result.stdout)

    def test_package_validator_rejects_checker_access_and_runtime_install(self) -> None:
        forbidden_cases = {
            "cat /tests/checker.py": "must not read /tests",
            "python3 -m pip install numpy": "must not install packages",
            "curl https://example.invalid": "must not access the network",
        }
        for command, expected in forbidden_cases.items():
            with self.subTest(command=command), tempfile.TemporaryDirectory() as directory:
                workspace = self.init_workspace(Path(directory))
                package = self.make_complete_package(workspace)
                solve_sh = package / "solution" / "solve.sh"
                solve_sh.write_text(
                    solve_sh.read_text(encoding="utf-8") + command + "\n",
                    encoding="utf-8",
                )
                result = self.validate_package(package, workspace / "authoring_record.json")
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(expected, result.stdout)

    def test_package_validator_rejects_copying_solution_into_environment(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            workspace = self.init_workspace(Path(directory))
            package = self.make_complete_package(workspace)
            dockerfile = package / "environment" / "Dockerfile"
            dockerfile.write_text(
                dockerfile.read_text(encoding="utf-8") + "COPY solution/ /solution/\n",
                encoding="utf-8",
            )
            result = self.validate_package(package, workspace / "authoring_record.json")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("do not copy the Harbor Oracle fixture", result.stdout)

    def test_init_rejects_unsafe_paper_id(self) -> None:
        for paper_id in ("../escape", "solution/x", "/absolute"):
            with self.subTest(paper_id=paper_id), tempfile.TemporaryDirectory() as directory:
                result = self.run_init(Path(directory), paper_id)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("--paper-id", result.stderr)

    def test_package_output_path_cannot_escape_app_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            workspace = self.init_workspace(Path(directory))
            package = self.make_complete_package(workspace)
            spec_path = package / "tests" / "grading_spec.json"
            spec = json.loads(spec_path.read_text())
            spec["output_contract"][0]["path"] = "/app/outputs/../escaped.json"
            spec_path.write_text(json.dumps(spec), encoding="utf-8")
            result = self.validate_package(package, workspace / "authoring_record.json")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("canonical path under /app/outputs", result.stdout)

    def test_authoring_resource_records_must_match_package_resources(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            workspace = self.init_workspace(Path(directory))
            package = self.make_complete_package(workspace)
            record_path = workspace / "authoring_record.json"
            record = json.loads(record_path.read_text())
            record["resource_records"][0]["filename"] = "other.csv"
            record_path.write_text(json.dumps(record), encoding="utf-8")
            result = self.validate_package(package, record_path)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("resource filename disagrees", result.stdout)

            record["resource_records"][0].pop("filename")
            record_path.write_text(json.dumps(record), encoding="utf-8")
            result = self.validate_package(package, record_path)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("resource filename is required", result.stdout)

    def test_resource_mapping_type_must_match_resource_type(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            workspace = self.init_workspace(Path(directory))
            package = self.make_complete_package(workspace)
            resources_path = package / "resources.json"
            resources = json.loads(resources_path.read_text())
            resources["resources_mapping"][0]["resource_type"] = "model"
            resources_path.write_text(json.dumps(resources), encoding="utf-8")
            result = self.validate_package(package, workspace / "authoring_record.json")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("mapping resource_type disagrees", result.stdout)


class AuthoringSkillPolicyTests(unittest.TestCase):
    def test_skill_commands_are_runnable_from_repository_root(self) -> None:
        skill = (AUTHORING / "SKILL.md").read_text(encoding="utf-8")
        command_root = ".cursor/skills/materials-benchmark-authoring/scripts/"
        for script in (
            "init_authoring_workspace.py",
            "validate_authoring_record.py",
            "validate_package.py",
        ):
            self.assertIn("python3 " + command_root + script, skill)
        self.assertNotIn("\npython " + command_root, skill)

    def test_missing_cif_is_not_an_asset_failure_by_itself(self) -> None:
        evidence = (AUTHORING / "references/paper-evidence-and-candidate-selection.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("A missing CIF is not an asset failure by itself", evidence)


if __name__ == "__main__":
    unittest.main()
