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
import review_path_policy  # noqa: E402


class MaterialsReviewExternalAuditTests(unittest.TestCase):
    def test_default_sibling_review_outputs_convention(self) -> None:
        package = Path(
            "/tmp/topic/ml-prediction/paper-1043370649185157132"
        )
        self.assertEqual(
            review_path_policy.default_review_output_dir(package),
            Path(
                "/tmp/topic/ml-prediction/review_outputs/1043370649185157132"
            ).resolve(),
        )

    def test_external_output_keeps_generated_audit_outside_package(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "theme" / "paper-1"
            package.mkdir(parents=True)
            output = Path(temporary) / "theme/review_outputs/1"

            context = prepare_audit_output.prepare_workspace(
                package,
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
            self.assertEqual(context["review_lane"], "dual")

    def test_external_output_inside_package_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "theme/paper-1"
            package.mkdir(parents=True)

            with self.assertRaisesRegex(ValueError, "canonical|outside the Harbor"):
                prepare_audit_output.prepare_workspace(
                    package,
                    audit_output_dir=package / "review_outputs",
                )

    def test_missing_low_level_output_path_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "theme/paper-1"
            package.mkdir(parents=True)

            with self.assertRaisesRegex(ValueError, "required"):
                prepare_audit_output.prepare_workspace(package)

    def test_wrong_sibling_output_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "theme-a/paper-1"
            package.mkdir(parents=True)
            wrong = Path(temporary) / "theme-b/review_outputs/1"
            with self.assertRaisesRegex(ValueError, "canonical|theme-sibling"):
                prepare_audit_output.prepare_workspace(
                    package,
                    audit_output_dir=wrong,
                )


if __name__ == "__main__":
    unittest.main()
