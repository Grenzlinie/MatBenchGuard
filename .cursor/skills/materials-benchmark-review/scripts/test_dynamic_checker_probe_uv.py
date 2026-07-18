#!/usr/bin/env python3
"""Focused unit tests for the uv-shim / dependency-detection checker runtime.

These tests are network-free: they exercise only the static dependency
derivation and shim-writing logic added so that checker execution runs through
`uv run --with ...` instead of the audit host interpreter.

Run: python3 test_dynamic_checker_probe_uv.py
"""

from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))

import dynamic_checker_probe as probe


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
