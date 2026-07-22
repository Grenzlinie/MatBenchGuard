"""Versioned schemas for the split Review/Repair artifact boundary.

This module is deliberately small and dependency-free.  Review and Repair
import the same constants so an artifact cannot be emitted under one version
and authenticated under another.
"""

from __future__ import annotations

from typing import Any


AUDIT_MANIFEST_SCHEMA_VERSION = "materials-audit-manifest/2.0"
AUDIT_BUNDLE_SCHEMA_VERSION = "materials-audit-bundle/2.0"
AUDIT_REPORT_SCHEMA_VERSION = "materials-audit-report/2.0"
IMPLEMENTATION_MANIFEST_SCHEMA_VERSION = (
    "materials-review-implementation-files/1.0"
)
IMPLEMENTATION_HASH_SCHEMA_VERSION = "materials-review-implementation/1.0"
DISPOSITION_SCHEMA_VERSION = "materials-audit-disposition/2.0"
CORPUS_INDEX_SCHEMA_VERSION = "materials-audit-index/2.0"
FINDINGS_SCHEMA_VERSION = "materials-audit-findings/2.0"
CHECKER_TESTS_SCHEMA_VERSION = "materials-checker-tests/2.0"
RESOURCE_CHECKS_SCHEMA_VERSION = "materials-resource-checks/2.0"
AGENT_ASSESSMENT_SCHEMA_VERSION = "materials-agent-assessment/2.0"
AGENT_CONTRACT_ASSESSMENT_SCHEMA_VERSION = (
    "materials-agent-contract-assessment/1.0"
)
AGENT_CONTRACT_REQUEST_SCHEMA_VERSION = (
    "materials-agent-contract-request/1.0"
)
EFFECTIVE_DETERMINISTIC_CONTRACT_SCHEMA_VERSION = (
    "materials-effective-deterministic-contract/1.0"
)
# Descriptive aliases keep the review-side seam discoverable without creating
# independent schema versions.
AGENT_CONTRACT_WIRING_SCHEMA_VERSION = (
    AGENT_CONTRACT_ASSESSMENT_SCHEMA_VERSION
)
AGENT_CONTRACT_WIRING_ASSESSMENT_SCHEMA_VERSION = (
    AGENT_CONTRACT_ASSESSMENT_SCHEMA_VERSION
)
EFFECTIVE_CONTRACT_SCHEMA_VERSION = (
    EFFECTIVE_DETERMINISTIC_CONTRACT_SCHEMA_VERSION
)
EFFECTIVE_CONTRACT_ARTIFACT_SCHEMA_VERSION = (
    EFFECTIVE_DETERMINISTIC_CONTRACT_SCHEMA_VERSION
)

DETERMINISTIC_CORE_ARTIFACT_SCHEMA_VERSION = (
    "materials-deterministic-core/2.0"
)
DETERMINISTIC_PROBE_RESULTS_SCHEMA_VERSION = (
    "materials-deterministic-probe-results/2.0"
)
AGENT_QUALITY_ARTIFACT_SCHEMA_VERSION = "materials-agent-quality/2.0"
QUALITY_PROBE_RESULTS_SCHEMA_VERSION = "materials-quality-probe-results/2.0"
REPAIR_FINDINGS_SCHEMA_VERSION = "materials-repair-findings/1.0"

DETERMINISTIC_CONTRACT_SCHEMA_VERSION = "materials-deterministic-contract/1.0"
DETERMINISTIC_REGISTRY_VERSION = "materials-deterministic-check-registry/1.0"
# Archival-only: historical bundles may retain this plan schema, but active
# Repair execution accepts only REPAIR_PLAN_SCHEMA_VERSION (2.0).
DETERMINISTIC_REPAIR_PLAN_SCHEMA_VERSION = (
    "materials-deterministic-repair-plan/1.0"
)
REPAIR_PLAN_SCHEMA_VERSION = "materials-repair-plan/2.0"
AGENT_REPAIR_ASSESSMENT_SCHEMA_VERSION = (
    "materials-agent-repair-assessment/1.0"
)
PUBLICATION_CLASSES = frozenset(
    {"DIRECT_DETERMINISTIC", "REAUDIT_REQUIRED"}
)

SCORING_SCHEMA_VERSION = "materials-review-scoring/2.0"
EVIDENCE_CONTRACT_SCHEMA_VERSION = "materials-evidence-contract/2.0"
AUDIT_ATTESTATION_SCHEMA_VERSION = "materials-audit-attestation/2.0"


def require_schema(value: Any, expected: str, context: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"{context} must be an object")
    if value.get("schema_version") != expected:
        raise ValueError(
            f"{context} schema_version must be {expected}"
        )
    return value
