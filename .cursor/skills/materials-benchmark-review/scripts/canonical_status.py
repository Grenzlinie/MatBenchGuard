"""Canonical review routing and repair lifecycle fields.

These fields deliberately model four different concerns:

* ``review_verdict`` is the quality assessment;
* ``publishability`` is the route consumed by publication tooling;
* ``repair_decision`` is the autonomous repair choice;
* ``repair_status`` is the repair lifecycle.
"""

from __future__ import annotations

import math
from typing import Any

from deterministic_contract import (
    DETERMINISTIC_REPAIR_PLAN_SCHEMA_ALIASES,
    LEGACY_REPAIR_PLAN_SCHEMA_VERSION,
)


REVIEW_VERDICTS = frozenset(
    {"PASS", "CONDITIONAL", "REJECT", "NOT_ASSESSABLE"}
)
PUBLISHABILITY_ROUTES = frozenset(
    {"PUBLISH_CANDIDATE", "REPAIR_QUEUE", "QUARANTINE", "EVIDENCE_PENDING"}
)
REPAIR_DECISIONS = frozenset(
    {"NOT_REQUIRED", "AUTO_FIX", "ASSISTED_FIX", "ABANDON"}
)
REPAIR_STATUSES = frozenset(
    {
        "NOT_APPLICABLE",
        # Review-time lifecycle state.  It routes a package to Repair but is
        # not a terminal outcome and never publishes a package.
        "DETERMINISTIC_REPAIR_REQUIRED",
        # ``PUBLISHED`` is retained only for the legacy certification archive.
        # The Repair skill now emits the batch four-state lifecycle below.
        "PUBLISHED",
        "REPAIRED",
        "PARTIALLY_REPAIRED",
        "ROLLED_BACK",
        "ABANDONED",
    }
)
# A repair that atomically publishes the fixed package.  ``REPAIRED`` is the
# batch-model success state; ``PUBLISHED`` is the legacy single-finding value.
SUCCESS_REPAIR_STATUSES = frozenset({"PUBLISHED", "REPAIRED"})
REPAIR_BUNDLE_FILES = (
    "repair_plan.json",
    "changes.json",
    "unresolved.json",
    "regression_results.json",
    "re_audit_comparison.json",
    "patch.json",
    "evidence.json",
    "repair.log",
    "history.json",
)

VERDICT_TO_PUBLISHABILITY = {
    "PASS": "PUBLISH_CANDIDATE",
    "CONDITIONAL": "REPAIR_QUEUE",
    "REJECT": "QUARANTINE",
    "NOT_ASSESSABLE": "EVIDENCE_PENDING",
}


def publishability_for_verdict(review_verdict: str) -> str:
    try:
        return VERDICT_TO_PUBLISHABILITY[review_verdict]
    except KeyError as exc:
        raise ValueError(f"invalid review_verdict: {review_verdict!r}") from exc


def canonical_fields(
    review_verdict: str,
    *,
    publishability: str | None = None,
    repair_decision: str = "NOT_REQUIRED",
    repair_status: str = "NOT_APPLICABLE",
) -> dict[str, str]:
    """Validate and return the four canonical fields.

    Publication routing always derives from the review verdict.  Repair
    lifecycle values may describe a failed or abandoned attempt without
    changing that source verdict.
    """

    expected_publishability = publishability_for_verdict(review_verdict)
    actual_publishability = publishability or expected_publishability
    if actual_publishability != expected_publishability:
        raise ValueError(
            "publishability does not match review_verdict: "
            f"{actual_publishability!r} != {expected_publishability!r}"
        )
    if repair_decision not in REPAIR_DECISIONS:
        raise ValueError(f"invalid repair_decision: {repair_decision!r}")
    if repair_status not in REPAIR_STATUSES:
        raise ValueError(f"invalid repair_status: {repair_status!r}")
    if repair_status == "NOT_APPLICABLE" and repair_decision != "NOT_REQUIRED":
        raise ValueError(
            "NOT_APPLICABLE repair_status requires NOT_REQUIRED decision"
        )
    if (
        repair_status == "DETERMINISTIC_REPAIR_REQUIRED"
        and repair_decision != "NOT_REQUIRED"
    ):
        raise ValueError(
            "DETERMINISTIC_REPAIR_REQUIRED requires NOT_REQUIRED decision"
        )
    if repair_status in {"PUBLISHED", "REPAIRED"} and repair_decision not in {
        "AUTO_FIX",
        "ASSISTED_FIX",
    }:
        raise ValueError(
            f"{repair_status} repair_status requires AUTO_FIX or ASSISTED_FIX"
        )
    if repair_status == "ABANDONED" and repair_decision != "ABANDON":
        raise ValueError("ABANDONED repair_status requires ABANDON decision")
    if repair_status in {"ROLLED_BACK", "PARTIALLY_REPAIRED"} and (
        repair_decision
        not in {
            "AUTO_FIX",
            "ASSISTED_FIX",
            "ABANDON",
        }
    ):
        raise ValueError(
            f"{repair_status} repair_status requires a repair decision"
        )
    return {
        "review_verdict": review_verdict,
        "publishability": actual_publishability,
        "repair_decision": repair_decision,
        "repair_status": repair_status,
    }


def require_canonical_fields(
    value: Any,
    *,
    expected_repair_decision: str | None = None,
    expected_repair_status: str | None = None,
) -> dict[str, str]:
    if not isinstance(value, dict):
        raise ValueError("canonical fields must be an object")
    fields = {
        name: value.get(name)
        for name in (
            "review_verdict",
            "publishability",
            "repair_decision",
            "repair_status",
        )
    }
    if any(
        not isinstance(item, str) or not item.strip()
        for item in fields.values()
    ):
        raise ValueError("canonical fields are incomplete")
    validated = canonical_fields(**fields)
    if (
        expected_repair_decision is not None
        and validated["repair_decision"] != expected_repair_decision
    ):
        raise ValueError("canonical repair_decision is inconsistent")
    if (
        expected_repair_status is not None
        and validated["repair_status"] != expected_repair_status
    ):
        raise ValueError("canonical repair_status is inconsistent")
    return validated


def validate_repair_bundle_semantics(
    values: dict[str, Any],
    *,
    repair_log: str,
) -> dict[str, str]:
    """Validate the fixed repair bundle's cross-file semantic schema."""

    missing = [name for name in REPAIR_BUNDLE_FILES if name not in values]
    if missing:
        raise ValueError(f"repair bundle semantic files are missing: {missing}")
    history = values["history.json"]
    fields = require_canonical_fields(history)
    plan = values["repair_plan.json"]
    changes = values["changes.json"]
    unresolved = values["unresolved.json"]
    regressions = values["regression_results.json"]
    comparison = values["re_audit_comparison.json"]
    patch = values["patch.json"]
    evidence = values["evidence.json"]
    if not isinstance(plan, dict) or not plan:
        raise ValueError("repair_plan.json must be a non-empty object")
    require_canonical_fields(
        plan,
        expected_repair_decision=fields["repair_decision"],
        expected_repair_status=fields["repair_status"],
    )
    if plan.get("schema_version") not in (
        {LEGACY_REPAIR_PLAN_SCHEMA_VERSION}
        | set(DETERMINISTIC_REPAIR_PLAN_SCHEMA_ALIASES)
    ):
        raise ValueError("repair_plan.json schema_version is invalid")
    # ``REPAIRED`` is the batch-model success state; ``PUBLISHED`` is the legacy
    # single-finding success value.  Both atomically publish the fixed package.
    published = fields["repair_status"] in SUCCESS_REPAIR_STATUSES
    batch_findings = plan.get("findings")
    is_batch = isinstance(batch_findings, list) and bool(batch_findings)
    required_plan_names = (
        ("audit_id",)
        if is_batch
        else ("audit_id", "finding_id", "justification")
    )
    for name in required_plan_names:
        if not isinstance(plan.get(name), str) or not plan[name].strip():
            raise ValueError(f"repair_plan.json requires {name}")
    if is_batch:
        plan_operations = [
            operation
            for finding in batch_findings
            if isinstance(finding, dict)
            for operation in finding.get("operations", [])
        ]
        plan_regressions = [
            specification
            for finding in batch_findings
            if isinstance(finding, dict)
            for specification in finding.get("regression_tests", [])
        ]
    else:
        plan_operations = plan.get("operations", [])
        plan_regressions = plan.get("regression_tests", [])
    if (
        published
        and not is_batch
        and plan.get("repair_class") != fields["repair_decision"]
    ):
        raise ValueError("repair_plan.json decision is inconsistent")
    if published and (
        not isinstance(plan_operations, list)
        or not plan_operations
        or not isinstance(plan_regressions, list)
        or not plan_regressions
    ):
        raise ValueError("repair_plan.json lacks repair operations or regressions")
    operation_ids = [
        item.get("id") for item in plan_operations
        if isinstance(item, dict)
    ]
    if (
        any(not isinstance(item, str) or not item for item in operation_ids)
        or len(set(operation_ids)) != len(operation_ids)
    ):
        raise ValueError("repair_plan.json operation IDs are invalid")
    if not isinstance(changes, list) or not all(
        isinstance(item, dict)
        and isinstance(item.get("operation_id"), str)
        and bool(item["operation_id"].strip())
        and isinstance(item.get("file"), str)
        and bool(item["file"].strip())
        and isinstance(item.get("operation"), str)
        and bool(item["operation"].strip())
        and (
            item.get("before_hash") is None
            or (
                isinstance(item.get("before_hash"), str)
                and bool(item["before_hash"].strip())
            )
        )
        and isinstance(item.get("after_hash"), str)
        and item["after_hash"].startswith("sha256:")
        and isinstance(item.get("evidence_ids"), list)
        and bool(item["evidence_ids"])
        for item in changes
    ):
        raise ValueError("changes.json semantic schema is invalid")
    if published and not changes:
        raise ValueError("changes.json is empty for a published repair")
    change_ids = [item["operation_id"] for item in changes]
    patch_files = patch.get("files") if isinstance(patch, dict) else None
    patch_ids = (
        [item.get("operation_id") for item in patch_files]
        if isinstance(patch_files, list)
        and all(isinstance(item, dict) for item in patch_files)
        else []
    )
    if (
        change_ids != patch_ids
        or len(set(change_ids)) != len(change_ids)
        or (
            operation_ids != change_ids
            if (published and not is_batch)
            else not set(change_ids).issubset(set(operation_ids))
        )
    ):
        raise ValueError("repair operation IDs differ across plan/changes/patch")
    if not isinstance(unresolved, list) or not all(
        isinstance(item, dict)
        and isinstance(item.get("finding_id"), str)
        and bool(item["finding_id"].strip())
        and isinstance(item.get("reason"), str)
        and bool(item["reason"].strip())
        for item in unresolved
    ):
        raise ValueError("unresolved.json semantic schema is invalid")
    if published and unresolved:
        raise ValueError("published repair has unresolved findings")
    if not published and not unresolved:
        raise ValueError("non-published repair lacks unresolved findings")
    if not isinstance(regressions, list) or not all(
        isinstance(item, dict)
        and isinstance(item.get("specification"), dict)
        and bool(item["specification"])
        and isinstance(item["specification"].get("id"), str)
        and bool(item["specification"]["id"].strip())
        and isinstance(item["specification"].get("type"), str)
        and bool(item["specification"]["type"].strip())
        and isinstance(item.get("before_passed"), bool)
        and isinstance(item.get("after_passed"), bool)
        for item in regressions
    ):
        raise ValueError("regression_results.json semantic schema is invalid")
    if published and not regressions:
        raise ValueError("regression_results.json is empty for a published repair")
    planned_regressions = plan_regressions
    planned_regression_ids = [
        item.get("id")
        for item in planned_regressions
        if isinstance(item, dict)
    ]
    result_regression_ids = [
        item["specification"].get("id") for item in regressions
    ]
    planned_regressions_by_id = {
        item["id"]: item for item in planned_regressions
    }
    if (
        len(set(planned_regression_ids)) != len(planned_regression_ids)
        or (
            planned_regression_ids != result_regression_ids
            if (published and not is_batch)
            else not set(result_regression_ids).issubset(
                set(planned_regression_ids)
            )
        )
    ):
        raise ValueError("regression IDs differ across plan and results")
    if any(
        item["specification"]
        != planned_regressions_by_id.get(item["specification"]["id"])
        for item in regressions
    ):
        raise ValueError("regression result specification differs from plan")
    for specification in planned_regressions:
        causal = specification.get("causal_operation_ids")
        if (
            not isinstance(causal, list)
            or not causal
            or len(set(causal)) != len(causal)
            or not set(causal).issubset(set(operation_ids))
        ):
            raise ValueError("regression causal operation IDs are invalid")
    if not isinstance(comparison, dict):
        raise ValueError("re_audit_comparison.json must be an object")
    if published and (
        comparison.get("target_resolved") is not True
        or not isinstance(comparison.get("reaudit_audit_id"), str)
        or not comparison["reaudit_audit_id"].strip()
        or not isinstance(comparison.get("source_finding"), dict)
        or not isinstance(comparison.get("source_configuration"), dict)
        or not isinstance(comparison.get("reaudit_configuration"), dict)
    ):
        raise ValueError("re_audit_comparison.json semantic schema is invalid")
    deterministic_plan = (
        plan.get("schema_version")
        in DETERMINISTIC_REPAIR_PLAN_SCHEMA_ALIASES
        or isinstance(plan.get("deterministic_contract"), dict)
    )
    if published and deterministic_plan:
        binding = plan.get("deterministic_contract")
        if (
            not isinstance(binding, dict)
            or not isinstance(binding.get("schema_version"), str)
            or not isinstance(binding.get("registry_version"), str)
            or not isinstance(binding.get("contract_digest"), str)
            or not binding["contract_digest"].startswith("sha256:")
            or not isinstance(binding.get("required_finding_ids"), list)
            or not binding["required_finding_ids"]
            or not all(
                isinstance(item, str) and item for item in binding["required_finding_ids"]
            )
            or len(binding["required_finding_ids"])
            != len(set(binding["required_finding_ids"]))
        ):
            raise ValueError("published deterministic plan binding is incomplete")
        planned_findings = plan.get("findings")
        if not isinstance(planned_findings, list) or [
            item.get("finding_id")
            for item in planned_findings
            if isinstance(item, dict)
        ] != sorted(binding["required_finding_ids"]):
            raise ValueError("published deterministic plan queue is incomplete")
        source_audit = plan.get("source_audit")
        if not isinstance(source_audit, dict):
            raise ValueError("published deterministic source audit is absent")
        if (
            source_audit.get("audit_id") != plan.get("audit_id")
            or source_audit.get("deterministic_contract") != binding
        ):
            raise ValueError("published deterministic source binding is stale")
    if published:
        required_comparison = {
            "reaudit_count": 1,
            "reaudit_verdict": "PASS",
            "publication_route": "PUBLISH_CANDIDATE",
            "deterministic_state": "CLEAN",
            "hard_gate_free": True,
            "evidence_contract_fail_closed": True,
            "evidence_contract_gaps": [],
            "hard_gate_codes": [
                "NON_MATERIALS_TASK",
                "SCIENTIFIC_TARGET_INVALID",
                "CHECKER_CORE_TASK_UNASSESSED",
                "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE",
            ],
            "hard_gate_statuses": ["PASS", "PASS", "PASS", "PASS"],
            "hard_gate_evidence": True,
            "identity_preserved": True,
            "mutation_scope_allowed": True,
            "target_resolved": True,
            "residual_blocking_finding_ids": [],
        }
        if any(
            comparison.get(key) != expected
            for key, expected in required_comparison.items()
        ):
            raise ValueError(
                "published repair does not satisfy the atomic publication invariant"
            )
        score = comparison.get("score")
        try:
            numeric_score = float(score)
        except (TypeError, ValueError, OverflowError):
            numeric_score = float("nan")
        if not math.isfinite(numeric_score) or not 80 <= numeric_score <= 100:
            raise ValueError(
                "published repair lacks a finite authoritative score >= 80"
            )
    if not isinstance(patch, dict) or (
        patch.get("schema_version") != "0.1"
        or patch.get("files") != changes
        or patch.get("atomic_publish") is not published
    ):
        raise ValueError("patch.json semantic schema is invalid")
    if not isinstance(evidence, list) or not evidence or not all(
        isinstance(item, dict)
        and isinstance(item.get("id", item.get("evidence_id")), str)
        and bool(item.get("id", item.get("evidence_id")).strip())
        and isinstance(item.get("source"), str)
        and bool(item["source"].strip())
        for item in evidence
    ):
        raise ValueError("evidence.json semantic schema is invalid")
    evidence_ids = [
        item.get("id", item.get("evidence_id")) for item in evidence
    ]
    referenced_evidence_ids = [
        evidence_id
        for change in changes
        for evidence_id in change["evidence_ids"]
    ]
    if (
        len(set(evidence_ids)) != len(evidence_ids)
        or (
            published
            and not is_batch
            and set(evidence_ids) != set(referenced_evidence_ids)
        )
        or (
            published
            and is_batch
            and not set(referenced_evidence_ids).issubset(set(evidence_ids))
        )
    ):
        raise ValueError("repair evidence IDs are missing, extra, or duplicated")
    audit_id = plan.get("audit_id")
    finding_id = plan.get("finding_id")
    package_identity = plan.get("package_identity")
    if not isinstance(package_identity, dict) or not package_identity:
        raise ValueError("repair package identity is absent")
    identity_values = [history]
    identity_values.extend(evidence)
    identity_values.extend(unresolved)
    if published:
        identity_values.extend(
            [comparison, comparison.get("source_finding", {})]
        )
    for item in identity_values:
        # Batch bundles bind identity on audit_id + package_identity because a
        # single batch resolves many findings; per-item finding_id is only bound
        # for the legacy single-finding bundle.
        if (
            item.get("audit_id") != audit_id
            or item.get("package_identity") != package_identity
            or (not is_batch and item.get("finding_id") != finding_id)
        ):
            raise ValueError(
                "repair audit/finding/package identities are inconsistent"
            )
    if not isinstance(history, dict) or not history:
        raise ValueError("history.json must be a non-empty object")
    if (
        history.get("bundle_complete") is not True
        or history.get("bundle_files") != list(REPAIR_BUNDLE_FILES)
        or not isinstance(history.get("root_cause"), str)
        or not history["root_cause"].strip()
        or not isinstance(history.get("attempt_number"), int)
        or isinstance(history.get("attempt_number"), bool)
        or history["attempt_number"] < 0
        or history.get("decision") != fields["repair_decision"]
        or (
            published
            and history.get("status") not in SUCCESS_REPAIR_STATUSES
        )
    ):
        raise ValueError("history.json semantic schema is invalid")
    if not isinstance(repair_log, str) or not repair_log.strip():
        raise ValueError("repair.log must be non-empty")
    if (
        f"decision={fields['repair_decision']}" not in repair_log
        or (
            f"status={fields['repair_status']}" not in repair_log
            and f"repair_status={fields['repair_status']}" not in repair_log
        )
    ):
        raise ValueError("repair.log lifecycle is inconsistent")
    return fields
