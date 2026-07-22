"""Single-run lifecycle and content-root helpers for materials review/repair.

This module deliberately owns coordination only.  Scientific assessment remains
in the existing review and repair modules.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import tempfile
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


RUN_CONTEXT_SCHEMA = "materials-review-run/1.0"
STATUS_SCHEMA = "materials-review-status/1.0"
AUDIT_ROOT_SCHEMA = "materials-audit-root/1.0"
REVIEW_CONTRACT_VERSION = "materials-review-contract/1"
LOCK_NAME = "lock"

TERMINAL_STATES = frozenset({"COMPLETED", "FAILED"})
ALLOWED_TRANSITIONS = {
    "ASSIGNED": {"AGENT_ASSESSMENT_PENDING", "REVIEWING", "FAILED"},
    "AGENT_ASSESSMENT_PENDING": {"REVIEWING", "FAILED"},
    "REVIEWING": {
        "AGENT_CONTRACT_PENDING",
        "AGENT_ASSESSMENT_PENDING",
        "REVIEWED",
        "FAILED",
    },
    "AGENT_CONTRACT_PENDING": {
        "REVIEWING",
        "REPAIRING",
        "AGENT_ASSESSMENT_PENDING",
        "FAILED",
    },
    # Legacy incomplete dual-lane audits may be demoted for assessment resume.
    "REVIEWED": {"COMPLETED", "REPAIRING", "FAILED", "AGENT_ASSESSMENT_PENDING"},
    "REPAIRING": {
        "AGENT_CONTRACT_PENDING",
        "AGENT_ASSESSMENT_PENDING",
        "COMPLETED",
        "FAILED",
    },
    "COMPLETED": set(),
    "FAILED": set(),
    "NOT_REQUIRED": set(),
    "REPAIRED": set(),
    "ABANDONED": set(),
}


class RunContextError(ValueError):
    """The requested run is malformed or in an illegal lifecycle state."""


class RunLockHeld(RunContextError):
    """Another review/repair process owns this package lifecycle."""


def now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _write_json_atomic(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
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


def package_id_from_path(corpus_root: Path, package: Path) -> str:
    try:
        return package.resolve().relative_to(corpus_root.resolve()).as_posix()
    except ValueError as exc:
        raise RunContextError("package must be below the corpus root") from exc


def management_root(corpus_root: Path, package_id: str) -> Path:
    parts = Path(package_id).parts
    if len(parts) != 3 or not all(parts) or any(part in {".", ".."} for part in parts):
        raise RunContextError("package_id must be cluster/theme/paper")
    return corpus_root.parent / ".review_records" / parts[0] / parts[1] / parts[2]


def create_run(corpus_root: Path, package_id: str, run_id: str) -> Path:
    package = (corpus_root / package_id).resolve()
    if not package.is_dir():
        raise RunContextError(f"package does not exist: {package_id}")
    if not run_id or "/" in run_id or run_id in {".", ".."}:
        raise RunContextError("run_id is invalid")
    run_dir = management_root(corpus_root, package_id) / "runs" / run_id
    if run_dir.exists():
        raise RunContextError(f"run already exists: {run_dir}")
    run_dir.mkdir(parents=True)
    # These are coordination-only locations. Phase directories that contain
    # package copies are created only by their owning stage.
    for name in ("agent_contract", "regressions", "roots"):
        (run_dir / name).mkdir()
    _write_json_atomic(run_dir / "agent_contract" / "assessment.json", {})
    context = {
        "schema_version": RUN_CONTEXT_SCHEMA,
        "run_id": run_id,
        "package_id": package_id,
        "package_path": str(package),
        "corpus_root": str(corpus_root.resolve()),
        "review_contract_version": REVIEW_CONTRACT_VERSION,
        "created_at": now(),
    }
    _write_json_atomic(run_dir / "context.json", context)
    _write_json_atomic(run_dir / "status.json", {"schema_version": STATUS_SCHEMA, "state": "ASSIGNED", "updated_at": now()})
    return run_dir


def load_context(run_dir: Path) -> dict[str, Any]:
    run_dir = run_dir.expanduser().resolve()
    try:
        context = json.loads((run_dir / "context.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RunContextError("run context is missing or invalid") from exc
    if context.get("schema_version") != RUN_CONTEXT_SCHEMA:
        raise RunContextError("run context schema is unsupported")
    if context.get("review_contract_version") != REVIEW_CONTRACT_VERSION:
        raise RunContextError("review contract version is incompatible")
    package = Path(context.get("package_path", ""))
    if not package.is_dir():
        raise RunContextError("run package no longer exists")
    return context


def status(run_dir: Path) -> dict[str, Any]:
    try:
        value = json.loads((run_dir / "status.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RunContextError("run status is missing or invalid") from exc
    if value.get("schema_version") != STATUS_SCHEMA or value.get("state") not in ALLOWED_TRANSITIONS:
        raise RunContextError("run status schema is invalid")
    return value


def transition(run_dir: Path, target: str, **fields: Any) -> dict[str, Any]:
    current = status(run_dir)
    if target not in ALLOWED_TRANSITIONS.get(current["state"], set()):
        raise RunContextError(f"illegal lifecycle transition: {current['state']} -> {target}")
    value = {**current, **fields, "state": target, "updated_at": now()}
    _write_json_atomic(run_dir / "status.json", value)
    return value


def complete(run_dir: Path, *, outcome: str, **fields: Any) -> dict[str, Any]:
    """Record a terminal outcome without adding outcome-specific states."""

    current = status(run_dir)
    if current["state"] not in {"REVIEWED", "REPAIRING"}:
        raise RunContextError(
            f"terminal outcome requires REVIEWED or REPAIRING, got {current['state']}"
        )
    return transition(run_dir, "COMPLETED", outcome=outcome, **fields)


def write_json_atomic(path: Path, value: Any) -> None:
    """Public atomic writer for run-local coordination artifacts."""

    _write_json_atomic(path, value)


class PackageRunLock:
    def __init__(self, run_dir: Path) -> None:
        self.path = run_dir.parent.parent / LOCK_NAME

    def __enter__(self) -> "PackageRunLock":
        self.path.parent.mkdir(parents=True, exist_ok=True)
        try:
            self.path.mkdir()
        except FileExistsError as exc:
            raise RunLockHeld(f"package lifecycle is already locked: {self.path}") from exc
        _write_json_atomic(self.path / "owner.json", {"pid": os.getpid(), "created_at": now()})
        return self

    def __exit__(self, *_: Any) -> None:
        shutil.rmtree(self.path, ignore_errors=True)


def snapshot_package(package: Path, run_dir: Path) -> Path:
    target = run_dir / "snapshot"
    if target.exists():
        raise RunContextError("snapshot already exists")
    shutil.copytree(package, target, ignore=shutil.ignore_patterns("benchmark_audit", "benchmark_repair", "review_outputs", ".review_records"))
    return target


def package_files(root: Path) -> dict[str, str]:
    """Return the byte identity used to detect a live-package race before Repair."""

    ignored = {"benchmark_audit", "benchmark_repair", "review_outputs", ".review_records"}
    return {
        path.relative_to(root).as_posix(): _file_hash(path)
        for path in sorted(root.rglob("*"))
        if path.is_file()
        and not path.is_symlink()
        and not (set(path.relative_to(root).parts) & ignored)
    }


def verify_live_package_matches_snapshot(run_dir: Path) -> None:
    context = load_context(run_dir)
    snapshot = run_dir / "snapshot"
    if not snapshot.is_dir():
        raise RunContextError("Repair requires the source snapshot")
    if package_files(Path(context["package_path"])) != package_files(snapshot):
        raise RunContextError("live package changed after A0; create a fresh run")


def _file_hash(path: Path) -> str:
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return f"sha256:{digest}"


PHASE_CONTENT = {
    "A0": ("snapshot", "audit"),
    "R0": ("snapshot", "audit", "plan.json", "candidate", "regressions", "repair_result.json"),
    "A1": ("candidate", "reaudit"),
}


def content_root(run_dir: Path, names: tuple[str, ...]) -> str:
    context = load_context(run_dir)
    entries: list[tuple[str, int, str]] = []
    for name in names:
        root = run_dir / name
        if not root.exists():
            continue
        paths = [root] if root.is_file() else root.rglob("*")
        for path in sorted(item for item in paths if item.is_file() and not item.is_symlink()):
            entries.append((path.relative_to(run_dir).as_posix(), path.stat().st_mode & 0o777, _file_hash(path)))
    payload = {
        "schema_version": AUDIT_ROOT_SCHEMA,
        "run_id": context["run_id"],
        "package_id": context["package_id"],
        "review_contract_version": context["review_contract_version"],
        "files": entries,
    }
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def write_content_root(run_dir: Path, phase: str) -> str:
    try:
        names = PHASE_CONTENT[phase]
    except KeyError as exc:
        raise RunContextError(f"unknown content-root phase: {phase}") from exc
    value = content_root(run_dir, names)
    _write_json_atomic(
        run_dir / "roots" / f"{phase}.json",
        {"schema_version": AUDIT_ROOT_SCHEMA, "phase": phase, "content_root": value},
    )
    return value


def verify_content_root(run_dir: Path, phase: str) -> str:
    try:
        names = PHASE_CONTENT[phase]
    except KeyError as exc:
        raise RunContextError(f"unknown content-root phase: {phase}") from exc
    path = run_dir / "roots" / f"{phase}.json"
    try:
        expected = json.loads(path.read_text(encoding="utf-8"))["content_root"]
    except (OSError, KeyError, json.JSONDecodeError) as exc:
        raise RunContextError(f"{phase} content root is missing") from exc
    actual = content_root(run_dir, names)
    if expected != actual:
        raise RunContextError(f"{phase} content root does not match run contents")
    return actual
