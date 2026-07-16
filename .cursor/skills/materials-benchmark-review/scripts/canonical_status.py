"""Canonical review routing and repair lifecycle fields.

These fields deliberately model four different concerns:

* ``review_verdict`` is the quality assessment;
* ``publishability`` is the route consumed by publication tooling;
* ``repair_decision`` is the autonomous repair choice;
* ``repair_status`` is the repair lifecycle.
"""

from __future__ import annotations

from typing import Any


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
    {"NOT_APPLICABLE", "PUBLISHED", "ROLLED_BACK", "ABANDONED"}
)
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
    if repair_status == "PUBLISHED" and repair_decision not in {
        "AUTO_FIX",
        "ASSISTED_FIX",
    }:
        raise ValueError(
            "PUBLISHED repair_status requires AUTO_FIX or ASSISTED_FIX"
        )
    if repair_status == "ABANDONED" and repair_decision != "ABANDON":
        raise ValueError("ABANDONED repair_status requires ABANDON decision")
    if repair_status == "ROLLED_BACK" and repair_decision not in {
        "AUTO_FIX",
        "ASSISTED_FIX",
        "ABANDON",
    }:
        raise ValueError(
            "ROLLED_BACK repair_status requires a repair decision"
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
    if plan.get("schema_version") != "0.1":
        raise ValueError("repair_plan.json schema_version is invalid")
    for name in ("audit_id", "finding_id", "justification"):
        if not isinstance(plan.get(name), str) or not plan[name].strip():
            raise ValueError(f"repair_plan.json requires {name}")
    if (
        fields["repair_status"] == "PUBLISHED"
        and plan.get("repair_class") != fields["repair_decision"]
    ):
        raise ValueError("repair_plan.json decision is inconsistent")
    if fields["repair_status"] == "PUBLISHED" and (
        not isinstance(plan.get("operations"), list)
        or not plan["operations"]
        or not isinstance(plan.get("regression_tests"), list)
        or not plan["regression_tests"]
    ):
        raise ValueError("repair_plan.json lacks repair operations or regressions")
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
    if fields["repair_status"] == "PUBLISHED" and not changes:
        raise ValueError("changes.json is empty for a published repair")
    if not isinstance(unresolved, list) or not all(
        isinstance(item, dict)
        and isinstance(item.get("finding_id"), str)
        and bool(item["finding_id"].strip())
        and isinstance(item.get("reason"), str)
        and bool(item["reason"].strip())
        for item in unresolved
    ):
        raise ValueError("unresolved.json semantic schema is invalid")
    if fields["repair_status"] == "PUBLISHED" and unresolved:
        raise ValueError("published repair has unresolved findings")
    if fields["repair_status"] != "PUBLISHED" and not unresolved:
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
    if fields["repair_status"] == "PUBLISHED" and not regressions:
        raise ValueError("regression_results.json is empty for a published repair")
    if not isinstance(comparison, dict):
        raise ValueError("re_audit_comparison.json must be an object")
    if fields["repair_status"] == "PUBLISHED" and (
        comparison.get("target_resolved") is not True
        or not isinstance(comparison.get("reaudit_audit_id"), str)
        or not comparison["reaudit_audit_id"].strip()
        or not isinstance(comparison.get("source_finding"), dict)
        or not isinstance(comparison.get("source_configuration"), dict)
        or not isinstance(comparison.get("reaudit_configuration"), dict)
    ):
        raise ValueError("re_audit_comparison.json semantic schema is invalid")
    if not isinstance(patch, dict) or (
        patch.get("schema_version") != "0.1"
        or patch.get("files") != changes
        or patch.get("atomic_publish")
        is not (fields["repair_status"] == "PUBLISHED")
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
            fields["repair_status"] == "PUBLISHED"
            and history.get("status") != "PUBLISHED"
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
