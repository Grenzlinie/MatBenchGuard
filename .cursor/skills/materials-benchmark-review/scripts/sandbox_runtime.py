#!/usr/bin/env python3
"""Run checker commands in the disposable prebuilt Docker sandbox.

The sandbox image contains the common materials-science stack.  A caller may
provide additional distribution names; those are installed for the single
container invocation with ``uv run --with`` and are cached outside the
container.  Docker/image/cache setup failures raise :class:`SandboxEnvError`
so callers can abort the operation, while a non-zero checker exit is returned
as a normal ``subprocess.CompletedProcess`` result.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import tempfile
import uuid
from collections.abc import Iterable, Mapping, Sequence
from pathlib import Path
from typing import TypeAlias

PathLike: TypeAlias = str | os.PathLike[str]
Mounts: TypeAlias = (
    Mapping[PathLike, PathLike | tuple[PathLike, str]]
    | Iterable[tuple[PathLike, PathLike] | tuple[PathLike, PathLike, str]]
)

DEFAULT_IMAGE_TAG = "qa-checker:1.0"
DEFAULT_PYTHON_VERSION = "3.11"
DEFAULT_WORKDIR = "/workspace"
UV_CACHE_CONTAINER = "/root/.cache/uv"
PREFLIGHT_TIMEOUT_SECONDS = 10.0

_SCRIPT_DIR = Path(__file__).resolve().parent
SANDBOX_DIR = _SCRIPT_DIR / "sandbox"
DOCKERFILE = SANDBOX_DIR / "Dockerfile"
BUILD_HELPER = SANDBOX_DIR / "build_qa_checker.sh"
_REPOSITORY_ROOT = _SCRIPT_DIR.parents[3]
DEFAULT_UV_CACHE_DIR = _REPOSITORY_ROOT / ".venv_qa" / "uv-cache"

# These distributions are installed by the image Dockerfile.  The names are
# normalized before comparison so import-derived names and constrained
# requirements do not unnecessarily trigger a second install.
BAKED_PACKAGES = frozenset(
    {
        "ase",
        "h5py",
        "lmfit",
        "matplotlib",
        "netcdf4",
        "networkx",
        "numpy",
        "pandas",
        "phonopy",
        "pint",
        "pip",
        "pymatgen",
        "scikit-image",
        "scikit-learn",
        "scipy",
        "seekpath",
        "spglib",
        "sympy",
        "uncertainties",
    }
)

__all__ = [
    "BAKED_PACKAGES",
    "BUILD_HELPER",
    "DOCKERFILE",
    "SandboxEnvError",
    "DEFAULT_IMAGE_TAG",
    "DEFAULT_PYTHON_VERSION",
    "DEFAULT_UV_CACHE_DIR",
    "Mounts",
    "SANDBOX_DIR",
    "SandboxResult",
    "build_command",
    "ensure_env",
    "image_tag",
    "run_in_sandbox",
    "uv_cache_dir",
]


SandboxResult = subprocess.CompletedProcess[str]


class SandboxEnvError(RuntimeError):
    """Raised when Docker, the checker image, or the uv cache is not ready."""

    def __init__(self, reason: str, *, tag: str | None = None) -> None:
        self.reason = reason
        self.image = tag or image_tag()
        self.fix_hint = f"Build it once with: {build_command(self.image)}"
        super().__init__(f"{reason} {self.fix_hint}")


def image_tag() -> str:
    """Return the configured local checker image tag."""
    configured = (
        os.environ.get("MATERIALS_CHECKER_IMAGE_TAG")
        or os.environ.get("MATERIALS_CHECKER_IMAGE")
        or DEFAULT_IMAGE_TAG
    ).strip()
    return configured or DEFAULT_IMAGE_TAG


def uv_cache_dir() -> Path:
    """Return the host directory used for the shared uv download cache."""
    configured = os.environ.get("MATERIALS_CHECKER_UV_CACHE_DIR", "").strip()
    return Path(configured).expanduser() if configured else DEFAULT_UV_CACHE_DIR


def build_command(tag: str | None = None) -> str:
    """Return the operator command that builds the configured image."""
    return " ".join(
        (
            "docker",
            "build",
            "-f",
            _shell_quote(DOCKERFILE),
            "-t",
            _shell_quote(tag or image_tag()),
            _shell_quote(SANDBOX_DIR),
        )
    )


def _shell_quote(value: PathLike) -> str:
    value_text = os.fspath(value)
    # The build hint is intended to be pasted into a POSIX shell.
    return "'" + value_text.replace("'", "'\\''") + "'"


def _probe(
    docker: str, arguments: Sequence[str]
) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(
            [docker, *arguments],
            capture_output=True,
            text=True,
            timeout=PREFLIGHT_TIMEOUT_SECONDS,
            check=False,
        )
    except FileNotFoundError as exc:
        raise SandboxEnvError(
            "Docker disappeared while checking the sandbox environment."
        ) from exc
    except subprocess.TimeoutExpired as exc:
        raise SandboxEnvError(
            "Docker did not respond while checking the sandbox environment."
        ) from exc
    except OSError as exc:
        raise SandboxEnvError(
            f"Could not invoke Docker while checking the sandbox environment: "
            f"{exc}"
        ) from exc


def _probe_error(result: subprocess.CompletedProcess[str]) -> str:
    output = (result.stderr or result.stdout or "").strip()
    if len(output) > 500:
        output = output[-500:]
    return output


def _ensure_writable_cache(path: Path) -> Path:
    try:
        path.mkdir(parents=True, exist_ok=True)
        if not path.is_dir():
            raise NotADirectoryError(path)
        with tempfile.NamedTemporaryFile(
            mode="wb", prefix=".write-test-", dir=path, delete=True
        ) as handle:
            handle.write(b"")
            handle.flush()
    except OSError as exc:
        raise SandboxEnvError(
            f"The uv cache directory is not writable: {path}"
        ) from exc
    return path


def ensure_env(cache_dir: PathLike | None = None) -> Path:
    """Validate Docker, the prebuilt image, and the writable uv cache.

    The returned path is the host cache directory that should be mounted by
    :func:`run_in_sandbox`.  All setup failures are operator errors, never
    per-package checker results.
    """
    docker = shutil.which("docker")
    tag = image_tag()
    if docker is None:
        raise SandboxEnvError(
            "Docker CLI is not available on PATH; start/install Docker before "
            "running the sandbox.",
            tag=tag,
        )

    daemon = _probe(docker, ["info"])
    if daemon.returncode != 0:
        detail = _probe_error(daemon)
        suffix = f" ({detail})" if detail else ""
        raise SandboxEnvError(
            f"Docker daemon is not reachable{suffix}; start Docker first.",
            tag=tag,
        )

    image = _probe(docker, ["image", "inspect", tag])
    if image.returncode != 0:
        detail = _probe_error(image)
        suffix = f" ({detail})" if detail else ""
        raise SandboxEnvError(
            f"Required checker image {tag!r} is not present locally{suffix}.",
            tag=tag,
        )

    return _ensure_writable_cache(
        Path(cache_dir).expanduser() if cache_dir is not None else uv_cache_dir()
    )


def _normalized_package_name(package: str) -> str:
    candidate = package.strip()
    if not candidate:
        return ""
    candidate = re.split(r"[<>=!~\[\];\s]", candidate, maxsplit=1)[0]
    return re.sub(r"[-_.]+", "-", candidate).lower()


def _extra_packages(packages: Iterable[str] | None) -> list[str]:
    """Deduplicate packages and omit distributions baked into the image."""
    if packages is None:
        return []
    result: list[str] = []
    seen: set[str] = set()
    for package in packages:
        if not isinstance(package, str) or not package.strip():
            raise ValueError("sandbox packages must be non-empty strings")
        normalized = _normalized_package_name(package)
        if normalized in BAKED_PACKAGES:
            continue
        if package not in seen:
            result.append(package)
            seen.add(package)
    return result


def _normalized_mounts(mounts: Mounts | None) -> list[tuple[str, str, str]]:
    if mounts is None:
        return []
    if isinstance(mounts, Mapping):
        entries = (
            (host, *value)
            if isinstance(value, tuple)
            else (host, value)
            for host, value in mounts.items()
        )
    else:
        entries = mounts
    normalized: list[tuple[str, str, str]] = []
    for entry in entries:
        if not isinstance(entry, Sequence) or isinstance(entry, (str, bytes)):
            raise TypeError(
                "sandbox mounts must be a mapping or (host, container[, mode]) "
                "iterable"
            )
        if len(entry) not in {2, 3}:
            raise ValueError(
                "sandbox mount entries must contain host, container, and "
                "optionally mode"
            )
        host, container = entry[0], entry[1]
        mode = entry[2] if len(entry) == 3 else "rw"
        if not isinstance(host, (str, os.PathLike)) or not isinstance(
            container, (str, os.PathLike)
        ):
            raise TypeError("sandbox mount paths must be strings or Path objects")
        if not isinstance(mode, str) or mode not in {"ro", "rw"}:
            raise ValueError("sandbox mount mode must be 'ro' or 'rw'")
        host_path = Path(host).expanduser().resolve()
        container_path = os.fspath(container)
        if not container_path.startswith("/"):
            raise ValueError("sandbox container mount paths must be absolute")
        normalized.append((str(host_path), container_path, mode))
    return normalized


def _runtime_command(
    argv: Sequence[str],
    packages: Iterable[str] | None,
    python_version: str | None,
    *,
    offline: bool = False,
) -> list[str]:
    command = list(argv)
    extras = _extra_packages(packages)
    if not extras:
        return command

    selected_python = (
        (python_version or "").strip()
        or os.environ.get("MATERIALS_CHECKER_UV_PYTHON", "").strip()
        or DEFAULT_PYTHON_VERSION
    )
    if not selected_python:
        raise ValueError("sandbox python_version must be non-empty")
    uv_command = [
        "uv",
        "run",
        "--active",
        "--no-project",
        "--no-build",
        "--python",
        selected_python,
    ]
    if offline:
        uv_command.append("--offline")
    for package in extras:
        uv_command.extend(["--with", package])
    return [*uv_command, "--", *command]


def _container_name() -> str:
    """Return a Docker-safe name unique to this sandbox invocation."""
    return f"materials-qa-{uuid.uuid4().hex}"


def _timeout_result(
    command: Sequence[str],
    timeout: float | None,
    exc: subprocess.TimeoutExpired,
) -> SandboxResult:
    """Represent a Docker timeout as an ordinary failed checker result."""
    timeout_text = (
        f"{timeout:g} seconds" if isinstance(timeout, (int, float)) else "the limit"
    )
    stdout = _timeout_stream_text(exc.stdout)
    stderr = _timeout_stream_text(exc.stderr)
    message = (
        f"sandbox timeout after {timeout_text}; Docker container was force-removed"
    )
    return subprocess.CompletedProcess(
        list(command),
        124,
        stdout,
        f"{stderr}\n{message}" if stderr else message,
    )


def _timeout_stream_text(value: str | bytes | None) -> str:
    """Normalize partial subprocess output for text-mode sandbox results."""
    if isinstance(value, bytes):
        return value.decode(errors="replace")
    return value or ""


def _launch_error_result(command: Sequence[str], exc: OSError) -> SandboxResult:
    """Keep post-preflight Docker launch failures in the checker-result channel."""
    return subprocess.CompletedProcess(
        list(command),
        125,
        "",
        f"sandbox Docker launch error: {exc}",
    )


def _force_remove_container(docker: str, name: str) -> None:
    """Best-effort cleanup that never obscures the checker result."""
    try:
        subprocess.run(
            [docker, "rm", "--force", name],
            capture_output=True,
            text=True,
            timeout=PREFLIGHT_TIMEOUT_SECONDS,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        pass


def _run_container(
    docker: str,
    name: str,
    command: list[str],
    timeout: float | None,
) -> SandboxResult:
    """Run one named container and force-remove it on every exit path."""
    try:
        return subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        return _timeout_result(command, timeout, exc)
    except OSError as exc:
        # A disappearing/killed Docker CLI is a package runtime failure after
        # preflight, not an uncaught exception that aborts Review or Repair.
        return _launch_error_result(command, exc)
    finally:
        _force_remove_container(docker, name)


def _docker_run_command(
    docker: str,
    name: str,
    cache: Path,
    mount_specs: Sequence[tuple[str, str, str]],
    workdir: str,
    command: Sequence[str],
    *,
    network: str,
) -> list[str]:
    """Build an argv-only Docker invocation for a named disposable container."""
    result = [
        docker,
        "run",
        "--name",
        name,
        "--network",
        network,
        "--workdir",
        workdir,
        "--mount",
        f"type=bind,src={cache.resolve()},dst={UV_CACHE_CONTAINER}",
        "--env",
        f"UV_CACHE_DIR={UV_CACHE_CONTAINER}",
    ]
    for host, container, mode in mount_specs:
        mode_flag = ",readonly" if mode == "ro" else ""
        result.extend(
            [
                "--mount",
                f"type=bind,src={host},dst={container}{mode_flag}",
            ]
        )
    return [*result, image_tag(), *command]


def run_in_sandbox(
    argv: Sequence[str],
    mounts: Mounts | None = None,
    workdir: str = DEFAULT_WORKDIR,
    timeout: float | None = None,
    packages: Iterable[str] | None = None,
    python_version: str | None = None,
) -> SandboxResult:
    """Run ``argv`` in a fresh, network-isolated checker container.

    ``mounts`` maps host paths to absolute container paths.  The container
    working directory is a container path, not a host path.  The shared uv
    cache is mounted automatically at ``/root/.cache/uv``.  Long-tail extras
    are first materialized by a non-package-controlled, wheel-only ``uv``
    invocation; the actual package command always runs with ``--network none``.
    """
    if not argv or not all(isinstance(item, str) and item for item in argv):
        raise ValueError("sandbox argv must be a non-empty string sequence")
    if not isinstance(workdir, str) or not workdir.startswith("/"):
        raise ValueError("sandbox workdir must be an absolute container path")
    if timeout is not None and (
        isinstance(timeout, bool) or not isinstance(timeout, (int, float))
        or timeout <= 0
    ):
        raise ValueError("sandbox timeout must be a positive number")

    cache = ensure_env()
    docker = shutil.which("docker")
    if docker is None:  # pragma: no cover - ensure_env already checked this.
        raise SandboxEnvError("Docker CLI disappeared before sandbox launch.")

    mount_specs = _normalized_mounts(mounts)
    if any(container == UV_CACHE_CONTAINER for _, container, _ in mount_specs):
        raise ValueError(
            f"{UV_CACHE_CONTAINER} is managed by sandbox_runtime and must not "
            "be supplied in mounts"
        )

    extras = _extra_packages(packages)
    if extras:
        selected_python = (
            (python_version or "").strip()
            or os.environ.get("MATERIALS_CHECKER_UV_PYTHON", "").strip()
            or DEFAULT_PYTHON_VERSION
        )
        # This command is owned by the sandbox, not the package.  --no-build
        # rejects sdists/build backends so an untrusted distribution cannot run
        # a build script while this preparation container has network access.
        prepare_name = _container_name()
        prepare = _docker_run_command(
            docker,
            prepare_name,
            cache,
            (),
            DEFAULT_WORKDIR,
            _runtime_command(["/bin/true"], extras, selected_python),
            network="bridge",
        )
        prepared = _run_container(
            docker, prepare_name, prepare, timeout
        )
        if prepared.returncode != 0:
            prepared.stderr = (
                "sandbox dependency preparation failed: "
                + (prepared.stderr or "unknown error")
            )
            return prepared

    name = _container_name()
    command = _docker_run_command(
        docker,
        name,
        cache,
        mount_specs,
        workdir,
        _runtime_command(argv, extras, python_version, offline=bool(extras)),
        network="none",
    )
    return _run_container(docker, name, command, timeout)
