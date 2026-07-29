#!/usr/bin/env python3
"""Validate the compact Agent-led repair record and its equal-depth re-audit."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
from typing import Any

SCHEMA = "materials-agent-repair-report/1.2"
OUTCOMES = {"REPAIRED", "PARTIALLY_REPAIRED", "ABANDONED", "ROLLED_BACK"}
DECISIONS = {"AUTO_FIX", "ASSISTED_FIX", "ABANDON"}
FRESH_REVIEW_STATUSES = {"COMPLETE", "INCOMPLETE"}


def _text(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be non-empty text")
    return value.strip()


def _review_validator():
    path = (
        Path(__file__).resolve().parents[2]
        / "materials-benchmark-review/scripts/validate_agent_decision.py"
    )
    spec = importlib.util.spec_from_file_location("materials_review_decision", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load Review decision validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _path_list(value: Any, label: str) -> list[str]:
    if not isinstance(value, list) or not value:
        raise ValueError(f"{label} must be a non-empty list")
    return [_text(item, f"{label}[{index}]") for index, item in enumerate(value)]


def _status_evidence(value: Any, statuses: set[str], label: str) -> dict[str, str]:
    if not isinstance(value, dict) or value.get("status") not in statuses:
        raise ValueError(f"{label}.status is invalid")
    return {
        "status": value["status"],
        "evidence": _text(value.get("evidence"), f"{label}.evidence"),
    }


def validate(value: Any, *, report_path: Path | None = None) -> dict[str, Any]:
    if not isinstance(value, dict) or value.get("schema_version") != SCHEMA:
        raise ValueError(f"repair report schema_version must be {SCHEMA}")
    for field in (
        "source_package",
        "candidate_package",
        "source_decision",
        "reaudit_decision",
    ):
        _text(value.get(field), field)
    if value.get("outcome") not in OUTCOMES or not isinstance(
        value.get("publishable"), bool
    ):
        raise ValueError("invalid outcome or publishable")
    if "author_self_check" in value:
        raise ValueError("author_self_check is forbidden because solution/ is out of scope")
    targets = value.get("targets")
    changes = value.get("changes")
    regressions = value.get("regressions")
    unresolved = value.get("unresolved_findings")
    source_probe_paths = _path_list(
        value.get("source_probe_observations"),
        "source_probe_observations",
    )
    candidate_probe_paths = _path_list(
        value.get("candidate_probe_observations"),
        "candidate_probe_observations",
    )
    fresh_review = _status_evidence(
        value.get("fresh_review"),
        FRESH_REVIEW_STATUSES,
        "fresh_review",
    )
    impact_matrix = value.get("impact_matrix")
    if (
        not isinstance(targets, list)
        or not targets
        or not isinstance(changes, list)
        or not isinstance(regressions, list)
        or not isinstance(unresolved, list)
    ):
        raise ValueError(
            "targets/changes/regressions/unresolved_findings must be lists"
        )
    if not isinstance(impact_matrix, list):
        raise ValueError("impact_matrix must be a list")
    target_ids: set[str] = set()
    for index, item in enumerate(targets):
        if not isinstance(item, dict):
            raise ValueError(f"targets[{index}] must be an object")
        target_id = _text(item.get("finding_id"), f"targets[{index}].finding_id")
        if target_id in target_ids or item.get("decision") not in DECISIONS:
            raise ValueError("target IDs must be unique and decisions valid")
        target_ids.add(target_id)
        _text(item.get("rationale"), f"targets[{index}].rationale")
        if not isinstance(item.get("resolved"), bool):
            raise ValueError(f"targets[{index}].resolved must be boolean")
    for index, item in enumerate(changes):
        if not isinstance(item, dict) or item.get("finding_id") not in target_ids:
            raise ValueError(f"changes[{index}] must bind a target")
        for field in ("path", "before_sha256", "after_sha256", "evidence"):
            _text(item.get(field), f"changes[{index}].{field}")
        normalized = item["path"].replace("\\", "/").lstrip("./")
        if normalized == "solution" or normalized.startswith("solution/"):
            raise ValueError(f"changes[{index}].path must not reference solution/")
    for index, item in enumerate(regressions):
        if not isinstance(item, dict) or item.get("finding_id") not in target_ids:
            raise ValueError(f"regressions[{index}] must bind a target")
        if (
            item.get("before_passed") is not False
            or item.get("after_passed") is not True
        ):
            raise ValueError(f"regressions[{index}] must fail before and pass after")
        _text(item.get("specification"), f"regressions[{index}].specification")
    impact_targets: set[str] = set()
    for index, item in enumerate(impact_matrix):
        if not isinstance(item, dict) or item.get("finding_id") not in target_ids:
            raise ValueError(f"impact_matrix[{index}] must bind a target")
        finding_id = item["finding_id"]
        if finding_id in impact_targets:
            raise ValueError("impact_matrix finding IDs must be unique")
        impact_targets.add(finding_id)
        affected_paths = _path_list(
            item.get("affected_paths"),
            f"impact_matrix[{index}].affected_paths",
        )
        if any(
            (normalized := path.replace("\\", "/").lstrip("./")) == "solution"
            or normalized.startswith("solution/")
            for path in affected_paths
        ):
            raise ValueError(
                f"impact_matrix[{index}].affected_paths must not reference solution/"
            )
        _text(item.get("rationale"), f"impact_matrix[{index}].rationale")
        if not isinstance(item.get("synchronized"), bool):
            raise ValueError(f"impact_matrix[{index}].synchronized must be boolean")

    if report_path is not None:
        source_path = Path(value["source_decision"])
        if not source_path.is_absolute():
            source_path = report_path.parent / source_path
        re_path = Path(value["reaudit_decision"])
        if not re_path.is_absolute():
            re_path = report_path.parent / re_path
        review_validator = _review_validator()
        source_value = json.loads(source_path.read_text(encoding="utf-8"))
        review_validator.validate(source_value)
        re_value = json.loads(re_path.read_text(encoding="utf-8"))
        review_validator.validate(re_value)

        def resolve_many(paths: list[str]) -> list[Path]:
            return [
                path if path.is_absolute() else report_path.parent / path
                for path in map(Path, paths)
            ]

        review_validator.validate_probe_observations(
            source_value,
            resolve_many(source_probe_paths),
        )
        review_validator.validate_probe_observations(
            re_value,
            resolve_many(candidate_probe_paths),
        )
        if value.get("reaudit_verdict") != re_value.get("verdict"):
            raise ValueError("reaudit_verdict does not match validated decision")
    verdict = value.get("reaudit_verdict")
    outcome = value["outcome"]
    expected = (
        "REPAIRED"
        if verdict == "PASS"
        and targets
        and all(x.get("resolved") for x in targets)
        and not unresolved
        else "PARTIALLY_REPAIRED"
        if verdict == "CONDITIONAL"
        else "ABANDONED"
        if verdict == "REJECT"
        or (targets and all(x.get("decision") == "ABANDON" for x in targets))
        else "ROLLED_BACK"
    )
    if outcome != expected:
        raise ValueError(f"outcome {outcome} is inconsistent; expected {expected}")
    if value["publishable"] is not (outcome == "REPAIRED"):
        raise ValueError("publishable is true only for REPAIRED")
    if outcome == "REPAIRED":
        changed_targets = {x["finding_id"] for x in changes}
        regression_targets = {x["finding_id"] for x in regressions}
        non_abandon = {x["finding_id"] for x in targets if x["decision"] != "ABANDON"}
        if not non_abandon.issubset(changed_targets) or not non_abandon.issubset(
            regression_targets
        ):
            raise ValueError(
                "REPAIRED requires change and regression evidence for every repaired target"
            )
        if not non_abandon.issubset(impact_targets):
            raise ValueError(
                "REPAIRED requires an impact-matrix record for every repaired target"
            )
        if any(
            not item["synchronized"]
            for item in impact_matrix
            if item["finding_id"] in non_abandon
        ):
            raise ValueError("REPAIRED requires every affected path to be synchronized")
        if fresh_review["status"] != "COMPLETE":
            raise ValueError("REPAIRED requires a COMPLETE independent fresh review")
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("report", type=Path)
    args = parser.parse_args()
    value = json.loads(args.report.read_text(encoding="utf-8"))
    validate(value, report_path=args.report.resolve())
    print(
        json.dumps(
            {
                "valid": True,
                "outcome": value["outcome"],
                "publishable": value["publishable"],
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
