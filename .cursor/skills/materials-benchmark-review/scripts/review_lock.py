"""Per-output-root concurrency exclusion for Review publication."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import time
import uuid
from pathlib import Path
from typing import Any


LOCK_SCHEMA_VERSION = "materials-review-lock/1.0"
LOCK_NAME = ".materials_review.lock"


class ReviewLockError(RuntimeError):
    """Base class for Review lock failures."""


class ReviewLockHeld(ReviewLockError):
    """Raised when another demonstrably live Review owns the output root."""


def process_start_token(pid: int) -> str | None:
    """Return a stable process-start token, or None when it is unavailable."""

    try:
        completed = subprocess.run(
            ["ps", "-p", str(pid), "-o", "lstart="],
            capture_output=True,
            text=True,
            timeout=2,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    token = completed.stdout.strip()
    return token if completed.returncode == 0 and token else None


def process_is_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    except OSError:
        return False
    return True


class ReviewOutputLock:
    """Own one canonical Review output root for one immutable run ID.

    The lock directory is created with ``mkdir`` as the atomic acquisition
    primitive.  Owner metadata is written once inside that directory.  A
    lock is reclaimable only when the recorded process is absent, or when its
    recorded process-start token differs from the currently running process
    with the same PID.  If process identity cannot be established, the lock
    is treated as live and is never reclaimed.
    """

    def __init__(self, output_root: Path, run_id: str) -> None:
        if not run_id or Path(run_id).name != run_id:
            raise ValueError("Review lock run_id must be a non-empty leaf name")
        self.output_root = output_root.expanduser().resolve()
        self.lock_path = self.output_root / LOCK_NAME
        self.run_id = run_id
        self.pid = os.getpid()
        self.process_start = process_start_token(self.pid)
        self.nonce = uuid.uuid4().hex
        self.owner: dict[str, Any] = {
            "schema_version": LOCK_SCHEMA_VERSION,
            "output_root": str(self.output_root),
            "run_id": self.run_id,
            "pid": self.pid,
            "process_start": self.process_start,
            "created_at": time.time(),
            "nonce": self.nonce,
        }
        self._acquired = False

    @property
    def owner_token(self) -> tuple[Any, ...]:
        return (
            self.owner["run_id"],
            self.owner["pid"],
            self.owner["process_start"],
            self.owner["nonce"],
        )

    def _read_owner(self, path: Path) -> dict[str, Any] | None:
        owner_path = path / "owner.json"
        try:
            value = json.loads(owner_path.read_text(encoding="utf-8"))
        except (OSError, ValueError, json.JSONDecodeError):
            return None
        if not isinstance(value, dict):
            return None
        required = {
            "schema_version",
            "output_root",
            "run_id",
            "pid",
            "process_start",
            "created_at",
            "nonce",
        }
        if (
            value.get("schema_version") != LOCK_SCHEMA_VERSION
            or set(value) != required
            or value.get("output_root") != str(self.output_root)
            or not isinstance(value.get("run_id"), str)
            or Path(value["run_id"]).name != value["run_id"]
            or not isinstance(value.get("pid"), int)
            or isinstance(value.get("pid"), bool)
            or value["pid"] <= 0
            or not isinstance(value.get("nonce"), str)
            or not value["nonce"]
            or not isinstance(value.get("created_at"), (int, float))
            or isinstance(value.get("created_at"), bool)
        ):
            return None
        return value

    def _owner_is_demonstrably_stale(self, owner: dict[str, Any]) -> bool:
        pid = owner["pid"]
        if not process_is_alive(pid):
            return True
        recorded_start = owner.get("process_start")
        current_start = process_start_token(pid)
        if (
            isinstance(recorded_start, str)
            and recorded_start
            and isinstance(current_start, str)
            and current_start
            and recorded_start != current_start
        ):
            return True
        # A live PID without two comparable identity tokens may be the owner
        # after PID reuse.  Fail closed rather than guessing.
        return False

    def _reclaim_stale(self, owner: dict[str, Any]) -> bool:
        if not self._owner_is_demonstrably_stale(owner):
            return False
        tombstone = self.output_root / (
            f"{LOCK_NAME}.stale-{self.run_id}-{uuid.uuid4().hex}"
        )
        try:
            self.lock_path.rename(tombstone)
        except FileNotFoundError:
            return False
        except OSError:
            return False
        shutil.rmtree(tombstone, ignore_errors=False)
        return True

    def acquire(self) -> "ReviewOutputLock":
        if self._acquired:
            raise ReviewLockError("Review lock is already acquired")
        self.output_root.mkdir(parents=True, exist_ok=True)
        for _ in range(3):
            try:
                self.lock_path.mkdir(mode=0o700)
            except FileExistsError:
                owner = self._read_owner(self.lock_path)
                if owner is None:
                    raise ReviewLockHeld(
                        "Review output root is locked by an owner with "
                        "unreadable or incomplete metadata"
                    )
                if not self._reclaim_stale(owner):
                    raise ReviewLockHeld(
                        "Review output root is already locked: "
                        f"run_id={owner['run_id']} pid={owner['pid']}"
                    )
                continue
            owner_path = self.lock_path / "owner.json"
            try:
                with owner_path.open("x", encoding="utf-8") as handle:
                    json.dump(self.owner, handle, indent=2, ensure_ascii=False)
                    handle.write("\n")
                owner_path.chmod(0o444)
            except Exception:
                shutil.rmtree(self.lock_path, ignore_errors=True)
                raise
            self._acquired = True
            return self
        raise ReviewLockHeld("Review output lock changed during stale recovery")

    def release(self) -> None:
        if not self._acquired:
            return
        owner = self._read_owner(self.lock_path)
        if owner is None or (
            owner.get("run_id"),
            owner.get("pid"),
            owner.get("process_start"),
            owner.get("nonce"),
        ) != self.owner_token:
            raise ReviewLockError(
                "Review lock owner changed before release; refusing to "
                "remove another run's lock"
            )
        shutil.rmtree(self.lock_path)
        self._acquired = False

    def __enter__(self) -> "ReviewOutputLock":
        return self.acquire()

    def __exit__(self, _type: Any, _value: Any, _traceback: Any) -> None:
        self.release()
