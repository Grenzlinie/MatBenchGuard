#!/usr/bin/env python3
"""Create a validated explicit batch of no more than three review runs."""

from __future__ import annotations

import argparse
import csv
import json
import os
import shutil
import sys
import tempfile
import uuid
from datetime import UTC, datetime
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / ".cursor/skills/materials-benchmark-review/scripts"))
from run_context import RunContextError, create_run  # noqa: E402

FIELDS = (
    "package_id", "run_id", "assigned_agent", "status", "record_dir",
    "started_at", "completed_at", "review_verdict", "repair_status",
)


def timestamp() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def atomic_ledger(path: Path, rows: list[dict[str, str]]) -> None:
    descriptor, temporary = tempfile.mkstemp(prefix=".assignments.", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(rows)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except Exception:
        Path(temporary).unlink(missing_ok=True)
        raise


def create_batch(corpus: Path, package_ids: list[str], agent: str, max_parallelism: int) -> list[Path]:
    if not package_ids or len(package_ids) != len(set(package_ids)):
        raise RunContextError("package_ids must be non-empty and unique")
    if not 1 <= max_parallelism <= 3:
        raise RunContextError("max_parallelism must be between 1 and 3")
    ledger = corpus.parent / ".review_records" / "assignments.csv"
    rows: list[dict[str, str]] = []
    if ledger.is_file():
        with ledger.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
    active = {row["package_id"] for row in rows if row.get("status") not in {"COMPLETED", "FAILED"}}
    if active & set(package_ids):
        raise RunContextError("a requested package already has an active run")
    # Validate every package before creating the first run.
    if any(not (corpus / package_id).is_dir() for package_id in package_ids):
        raise RunContextError("one or more package_ids do not exist")
    created: list[Path] = []
    try:
        for package_id in package_ids:
            run_id = f"run-{uuid.uuid4().hex[:12]}"
            created.append(create_run(corpus, package_id, run_id))
        started = timestamp()
        rows.extend(
            {
                "package_id": package_id,
                "run_id": run_dir.name,
                "assigned_agent": agent,
                "status": "ASSIGNED",
                "record_dir": str(run_dir),
                "started_at": started,
                "completed_at": "",
                "review_verdict": "",
                "repair_status": "",
            }
            for package_id, run_dir in zip(package_ids, created, strict=True)
        )
        ledger.parent.mkdir(parents=True, exist_ok=True)
        atomic_ledger(ledger, rows)
    except Exception:
        for run_dir in created:
            shutil.rmtree(run_dir)
        raise
    return created


def main() -> int:
    parser = argparse.ArgumentParser(description="Assign an explicit materials review batch.")
    parser.add_argument("package_id", nargs="+")
    parser.add_argument("--agent", required=True)
    parser.add_argument("--max-parallelism", type=int, default=3)
    args = parser.parse_args()
    runs = create_batch(
        REPO_ROOT / "materials_science_questions",
        args.package_id,
        args.agent,
        args.max_parallelism,
    )
    print(json.dumps({"runs": [str(run) for run in runs], "max_parallelism": args.max_parallelism}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
