#!/usr/bin/env python3
"""Validate, manifest, archive, and atomically publish benchmark repair output."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

STATUSES = ("REPAIRED", "PARTIALLY_REPAIRED", "ABANDONED", "ROLLED_BACK")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return f"sha256:{h.hexdigest()}"


def newest_work(root: Path) -> Path:
    parent = root / ".benchmark_repair_tmp"
    candidates = [p for p in parent.iterdir() if p.is_dir()]
    if not candidates:
        raise FileNotFoundError("No prepared repair workspace")
    return max(candidates, key=lambda p: p.stat().st_mtime)


def read_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"Expected object: {path}")
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("benchmark_root", type=Path)
    parser.add_argument("--status", choices=STATUSES, required=True)
    parser.add_argument("--work-dir", type=Path)
    args = parser.parse_args()

    root = args.benchmark_root.resolve()
    work = args.work_dir.resolve() if args.work_dir else newest_work(root)
    context = read_json(work / ".repair_context.json")
    report_path = work / "repair_report.json"
    report = read_json(report_path)
    report["summary"]["repair_status"] = args.status
    report["summary"]["publishable"] = args.status == "REPAIRED"
    report["configuration"]["completed_at"] = datetime.now(timezone.utc).isoformat()
    if args.status in {"ABANDONED", "ROLLED_BACK"}:
        report["summary"]["publishable"] = False
    report_path.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    if args.status == "ABANDONED" and not (work / "abandoned_findings.jsonl").exists():
        source = work / "unresolved_findings.jsonl"
        shutil.copy2(source, work / "abandoned_findings.jsonl")

    validator = Path(__file__).with_name("validate_repair_output.py")
    subprocess.run(
        [sys.executable, str(validator), str(work), "--expected-status", args.status],
        check=True,
    )

    outputs = {}
    for path in sorted(work.rglob("*")):
        if path.is_file() and path.name not in {".repair_context.json", "repair_manifest.json"}:
            outputs[str(path.relative_to(work))] = sha256_file(path)
    manifest = {
        "schema_version": "1.0",
        "repair_id": context["repair_id"],
        "parent_audit_id": context["parent_audit_id"],
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "repair_skill": "biomaster-benchmark-repair",
        "repairer_version": "1.0",
        "status": args.status,
        "audit_hashes": context.get("audit_hashes", {}),
        "output_hashes": outputs,
        "rolled_back": bool(report.get("summary", {}).get("rolled_back", False)),
    }
    (work / "repair_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (work / ".repair_context.json").unlink(missing_ok=True)

    target = root / "benchmark_repair"
    history = root / "benchmark_repair_history"
    if target.exists():
        old_id = "unknown"
        old_manifest = target / "repair_manifest.json"
        if old_manifest.is_file():
            try:
                old_id = str(read_json(old_manifest).get("repair_id") or "unknown")
            except (OSError, ValueError, json.JSONDecodeError):
                pass
        destination = history / old_id
        suffix = 1
        while destination.exists():
            destination = history / f"{old_id}-{suffix}"
            suffix += 1
        destination.parent.mkdir(parents=True, exist_ok=True)
        os.replace(target, destination)

    os.replace(work, target)
    temp_parent = root / ".benchmark_repair_tmp"
    try:
        temp_parent.rmdir()
    except OSError:
        pass
    print(json.dumps({"status": args.status, "output_dir": str(target)}, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError, subprocess.CalledProcessError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)
