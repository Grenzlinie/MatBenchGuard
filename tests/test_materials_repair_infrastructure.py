from __future__ import annotations

import importlib.util
import json
import sys
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
            "attestation-control",
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

    def test_removed_fixture_lineage_api_cannot_reenter_repair(self) -> None:
        module = repair_module()
        self.assertFalse(hasattr(module, "rebound_known_valid_fixture"))
        self.assertFalse(hasattr(dynamic_checker_probe, "fixture_hashes"))
        self.assertFalse(
            hasattr(dynamic_checker_probe, "validate_known_valid_fixture")
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
