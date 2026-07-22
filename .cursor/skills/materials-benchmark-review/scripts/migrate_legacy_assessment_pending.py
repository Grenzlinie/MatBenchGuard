#!/usr/bin/env python3
"""Idempotently migrate known incomplete dual-lane audits to assessment-pending.

Preserves audit diagnostics and never updates corpus tracking. Only demotes
runs that lack a validated paper Agent assessment (legacy NOT_SUPPLIED /
empty agent_quality.assessment with paper_assessment gaps).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from prepare_audit_output import AGENT_ASSESSMENT_PENDING, skill_root
from run_context import (
    RunContextError,
    load_context,
    now,
    status,
    transition,
    write_json_atomic,
)


INVENTORY_RELATIVE = "references/legacy_not_supplied_assessment_runs.json"
MIGRATION_MARKER = "legacy_assessment_pending_migration.json"


def inventory_path() -> Path:
    return skill_root() / INVENTORY_RELATIVE


def load_inventory(path: Path | None = None) -> dict[str, Any]:
    resolved = (path or inventory_path()).expanduser().resolve()
    payload = json.loads(resolved.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or not isinstance(payload.get("runs"), list):
        raise RunContextError("legacy assessment inventory is invalid")
    return payload


def run_dir_for(
    review_records_root: Path,
    package_id: str,
    run_id: str,
) -> Path:
    return review_records_root.joinpath(*package_id.split("/")) / "runs" / run_id


def report_lacks_validated_paper_assessment(report: dict[str, Any]) -> bool:
    quality = report.get("agent_quality")
    assessment: Any = None
    if isinstance(quality, dict):
        assessment = quality.get("assessment")
    if isinstance(assessment, dict) and assessment.get("materials_qualification"):
        return False
    evidence = report.get("evidence_contract")
    gaps: list[Any] = []
    if isinstance(evidence, dict) and isinstance(evidence.get("gaps"), list):
        gaps = evidence["gaps"]
    elif isinstance(report.get("gaps"), list):
        gaps = report["gaps"]
    gap_set = {item for item in gaps if isinstance(item, str)}
    if {
        "paper_assessment",
        "authoritative_materials_qualification",
    } & gap_set:
        return True
    if assessment in (None, {}, []):
        return True
    if isinstance(assessment, dict) and not assessment:
        return True
    return False


def read_audit_report(run_dir: Path) -> dict[str, Any] | None:
    candidates = (
        run_dir / "audit" / "benchmark_audit" / "audit_report.json",
        run_dir / "audit" / "audit_report.json",
    )
    for path in candidates:
        if not path.is_file():
            continue
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(payload, dict):
            return payload
    return None


def migrate_run(run_dir: Path, *, inventory_entry: dict[str, Any]) -> dict[str, Any]:
    run_dir = run_dir.expanduser().resolve()
    load_context(run_dir)
    current = status(run_dir)
    marker_path = run_dir / MIGRATION_MARKER
    if current["state"] == AGENT_ASSESSMENT_PENDING and marker_path.is_file():
        return {
            "run_dir": str(run_dir),
            "action": "already_migrated",
            "state": current["state"],
        }
    report = read_audit_report(run_dir)
    if report is None:
        return {
            "run_dir": str(run_dir),
            "action": "skipped_missing_report",
            "state": current["state"],
        }
    if not report_lacks_validated_paper_assessment(report):
        return {
            "run_dir": str(run_dir),
            "action": "skipped_has_paper_assessment",
            "state": current["state"],
        }
    if current["state"] not in {"REVIEWED", AGENT_ASSESSMENT_PENDING}:
        raise RunContextError(
            f"legacy assessment migration refuses state {current['state']}: {run_dir}"
        )
    preserved = {
        "schema_version": "materials-legacy-assessment-pending-migration/1.0",
        "migrated_at": now(),
        "previous_state": current["state"],
        "inventory_entry": inventory_entry,
        "diagnostics_preserved": True,
        "tracking_updated": False,
        "audit_report_present": True,
        "reason": (
            "legacy dual-lane audit lacks validated paper Agent assessment "
            "(NOT_SUPPLIED / empty agent_quality.assessment)"
        ),
    }
    write_json_atomic(marker_path, preserved)
    if current["state"] == "REVIEWED":
        transition(
            run_dir,
            AGENT_ASSESSMENT_PENDING,
            review_result={
                "status": AGENT_ASSESSMENT_PENDING,
                "review_status": AGENT_ASSESSMENT_PENDING,
                "verdict": "NOT_ASSESSABLE",
                "publishable": False,
                "message": preserved["reason"],
                "legacy_migration": True,
            },
            legacy_assessment_migration=True,
        )
    else:
        write_json_atomic(
            run_dir / "status.json",
            {
                **current,
                "legacy_assessment_migration": True,
                "updated_at": now(),
            },
        )
    return {
        "run_dir": str(run_dir),
        "action": "migrated",
        "state": AGENT_ASSESSMENT_PENDING,
        "previous_state": current["state"],
    }


def migrate_inventory(
    review_records_root: Path,
    inventory: dict[str, Any] | None = None,
) -> dict[str, Any]:
    payload = inventory or load_inventory()
    results = []
    for entry in payload["runs"]:
        if not isinstance(entry, dict):
            raise RunContextError("inventory run entry must be an object")
        package_id = entry.get("package_id")
        run_id = entry.get("run_id")
        if not isinstance(package_id, str) or not isinstance(run_id, str):
            raise RunContextError("inventory run entry requires package_id and run_id")
        target = run_dir_for(review_records_root, package_id, run_id)
        if not target.is_dir():
            results.append(
                {
                    "package_id": package_id,
                    "run_id": run_id,
                    "action": "skipped_missing_run_dir",
                    "run_dir": str(target),
                }
            )
            continue
        result = migrate_run(target, inventory_entry=entry)
        result["package_id"] = package_id
        result["run_id"] = run_id
        results.append(result)
    return {
        "inventory": str(inventory_path()),
        "review_records_root": str(review_records_root.resolve()),
        "results": results,
        "tracking_updated": False,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Migrate known legacy NOT_SUPPLIED paper-assessment audits to "
            "AGENT_ASSESSMENT_PENDING without updating tracking."
        )
    )
    parser.add_argument(
        "--review-records-root",
        type=Path,
        default=Path(".review_records"),
        help="root that contains cluster/.../runs/<run-id>",
    )
    parser.add_argument(
        "--inventory",
        type=Path,
        default=None,
        help="optional override inventory JSON",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    inventory = load_inventory(args.inventory) if args.inventory else load_inventory()
    result = migrate_inventory(args.review_records_root, inventory=inventory)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
