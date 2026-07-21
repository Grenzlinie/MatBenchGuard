from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import sys
import tempfile
import threading
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
REVIEW_SCRIPTS = (
    REPO_ROOT / ".cursor/skills/materials-benchmark-review/scripts"
)
REPAIR_RUNNER = (
    REPO_ROOT
    / ".cursor/skills/materials-benchmark-repair/scripts/run_repair.py"
)
if str(REVIEW_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(REVIEW_SCRIPTS))

import audit_integrity  # noqa: E402
import prepare_audit_output  # noqa: E402
import review_lock  # noqa: E402
import run_review  # noqa: E402


def sha256_file(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def repair_module():
    spec = importlib.util.spec_from_file_location(
        "materials_review_repair_integrity", REPAIR_RUNNER
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class MaterialsReviewConcurrencyIntegrityTests(unittest.TestCase):
    def package(self, root: Path, paper_id: str) -> Path:
        package = root / f"topic/paper-{paper_id}"
        (package / "tests").mkdir(parents=True)
        (package / "instruction.md").write_text("instruction\n")
        (package / "tests/checker.py").write_text("checker\n")
        return package

    def test_same_output_concurrency_one_run_enters_and_one_fails_before_work(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = self.package(root, "one")
            output = package.parent / "review_outputs/one"
            entered = threading.Event()
            release = threading.Event()
            calls: list[Path] = []

            def fake_review(candidate: Path, **_kwargs: object) -> dict[str, str]:
                calls.append(candidate)
                entered.set()
                self.assertTrue(release.wait(5))
                return {"status": "SUCCEEDED", "candidate": str(candidate)}

            with patch.object(
                run_review, "_run_review_locked", side_effect=fake_review
            ):
                with ThreadPoolExecutor(max_workers=2) as pool:
                    first = pool.submit(
                        run_review.run_review,
                        package,
                        audit_output_dir=output,
                    )
                    self.assertTrue(entered.wait(5))
                    second = pool.submit(
                        run_review.run_review,
                        package,
                        audit_output_dir=output,
                    )
                    with self.assertRaises(review_lock.ReviewLockHeld):
                        second.result(timeout=5)
                    release.set()
                    self.assertEqual(first.result(timeout=5)["status"], "SUCCEEDED")

            self.assertEqual(calls, [package])
            self.assertFalse((output / review_lock.LOCK_NAME).exists())

    def test_different_output_roots_run_concurrently(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            packages = [self.package(root, str(index)) for index in (1, 2)]
            entered = threading.Barrier(2)
            release = threading.Event()

            def fake_review(candidate: Path, **_kwargs: object) -> dict[str, str]:
                entered.wait(5)
                self.assertTrue(release.wait(5))
                return {"status": "SUCCEEDED", "candidate": str(candidate)}

            with patch.object(
                run_review, "_run_review_locked", side_effect=fake_review
            ):
                with ThreadPoolExecutor(max_workers=2) as pool:
                    futures = [
                        pool.submit(
                            run_review.run_review,
                            package,
                            audit_output_dir=package.parent
                            / f"review_outputs/{package.name[6:]}",
                        )
                        for package in packages
                    ]
                    release.set()
                    self.assertEqual(
                        [future.result(timeout=5)["status"] for future in futures],
                        ["SUCCEEDED", "SUCCEEDED"],
                    )

    def test_failed_review_releases_lock_and_own_temp_only(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = self.package(root, "failure")
            output = package.parent / "review_outputs/failure"

            with patch.object(
                run_review,
                "_run_review_locked",
                side_effect=RuntimeError("probe failure"),
            ):
                with self.assertRaisesRegex(RuntimeError, "probe failure"):
                    run_review.run_review(package, audit_output_dir=output)

            self.assertFalse((output / review_lock.LOCK_NAME).exists())
            temp_parent = output / ".benchmark_audit_tmp"
            self.assertFalse(
                any(path.name.startswith("audit-") for path in temp_parent.glob("*"))
            )

    def test_stale_lock_recovery_requires_demonstrable_process_identity(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "review_outputs/one"
            lock_path = output / review_lock.LOCK_NAME
            lock_path.mkdir(parents=True)
            (lock_path / "owner.json").write_text(
                json.dumps(
                    {
                        "schema_version": review_lock.LOCK_SCHEMA_VERSION,
                        "output_root": str(output.resolve()),
                        "run_id": "audit-dead",
                        "pid": 999999,
                        "process_start": "dead",
                        "created_at": 0,
                        "nonce": "dead",
                    }
                )
            )
            with review_lock.ReviewOutputLock(output, "audit-new"):
                self.assertTrue(lock_path.is_dir())

            lock_path.mkdir(parents=True)
            owner = {
                "schema_version": review_lock.LOCK_SCHEMA_VERSION,
                "output_root": str(output.resolve()),
                "run_id": "audit-live",
                "pid": os.getpid(),
                "process_start": review_lock.process_start_token(os.getpid()),
                "created_at": 0,
                "nonce": "live",
            }
            (lock_path / "owner.json").write_text(json.dumps(owner))
            with self.assertRaises(review_lock.ReviewLockHeld):
                review_lock.ReviewOutputLock(output, "audit-new").acquire()

            with patch.object(
                review_lock,
                "process_start_token",
                return_value=None,
            ):
                with self.assertRaises(review_lock.ReviewLockHeld):
                    review_lock.ReviewOutputLock(output, "audit-new").acquire()

    def test_integrity_rejects_exact_output_and_aggregate_tampering(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            audit = Path(temporary) / "audit"
            audit.mkdir()
            for name, content in {
                "audit_report.json": '{"audit_id":"a"}\n',
                "disposition.json": '{"audit_id":"a"}\n',
                "payload.json": "{}\n",
            }.items():
                (audit / name).write_text(content)
            implementation_files = {
                "scripts/example.py": "sha256:" + "1" * 64,
            }
            manifest = {
                "audit_id": "a",
                "output_hashes": audit_integrity.actual_output_hashes(audit),
                "review_implementation": {
                    "schema_version": (
                        "materials-review-implementation/1.0"
                    ),
                    "files": implementation_files,
                    "aggregate_hash": audit_integrity.implementation_aggregate(
                        implementation_files
                    ),
                },
            }
            manifest["bundle_hash"] = audit_integrity.canonical_json_hash(
                manifest["output_hashes"]
            )
            report = {
                "audit_binding": {
                    "implementation_hash": manifest["review_implementation"][
                        "aggregate_hash"
                    ]
                }
            }
            disposition = {"audit_id": "a"}
            audit_integrity.validate_finalized_audit_bundle(
                audit, manifest, report, disposition
            )

            (audit / "unexpected.json").write_text("{}\n")
            with self.assertRaisesRegex(ValueError, "file set"):
                audit_integrity.validate_finalized_audit_bundle(
                    audit, manifest, report, disposition
                )
            (audit / "unexpected.json").unlink()
            manifest["review_implementation"]["aggregate_hash"] = (
                "sha256:" + "2" * 64
            )
            with self.assertRaisesRegex(ValueError, "aggregate"):
                audit_integrity.validate_finalized_audit_bundle(
                    audit, manifest, report, disposition
                )

    def test_attestation_freezes_bundle_and_repair_rejects_refresh(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "topic/paper-one"
            root.mkdir(parents=True)
            audit = root.parent / "review_outputs/one/benchmark_audit"
            audit.mkdir(parents=True)
            implementation_files = {"scripts/example.py": "sha256:" + "1" * 64}
            implementation = {
                "schema_version": "materials-review-implementation/1.0",
                "files": implementation_files,
                "aggregate_hash": audit_integrity.implementation_aggregate(
                    implementation_files
                ),
            }
            report = {
                "audit_id": "audit-one",
                "audit_binding": {
                    "implementation_hash": implementation["aggregate_hash"]
                },
            }
            disposition = {"audit_id": "audit-one"}
            (audit / "audit_report.json").write_text(json.dumps(report))
            (audit / "disposition.json").write_text(json.dumps(disposition))
            (audit / "deterministic_core").mkdir()
            (audit / "agent_quality").mkdir()
            (audit / "deterministic_core/report.json").write_text("{}")
            (audit / "deterministic_core/probe_results.json").write_text("{}")
            (audit / "agent_quality/assessment.json").write_text("{}")
            output_hashes = audit_integrity.actual_output_hashes(audit)
            manifest = {
                "schema_version": "materials-audit-manifest/2.0",
                "bundle_schema_version": "materials-audit-bundle/2.0",
                "audit_id": "audit-one",
                "review_implementation": implementation,
                "output_hashes": output_hashes,
                "bundle_hash": audit_integrity.canonical_json_hash(
                    output_hashes
                ),
            }
            (audit / "audit_manifest.json").write_text(json.dumps(manifest))
            attestation = root.parent / "audit-attestation.json"
            prepare_audit_output.write_audit_attestation(
                root, attestation, audit_dir=audit
            )
            self.assertEqual(
                json.loads((audit / "audit_manifest.json").read_text())[
                    "immutability_state"
                ],
                "ATTESTED",
            )
            self.assertTrue(
                all(
                    path.stat().st_mode & 0o222 == 0
                    for path in audit.rglob("*")
                    if path.is_file()
                )
            )
            with self.assertRaisesRegex(ValueError, "immutable"):
                repair_module().refresh_audit_manifest_hashes(audit)

    def test_repair_source_hash_detects_lifecycle_tamper(self) -> None:
        module = repair_module()
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "topic/paper-one"
            source = root.parent / "review_outputs/one/benchmark_audit"
            source.mkdir(parents=True)
            (root / "instruction.md").parent.mkdir(parents=True)
            (root / "instruction.md").write_text("source\n")
            plan = {}
            expected = module.source_audit_bundle_hash(root, plan)
            (source / "audit_report.json").write_text("changed\n")
            with self.assertRaisesRegex(ValueError, "fresh audit"):
                module.assert_source_audit_unchanged(root, plan, expected)


if __name__ == "__main__":
    unittest.main()
