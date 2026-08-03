from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERIFY = (
    ROOT
    / ".cursor/skills/materials-benchmark-review/scripts/verify_harbor.py"
)
CORE = {
    "instruction.md",
    "manifest.json",
    "paper/paper.md",
    "resources.json",
    "steps.json",
    "task.toml",
    "tests/checker.py",
    "tests/grading_spec.json",
    "tests/test.sh",
}


def make_package(root: Path, *, include_test_entrypoint: bool) -> None:
    package = root / "_publish/cluster/theme/paper-1"
    for name in CORE:
        if name == "tests/test.sh" and not include_test_entrypoint:
            continue
        path = package / name
        path.parent.mkdir(parents=True, exist_ok=True)
        content = "#!/usr/bin/env bash\nexit 0\n" if name == "tests/test.sh" else "# fixture\n"
        path.write_text(content, encoding="utf-8")
        if name == "tests/test.sh":
            path.chmod(0o755)


def run_verify(root: Path) -> subprocess.CompletedProcess[str]:
    env = {**os.environ, "QA_ROOT": str(root)}
    return subprocess.run(
        [sys.executable, str(VERIFY)],
        check=False,
        capture_output=True,
        text=True,
        env=env,
    )


class HarborFormatTests(unittest.TestCase):
    def test_missing_test_sh_fails_format_verification(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            make_package(root, include_test_entrypoint=False)
            result = run_verify(root)
            self.assertEqual(result.returncode, 1)
            self.assertIn("tests/test.sh", result.stdout)
            self.assertIn("RESULT: FAIL", result.stdout)

    def test_complete_core_package_passes_format_verification(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            make_package(root, include_test_entrypoint=True)
            result = run_verify(root)
            self.assertEqual(result.returncode, 0)
            self.assertIn("RESULT: PASS", result.stdout)

    def test_non_executable_test_sh_fails_format_verification(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            make_package(root, include_test_entrypoint=True)
            entrypoint = (
                root
                / "_publish/cluster/theme/paper-1/tests/test.sh"
            )
            entrypoint.chmod(0o644)
            result = run_verify(root)
            self.assertEqual(result.returncode, 1)
            self.assertIn("not executable", result.stdout)
            self.assertIn("RESULT: FAIL", result.stdout)

    def test_solution_contents_are_not_inspected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            make_package(root, include_test_entrypoint=True)
            solution = root / "_publish/cluster/theme/paper-1/solution"
            solution.mkdir()
            (solution / "agent_final_decision.pyc").write_bytes(b"opaque")
            result = run_verify(root)
            self.assertEqual(result.returncode, 0)
            self.assertIn("RESULT: PASS", result.stdout)


if __name__ == "__main__":
    unittest.main()
