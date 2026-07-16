#!/usr/bin/env python3
"""Discover a Harbor 题包 and prepare its isolated audit workspace."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
import time
import uuid
from pathlib import Path
from typing import Any, Iterable


REQUIRED_ROLES = {
    "task.toml": "toml",
    "manifest.json": "json",
    "instruction.md": "text",
    "steps.json": "json",
    "resources.json": "json",
    "environment/Dockerfile": "text",
    "tests/grading_spec.json": "json",
    "tests/checker.py": "text",
    "tests/test.sh": "text",
}
QUALITY_EVIDENCE_ROLES = {
    "instruction.md": "text",
    "tests/grading_spec.json": "json",
    "tests/checker.py": "text",
    "tests/test.sh": "text",
}
PRUNED_DIRS = {
    "paper",
    "solution",
    "benchmark_audit",
    "benchmark_audit_history",
    ".benchmark_audit_tmp",
    "__MACOSX",
}
AUTHORITATIVE_EXECUTION_LEVEL = "E1"
HASH_NAMES = {
    *QUALITY_EVIDENCE_ROLES,
}
REVIEW_IMPLEMENTATION_FILES = (
    "scripts/prepare_audit_output.py",
    "scripts/audit_package.py",
    "scripts/dynamic_checker_probe.py",
    "scripts/finalize_audit_output.py",
    "scripts/run_review.py",
    "scripts/run_fast_e1_batch.py",
)


def skill_root() -> Path:
    return Path(__file__).resolve().parent.parent


def assets_root() -> Path:
    return skill_root() / "assets"


def basename(value: Any) -> str:
    return str(value or "").replace("\\", "/").split("/")[-1]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()


def iter_public_files(root: Path) -> Iterable[Path]:
    """Yield files without entering solution or generated audit directories."""
    for current, directories, filenames in os.walk(root, topdown=True):
        current_path = Path(current)
        for name in directories:
            if (current_path / name).is_symlink():
                raise ValueError(
                    "symbolic-link directories are not allowed in the audit "
                    f"boundary: {current_path / name}"
                )
        directories[:] = [
            name for name in directories if name not in PRUNED_DIRS
        ]
        for filename in filenames:
            path = current_path / filename
            if path.is_symlink():
                raise ValueError(
                    f"symbolic links are not allowed in the audit boundary: {path}"
                )
            yield path


def validate_role_boundary(root: Path) -> None:
    """Reject role paths that escape the 题包 or route through symlinks."""
    root = root.resolve()
    solution = root / "solution"
    if solution.is_symlink():
        raise ValueError("solution/ must not be a symbolic link")
    for role in QUALITY_EVIDENCE_ROLES:
        path = root / role
        if not path.exists():
            continue
        current = path
        while current != root:
            if current.is_symlink():
                raise ValueError(
                    f"required Harbor role routes through a symlink: {role}"
                )
            current = current.parent
        resolved = path.resolve()
        if not resolved.is_relative_to(root):
            raise ValueError(f"required Harbor role escapes 题包 root: {role}")
        if resolved.is_relative_to(solution):
            raise ValueError(f"required Harbor role routes through solution/: {role}")


def locate_root(source: Path) -> Path:
    source = source.expanduser().resolve()
    if not source.is_dir():
        raise ValueError("input must be a Harbor 题包 directory")
    if sum((source / role).exists() for role in QUALITY_EVIDENCE_ROLES) >= 2:
        validate_role_boundary(source)
        return source

    candidates: list[tuple[int, int, Path]] = []
    for current, directories, _ in os.walk(source, topdown=True):
        directories[:] = [
            name for name in directories if name not in PRUNED_DIRS
        ]
        candidate = Path(current)
        score = sum(
            (candidate / role).exists() for role in QUALITY_EVIDENCE_ROLES
        )
        if score:
            candidates.append((-score, len(candidate.parts), candidate))
    if not candidates:
        raise ValueError("could not locate a Harbor 题包 root")
    candidates.sort()
    root = candidates[0][2].resolve()
    validate_role_boundary(root)
    return root


def render_template(source: Path, values: dict[str, str]) -> str:
    text = source.read_text(encoding="utf-8")
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", value)
    return text


def collect_input_hashes(root: Path) -> dict[str, str]:
    hashes: dict[str, str] = {}
    candidates = [root / "instruction.md"]
    tests = root / "tests"
    if tests.is_dir():
        candidates.extend(path for path in tests.rglob("*") if path.is_file())
    for path in candidates:
        if not path.is_file():
            continue
        if path.is_symlink():
            raise ValueError(f"quality evidence cannot be a symlink: {path}")
        relative = path.relative_to(root).as_posix()
        hashes[relative] = sha256_file(path)
    return dict(sorted(hashes.items()))


def collect_review_implementation_hashes() -> dict[str, Any]:
    files = {
        relative: sha256_file(skill_root() / relative)
        for relative in REVIEW_IMPLEMENTATION_FILES
    }
    payload = json.dumps(
        files, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return {
        "schema_version": "materials-review-implementation/1.0",
        "root": ".cursor/skills/materials-benchmark-review",
        "files": files,
        "aggregate_hash": "sha256:" + hashlib.sha256(payload).hexdigest(),
    }


def validate_paper_boundary(root: Path) -> None:
    """Ensure bundled paper roles are local files outside solution/."""
    resolved_root = root.resolve()
    solution = resolved_root / "solution"
    paper_dir = root / "paper"
    if paper_dir.is_symlink():
        raise ValueError("paper role routes through a symlink: paper/")
    for relative in ("paper/paper.md", "paper/images_manifest.json"):
        path = root / relative
        if path.is_symlink():
            raise ValueError(
                f"paper role routes through a symlink: {relative}"
            )
        if not path.is_file():
            raise ValueError(
                f"paper_grounded mode requires bundled paper role: {relative}"
            )
        resolved = path.resolve()
        if not resolved.is_relative_to(resolved_root):
            raise ValueError(f"paper role escapes 题包 root: {relative}")
        if resolved.is_relative_to(solution):
            raise ValueError(f"paper role routes through solution/: {relative}")


def record_paper_input_hashes(root: Path, temp_dir: Path) -> None:
    """Add bundled paper hashes only after the no-paper Hard gate passes."""
    validate_paper_boundary(root)
    manifest_path = temp_dir / "audit_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for relative in ("paper/paper.md", "paper/images_manifest.json"):
        path = root / relative
        manifest["input_hashes"][relative] = sha256_file(path)
    manifest["input_hashes"] = dict(
        sorted(manifest["input_hashes"].items())
    )
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def prepare_workspace(
    root: Path, paper_mode: str, execution_level: str
) -> dict[str, Any]:
    """Prepare a new candidate audit without moving the authoritative prior one."""
    if execution_level != AUTHORITATIVE_EXECUTION_LEVEL:
        raise ValueError(
            "authoritative materials review is E1-only; "
            f"received execution level {execution_level!r}"
        )
    temp_dir = root / ".benchmark_audit_tmp"
    if temp_dir.exists():
        shutil.rmtree(temp_dir)
    for relative in (
        "evidence/static_checks",
        "evidence/resource_checks",
        "evidence/checker_tests",
        "evidence/paper_checks",
        "logs",
        "patches",
    ):
        (temp_dir / relative).mkdir(parents=True, exist_ok=True)

    started_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    audit_id = (
        time.strftime("audit-%Y%m%dT%H%M%SZ-", time.gmtime())
        + uuid.uuid4().hex[:8]
    )
    values = {
        "AUDIT_ID": audit_id,
        "BENCHMARK_NAME": root.name,
        "BENCHMARK_ROOT": str(root),
        "PAPER_MODE": paper_mode,
        "EXECUTION_LEVEL": execution_level,
        "STARTED_AT": started_at,
    }
    (temp_dir / "audit_report.md").write_text(
        render_template(assets_root() / "audit_report_template.md", values),
        encoding="utf-8",
    )
    (temp_dir / "audit_report.json").write_text(
        render_template(assets_root() / "audit_report_template.json", values),
        encoding="utf-8",
    )
    shutil.copy2(
        assets_root() / "resource_checks_template.json",
        temp_dir / "resource_checks.json",
    )
    shutil.copy2(
        assets_root() / "checker_tests_template.json",
        temp_dir / "checker_tests.json",
    )
    (temp_dir / "findings.jsonl").write_text("", encoding="utf-8")
    (temp_dir / "logs/audit.log").write_text(
        f"{started_at}\tINFO\taudit workspace prepared\taudit_id={audit_id}\n",
        encoding="utf-8",
    )
    manifest = {
        "schema_version": "0.1",
        "audit_id": audit_id,
        "parent_audit_id": None,
        "review_type": "INITIAL_AUDIT",
        "generated_at": started_at,
        "completed_at": None,
        "auditor_version": "materials-benchmark-review/0.1",
        "benchmark_root": str(root),
        # Paper roles are deliberately added only after the no-paper gate
        # passes, so a terminal E0/E1 result never traverses paper content.
        "input_hashes": collect_input_hashes(root),
        "review_implementation": collect_review_implementation_hashes(),
        "output_hashes": {},
        "resolved_findings": [],
        "new_findings": [],
        "solution_content_inspected": False,
    }
    (temp_dir / "audit_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    context = {
        "audit_id": audit_id,
        "benchmark_root": str(root),
        "audit_temp_dir": str(temp_dir),
        "final_audit_dir": str(root / "benchmark_audit"),
        "paper_mode": paper_mode,
        "execution_level": execution_level,
    }
    (temp_dir / "audit_context.json").write_text(
        json.dumps(context, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    return context


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument(
        "--paper-mode",
        choices=["no_paper", "paper_grounded"],
        default="no_paper",
    )
    parser.add_argument(
        "--execution-level",
        choices=[AUTHORITATIVE_EXECUTION_LEVEL],
        default=AUTHORITATIVE_EXECUTION_LEVEL,
    )
    arguments = parser.parse_args()
    try:
        context = prepare_workspace(
            locate_root(Path(arguments.input)),
            arguments.paper_mode,
            arguments.execution_level,
        )
        print(json.dumps(context, indent=2, ensure_ascii=False))
        return 0
    except Exception as exc:  # noqa: BLE001
        print(f"prepare audit output failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
