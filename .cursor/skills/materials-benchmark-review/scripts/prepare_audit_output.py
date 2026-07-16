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

from canonical_status import canonical_fields


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
PAPER_EVIDENCE_ROLES = {
    "paper/paper.md": "text",
    "paper/images_manifest.json": "json",
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
REVIEW_IMPLEMENTATION_FILES_MANIFEST = (
    "references/review-implementation-files.json"
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


def sha256_path(path: Path) -> str:
    if path.is_symlink():
        raise ValueError(f"external evidence may not be a symbolic link: {path}")
    if path.is_file():
        return sha256_file(path)
    if not path.is_dir():
        raise FileNotFoundError(path)
    entries = []
    for child in sorted(path.rglob("*")):
        if child.is_symlink():
            raise ValueError(
                f"external evidence may not contain symbolic links: {child}"
            )
        if child.is_file():
            entries.append(
                (child.relative_to(path).as_posix(), sha256_file(child))
            )
    payload = json.dumps(
        entries, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def core_contract_snapshot(root: Path) -> dict[str, Any]:
    paths: list[Path] = []
    instruction = root / "instruction.md"
    if instruction.is_file():
        paths.append(instruction)
    for role in ("tests", "solution"):
        directory = root / role
        if directory.is_symlink():
            raise ValueError(f"core contract role may not be a symlink: {role}")
        if directory.is_dir():
            for path in sorted(directory.rglob("*")):
                if path.is_symlink():
                    raise ValueError(
                        f"core contract surface may not be a symlink: {path}"
                    )
                if path.is_file():
                    paths.append(path)
    return {
        "schema_version": "materials-core-contract/1.0",
        "surface_hashes": {
            path.relative_to(root).as_posix(): sha256_file(path)
            for path in sorted(paths)
        },
    }


def core_contract_digest(root: Path) -> str:
    payload = json.dumps(
        core_contract_snapshot(root),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def bind_external_evidence(
    temp_dir: Path,
    known_valid_output: Path | None,
    agent_assessment: Path | None,
) -> dict[str, dict[str, str]]:
    manifest_path = temp_dir / "audit_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    root = Path(manifest["benchmark_root"]).resolve()
    fixture_hashes: dict[str, str] = {}
    assessment_hashes: dict[str, str] = {}
    if known_valid_output is not None:
        resolved = known_valid_output.expanduser().resolve()
        if resolved.is_relative_to(root):
            raise ValueError("known-valid output must remain outside the Harbor 题包")
        fixture_hashes["known_valid_output"] = sha256_path(
            resolved
        )
    if agent_assessment is not None:
        resolved = agent_assessment.expanduser().resolve()
        if resolved.is_relative_to(root):
            raise ValueError("agent assessment must remain outside the Harbor 题包")
        assessment_hashes["agent_assessment"] = sha256_path(
            resolved
        )
    manifest["fixture_hashes"] = fixture_hashes
    manifest["assessment_hashes"] = assessment_hashes
    manifest["core_contract_digest"] = core_contract_digest(
        Path(manifest["benchmark_root"])
    )
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    return {
        "fixture_hashes": fixture_hashes,
        "assessment_hashes": assessment_hashes,
        "core_contract_digest": manifest["core_contract_digest"],
    }


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


def collect_source_role_inventory(
    root: Path,
    *,
    paper_mode: str,
) -> dict[str, dict[str, Any]]:
    hashes = collect_input_hashes(root)
    if paper_mode == "paper_grounded":
        for relative in PAPER_EVIDENCE_ROLES:
            path = root / relative
            if path.is_file():
                hashes[relative] = sha256_file(path)
    role_types = {
        **QUALITY_EVIDENCE_ROLES,
        **PAPER_EVIDENCE_ROLES,
    }
    inventory: dict[str, dict[str, Any]] = {}
    for relative in sorted(set(hashes) | set(role_types)):
        role_type = role_types.get(
            relative,
            "json" if relative.endswith(".json") else "text",
        )
        required = relative in {
            "instruction.md",
            "tests/checker.py",
            "tests/test.sh",
        }
        if relative.startswith("paper/"):
            required = paper_mode == "paper_grounded"
            if paper_mode == "no_paper":
                inventory[relative] = {
                    "status": "NOT_IN_SCOPE",
                    "required": False,
                    "type": role_type,
                    "sha256": None,
                    "size_bytes": None,
                }
                continue
        path = root / relative
        if path.is_file():
            inventory[relative] = {
                "status": "PRESENT",
                "required": required,
                "type": role_type,
                "sha256": hashes[relative],
                "size_bytes": path.stat().st_size,
            }
        else:
            inventory[relative] = {
                "status": "ABSENT",
                "required": required,
                "type": role_type,
                "sha256": None,
                "size_bytes": None,
            }
    return inventory


def review_implementation_files(root: Path | None = None) -> tuple[str, ...]:
    root = root or skill_root()
    manifest_path = root / REVIEW_IMPLEMENTATION_FILES_MANIFEST
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if (
        not isinstance(manifest, dict)
        or manifest.get("schema_version")
        != "materials-review-implementation-files/1.0"
        or not isinstance(manifest.get("files"), list)
    ):
        raise ValueError("Review implementation file manifest is invalid")
    files = manifest["files"]
    if (
        not files
        or files != sorted(set(files))
        or REVIEW_IMPLEMENTATION_FILES_MANIFEST not in files
        or not all(isinstance(item, str) and item for item in files)
    ):
        raise ValueError("Review implementation file list is not canonical")
    for relative in files:
        relative_path = Path(relative)
        path = root / relative_path
        if (
            relative_path.is_absolute()
            or ".." in relative_path.parts
            or not path.is_file()
            or path.is_symlink()
        ):
            raise ValueError(
                f"Review implementation dependency is unsafe: {relative}"
            )
    return tuple(files)


def collect_review_implementation_hashes(
    root: Path | None = None,
) -> dict[str, Any]:
    root = root or skill_root()
    files = {
        relative: sha256_file(root / relative)
        for relative in review_implementation_files(root)
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


def audit_attestation_payload(audit_dir: Path) -> dict[str, Any]:
    manifest_path = audit_dir / "audit_manifest.json"
    report_path = audit_dir / "audit_report.json"
    disposition_path = audit_dir / "disposition.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    return {
        "audit_id": manifest["audit_id"],
        "manifest_hash": sha256_file(manifest_path),
        "report_hash": sha256_file(report_path),
        "disposition_hash": sha256_file(disposition_path),
        "fixture_hashes": manifest.get("fixture_hashes", {}),
        "assessment_hashes": manifest.get("assessment_hashes", {}),
    }


def write_audit_attestation(
    benchmark_root: Path, output_path: Path
) -> dict[str, Any]:
    benchmark_root = benchmark_root.expanduser().resolve()
    output_path = output_path.expanduser().resolve()
    if output_path.is_relative_to(benchmark_root):
        raise ValueError("audit attestation must remain outside the Harbor 题包")
    if output_path.exists() or output_path.is_symlink():
        raise FileExistsError(
            "audit attestation output is immutable and must not already exist"
        )
    payload = audit_attestation_payload(benchmark_root / "benchmark_audit")
    encoded = json.dumps(
        payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    attestation = {
        "schema_version": "materials-audit-attestation/1.0",
        **payload,
        "bundle_digest": "sha256:" + hashlib.sha256(encoded).hexdigest(),
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with output_path.open("x", encoding="utf-8") as handle:
            handle.write(
                json.dumps(attestation, indent=2, ensure_ascii=False) + "\n"
            )
    except FileExistsError as exc:
        raise FileExistsError(
            "audit attestation output is immutable and must not already exist"
        ) from exc
    output_path.chmod(0o444)
    return attestation


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
    manifest["source_role_inventory"] = collect_source_role_inventory(
        root,
        paper_mode="paper_grounded",
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
    parent_audit_id: str | None = None
    previous_manifest = root / "benchmark_audit/audit_manifest.json"
    if paper_mode == "paper_grounded" and previous_manifest.is_file():
        previous = json.loads(
            previous_manifest.read_text(encoding="utf-8")
        )
        candidate = previous.get("audit_id")
        if isinstance(candidate, str) and candidate:
            parent_audit_id = candidate
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
        "bundle_schema_version": "materials-audit-bundle/1.0",
        "audit_id": audit_id,
        "parent_audit_id": parent_audit_id,
        "review_type": (
            "PAPER_GROUNDED_REAUDIT"
            if parent_audit_id is not None
            else "INITIAL_AUDIT"
        ),
        "generated_at": started_at,
        "completed_at": None,
        "auditor_version": "materials-benchmark-review/0.1",
        "benchmark_root": str(root),
        **canonical_fields("NOT_ASSESSABLE"),
        "execution_level": execution_level,
        # Paper roles are deliberately added only after the no-paper gate
        # passes, so a terminal E0/E1 result never traverses paper content.
        "input_hashes": collect_input_hashes(root),
        "source_role_inventory": collect_source_role_inventory(
            root,
            paper_mode=paper_mode,
        ),
        "review_implementation": collect_review_implementation_hashes(),
        "core_contract_digest": core_contract_digest(root),
        "fixture_hashes": {},
        "assessment_hashes": {},
        "output_hashes": {},
        "bundle_hash": None,
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
