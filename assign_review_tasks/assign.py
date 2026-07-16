#!/usr/bin/env python3
"""Atomic external dispatcher for review and repair assignments.

The registry is deliberately small and boring: all coordination state lives in
one JSON document, and all readers/writers take an OS-level sibling lock before
loading or changing it.  The parent agent owns this protocol; worker agents
only receive the claim details and must not edit the registry.
"""

from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import fcntl
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import secrets
import sys
import tempfile
from typing import Any, Iterator


SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parent.parent
DEFAULT_REGISTRY = SCRIPT_PATH.parent / "assignment_lock.json"
SCHEMA_VERSION = "assignment-lock/1.0"
MANIFEST_RELATIVE_PATH = (
    "review_artifacts/materials_bench_whitelist_100_20260716/manifest.json"
)

OPERATIONS = {"REVIEW", "REPAIR"}
OUTCOMES = {"PASS", "CONDITIONAL", "REJECT", "NOT_ASSESSABLE"}
STATES = {
    "AVAILABLE",
    "REVIEWING",
    "ACCEPTED",
    "REVIEWED_CONDITIONAL",
    "REVIEWED_REJECT",
    "REVIEWED_NOT_ASSESSABLE",
    "REPAIRING",
    "ABANDONED",
}
ACTIVE_STATES = {"REVIEWING", "REPAIRING"}
HISTORY_EVENTS = {
    "CLAIMED",
    "HEARTBEAT",
    "COMPLETED",
    "RELEASED",
    "ABANDONED",
    "EXPIRED",
}
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
CLUSTER_RE = re.compile(r"^cluster-.+$")
PAPER_RE = re.compile(r"^paper-.+$")


class AssignmentError(Exception):
    """A safe, user-facing dispatcher error."""


def _timestamp() -> str:
    return (
        dt.datetime.now(dt.timezone.utc)
        .isoformat(timespec="microseconds")
        .replace("+00:00", "Z")
    )


def _parse_timestamp(value: Any, field: str) -> dt.datetime:
    if not isinstance(value, str) or not value.endswith("Z"):
        raise AssignmentError(f"{field} must be a UTC ISO timestamp ending in Z")
    try:
        parsed = dt.datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError as exc:
        raise AssignmentError(f"{field} is not a valid UTC ISO timestamp") from exc
    if parsed.tzinfo != dt.timezone.utc:
        raise AssignmentError(f"{field} must use UTC")
    return parsed


def _is_nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value)


def validate_package_id(package_id: Any) -> str:
    """Validate the exact three-segment dispatcher identity."""

    if not isinstance(package_id, str) or not package_id:
        raise AssignmentError("package_id must be a nonempty string")
    if "\x00" in package_id or "\\" in package_id:
        raise AssignmentError("package_id must use POSIX path segments only")
    if package_id.startswith("/") or package_id.endswith("/"):
        raise AssignmentError("package_id must be a relative path")
    parts = package_id.split("/")
    if len(parts) != 3 or any(not part for part in parts):
        raise AssignmentError(
            "package_id must be exactly cluster-id/theme/paper-id"
        )
    if any(part in {".", ".."} for part in parts):
        raise AssignmentError("package_id cannot contain . or .. segments")
    if not CLUSTER_RE.fullmatch(parts[0]):
        raise AssignmentError("package_id cluster segment must match cluster-*")
    if not PAPER_RE.fullmatch(parts[2]):
        raise AssignmentError("package_id paper segment must match paper-*")
    return package_id


def _safe_relative_path(value: Any, field: str) -> Path:
    if not isinstance(value, str) or not value:
        raise AssignmentError(f"{field} must be a nonempty relative path")
    if "\x00" in value or "\\" in value:
        raise AssignmentError(f"{field} must use POSIX path syntax")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in {".", "..", ""} for part in path.parts):
        raise AssignmentError(f"{field} must not be absolute or contain . or ..")
    return Path(*path.parts)


def _source_manifest_path(source: dict[str, Any]) -> Path:
    relative = _safe_relative_path(source.get("manifest"), "source.manifest")
    candidate = REPO_ROOT / relative
    try:
        resolved = candidate.resolve(strict=True)
        resolved.relative_to(REPO_ROOT)
    except (FileNotFoundError, OSError, ValueError) as exc:
        raise AssignmentError(
            f"source manifest is missing or outside the repository: {relative}"
        ) from exc
    if not resolved.is_file():
        raise AssignmentError(f"source manifest is not a file: {relative}")
    return candidate


def _manifest_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    try:
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
    except OSError as exc:
        raise AssignmentError(f"cannot read source manifest: {path}") from exc
    return digest.hexdigest()


def _validate_source(source: Any) -> Path:
    if not isinstance(source, dict):
        raise AssignmentError("registry source must be an object")
    if set(source) != {"manifest", "sha256"}:
        raise AssignmentError("registry source must contain manifest and sha256")
    if source.get("manifest") != MANIFEST_RELATIVE_PATH:
        raise AssignmentError(
            f"source.manifest must be {MANIFEST_RELATIVE_PATH}"
        )
    if not isinstance(source.get("sha256"), str) or not SHA256_RE.fullmatch(
        source["sha256"]
    ):
        raise AssignmentError("source.sha256 must be a lowercase SHA-256 hash")
    path = _source_manifest_path(source)
    actual = _manifest_sha256(path)
    if actual != source["sha256"]:
        raise AssignmentError(
            f"source manifest hash mismatch: expected {source['sha256']}, got {actual}"
        )
    return path


def _manifest_seed_ids(path: Path) -> set[str]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            manifest = json.load(handle)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise AssignmentError(f"source manifest is malformed: {path}") from exc
    if not isinstance(manifest, dict) or not isinstance(manifest.get("tasks"), list):
        raise AssignmentError("source manifest must contain a tasks list")
    package_ids: list[str] = []
    for task in manifest["tasks"]:
        if not isinstance(task, dict):
            raise AssignmentError("source manifest task must be an object")
        package_ids.append(validate_package_id(task.get("relpath")))
    if len(package_ids) != 100 or len(set(package_ids)) != 100:
        raise AssignmentError(
            "source manifest must contain exactly 100 unique canonical identities"
        )
    return set(package_ids)


def _validate_history(history: Any, package_id: str) -> None:
    if not isinstance(history, list):
        raise AssignmentError(f"history for {package_id} must be a list")
    previous: dt.datetime | None = None
    for index, event in enumerate(history):
        if not isinstance(event, dict):
            raise AssignmentError(f"history event {index} for {package_id} is invalid")
        if event.get("event") not in HISTORY_EVENTS:
            raise AssignmentError(f"history event {index} for {package_id} is invalid")
        current = _parse_timestamp(event.get("at"), f"history[{index}].at")
        if previous is not None and current < previous:
            raise AssignmentError(f"history for {package_id} is not chronological")
        previous = current
        if not _is_nonempty_string(event.get("owner")):
            raise AssignmentError(f"history event {index} owner is invalid")
        if event.get("operation") not in OPERATIONS:
            raise AssignmentError(f"history event {index} operation is invalid")
        if "reason" in event and not isinstance(event["reason"], str):
            raise AssignmentError(f"history event {index} reason is invalid")
        if "outcome" in event and event["outcome"] not in OUTCOMES:
            raise AssignmentError(f"history event {index} outcome is invalid")


def _validate_active_claim(
    active_claim: Any, state: str, package_id: str
) -> None:
    if active_claim is None:
        if state in ACTIVE_STATES:
            raise AssignmentError(f"active state {state} lacks a claim")
        return
    if state not in ACTIVE_STATES or not isinstance(active_claim, dict):
        raise AssignmentError(f"active claim is invalid for {package_id}")
    required = {
        "claimed_at",
        "lease_expires_at",
        "lease_seconds",
        "operation",
        "owner",
        "previous_state",
        "token",
    }
    if set(active_claim) != required:
        raise AssignmentError(f"active claim fields are invalid for {package_id}")
    if not _is_nonempty_string(active_claim["owner"]):
        raise AssignmentError(f"active claim owner is invalid for {package_id}")
    if not _is_nonempty_string(active_claim["token"]):
        raise AssignmentError(f"active claim token is invalid for {package_id}")
    if active_claim["operation"] not in OPERATIONS:
        raise AssignmentError(f"active claim operation is invalid for {package_id}")
    if not isinstance(active_claim["lease_seconds"], int) or isinstance(
        active_claim["lease_seconds"], bool
    ) or active_claim["lease_seconds"] <= 0:
        raise AssignmentError(f"active claim lease_seconds is invalid for {package_id}")
    claimed_at = _parse_timestamp(
        active_claim["claimed_at"], "active_claim.claimed_at"
    )
    expires_at = _parse_timestamp(
        active_claim["lease_expires_at"], "active_claim.lease_expires_at"
    )
    if expires_at <= claimed_at:
        raise AssignmentError(f"active claim lease is invalid for {package_id}")
    previous_state = active_claim["previous_state"]
    expected = {
        "REVIEWING": ("REVIEW", "AVAILABLE"),
        "REPAIRING": ("REPAIR", "REVIEWED_CONDITIONAL"),
    }[state]
    if (active_claim["operation"], previous_state) != expected:
        raise AssignmentError(f"active claim transition is invalid for {package_id}")


def _validate_entry(entry: Any, seen: set[str]) -> None:
    if not isinstance(entry, dict):
        raise AssignmentError("each registry entry must be an object")
    expected_fields = {
        "active_claim",
        "history",
        "operation",
        "package_id",
        "result",
        "source",
        "state",
    }
    if set(entry) != expected_fields:
        raise AssignmentError("registry entry fields are invalid")
    package_id = validate_package_id(entry.get("package_id"))
    if package_id in seen:
        raise AssignmentError(f"duplicate package_id: {package_id}")
    seen.add(package_id)
    state = entry.get("state")
    if state not in STATES:
        raise AssignmentError(f"invalid state for {package_id}: {state}")
    if entry.get("operation") is not None and entry["operation"] not in OPERATIONS:
        raise AssignmentError(f"invalid operation for {package_id}")
    if entry.get("result") is not None and entry["result"] not in OUTCOMES:
        raise AssignmentError(f"invalid result for {package_id}")
    if not _is_nonempty_string(entry.get("source")):
        raise AssignmentError(f"source is invalid for {package_id}")
    _validate_active_claim(entry.get("active_claim"), state, package_id)
    expected_by_state = {
        "AVAILABLE": (None, None),
        "REVIEWING": ("REVIEW", None),
        "ACCEPTED": ({"REVIEW", "REPAIR"}, "PASS"),
        "REVIEWED_CONDITIONAL": ("REVIEW", "CONDITIONAL"),
        "REVIEWED_REJECT": ("REVIEW", "REJECT"),
        "REVIEWED_NOT_ASSESSABLE": ("REVIEW", "NOT_ASSESSABLE"),
        "REPAIRING": ("REPAIR", None),
        "ABANDONED": ("REPAIR", None),
    }[state]
    expected_operation, expected_result = expected_by_state
    if isinstance(expected_operation, set):
        if entry["operation"] not in expected_operation:
            raise AssignmentError(f"invalid operation transition for {package_id}")
    elif entry["operation"] != expected_operation:
        raise AssignmentError(f"invalid operation transition for {package_id}")
    if isinstance(expected_result, set):
        if entry["result"] not in expected_result:
            raise AssignmentError(f"invalid result transition for {package_id}")
    elif entry["result"] != expected_result:
        raise AssignmentError(f"invalid result transition for {package_id}")
    _validate_history(entry.get("history"), package_id)


def validate_registry(data: Any) -> None:
    if not isinstance(data, dict):
        raise AssignmentError("registry root must be an object")
    if set(data) != {"entries", "schema_version", "source"}:
        raise AssignmentError(
            "registry must contain exactly entries, schema_version, and source"
        )
    if data.get("schema_version") != SCHEMA_VERSION:
        raise AssignmentError("unsupported registry schema_version")
    source_manifest = _validate_source(data.get("source"))
    entries = data.get("entries")
    if not isinstance(entries, list):
        raise AssignmentError("registry entries must be a list")
    seen: set[str] = set()
    previous: str | None = None
    for entry in entries:
        _validate_entry(entry, seen)
        package_id = entry["package_id"]
        if previous is not None and package_id <= previous:
            raise AssignmentError("registry entries must be sorted by package_id")
        previous = package_id
    expected_seed_ids = _manifest_seed_ids(source_manifest)
    seed_entries = [
        entry
        for entry in entries
        if entry["source"] == "historical-v9-maintainer-accepted"
    ]
    actual_seed_ids = {entry["package_id"] for entry in seed_entries}
    if actual_seed_ids != expected_seed_ids or len(seed_entries) != 100:
        missing = sorted(expected_seed_ids - actual_seed_ids)
        extra = sorted(actual_seed_ids - expected_seed_ids)
        raise AssignmentError(
            "historical seed identities do not exactly match the source manifest "
            f"(missing={missing}, extra={extra})"
        )
    if any(
        entry["state"] != "ACCEPTED"
        or entry["operation"] != "REVIEW"
        or entry["result"] != "PASS"
        or entry["active_claim"] is not None
        for entry in seed_entries
    ):
        raise AssignmentError(
            "historical seed entries must be ACCEPTED/REVIEW/PASS with no active claim"
        )


def _load_registry(registry: Path) -> dict[str, Any]:
    try:
        with registry.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except FileNotFoundError as exc:
        raise AssignmentError(f"registry does not exist: {registry}") from exc
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise AssignmentError(f"registry is malformed: {registry}") from exc
    validate_registry(data)
    return data


@contextlib.contextmanager
def _registry_lock(registry: Path) -> Iterator[None]:
    if not registry.parent.exists():
        raise AssignmentError(f"registry parent does not exist: {registry.parent}")
    guard = Path(str(registry) + ".lock")
    try:
        handle = guard.open("a+b")
    except OSError as exc:
        raise AssignmentError(f"cannot open registry guard: {guard}") from exc
    try:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        yield
    finally:
        fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        handle.close()


def _fsync_directory(directory: Path) -> None:
    try:
        descriptor = os.open(str(directory), os.O_RDONLY)
    except OSError:
        return
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _atomic_write(registry: Path, data: dict[str, Any]) -> None:
    temporary: str | None = None
    try:
        with tempfile.NamedTemporaryFile(
            "w",
            encoding="utf-8",
            dir=registry.parent,
            prefix=f".{registry.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            temporary = handle.name
            json.dump(
                data,
                handle,
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            )
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, registry)
        temporary = None
        _fsync_directory(registry.parent)
    except OSError as exc:
        raise AssignmentError(f"could not atomically write registry: {registry}") from exc
    finally:
        if temporary is not None:
            try:
                os.unlink(temporary)
            except FileNotFoundError:
                pass


def _entry_map(data: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {entry["package_id"]: entry for entry in data["entries"]}


def _new_entry(package_id: str) -> dict[str, Any]:
    return {
        "active_claim": None,
        "history": [],
        "operation": None,
        "package_id": package_id,
        "result": None,
        "source": "dispatcher",
        "state": "AVAILABLE",
    }


def _append_history(
    entry: dict[str, Any],
    event: str,
    *,
    owner: str,
    operation: str,
    token: str | None = None,
    outcome: str | None = None,
    reason: str | None = None,
    at: str | None = None,
) -> None:
    record: dict[str, Any] = {
        "at": at or _timestamp(),
        "event": event,
        "operation": operation,
        "owner": owner,
    }
    if outcome is not None:
        record["outcome"] = outcome
    if reason is not None:
        record["reason"] = reason
    if token is not None:
        record["token"] = token
    entry["history"].append(record)


def _find_entry(
    data: dict[str, Any], package_id: str
) -> dict[str, Any] | None:
    return _entry_map(data).get(package_id)


def _claimable(entry: dict[str, Any] | None, operation: str) -> bool:
    if entry is None:
        return False
    if entry["active_claim"] is not None:
        return False
    if operation == "REVIEW":
        return entry["state"] == "AVAILABLE"
    return entry["state"] == "REVIEWED_CONDITIONAL"


def _restore_previous_state(
    entry: dict[str, Any], active: dict[str, Any]
) -> str:
    previous_state = active["previous_state"]
    entry["active_claim"] = None
    entry["state"] = previous_state
    if previous_state == "AVAILABLE":
        entry["operation"] = None
        entry["result"] = None
    else:
        entry["operation"] = "REVIEW"
        entry["result"] = "CONDITIONAL"
    return previous_state


def _expired_claim_can_reclaim(
    entry: dict[str, Any] | None, operation: str
) -> bool:
    if entry is None or entry["active_claim"] is None:
        return False
    active = entry["active_claim"]
    expired = _parse_timestamp(
        active["lease_expires_at"], "active_claim.lease_expires_at"
    ) <= dt.datetime.now(dt.timezone.utc)
    if not expired:
        return False
    return (
        operation == "REVIEW" and active["previous_state"] == "AVAILABLE"
    ) or (
        operation == "REPAIR"
        and active["previous_state"] == "REVIEWED_CONDITIONAL"
    )


def _check_owner_token(
    entry: dict[str, Any] | None, owner: str, token: str
) -> dict[str, Any]:
    if entry is None or entry["active_claim"] is None:
        raise AssignmentError("package has no active claim")
    active = entry["active_claim"]
    if active["owner"] != owner or active["token"] != token:
        raise AssignmentError("owner and token do not match the active claim")
    if _parse_timestamp(active["lease_expires_at"], "lease_expires_at") <= dt.datetime.now(
        dt.timezone.utc
    ):
        raise AssignmentError("claim lease has expired; reclaim it explicitly")
    return active


def _claim_response(entry: dict[str, Any]) -> dict[str, Any]:
    active = entry["active_claim"]
    return {
        "expires_at": active["lease_expires_at"],
        "operation": active["operation"],
        "owner": active["owner"],
        "package_id": entry["package_id"],
        "previous_state": active["previous_state"],
        "token": active["token"],
    }


def _claim_entry(
    data: dict[str, Any],
    package_id: str,
    operation: str,
    owner: str,
    lease_seconds: int,
    reclaim_expired: bool,
    allow_create: bool = False,
) -> dict[str, Any]:
    entries = _entry_map(data)
    entry = entries.get(package_id)
    if entry is None:
        if not allow_create:
            raise AssignmentError(
                "package is absent from the registry; use claim-next with a "
                "validated corpus or manifest"
            )
        if operation != "REVIEW":
            raise AssignmentError("new entries can only be claimed for REVIEW")
        entry = _new_entry(package_id)
        data["entries"].append(entry)
        entries[package_id] = entry
    elif entry["active_claim"] is not None:
        active = entry["active_claim"]
        expired = _parse_timestamp(
            active["lease_expires_at"], "active_claim.lease_expires_at"
        ) <= dt.datetime.now(dt.timezone.utc)
        if not expired:
            raise AssignmentError("package already has an active claim")
        if not reclaim_expired:
            raise AssignmentError(
                "claim lease has expired; pass --reclaim-expired explicitly"
            )
        old_operation = active["operation"]
        old_owner = active["owner"]
        old_token = active["token"]
        _restore_previous_state(entry, active)
        _append_history(
            entry,
            "EXPIRED",
            owner=old_owner,
            operation=old_operation,
            token=old_token,
            reason="lease expired and was explicitly reclaimed",
        )
    if not _claimable(entry, operation):
        raise AssignmentError(
            f"package is not assignable for {operation}: state={entry['state']}"
        )
    previous_state = entry["state"]
    # Hex avoids an option-looking leading "-" when the handoff is copied to
    # a subprocess command line while retaining 256 bits of randomness.
    token = secrets.token_hex(32)
    claimed_at = _timestamp()
    expires_at = (
        dt.datetime.fromisoformat(claimed_at[:-1] + "+00:00")
        + dt.timedelta(seconds=lease_seconds)
    ).isoformat(timespec="microseconds").replace("+00:00", "Z")
    entry["state"] = "REVIEWING" if operation == "REVIEW" else "REPAIRING"
    entry["operation"] = operation
    entry["result"] = None
    entry["active_claim"] = {
        "claimed_at": claimed_at,
        "lease_expires_at": expires_at,
        "lease_seconds": lease_seconds,
        "operation": operation,
        "owner": owner,
        "previous_state": previous_state,
        "token": token,
    }
    _append_history(
        entry,
        "CLAIMED",
        owner=owner,
        operation=operation,
        token=token,
        at=claimed_at,
    )
    data["entries"].sort(key=lambda item: item["package_id"])
    return _claim_response(entry)


def _scan_corpus(corpus: Path) -> list[str]:
    try:
        root_stat = corpus.lstat()
    except OSError as exc:
        raise AssignmentError(f"corpus does not exist: {corpus}") from exc
    if not corpus.is_dir() or corpus.is_symlink():
        raise AssignmentError("corpus must be a real directory, not a symlink")

    package_ids: list[str] = []

    def directories(path: Path) -> list[Path]:
        try:
            children = list(path.iterdir())
        except OSError as exc:
            raise AssignmentError(f"cannot read corpus directory: {path}") from exc
        result: list[Path] = []
        for child in children:
            try:
                child_stat = child.lstat()
            except OSError as exc:
                raise AssignmentError(f"cannot inspect corpus path: {child}") from exc
            if child.is_symlink():
                # A symlink can never supply a canonical package identity.
                raise AssignmentError(f"symlink-derived identity is forbidden: {child}")
            if child_stat and child.is_dir():
                result.append(child)
        return result

    for cluster in directories(corpus):
        if not CLUSTER_RE.fullmatch(cluster.name):
            continue
        for theme in directories(cluster):
            if not theme.name:
                continue
            for paper in directories(theme):
                if not PAPER_RE.fullmatch(paper.name):
                    continue
                package_ids.append(
                    validate_package_id(
                        f"{cluster.name}/{theme.name}/{paper.name}"
                    )
                )
    return sorted(set(package_ids))


def _manifest_package_ids(manifest: Path) -> list[str]:
    if manifest.is_symlink():
        raise AssignmentError("manifest symlink is not allowed")
    try:
        with manifest.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise AssignmentError(f"manifest is unreadable or malformed: {manifest}") from exc
    if not isinstance(data, dict) or not isinstance(data.get("tasks"), list):
        raise AssignmentError("manifest must contain a tasks list")
    result: list[str] = []
    seen: set[str] = set()
    for task in data["tasks"]:
        if not isinstance(task, dict):
            raise AssignmentError("manifest task must be an object")
        package_id = validate_package_id(task.get("relpath"))
        if package_id in seen:
            raise AssignmentError(f"manifest contains duplicate package_id: {package_id}")
        seen.add(package_id)
        result.append(package_id)
    return result


def _write_result(result: Any) -> None:
    json.dump(result, sys.stdout, ensure_ascii=False, sort_keys=True)
    sys.stdout.write("\n")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Coordinate parent-owned review and repair claims."
    )
    parser.add_argument("--registry", default=None, help="registry JSON path")
    commands = parser.add_subparsers(dest="command", required=True)

    def registry_option(command: argparse.ArgumentParser) -> None:
        command.add_argument(
            "--registry", default=argparse.SUPPRESS, help="registry JSON path"
        )

    list_command = commands.add_parser("list", help="list validated registry entries")
    registry_option(list_command)

    claim = commands.add_parser("claim", help="claim one package")
    registry_option(claim)
    claim.add_argument("--package-id", required=True)
    claim.add_argument("--operation", required=True, choices=sorted(OPERATIONS))
    claim.add_argument("--owner", required=True)
    claim.add_argument("--lease-seconds", type=int, default=3600)
    claim.add_argument("--reclaim-expired", action="store_true")

    claim_next = commands.add_parser("claim-next", help="claim the next packages")
    registry_option(claim_next)
    claim_next.add_argument("--owner", required=True)
    claim_next.add_argument("--operation", required=True, choices=sorted(OPERATIONS))
    claim_next.add_argument("--count", type=int, required=True)
    claim_next.add_argument("--reclaim-expired", action="store_true")
    candidates = claim_next.add_mutually_exclusive_group(required=True)
    candidates.add_argument("--corpus")
    candidates.add_argument("--manifest")

    heartbeat = commands.add_parser("heartbeat", help="extend one lease")
    registry_option(heartbeat)
    heartbeat.add_argument("--package-id", required=True)
    heartbeat.add_argument("--owner", required=True)
    heartbeat.add_argument("--token", required=True)

    complete = commands.add_parser("complete", help="complete one claim")
    registry_option(complete)
    complete.add_argument("--package-id", required=True)
    complete.add_argument("--owner", required=True)
    complete.add_argument("--token", required=True)
    complete.add_argument("--outcome", required=True, choices=sorted(OUTCOMES))

    for name, help_text in (
        ("release", "release one claim"),
        ("abandon", "abandon one claim"),
    ):
        command = commands.add_parser(name, help=help_text)
        registry_option(command)
        command.add_argument("--package-id", required=True)
        command.add_argument("--owner", required=True)
        command.add_argument("--token", required=True)
        command.add_argument("--reason", required=True)

    validate = commands.add_parser("validate", help="validate registry and source hash")
    registry_option(validate)
    return parser


def _registry_from_args(args: argparse.Namespace) -> Path:
    value = getattr(args, "registry", None)
    return Path(value).expanduser() if value else DEFAULT_REGISTRY


def _ensure_owner(owner: str) -> None:
    if not _is_nonempty_string(owner):
        raise AssignmentError("owner must be nonempty")


def _ensure_lease(lease_seconds: int) -> None:
    if (
        not isinstance(lease_seconds, int)
        or isinstance(lease_seconds, bool)
        or lease_seconds <= 0
    ):
        raise AssignmentError("lease-seconds must be a positive integer")


def _command(args: argparse.Namespace) -> Any:
    registry = _registry_from_args(args)
    command = args.command
    if command == "list":
        with _registry_lock(registry):
            data = _load_registry(registry)
            return {"entries": data["entries"]}

    if command == "validate":
        with _registry_lock(registry):
            data = _load_registry(registry)
            return {
                "entries": len(data["entries"]),
                "registry": str(registry),
                "valid": True,
            }

    if command == "claim":
        package_id = validate_package_id(args.package_id)
        _ensure_owner(args.owner)
        _ensure_lease(args.lease_seconds)
        with _registry_lock(registry):
            data = _load_registry(registry)
            result = _claim_entry(
                data,
                package_id,
                args.operation,
                args.owner,
                args.lease_seconds,
                args.reclaim_expired,
            )
            _atomic_write(registry, data)
            return result

    if command == "claim-next":
        _ensure_owner(args.owner)
        if args.count <= 0:
            raise AssignmentError("count must be a positive integer")
        with _registry_lock(registry):
            data = _load_registry(registry)
            package_ids = (
                _scan_corpus(Path(args.corpus))
                if args.corpus is not None
                else _manifest_package_ids(Path(args.manifest))
            )
            claims: list[dict[str, Any]] = []
            for package_id in package_ids:
                entry = _find_entry(data, package_id)
                can_create = entry is None and args.operation == "REVIEW"
                can_reclaim = (
                    args.reclaim_expired
                    and _expired_claim_can_reclaim(entry, args.operation)
                )
                if not (
                    can_create
                    or _claimable(entry, args.operation)
                    or can_reclaim
                ):
                    continue
                claims.append(
                    _claim_entry(
                        data,
                        package_id,
                        args.operation,
                        args.owner,
                        3600,
                        args.reclaim_expired,
                        allow_create=can_create,
                    )
                )
                if len(claims) == args.count:
                    break
            if claims:
                _atomic_write(registry, data)
            return {"claims": claims}

    package_id = validate_package_id(args.package_id)
    _ensure_owner(args.owner)
    if command in {"heartbeat", "complete", "release", "abandon"}:
        with _registry_lock(registry):
            data = _load_registry(registry)
            entry = _find_entry(data, package_id)
            active = _check_owner_token(entry, args.owner, args.token)
            if command == "heartbeat":
                now = _timestamp()
                expires = (
                    dt.datetime.fromisoformat(now[:-1] + "+00:00")
                    + dt.timedelta(seconds=active["lease_seconds"])
                ).isoformat(timespec="microseconds").replace("+00:00", "Z")
                active["lease_expires_at"] = expires
                _append_history(
                    entry,
                    "HEARTBEAT",
                    owner=args.owner,
                    operation=active["operation"],
                    token=args.token,
                    at=now,
                )
                _atomic_write(registry, data)
                return _claim_response(entry)

            if command == "complete":
                operation = active["operation"]
                if operation == "REVIEW":
                    state_by_outcome = {
                        "PASS": "ACCEPTED",
                        "CONDITIONAL": "REVIEWED_CONDITIONAL",
                        "REJECT": "REVIEWED_REJECT",
                        "NOT_ASSESSABLE": "REVIEWED_NOT_ASSESSABLE",
                    }
                    next_state = state_by_outcome[args.outcome]
                else:
                    if args.outcome != "PASS":
                        raise AssignmentError("REPAIR completion must be PASS")
                    next_state = "ACCEPTED"
                entry["active_claim"] = None
                entry["state"] = next_state
                entry["operation"] = operation
                entry["result"] = args.outcome
                _append_history(
                    entry,
                    "COMPLETED",
                    owner=args.owner,
                    operation=operation,
                    token=args.token,
                    outcome=args.outcome,
                )
                _atomic_write(registry, data)
                return {
                    "outcome": args.outcome,
                    "package_id": package_id,
                    "state": next_state,
                }

            if not isinstance(args.reason, str) or not args.reason:
                raise AssignmentError("reason must be nonempty")
            if command == "release":
                previous_state = _restore_previous_state(entry, active)
                _append_history(
                    entry,
                    "RELEASED",
                    owner=args.owner,
                    operation=active["operation"],
                    token=args.token,
                    reason=args.reason,
                )
                _atomic_write(registry, data)
                return {"package_id": package_id, "state": previous_state}

            if active["operation"] != "REPAIR":
                raise AssignmentError(
                    "abandon is only valid for an active REPAIR claim"
                )
            entry["active_claim"] = None
            entry["state"] = "ABANDONED"
            entry["operation"] = active["operation"]
            entry["result"] = None
            _append_history(
                entry,
                "ABANDONED",
                owner=args.owner,
                operation=active["operation"],
                token=args.token,
                reason=args.reason,
            )
            _atomic_write(registry, data)
            return {"package_id": package_id, "state": "ABANDONED"}

    raise AssignmentError(f"unsupported command: {command}")


def main(argv: list[str] | None = None) -> int:
    parser = _parser()
    try:
        args = parser.parse_args(argv)
        _write_result(_command(args))
        return 0
    except AssignmentError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    except (OSError, ValueError, TypeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
