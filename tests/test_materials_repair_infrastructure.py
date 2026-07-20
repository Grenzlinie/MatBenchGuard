from __future__ import annotations

import importlib.util
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
REVIEW_SCRIPTS = (
    REPO_ROOT
    / ".cursor"
    / "skills"
    / "materials-benchmark-review"
    / "scripts"
)
REPAIR_RUNNER = (
    REPO_ROOT
    / ".cursor"
    / "skills"
    / "materials-benchmark-repair"
    / "scripts"
    / "run_repair.py"
)
if str(REVIEW_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(REVIEW_SCRIPTS))

import dynamic_checker_probe  # noqa: E402


def repair_module() -> Any:
    spec = importlib.util.spec_from_file_location(
        "repair_infrastructure", REPAIR_RUNNER
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


class MaterialsRepairInfrastructureTests(unittest.TestCase):
    def test_control_breaker_separates_transient_and_deterministic_failures(
        self,
    ) -> None:
        module = repair_module()
        prior = [
            (
                Path("/history/one"),
                {"control_failure_fingerprint": "different-one"},
            ),
            (
                Path("/history/two"),
                {"control_failure_fingerprint": "different-two"},
            ),
        ]

        same_twice = module.control_failure_decision(
            [
                (
                    Path("/history/one"),
                    {"control_failure_fingerprint": "same"},
                )
            ],
            "same",
            transient=True,
        )
        rotating_third = module.control_failure_decision(
            prior,
            "different-three",
            transient=True,
        )
        deterministic = module.control_failure_decision(
            [],
            "fixture-lineage",
            transient=False,
        )

        self.assertTrue(same_twice["blocked"])
        self.assertEqual(same_twice["same_fingerprint"], 2)
        self.assertTrue(rotating_third["blocked"])
        self.assertEqual(rotating_third["number"], 3)
        self.assertTrue(deterministic["blocked"])
        self.assertFalse(
            module.control_failure_retryable(
                ValueError("source-audit attestation is invalid")
            )
        )
        self.assertTrue(
            module.control_failure_retryable(
                RuntimeError("Docker daemon is temporarily unavailable")
            )
        )

    def test_candidate_fixture_lineage_preserves_public_bytes(self) -> None:
        module = repair_module()
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            snapshot = workspace / "snapshot"
            candidate = workspace / "candidate"
            fixture = workspace / "public-fixture"
            for root in (snapshot, fixture):
                root.mkdir()
            (snapshot / "tests").mkdir()
            (snapshot / "instruction.md").write_text(
                "Public task.\n", encoding="utf-8"
            )
            (snapshot / "tests/checker.py").write_text(
                "def score():\n    pass\n", encoding="utf-8"
            )
            (snapshot / "tests/test.sh").write_text(
                "#!/bin/sh\n", encoding="utf-8"
            )
            specification = {
                "output_contract": {
                    "outputs": [{"file": "result.json", "format": "json"}]
                }
            }
            write_json(snapshot / "tests/grading_spec.json", specification)
            (fixture / "result.json").write_text(
                '{"value": 1}\n', encoding="utf-8"
            )
            source_hashes = {
                role: dynamic_checker_probe.sha256_file(snapshot / role)
                for role in sorted(
                    dynamic_checker_probe.QUALITY_EVIDENCE_ROLES
                )
                if (snapshot / role).is_file()
            }
            fixture_hashes = dynamic_checker_probe.fixture_hashes(
                fixture, specification
            )
            write_json(
                fixture / dynamic_checker_probe.FIXTURE_MANIFEST_NAME,
                {
                    "schema_version": (
                        dynamic_checker_probe.FIXTURE_MANIFEST_SCHEMA
                    ),
                    "source_kind": "INDEPENDENT_PUBLIC_FIXTURE",
                    "public": True,
                    "oracle_used": False,
                    "source_role_hashes": source_hashes,
                    "fixture_hashes": fixture_hashes,
                },
            )
            shutil.copytree(snapshot, candidate)
            (candidate / "tests/checker.py").write_text(
                "def score():\n    return 1.0\n", encoding="utf-8"
            )

            derived = module.rebound_known_valid_fixture(
                candidate, fixture, {"audit_id": "audit-source"}
            )
            provenance = dynamic_checker_probe.validate_known_valid_fixture(
                candidate, derived, specification
            )

            self.assertEqual(
                (derived / "result.json").read_bytes(),
                (fixture / "result.json").read_bytes(),
            )
            lineage = provenance["repair_reaudit_lineage"]
            self.assertTrue(lineage["fixture_bytes_preserved"])
            self.assertEqual(lineage["source_audit_id"], "audit-source")
            self.assertEqual(
                lineage["changed_source_roles"], ["tests/checker.py"]
            )

            (derived / "result.json").write_text(
                '{"value": 2}\n', encoding="utf-8"
            )
            with self.assertRaisesRegex(ValueError, "lineage"):
                dynamic_checker_probe.validate_known_valid_fixture(
                    candidate, derived, specification
                )

    def test_residual_reporting_uses_blockers_and_stable_identity(self) -> None:
        module = repair_module()
        blocker = {
            "finding_id": "FINDING-002",
            "title": "ADVERSARIAL_OUTPUT_PASSES",
            "deterministic_check": "D6",
            "severity": "HIGH",
            "blocking": True,
            "affected_files": ["tests/checker.py"],
            "evidence": {"root_cause": "single_component_bypass"},
        }
        advisory = {
            "finding_id": "FINDING-001",
            "title": "SINGLE_COMPONENT_THRESHOLD_REACHABLE",
            "deterministic_check": "D4",
            "severity": "MEDIUM",
            "blocking": False,
        }

        references = module.blocking_finding_references(
            [advisory, blocker], audit_id="audit-2"
        )
        renamed = dict(blocker, finding_id="FINDING-099")
        renamed_reference = module.finding_reference(
            renamed, audit_id="audit-3"
        )

        self.assertEqual(len(references), 1)
        self.assertEqual(
            references[0]["finding_code"], "ADVERSARIAL_OUTPUT_PASSES"
        )
        self.assertEqual(
            references[0]["finding_fingerprint"],
            renamed_reference["finding_fingerprint"],
        )


if __name__ == "__main__":
    unittest.main()
