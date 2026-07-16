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
    if any(not isinstance(item, str) for item in fields.values()):
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
