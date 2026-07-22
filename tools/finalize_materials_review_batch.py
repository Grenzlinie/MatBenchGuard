#!/usr/bin/env python3
"""Atomically reflect terminal run outcomes in corpus review tracking.

This is deliberately main-Agent-only coordination. It never launches review or
repair, and it refuses a batch until every supplied run is terminal.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import tempfile
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / ".cursor/skills/materials-benchmark-review/scripts"))
from run_context import RunContextError, load_context, status  # noqa: E402


def atomic_json(path: Path, value: Any) -> None:
    descriptor, temporary = tempfile.mkstemp(prefix=".tracking.", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            json.dump(value, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except Exception:
        Path(temporary).unlink(missing_ok=True)
        raise


def tracking_update(run_dirs: list[Path], tracking_path: Path) -> dict[str, Any]:
    tracking = json.loads(tracking_path.read_text(encoding="utf-8"))
    if not isinstance(tracking, dict) or not isinstance(tracking.get("records"), list):
        raise RunContextError("tracking file is invalid")
    records = {item.get("package_id"): item for item in tracking["records"] if isinstance(item, dict)}
    updates: list[dict[str, str]] = []
    for run_dir in run_dirs:
        context = load_context(run_dir)
        current = status(run_dir)
        if current["state"] not in {"COMPLETED", "FAILED"}:
            raise RunContextError(
                f"run is not terminal: {run_dir} (state={current['state']}; "
                "AGENT_ASSESSMENT_PENDING and AGENT_CONTRACT_PENDING cannot be "
                "recorded as completed corpus outcomes)"
            )
        record = records.get(context["package_id"])
        if not isinstance(record, dict):
            raise RunContextError(f"package is absent from tracking: {context['package_id']}")
        outcome = current.get("outcome", "FAILED")
        result = current.get("repair_result") or current.get("review_result") or {}
        if not isinstance(result, dict):
            result = {}
        verdict = result.get("review_verdict") or result.get("disposition")
        if verdict is None and isinstance(result.get("summary"), dict):
            verdict = result["summary"].get("final_verdict")
        record.update(
            {
                "review_status": "failed" if current["state"] == "FAILED" else "reviewed",
                "review_verdict": verdict,
                "publishability": result.get("publishability"),
                "repair_status": current.get("repair_status", outcome.lower()),
                "last_audit_id": result.get("audit_id"),
                "audit_output_dir": str(run_dir / "audit"),
                "last_reviewed_at": datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
                "reviewer": "main-agent",
            }
        )
        updates.append({"package_id": context["package_id"], "outcome": str(outcome)})
    atomic_json(tracking_path, tracking)
    return {"tracking": str(tracking_path), "updated": updates}


def update_assignment_ledger(run_dirs: list[Path], ledger_path: Path) -> None:
    """The main Agent is the only writer of assignment terminal fields."""

    if not ledger_path.is_file():
        raise RunContextError("assignment ledger is missing")
    with ledger_path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames
        rows = list(reader)
    if not fields:
        raise RunContextError("assignment ledger lacks a header")
    by_run: dict[str, tuple[dict[str, Any], dict[str, Any]]] = {}
    for run_dir in run_dirs:
        context = load_context(run_dir)
        by_run[context["run_id"]] = (context, status(run_dir))
    updated: set[str] = set()
    for row in rows:
        pair = by_run.get(row.get("run_id", ""))
        if pair is None:
            continue
        context, current = pair
        if row.get("package_id") != context["package_id"]:
            raise RunContextError("assignment ledger package/run mismatch")
        if current["state"] not in {"COMPLETED", "FAILED"}:
            raise RunContextError("assignment update requires terminal run")
        result = current.get("repair_result") or current.get("review_result") or {}
        if not isinstance(result, dict):
            result = {}
        row["status"] = current["state"]
        row["completed_at"] = datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")
        row["review_verdict"] = str(result.get("review_verdict", ""))
        row["repair_status"] = str(current.get("repair_status", current.get("outcome", "")))
        updated.add(context["run_id"])
    if updated != set(by_run):
        raise RunContextError("one or more runs are absent from assignment ledger")
    descriptor, temporary = tempfile.mkstemp(prefix=".assignments.", dir=ledger_path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, ledger_path)
    except Exception:
        Path(temporary).unlink(missing_ok=True)
        raise


def main() -> int:
    parser = argparse.ArgumentParser(description="Finalize one explicit terminal Review/Repair batch.")
    parser.add_argument("--run-dir", action="append", type=Path, required=True)
    parser.add_argument(
        "--tracking",
        type=Path,
        default=REPO_ROOT / "materials_science_questions/corpus_review_tracking.json",
    )
    args = parser.parse_args()
    result = tracking_update(args.run_dir, args.tracking)
    ledger = REPO_ROOT / ".review_records" / "assignments.csv"
    if ledger.is_file():
        update_assignment_ledger(args.run_dir, ledger)
        result["assignment_ledger"] = str(ledger)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
