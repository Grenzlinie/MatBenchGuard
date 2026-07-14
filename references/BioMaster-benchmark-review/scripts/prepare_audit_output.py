#!/usr/bin/env python3
"""Prepare a fixed, atomic audit workspace inside a benchmark root."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import stat
import sys
import time
import uuid
import zipfile
from pathlib import Path
from typing import Any

CORE_HINTS = (
    "instruction.md",
    "task.toml",
    "manifest.json",
    "steps.json",
    "resources.json",
    "tests/grading_spec.json",
    "tests/checker.py",
)
HASH_PATTERNS = {
    "instruction.md",
    "task.toml",
    "manifest.json",
    "steps.json",
    "resources.json",
    "grading_spec.json",
    "checker.py",
    "Dockerfile",
    "requirements.txt",
    "environment.yml",
    "environment.yaml",
    "poetry.lock",
    "uv.lock",
    "paper.md",
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return "sha256:" + h.hexdigest()


def safe_extract(zpath: Path, dest: Path) -> None:
    dest_resolved = dest.resolve()
    with zipfile.ZipFile(zpath) as zf:
        for member in zf.infolist():
            mode = member.external_attr >> 16
            if stat.S_ISLNK(mode):
                raise ValueError(f"symbolic links are not allowed in benchmark zip: {member.filename}")
            target = (dest / member.filename).resolve()
            if target != dest_resolved and not str(target).startswith(str(dest_resolved) + os.sep):
                raise ValueError(f"unsafe zip path: {member.filename}")
        zf.extractall(dest)


def locate_root(path: Path) -> Path:
    candidates: list[tuple[int, int, Path]] = []
    search = [path, *[p for p in path.rglob("*") if p.is_dir()]]
    for candidate in search:
        if "__MACOSX" in candidate.parts or "solution" in candidate.parts:
            continue
        score = sum((candidate / rel).exists() for rel in CORE_HINTS)
        if score:
            candidates.append((-score, len(candidate.parts), candidate))
    if not candidates:
        raise ValueError("could not locate a benchmark root")
    candidates.sort()
    return candidates[0][2].resolve()


def render_template(source: Path, destination: Path, values: dict[str, str]) -> None:
    text = source.read_text(encoding="utf-8")
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", value)
    destination.write_text(text, encoding="utf-8")


def previous_audit_id(audit_dir: Path) -> str:
    manifest = audit_dir / "audit_manifest.json"
    if manifest.exists():
        try:
            value = json.loads(manifest.read_text(encoding="utf-8")).get("audit_id")
            if value:
                return str(value)
        except Exception:
            pass
    return time.strftime("legacy-%Y%m%dT%H%M%SZ", time.gmtime())


def collect_input_hashes(root: Path) -> dict[str, str]:
    hashes: dict[str, str] = {}
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in {"benchmark_audit", "benchmark_audit_history", ".benchmark_audit_tmp", "solution"} for part in path.parts):
            continue
        if path.name in HASH_PATTERNS or path.suffix.lower() in {".toml", ".yaml", ".yml"}:
            rel = path.relative_to(root).as_posix()
            try:
                hashes[rel] = sha256_file(path)
            except OSError:
                continue
    return dict(sorted(hashes.items()))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="benchmark directory or zip archive")
    parser.add_argument("--paper-mode", choices=["no_paper", "paper_grounded"], default="no_paper")
    parser.add_argument("--execution-level", choices=["E0", "E1", "E2", "E3", "E4"], default="E1")
    parser.add_argument("--extract-dir", help="destination used when the input is a zip")
    args = parser.parse_args()

    try:
        source = Path(args.input).expanduser().resolve()
        if not source.exists():
            raise FileNotFoundError(source)

        input_type = "directory"
        extracted_dir: Path | None = None
        if source.is_file():
            if source.suffix.lower() != ".zip":
                raise ValueError("input file must be a zip archive")
            input_type = "zip"
            extracted_dir = Path(args.extract_dir).expanduser().resolve() if args.extract_dir else source.parent / f"{source.stem}_audited"
            if extracted_dir.exists():
                raise FileExistsError(f"zip extraction directory already exists: {extracted_dir}")
            extracted_dir.mkdir(parents=True)
            safe_extract(source, extracted_dir)
            root = locate_root(extracted_dir)
        elif source.is_dir():
            root = locate_root(source)
        else:
            raise ValueError("input must be a directory or zip archive")

        now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        audit_id = time.strftime("audit-%Y%m%dT%H%M%SZ-", time.gmtime()) + uuid.uuid4().hex[:8]
        audit_dir = root / "benchmark_audit"
        temp_dir = root / ".benchmark_audit_tmp"
        history_dir = root / "benchmark_audit_history"

        if temp_dir.exists():
            shutil.rmtree(temp_dir)
        if audit_dir.exists():
            history_dir.mkdir(exist_ok=True)
            target = history_dir / previous_audit_id(audit_dir)
            suffix = 1
            while target.exists():
                target = history_dir / f"{previous_audit_id(audit_dir)}-{suffix}"
                suffix += 1
            audit_dir.rename(target)

        for rel in [
            "evidence/static_checks",
            "evidence/resource_checks",
            "evidence/checker_tests",
            "evidence/paper_checks",
            "logs",
            "patches",
        ]:
            (temp_dir / rel).mkdir(parents=True, exist_ok=True)

        assets = Path(__file__).resolve().parent.parent / "assets"
        values = {
            "AUDIT_ID": audit_id,
            "BENCHMARK_NAME": root.name,
            "BENCHMARK_ROOT": str(root),
            "INPUT_TYPE": input_type,
            "PAPER_MODE": args.paper_mode,
            "EXECUTION_LEVEL": args.execution_level,
            "STARTED_AT": now,
        }
        render_template(assets / "audit_report_template.md", temp_dir / "audit_report.md", values)
        render_template(assets / "audit_report_template.json", temp_dir / "audit_report.json", values)
        shutil.copy2(assets / "resource_checks_template.json", temp_dir / "resource_checks.json")
        shutil.copy2(assets / "checker_tests_template.json", temp_dir / "checker_tests.json")
        (temp_dir / "findings.jsonl").write_text("", encoding="utf-8")
        (temp_dir / "logs/audit.log").write_text(
            f"{now}\tINFO\taudit workspace prepared\taudit_id={audit_id}\n",
            encoding="utf-8",
        )

        manifest: dict[str, Any] = {
            "schema_version": "1.0",
            "audit_id": audit_id,
            "parent_audit_id": None,
            "review_type": "INITIAL_AUDIT",
            "generated_at": now,
            "completed_at": None,
            "auditor_version": "benchmark-biology-auditor/1.0",
            "input_source": str(source),
            "input_type": input_type,
            "benchmark_root": str(root),
            "input_hashes": collect_input_hashes(root),
            "output_hashes": {},
            "resolved_findings": [],
            "new_findings": [],
        }
        (temp_dir / "audit_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

        context = {
            "audit_id": audit_id,
            "benchmark_root": str(root),
            "audit_temp_dir": str(temp_dir),
            "final_audit_dir": str(audit_dir),
            "input_type": input_type,
            "extracted_dir": str(extracted_dir) if extracted_dir else None,
            "paper_mode": args.paper_mode,
            "execution_level": args.execution_level,
        }
        (temp_dir / "audit_context.json").write_text(json.dumps(context, indent=2, ensure_ascii=False), encoding="utf-8")
        print(json.dumps(context, indent=2, ensure_ascii=False))
        return 0
    except Exception as exc:
        print(f"prepare audit output failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
