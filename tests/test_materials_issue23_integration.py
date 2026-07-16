from __future__ import annotations

import hashlib
import importlib.util
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
REVIEW_SCRIPTS = (
    REPO_ROOT
    / ".cursor"
    / "skills"
    / "materials-benchmark-review"
    / "scripts"
)
REPAIR_SCRIPT = (
    REPO_ROOT
    / ".cursor"
    / "skills"
    / "materials-benchmark-repair"
    / "scripts"
    / "run_repair.py"
)
SOURCE_PACKAGE = (
    REPO_ROOT
    / "materials_science_questions"
    / "cluster-18137"
    / "compute-sound-velocities-and-debye-temperature-from-elastic-data"
    / "paper-814614162100453378"
)
FIVE_PROBE_CLASSES = {
    "positive",
    "negative",
    "discrimination",
    "equivalence",
    "component_isolation",
}

if str(REVIEW_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(REVIEW_SCRIPTS))

import audit_package  # noqa: E402
import dynamic_checker_probe  # noqa: E402
import finalize_audit_output  # noqa: E402
import prepare_audit_output  # noqa: E402
import run_fast_e1_batch  # noqa: E402
import run_review  # noqa: E402


def load_repair_module():
    spec = importlib.util.spec_from_file_location("issue23_repair", REPAIR_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load integrated Repair")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def copy_source_package(destination: Path) -> None:
    shutil.copytree(
        SOURCE_PACKAGE,
        destination,
        ignore=shutil.ignore_patterns("solution"),
    )
    (destination / "solution").mkdir()


def file_hash(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


class MaterialsIssue23IntegrationTests(unittest.TestCase):
    def test_e1_runtime_provenance_and_five_class_paper_routing(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / SOURCE_PACKAGE.name
            copy_source_package(package)
            run_review.run_review(package, None, paper_mode="no_paper")
            report = json.loads(
                (package / "benchmark_audit/audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            checker = json.loads(
                (package / "benchmark_audit/checker_tests.json").read_text(
                    encoding="utf-8"
                )
            )

        self.assertEqual(set(checker["probe_coverage"]), FIVE_PROBE_CLASSES)
        self.assertEqual(
            checker["runtime"]["verifier_entrypoint"], "tests/test.sh"
        )
        self.assertIn(
            checker["runtime"]["runtime_provenance"],
            {"Harbor-equivalent", "audit-host-copy", "not-assessable"},
        )
        self.assertEqual(
            report["execution_evidence"]["claim"], "E1_CHECKER_ONLY"
        )
        self.assertFalse(report["execution_evidence"]["scientific_reproduction"])
        self.assertEqual(report["summary"]["route"], "PAPER_GROUNDED_E1")

    def test_process_exclusion_core_escalation_and_four_qa_axes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / SOURCE_PACKAGE.name
            copy_source_package(package)
            (package / "instruction.md").write_text(
                """
### Step 1: Build the complete crystal structure model
- Role: process
- Action: Return the complete load-bearing crystal structure.
- Evidence: `/app/outputs/structure.cif`

### Step 2: Save an intermediate audit log
- Role: process
- Action: Save the process log.
- Evidence: `/app/outputs/process.log`
""",
                encoding="utf-8",
            )
            static = audit_package.static_audit(
                package, Path(temporary) / "static.json"
            )

        contract_map = static["contract_map"]
        self.assertIn("structure.cif", contract_map["core_outputs"])
        self.assertEqual(contract_map["process_evidence"], ["process.log"])
        self.assertIn(
            "CHECKER_CORE_TASK_UNASSESSED",
            {item["code"] for item in static["issues"]},
        )
        self.assertEqual(
            set(finalize_audit_output.QA_AXIS_NAMES),
            {
                "factual_accuracy",
                "answer_leakage",
                "instruction_completeness",
                "checker_instruction_consistency",
            },
        )

    def test_review_digest_is_complete_and_repair_accepts_it(self) -> None:
        repair = load_repair_module()
        canonical = set(prepare_audit_output.review_implementation_files())
        self.assertTrue(
            {
                "scripts/probe_resources.py",
                "scripts/run_fast_e1_batch.py",
                "scripts/dynamic_checker_probe.py",
                "references/materials-taxonomy.json",
            }.issubset(canonical)
        )
        self.assertEqual(
            prepare_audit_output.collect_review_implementation_hashes(),
            repair.collect_review_implementation_hashes(),
        )

    def test_source_bound_fixture_satisfies_review_and_repair(self) -> None:
        repair = load_repair_module()
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / SOURCE_PACKAGE.name
            copy_source_package(package)
            specification = json.loads(
                (package / "tests/grading_spec.json").read_text(
                    encoding="utf-8"
                )
            )
            fixture = workspace / "known-valid-output"
            fixture.mkdir()
            output_names = {
                Path(str(item["file"])).name
                for item in specification["output_contract"]["outputs"]
            }
            for name in output_names:
                (fixture / name).write_text("independent fixture\n")
            source_roles = {
                role: file_hash(package / role)
                for role in dynamic_checker_probe.QUALITY_EVIDENCE_ROLES
                if (package / role).is_file()
            }
            fixture_hashes = {
                name: file_hash(fixture / name) for name in sorted(output_names)
            }
            (fixture / "fixture_manifest.json").write_text(
                json.dumps(
                    {
                        "schema_version": (
                            "materials-known-valid-fixture/1.0"
                        ),
                        "source_kind": "INDEPENDENT_PUBLIC_FIXTURE",
                        "public": True,
                        "oracle_used": False,
                        "source_role_hashes": source_roles,
                        "fixture_hashes": fixture_hashes,
                    }
                ),
                encoding="utf-8",
            )
            review_binding = dynamic_checker_probe.validate_known_valid_fixture(
                package, fixture, specification
            )
            fixture_digest = repair.sha256_path(fixture)
            repair_binding, assessment_binding = repair.external_binding_hashes(
                package,
                {"known_valid_output": str(fixture)},
                {
                    "fixture_hashes": {
                        "known_valid_output": fixture_digest
                    },
                    "assessment_hashes": {},
                },
            )

        self.assertEqual(
            review_binding["source_kind"], "INDEPENDENT_PUBLIC_FIXTURE"
        )
        self.assertFalse(review_binding["oracle_used"])
        self.assertEqual(
            repair_binding["known_valid_output"], fixture_digest
        )
        self.assertEqual(assessment_binding, {})

    def test_direct_input_hard_gate_propagates_to_batch_state(self) -> None:
        codes = run_review.pre_paper_hard_gate_codes(
            {
                "issues": [
                    {"code": "UNRECOVERABLE_TASK_DEFINITION"},
                    {"code": "CHECKER_CORE_TASK_UNASSESSED"},
                ]
            },
            {"findings": [{"code": "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE"}]},
            {"classification": "NON_MAT"},
        )
        self.assertEqual(
            codes,
            [
                "NON_MATERIALS_TASK",
                "UNRECOVERABLE_TASK_DEFINITION",
                "CHECKER_CORE_TASK_UNASSESSED",
                "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE",
            ],
        )
        gates = [{"code": code, "status": "FAIL"} for code in codes]
        reasons = run_fast_e1_batch.hard_gate_exclusion_reasons(gates)
        self.assertEqual(
            reasons,
            [f"HARD_GATE_{code}" for code in codes],
        )
        scoring = {"execution_level": "E1", "hard_gates": gates}
        with self.assertRaisesRegex(
            ValueError, "failed Hard Gate cannot be a usable candidate"
        ):
            run_fast_e1_batch.validate_authoritative_candidate_state(
                {"state": "E1_USABLE_CANDIDATE", "exclusion_reasons": []},
                scoring,
            )
        run_fast_e1_batch.validate_authoritative_candidate_state(
            {
                "state": "E1_EXCLUDED",
                "exclusion_reasons": reasons,
            },
            scoring,
        )

    def test_repair_reaudit_invokes_integrated_review_at_e1(self) -> None:
        repair = load_repair_module()
        with tempfile.TemporaryDirectory() as temporary:
            candidate = Path(temporary) / "candidate"
            audit = candidate / "benchmark_audit"
            audit.mkdir(parents=True)
            report = {
                "configuration": {
                    "paper_mode": "no_paper",
                    "execution_level": "E1",
                }
            }
            (audit / "audit_report.json").write_text(
                json.dumps(report), encoding="utf-8"
            )
            with mock.patch.object(
                repair.subprocess,
                "run",
                return_value=repair.subprocess.CompletedProcess(
                    [], 0, "", ""
                ),
            ) as run:
                repair.run_equal_depth_review(
                    candidate,
                    report,
                    {"fixture_hashes": {}, "assessment_hashes": {}},
                    {},
                )

        command = run.call_args.args[0]
        self.assertIn("--paper-mode", command)
        self.assertEqual(command[command.index("--paper-mode") + 1], "no_paper")
        self.assertIn("--execution-level", command)
        self.assertEqual(
            command[command.index("--execution-level") + 1], "E1"
        )


if __name__ == "__main__":
    unittest.main()
