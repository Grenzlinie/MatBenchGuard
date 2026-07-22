#!/usr/bin/env python3
"""Create a single assigned materials Review/Repair run.

Only the human-prompted main agent should invoke this tool.  Workers receive
the resulting run directory and never write the assignment ledger themselves.
"""

from __future__ import annotations

import argparse
import csv
import os
import sys
import tempfile
import uuid
from datetime import UTC, datetime
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / ".cursor/skills/materials-benchmark-review/scripts"))
from run_context import create_run  # noqa: E402


FIELDS = (
    "package_id",
    "run_id",
    "assigned_agent",
    "status",
    "record_dir",
    "started_at",
    "completed_at",
    "review_verdict",
    "repair_status",
)


def timestamp() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def append_assignment(path: Path, row: dict[str, str]) -> None:
    rows: list[dict[str, str]] = []
    if path.is_file():
        with path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        if any(existing["package_id"] == row["package_id"] and existing["status"] not in {"COMPLETED", "FAILED"} for existing in rows):
            raise ValueError("package already has an active assigned run")
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=".assignments.", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(rows)
            writer.writerow(row)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except Exception:
        Path(temporary).unlink(missing_ok=True)
        raise


def main() -> int:
    parser = argparse.ArgumentParser(description="Assign one materials package to a fresh run.")
    parser.add_argument("package_id", help="cluster/theme/paper package id")
    parser.add_argument("--agent", required=True, help="assigned worker identity")
    parser.add_argument("--run-id", default=None)
    args = parser.parse_args()
    corpus = REPO_ROOT / "materials_science_questions"
    run_id = args.run_id or f"run-{uuid.uuid4().hex[:12]}"
    run_dir = create_run(corpus, args.package_id, run_id)
    try:
        append_assignment(
            REPO_ROOT / ".review_records" / "assignments.csv",
            {
                "package_id": args.package_id,
                "run_id": run_id,
                "assigned_agent": args.agent,
                "status": "ASSIGNED",
                "record_dir": str(run_dir),
                "started_at": timestamp(),
                "completed_at": "",
                "review_verdict": "",
                "repair_status": "",
            },
        )
    except Exception:
        # A run with no ledger entry is never assigned; retain no dangling work.
        import shutil
        shutil.rmtree(run_dir)
        raise
    print(run_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
