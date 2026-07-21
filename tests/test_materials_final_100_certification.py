from __future__ import annotations

import json
import sys
import unittest


from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / ".cursor/skills/materials-benchmark-review/scripts"
sys.path.insert(0, str(SCRIPTS))

import artifact_schema  # noqa: E402
import certify_final_100  # noqa: E402


def dimensions() -> list[dict[str, object]]:
    return [
        {
            "dimension": name,
            "weight": weight,
            "max_points": weight,
            "points_earned": weight,
            "normalized": 100,
            "status": "PASS",
        }
        for name, weight in (
            ("C01", 10),
            ("C02", 20),
            ("C03", 20),
            ("C04", 20),
            ("C05", 10),
            ("C06", 10),
            ("C07", 10),
        )
    ]


def hard_gates() -> list[dict[str, object]]:
    return [
        {
            "code": code,
            "status": "PASS",
            "evidence": [{"fact": "gate assessed"}],
            "affected_locations": [
                {"file": "instruction.md", "line": 1, "quote": "task"}
            ],
        }
        for code in (
            "NON_MATERIALS_TASK",
            "SCIENTIFIC_TARGET_INVALID",
            "CHECKER_CORE_TASK_UNASSESSED",
            "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE",
        )
    ]


def probe_coverage() -> dict[str, object]:
    unavailable = {
        "status": "NOT_ASSESSABLE",
        "reason": "Agent-quality evidence was not supplied.",
        "provenance": {
            "source_kind": "NONE",
            "oracle_used": False,
            "external_result_directory_accepted": False,
        },
    }
    return {
        "positive": {
            "status": "ASSESSED",
            "provenance": {
                "source_kinds": ["ORACLE_POSITIVE_MOCK"],
                "oracle_used": True,
                "oracle_scientific_evidence": False,
            },
        },
        "negative": {
            "status": "ASSESSED",
            "provenance": {
                "source_kind": "SCHEMA_SHAPED_SYNTHETIC_ATTACKS",
                "oracle_used": False,
            },
        },
        "discrimination": unavailable,
        "equivalence": unavailable,
        "component_isolation": unavailable,
    }


class MaterialsFinal100CertificationTests(unittest.TestCase):
    def test_v2_dimensions_and_score_snapshot_are_self_consistent(self) -> None:
        dims = dimensions()
        report = {
            "summary": {
                "scoring_version": artifact_schema.SCORING_SCHEMA_VERSION,
                "total_score": 100,
            },
            "dimensions_v11": dims,
            "hard_gates": hard_gates(),
        }
        snapshot = {
            "scoring_version": artifact_schema.SCORING_SCHEMA_VERSION,
            "total_score": 100,
            "final_verdict": "PASS",
            "dimensions_v11": dims,
            "hard_gates": report["hard_gates"],
        }
        snapshot["snapshot_hash"] = certify_final_100.canonical_json_hash(
            snapshot
        )

        certify_final_100.validate_dimensions(report)
        certify_final_100.validate_score(report, snapshot)
        certify_final_100.validate_hard_gates(report)


    def test_legacy_scoring_schema_is_rejected(self) -> None:
        with self.assertRaisesRegex(
            ValueError, artifact_schema.AUDIT_REPORT_SCHEMA_VERSION
        ):
            artifact_schema.require_schema(
                {"schema_version": "materials-review-scoring/1.0"},
                artifact_schema.AUDIT_REPORT_SCHEMA_VERSION,
                "legacy artifact",
            )


if __name__ == "__main__":
    unittest.main()
