#!/usr/bin/env python3
"""Focused tests for sandbox checker dependency detection and runtime labels.

These tests are network-free: they exercise static dependency derivation,
Oracle shim-writing compatibility, and the Docker sandbox preflight contract.

Run: python3 test_dynamic_checker_probe_uv.py
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))

import dynamic_checker_probe as probe
import sandbox_runtime

# The Harbor verifier finalizer only accepts the shared checker runtime label.
FINALIZER_ALLOWED_PROVENANCE = {
    "sandbox",
}


def test_detect_import_packages_maps_names() -> None:
    text = (
        "import numpy as np\n"
        "import os, json\n"
        "from scipy.optimize import curve_fit\n"
        "import sklearn\n"
        "from . import local_helper\n"
    )
    detected = probe.detect_import_packages(text)
    assert "numpy" in detected
    assert "scipy" in detected
    assert "scikit-learn" in detected
    # stdlib and relative imports are never emitted as PyPI deps.
    assert "os" not in detected
    assert "json" not in detected


def test_detect_import_packages_falls_back_to_unmapped_third_party() -> None:
    text = (
        "import crystalmetrics\n"
        "from thermo_tools.analysis import fit_curve\n"
    )
    detected = probe.detect_import_packages(text)
    assert "crystalmetrics" in detected
    assert "thermo_tools" in detected


def test_detect_import_packages_excludes_unmapped_stdlib() -> None:
    text = (
        "import pathlib, tomllib\n"
        "from collections import abc\n"
    )
    detected = probe.detect_import_packages(text)
    assert "pathlib" not in detected
    assert "tomllib" not in detected
    assert "collections" not in detected


def test_detect_pip_install_packages_list_and_shell() -> None:
    list_form = (
        'subprocess.check_call([sys.executable, "-m", "pip", "install", '
        '"-q", "--no-cache-dir", "-i", '
        '"https://pypi.tuna.tsinghua.edu.cn/simple", "numpy"])\n'
    )
    shell_form = "pip install scipy pandas==2.0.0\n"
    detected = probe.detect_pip_install_packages(list_form + shell_form)
    assert "numpy" in detected
    assert "scipy" in detected
    assert "pandas" in detected
    # index URLs and flags must never be treated as packages.
    assert not any("/" in name or name.startswith("-") for name in detected)
    assert "https" not in detected


def test_checker_uv_packages_includes_baseline_and_extras() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "tests").mkdir()
        (root / "solution").mkdir()
        (root / "solution" / "solve.sh").write_text(
            "#!/bin/bash\npip install ase\n", encoding="utf-8"
        )
        checker_text = "import numpy as np\nfrom pymatgen.core import Structure\n"
        previous = os.environ.get("MATERIALS_CHECKER_UV_WITH")
        os.environ["MATERIALS_CHECKER_UV_WITH"] = "custompkg, another-pkg"
        try:
            packages = probe.checker_uv_packages(root, checker_text)
        finally:
            if previous is None:
                os.environ.pop("MATERIALS_CHECKER_UV_WITH", None)
            else:
                os.environ["MATERIALS_CHECKER_UV_WITH"] = previous
    for baseline in probe.CHECKER_UV_BASELINE_PACKAGES:
        assert baseline in packages
    assert "pymatgen" in packages
    assert "ase" in packages
    assert "custompkg" in packages
    assert "another-pkg" in packages
    # no duplicates.
    assert len(packages) == len(set(packages))


def test_write_python_shim_execs_uv() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        bin_dir = Path(tmp)
        probe.write_python_shim(
            bin_dir, "/usr/bin/uv", ["numpy", "scipy", "pip"], "3.12"
        )
        for name in ("python", "python3"):
            shim = bin_dir / name
            assert shim.is_file()
            assert os.access(shim, os.X_OK)
            body = shim.read_text(encoding="utf-8")
            assert body.startswith("#!/bin/sh")
            assert "uv run" in body
            assert "--python 3.12" in body
            assert "--with numpy" in body
            assert "--with scipy" in body
            assert "--with pip" in body
            assert body.rstrip().endswith('python "$@"')


def test_uv_python_version_default_and_override() -> None:
    previous = os.environ.get("MATERIALS_CHECKER_UV_PYTHON")
    os.environ.pop("MATERIALS_CHECKER_UV_PYTHON", None)
    try:
        assert probe.uv_python_version() == probe.CHECKER_UV_DEFAULT_PYTHON
        os.environ["MATERIALS_CHECKER_UV_PYTHON"] = "3.11"
        assert probe.uv_python_version() == "3.11"
    finally:
        if previous is None:
            os.environ.pop("MATERIALS_CHECKER_UV_PYTHON", None)
        else:
            os.environ["MATERIALS_CHECKER_UV_PYTHON"] = previous


def test_checker_timeout_can_tighten_but_not_exceed_sixty_seconds() -> None:
    previous = os.environ.get("MATERIALS_CHECKER_RUN_TIMEOUT_SECONDS")
    try:
        os.environ["MATERIALS_CHECKER_RUN_TIMEOUT_SECONDS"] = "12.5"
        assert probe.checker_run_timeout() == 12.5
        os.environ["MATERIALS_CHECKER_RUN_TIMEOUT_SECONDS"] = "120"
        assert probe.checker_run_timeout() == 60.0
    finally:
        if previous is None:
            os.environ.pop("MATERIALS_CHECKER_RUN_TIMEOUT_SECONDS", None)
        else:
            os.environ["MATERIALS_CHECKER_RUN_TIMEOUT_SECONDS"] = previous


def test_prober_emits_only_finalizer_allowed_provenance() -> None:
    source = Path(probe.__file__).read_text(encoding="utf-8")
    literals = set(
        re.findall(r'runtime_provenance\s*=\s*"([^"]+)"', source)
    )
    assert literals, "expected runtime_provenance assignments in the prober"
    illegal = literals - FINALIZER_ALLOWED_PROVENANCE
    assert not illegal, (
        "prober emits runtime_provenance labels the finalizer rejects: "
        f"{sorted(illegal)}"
    )
    assert 'runtime_provenance = "sandbox"' in source
    assert '"checker_dependency_env"' in source


def test_finalizer_allowlist_matches_reference() -> None:
    finalizer = (
        Path(probe.__file__).resolve().parent / "finalize_audit_output.py"
    ).read_text(encoding="utf-8")
    found = re.findall(r'not in \{"sandbox"\}', finalizer)
    assert len(found) >= 3, (
        "finalizer runtime provenance allowlist changed; update "
        "FINALIZER_ALLOWED_PROVENANCE and the prober labels to match"
    )


def test_sandbox_preflight_aborts_without_docker() -> None:
    original_which = sandbox_runtime.shutil.which
    sandbox_runtime.shutil.which = (
        lambda command: None if command == "docker" else original_which(command)
    )
    try:
        try:
            sandbox_runtime.ensure_env()
        except sandbox_runtime.SandboxEnvError as exc:
            assert "docker build" in str(exc)
            assert "qa-checker" in str(exc)
        else:
            raise AssertionError("missing Docker must abort sandbox preflight")
    finally:
        sandbox_runtime.shutil.which = original_which


def test_sandbox_timeout_becomes_checker_failure_and_cleans_up() -> None:
    command = ["/usr/local/bin/docker", "run", "--name", "example"]
    with (
        patch.object(sandbox_runtime, "ensure_env", return_value=Path("/tmp/cache")),
        patch.object(sandbox_runtime.shutil, "which", return_value="/usr/local/bin/docker"),
        patch.object(
            sandbox_runtime.subprocess,
            "run",
            side_effect=[
                subprocess.TimeoutExpired(
                    command,
                    3,
                    output=b"partial checker stdout",
                    stderr=b"partial checker stderr",
                ),
                subprocess.CompletedProcess(command, 0, "", ""),
            ],
        ) as run,
    ):
        result = sandbox_runtime.run_in_sandbox(
            ["/bin/true"], timeout=3, mounts=[]
        )
    assert result.returncode == 124
    assert "partial checker stdout" in result.stdout
    assert "partial checker stderr" in result.stderr
    assert "timeout" in result.stderr.lower()
    cleanup = run.call_args_list[1].args[0]
    assert cleanup[:3] == ["/usr/local/bin/docker", "rm", "--force"]


def test_sandbox_launch_error_becomes_checker_failure_and_cleans_up() -> None:
    command = ["/usr/local/bin/docker", "run", "--name", "example"]
    with (
        patch.object(sandbox_runtime, "ensure_env", return_value=Path("/tmp/cache")),
        patch.object(sandbox_runtime.shutil, "which", return_value="/usr/local/bin/docker"),
        patch.object(
            sandbox_runtime.subprocess,
            "run",
            side_effect=[
                FileNotFoundError("docker disappeared"),
                subprocess.CompletedProcess(command, 0, "", ""),
            ],
        ) as run,
    ):
        result = sandbox_runtime.run_in_sandbox(["/bin/true"], mounts=[])
    assert result.returncode == 125
    assert "launch error" in result.stderr
    cleanup = run.call_args_list[1].args[0]
    assert cleanup[:3] == ["/usr/local/bin/docker", "rm", "--force"]


def test_sandbox_prepares_extras_then_runs_checker_offline() -> None:
    completed = subprocess.CompletedProcess(["docker"], 0, "", "")
    with (
        patch.object(sandbox_runtime, "ensure_env", return_value=Path("/tmp/cache")),
        patch.object(sandbox_runtime.shutil, "which", return_value="/usr/local/bin/docker"),
        patch.object(
            sandbox_runtime.subprocess, "run", return_value=completed
        ) as run,
    ):
        result = sandbox_runtime.run_in_sandbox(
            ["/bin/bash", "/workspace/test.sh"],
            mounts=[],
            timeout=5,
            packages=["long-tail-package"],
            python_version="3.11",
        )
    assert result.returncode == 0
    docker_runs = [
        call.args[0]
        for call in run.call_args_list
        if len(call.args[0]) > 1 and call.args[0][1] == "run"
    ]
    assert len(docker_runs) == 2
    preparation, execution = docker_runs
    assert preparation[preparation.index("--network") + 1] == "bridge"
    assert "/bin/true" in preparation
    assert "--no-build" in preparation
    assert execution[execution.index("--network") + 1] == "none"
    assert "--offline" in execution
    assert "--no-build" in execution
    assert "/workspace/test.sh" in execution


def main() -> int:
    tests = [
        value
        for name, value in sorted(globals().items())
        if name.startswith("test_") and callable(value)
    ]
    failures = 0
    for test in tests:
        try:
            test()
        except AssertionError as exc:
            failures += 1
            print(f"FAIL {test.__name__}: {exc}")
        except Exception as exc:  # noqa: BLE001
            failures += 1
            print(f"ERROR {test.__name__}: {exc!r}")
        else:
            print(f"PASS {test.__name__}")
    print(f"\n{len(tests) - failures}/{len(tests)} passed")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
