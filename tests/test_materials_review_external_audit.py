from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = (
    REPO_ROOT
    / ".cursor"
    / "skills"
    / "materials-benchmark-review"
    / "scripts"
)
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import prepare_audit_output  # noqa: E402


class MaterialsReviewExternalAuditTests(unittest.TestCase):
    def test_external_output_keeps_generated_audit_outside_package(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "paper-1"
            package.mkdir()
            output = Path(temporary) / "review_records/paper-1"

            context = prepare_audit_output.prepare_workspace(
                package,
                "no_paper",
                "E1",
                audit_output_dir=output,
            )

            self.assertFalse((package / "benchmark_audit").exists())
            self.assertFalse((package / ".benchmark_audit_tmp").exists())
            self.assertEqual(
                Path(context["audit_output_root"]),
                output.resolve(),
            )
            self.assertTrue(
                (output / ".benchmark_audit_tmp/audit_manifest.json").is_file()
            )

    def test_external_output_inside_package_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "paper-1"
            package.mkdir()

            with self.assertRaises(ValueError):
                prepare_audit_output.prepare_workspace(
                    package,
                    "no_paper",
                    "E1",
                    audit_output_dir=package / "review_records",
                )


if __name__ == "__main__":
    unittest.main()
