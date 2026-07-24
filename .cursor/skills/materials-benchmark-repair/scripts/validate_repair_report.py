#!/usr/bin/env python3
"""Validate the compact Agent-led repair record and its equal-depth re-audit."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
from typing import Any

SCHEMA = "materials-agent-repair-report/1.0"
OUTCOMES = {"REPAIRED", "PARTIALLY_REPAIRED", "ABANDONED", "ROLLED_BACK"}
DECISIONS = {"AUTO_FIX", "ASSISTED_FIX", "ABANDON"}


def _text(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be non-empty text")
    return value.strip()


def _review_validator():
    path = Path(__file__).resolve().parents[2] / "materials-benchmark-review/scripts/validate_agent_decision.py"
    spec = importlib.util.spec_from_file_location("materials_review_decision", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load Review decision validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate(value: Any, *, report_path: Path | None = None) -> dict[str, Any]:
    if not isinstance(value, dict) or value.get("schema_version") != SCHEMA:
        raise ValueError(f"repair report schema_version must be {SCHEMA}")
    for field in ("source_package", "candidate_package", "source_decision", "reaudit_decision"):
        _text(value.get(field), field)
    if value.get("outcome") not in OUTCOMES or not isinstance(value.get("publishable"), bool):
        raise ValueError("invalid outcome or publishable")
    targets = value.get("targets")
    changes = value.get("changes")
    regressions = value.get("regressions")
    unresolved = value.get("unresolved_findings")
    if not isinstance(targets, list) or not targets or not isinstance(changes, list) or not isinstance(regressions, list) or not isinstance(unresolved, list):
        raise ValueError("targets/changes/regressions/unresolved_findings must be lists")
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
    for index, item in enumerate(regressions):
        if not isinstance(item, dict) or item.get("finding_id") not in target_ids:
            raise ValueError(f"regressions[{index}] must bind a target")
        if item.get("before_passed") is not False or item.get("after_passed") is not True:
            raise ValueError(f"regressions[{index}] must fail before and pass after")
        _text(item.get("specification"), f"regressions[{index}].specification")

    if report_path is not None:
        source_path = Path(value["source_decision"])
        if not source_path.is_absolute():
            source_path = report_path.parent / source_path
        re_path = Path(value["reaudit_decision"])
        if not re_path.is_absolute():
            re_path = report_path.parent / re_path
        review_validator = _review_validator()
        review_validator.validate(json.loads(source_path.read_text(encoding="utf-8")))
        re_value = json.loads(re_path.read_text(encoding="utf-8"))
        review_validator.validate(re_value)
        if value.get("reaudit_verdict") != re_value.get("verdict"):
            raise ValueError("reaudit_verdict does not match validated decision")
    verdict = value.get("reaudit_verdict")
    outcome = value["outcome"]
    expected = (
        "REPAIRED" if verdict == "PASS" and targets and all(x.get("resolved") for x in targets) and not unresolved
        else "PARTIALLY_REPAIRED" if verdict == "CONDITIONAL"
        else "ABANDONED" if verdict == "REJECT" or (targets and all(x.get("decision") == "ABANDON" for x in targets))
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
        if not non_abandon.issubset(changed_targets) or not non_abandon.issubset(regression_targets):
            raise ValueError("REPAIRED requires change and regression evidence for every repaired target")
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("report", type=Path)
    args = parser.parse_args()
    value = json.loads(args.report.read_text(encoding="utf-8"))
    validate(value, report_path=args.report.resolve())
    print(json.dumps({"valid": True, "outcome": value["outcome"], "publishable": value["publishable"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
