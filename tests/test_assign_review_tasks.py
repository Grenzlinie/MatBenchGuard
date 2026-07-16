from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
CLI = REPO_ROOT / "assign_review_tasks" / "assign.py"
REGISTRY = REPO_ROOT / "assign_review_tasks" / "assignment_lock.json"
SOURCE_MANIFEST = (
    REPO_ROOT
    / "review_artifacts"
    / "materials_bench_whitelist_100_20260716"
    / "manifest.json"
)


def run_cli(
    registry: Path, *arguments: str, timeout: float = 20
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(CLI),
            "--registry",
            str(registry),
            *arguments,
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=timeout,
        check=False,
    )


def result_json(process: subprocess.CompletedProcess[str]) -> dict[str, object]:
    if process.returncode != 0:
        raise AssertionError(
            f"CLI failed ({process.returncode}): {process.stderr}"
        )
    return json.loads(process.stdout)


def seeded_data() -> dict[str, object]:
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def entry(
    package_id: str,
    state: str = "AVAILABLE",
    *,
    operation: str | None = None,
    result: str | None = None,
    source: str = "test",
) -> dict[str, object]:
    return {
        "active_claim": None,
        "history": [],
        "operation": operation,
        "package_id": package_id,
        "result": result,
        "source": source,
        "state": state,
    }


def write_registry(path: Path, entries: list[dict[str, object]]) -> None:
    data = seeded_data()
    data["entries"] = sorted(
        [*data["entries"], *entries], key=lambda item: item["package_id"]
    )
    path.write_text(
        json.dumps(data, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


class AssignmentDispatcherTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tempdir.cleanup)
        self.root = Path(self.tempdir.name)
        self.registry = self.root / "assignment_lock.json"

    def make_registry(
        self, package_ids: list[str], *, state: str = "AVAILABLE"
    ) -> None:
        write_registry(
            self.registry,
            [entry(package_id, state=state) for package_id in package_ids],
        )

    def read_registry(self) -> dict[str, object]:
        return json.loads(self.registry.read_text(encoding="utf-8"))

    def registry_entry(self, package_id: str) -> dict[str, object]:
        return next(
            item
            for item in self.read_registry()["entries"]
            if item["package_id"] == package_id
        )

    def claim(
        self,
        package_id: str = "cluster-1/theme/paper-1",
        *,
        operation: str = "REVIEW",
        owner: str = "parent",
        lease_seconds: int = 60,
    ) -> dict[str, object]:
        return result_json(
            run_cli(
                self.registry,
                "claim",
                "--package-id",
                package_id,
                "--operation",
                operation,
                "--owner",
                owner,
                "--lease-seconds",
                str(lease_seconds),
            )
        )

    def test_two_processes_racing_same_key_have_one_winner(self) -> None:
        package_id = "cluster-1/theme/paper-1"
        self.make_registry([package_id])
        commands = [
            [
                sys.executable,
                str(CLI),
                "--registry",
                str(self.registry),
                "claim",
                "--package-id",
                package_id,
                "--operation",
                "REVIEW",
                "--owner",
                "parent-a",
                "--lease-seconds",
                "60",
            ],
            [
                sys.executable,
                str(CLI),
                "--registry",
                str(self.registry),
                "claim",
                "--package-id",
                package_id,
                "--operation",
                "REVIEW",
                "--owner",
                "parent-b",
                "--lease-seconds",
                "60",
            ],
        ]
        processes = [
            subprocess.Popen(
                command,
                cwd=REPO_ROOT,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            for command in commands
        ]
        results = [process.communicate(timeout=20) for process in processes]
        self.assertEqual(
            [sum(process.returncode == 0 for process in processes)], [1]
        )
        self.assertEqual(
            sum(returncode != 0 for returncode in [p.returncode for p in processes]),
            1,
        )
        self.assertIsNotNone(self.registry_entry(package_id)["active_claim"])
        self.assertEqual(sum(bool(stdout) for stdout, _ in results), 1)

    def test_review_and_repair_claims_cannot_collide(self) -> None:
        package_id = "cluster-1/theme/paper-1"
        self.make_registry([package_id])
        review = self.claim(package_id)
        repair = run_cli(
            self.registry,
            "claim",
            "--package-id",
            package_id,
            "--operation",
            "REPAIR",
            "--owner",
            "repair-parent",
        )
        self.assertNotEqual(repair.returncode, 0)
        self.assertIn("active claim", repair.stderr)
        self.assertEqual(
            self.registry_entry(package_id)["active_claim"]["token"],
            review["token"],
        )

    def test_wrong_owner_or_token_cannot_mutate_registry(self) -> None:
        package_id = "cluster-1/theme/paper-1"
        self.make_registry([package_id])
        claim = self.claim(package_id)
        original = self.registry.read_bytes()
        wrong_owner = run_cli(
            self.registry,
            "heartbeat",
            "--package-id",
            package_id,
            "--owner",
            "other-parent",
            "--token",
            str(claim["token"]),
        )
        wrong_token = run_cli(
            self.registry,
            "release",
            "--package-id",
            package_id,
            "--owner",
            "parent",
            "--token",
            "wrong-token",
            "--reason",
            "not mine",
        )
        self.assertNotEqual(wrong_owner.returncode, 0)
        self.assertNotEqual(wrong_token.returncode, 0)
        self.assertEqual(self.registry.read_bytes(), original)

    def test_heartbeat_extends_original_lease(self) -> None:
        package_id = "cluster-1/theme/paper-1"
        self.make_registry([package_id])
        claim = self.claim(package_id, lease_seconds=2)
        before = claim["expires_at"]
        heartbeat = result_json(
            run_cli(
                self.registry,
                "heartbeat",
                "--package-id",
                package_id,
                "--owner",
                "parent",
                "--token",
                str(claim["token"]),
            )
        )
        self.assertGreater(str(heartbeat["expires_at"]), str(before))

    def test_release_then_reclaim(self) -> None:
        package_id = "cluster-1/theme/paper-1"
        self.make_registry([package_id])
        first = self.claim(package_id)
        released = result_json(
            run_cli(
                self.registry,
                "release",
                "--package-id",
                package_id,
                "--owner",
                "parent",
                "--token",
                str(first["token"]),
                "--reason",
                "worker stopped",
            )
        )
        self.assertEqual(released["state"], "AVAILABLE")
        second = self.claim(package_id, owner="recovery-parent")
        self.assertNotEqual(first["token"], second["token"])

    def test_terminal_states_remain_blocked(self) -> None:
        outcomes = {
            "PASS": "ACCEPTED",
            "REJECT": "REVIEWED_REJECT",
            "NOT_ASSESSABLE": "REVIEWED_NOT_ASSESSABLE",
        }
        for outcome, state in outcomes.items():
            with self.subTest(outcome=outcome):
                package_id = f"cluster-1/theme/paper-{outcome.lower()}"
                self.make_registry([package_id])
                claim = self.claim(package_id)
                result_json(
                    run_cli(
                        self.registry,
                        "complete",
                        "--package-id",
                        package_id,
                        "--owner",
                        "parent",
                        "--token",
                        str(claim["token"]),
                        "--outcome",
                        outcome,
                    )
                )
                blocked = run_cli(
                    self.registry,
                    "claim",
                    "--package-id",
                    package_id,
                    "--operation",
                    "REVIEW",
                    "--owner",
                    "parent-2",
                )
                self.assertNotEqual(blocked.returncode, 0)
                self.assertEqual(
                    self.registry_entry(package_id)["state"], state
                )

    def test_expired_claim_requires_reclaim_and_records_expired(self) -> None:
        package_id = "cluster-1/theme/paper-1"
        self.make_registry([package_id])
        first = self.claim(package_id, lease_seconds=1)
        time.sleep(1.2)
        blocked = run_cli(
            self.registry,
            "claim",
            "--package-id",
            package_id,
            "--operation",
            "REVIEW",
            "--owner",
            "recovery",
        )
        self.assertNotEqual(blocked.returncode, 0)
        reclaimed = result_json(
            run_cli(
                self.registry,
                "claim",
                "--package-id",
                package_id,
                "--operation",
                "REVIEW",
                "--owner",
                "recovery",
                "--reclaim-expired",
            )
        )
        self.assertNotEqual(first["token"], reclaimed["token"])
        history = self.registry_entry(package_id)["history"]
        self.assertEqual([event["event"] for event in history], [
            "CLAIMED",
            "EXPIRED",
            "CLAIMED",
        ])

    def test_claim_next_reclaims_expired_in_manifest_order_only_when_requested(
        self,
    ) -> None:
        package_ids = [
            "cluster-1/theme/paper-1",
            "cluster-1/theme/paper-2",
        ]
        self.make_registry(package_ids)
        first_claims = [
            self.claim(package_id, owner="old-parent", lease_seconds=1)
            for package_id in package_ids
        ]
        time.sleep(1.2)
        manifest_order = list(reversed(package_ids))
        manifest = self.root / "manifest.json"
        manifest.write_text(
            json.dumps(
                {"tasks": [{"relpath": package_id} for package_id in manifest_order]}
            ),
            encoding="utf-8",
        )
        skipped = result_json(
            run_cli(
                self.registry,
                "claim-next",
                "--manifest",
                str(manifest),
                "--operation",
                "REVIEW",
                "--owner",
                "new-parent",
                "--count",
                "2",
            )
        )
        self.assertEqual(skipped["claims"], [])
        reclaimed = result_json(
            run_cli(
                self.registry,
                "claim-next",
                "--manifest",
                str(manifest),
                "--operation",
                "REVIEW",
                "--owner",
                "new-parent",
                "--count",
                "2",
                "--reclaim-expired",
            )
        )
        self.assertEqual(
            [claim["package_id"] for claim in reclaimed["claims"]],
            manifest_order,
        )
        for package_id, old_claim in zip(package_ids, first_claims):
            current = self.registry_entry(package_id)
            self.assertNotEqual(
                current["active_claim"]["token"], old_claim["token"]
            )
            self.assertEqual(
                [event["event"] for event in current["history"]],
                ["CLAIMED", "EXPIRED", "CLAIMED"],
            )

    def test_direct_claim_rejects_absent_registry_entry_without_rewrite(self) -> None:
        self.make_registry([])
        original = self.registry.read_bytes()
        process = run_cli(
            self.registry,
            "claim",
            "--package-id",
            "cluster-1/theme/paper-phantom",
            "--operation",
            "REVIEW",
            "--owner",
            "parent",
        )
        self.assertNotEqual(process.returncode, 0)
        self.assertIn("absent from the registry", process.stderr)
        self.assertEqual(self.registry.read_bytes(), original)

    def test_claim_next_rejects_symlink_candidate_sources(self) -> None:
        self.make_registry([])
        manifest = self.root / "real-manifest.json"
        manifest.write_text(
            json.dumps(
                {"tasks": [{"relpath": "cluster-1/theme/paper-1"}]}
            ),
            encoding="utf-8",
        )
        manifest_link = self.root / "manifest-link.json"
        manifest_link.symlink_to(manifest)
        corpus = self.root / "real-corpus"
        (corpus / "cluster-1/theme/paper-1").mkdir(parents=True)
        corpus_link = self.root / "corpus-link"
        corpus_link.symlink_to(corpus, target_is_directory=True)
        original = self.registry.read_bytes()
        for option, source in (
            ("--manifest", manifest_link),
            ("--corpus", corpus_link),
        ):
            with self.subTest(option=option):
                process = run_cli(
                    self.registry,
                    "claim-next",
                    option,
                    str(source),
                    "--operation",
                    "REVIEW",
                    "--owner",
                    "parent",
                    "--count",
                    "1",
                )
                self.assertNotEqual(process.returncode, 0)
                self.assertEqual(self.registry.read_bytes(), original)

    def test_malformed_duplicate_and_noncanonical_registries_are_not_rewritten(
        self,
    ) -> None:
        cases = []
        valid = seeded_data()
        valid["entries"] = [
            entry("cluster-1/theme/paper-1"),
            entry("cluster-1/theme/paper-1"),
        ]
        cases.append(valid)
        valid = seeded_data()
        valid["entries"] = [entry("cluster-1/../theme/paper-1")]
        cases.append(valid)
        valid = seeded_data()
        valid["entries"] = [
            entry("cluster-1/theme/paper-1", state="REVIEWING")
        ]
        cases.append(valid)
        for malformed in cases:
            with self.subTest(malformed=malformed["entries"][0]["package_id"]):
                self.registry.write_text(
                    json.dumps(malformed, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8",
                )
                original = self.registry.read_bytes()
                process = run_cli(self.registry, "validate")
                self.assertNotEqual(process.returncode, 0)
                self.assertEqual(self.registry.read_bytes(), original)

    def test_claim_next_preserves_manifest_order(self) -> None:
        package_ids = [
            "cluster-2/theme/paper-2",
            "cluster-1/theme/paper-1",
            "cluster-3/theme/paper-3",
        ]
        self.make_registry([])
        manifest = self.root / "manifest.json"
        manifest.write_text(
            json.dumps(
                {"tasks": [{"relpath": package_id} for package_id in package_ids]}
            ),
            encoding="utf-8",
        )
        response = result_json(
            run_cli(
                self.registry,
                "claim-next",
                "--manifest",
                str(manifest),
                "--operation",
                "REVIEW",
                "--owner",
                "parent",
                "--count",
                "2",
            )
        )
        self.assertEqual(
            [claim["package_id"] for claim in response["claims"]],
            package_ids[:2],
        )

    def test_corpus_claim_next_is_canonical_lexical_order(self) -> None:
        package_ids = [
            "cluster-2/theme-b/paper-2",
            "cluster-1/theme-c/paper-3",
            "cluster-1/theme-a/paper-1",
        ]
        self.make_registry([])
        corpus = self.root / "corpus"
        for package_id in package_ids:
            (corpus / package_id).mkdir(parents=True)
        response = result_json(
            run_cli(
                self.registry,
                "claim-next",
                "--corpus",
                str(corpus),
                "--operation",
                "REVIEW",
                "--owner",
                "parent",
                "--count",
                "3",
            )
        )
        self.assertEqual(
            [claim["package_id"] for claim in response["claims"]],
            sorted(package_ids),
        )

    def test_concurrent_claim_next_has_no_duplicate_claims(self) -> None:
        package_ids = [
            "cluster-1/theme/paper-1",
            "cluster-1/theme/paper-2",
        ]
        self.make_registry(package_ids)
        manifest = self.root / "manifest.json"
        manifest.write_text(
            json.dumps({"tasks": [{"relpath": item} for item in package_ids]}),
            encoding="utf-8",
        )
        command = [
            sys.executable,
            str(CLI),
            "--registry",
            str(self.registry),
            "claim-next",
            "--manifest",
            str(manifest),
            "--operation",
            "REVIEW",
            "--count",
            "1",
        ]
        processes = [
            subprocess.Popen(
                [*command, "--owner", f"parent-{index}"],
                cwd=REPO_ROOT,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            for index in range(2)
        ]
        outputs = [process.communicate(timeout=20) for process in processes]
        claims = []
        for process, (stdout, stderr) in zip(processes, outputs):
            self.assertEqual(process.returncode, 0, stderr)
            claims.extend(json.loads(stdout)["claims"])
        self.assertEqual(len(claims), 2)
        self.assertEqual(
            len({claim["package_id"] for claim in claims}), 2
        )

    def test_repair_only_follows_conditional_review(self) -> None:
        package_id = "cluster-1/theme/paper-1"
        self.make_registry([package_id])
        review = self.claim(package_id)
        result_json(
            run_cli(
                self.registry,
                "complete",
                "--package-id",
                package_id,
                "--owner",
                "parent",
                "--token",
                str(review["token"]),
                "--outcome",
                "CONDITIONAL",
            )
        )
        repair = self.claim(package_id, operation="REPAIR", owner="repair")
        invalid = run_cli(
            self.registry,
            "complete",
            "--package-id",
            package_id,
            "--owner",
            "repair",
            "--token",
            str(repair["token"]),
            "--outcome",
            "REJECT",
        )
        self.assertNotEqual(invalid.returncode, 0)
        published = run_cli(
            self.registry,
            "complete",
            "--package-id",
            package_id,
            "--owner",
            "repair",
            "--token",
            str(repair["token"]),
            "--outcome",
            "PUBLISHED",
        )
        self.assertNotEqual(published.returncode, 0)
        repaired = result_json(
            run_cli(
                self.registry,
                "complete",
                "--package-id",
                package_id,
                "--owner",
                "repair",
                "--token",
                str(repair["token"]),
                "--outcome",
                "PASS",
            )
        )
        self.assertEqual(repaired["state"], "ACCEPTED")

    def test_abandon_is_repair_only(self) -> None:
        package_id = "cluster-1/theme/paper-1"
        self.make_registry([package_id])
        review = self.claim(package_id)
        original = self.registry.read_bytes()
        blocked = run_cli(
            self.registry,
            "abandon",
            "--package-id",
            package_id,
            "--owner",
            "parent",
            "--token",
            str(review["token"]),
            "--reason",
            "review cannot continue",
        )
        self.assertNotEqual(blocked.returncode, 0)
        self.assertIn("only valid for an active REPAIR", blocked.stderr)
        self.assertEqual(self.registry.read_bytes(), original)
        result_json(
            run_cli(
                self.registry,
                "complete",
                "--package-id",
                package_id,
                "--owner",
                "parent",
                "--token",
                str(review["token"]),
                "--outcome",
                "CONDITIONAL",
            )
        )
        repair = self.claim(package_id, operation="REPAIR", owner="repair-parent")
        abandoned = result_json(
            run_cli(
                self.registry,
                "abandon",
                "--package-id",
                package_id,
                "--owner",
                "repair-parent",
                "--token",
                str(repair["token"]),
                "--reason",
                "repair lacks evidence",
            )
        )
        self.assertEqual(abandoned["state"], "ABANDONED")
        self.assertEqual(self.registry_entry(package_id)["operation"], "REPAIR")

    def test_seeded_registry_has_exact_manifest_set_and_hash(self) -> None:
        data = seeded_data()
        manifest = json.loads(SOURCE_MANIFEST.read_text(encoding="utf-8"))
        expected = sorted(task["relpath"] for task in manifest["tasks"])
        actual = [entry["package_id"] for entry in data["entries"]]
        self.assertEqual(len(actual), 100)
        self.assertEqual(actual, expected)
        self.assertEqual(len(set(actual)), 100)
        self.assertEqual(
            data["source"]["manifest"],
            "review_artifacts/materials_bench_whitelist_100_20260716/manifest.json",
        )
        self.assertEqual(
            data["source"]["sha256"],
            hashlib.sha256(SOURCE_MANIFEST.read_bytes()).hexdigest(),
        )
        self.assertTrue(all(entry["state"] == "ACCEPTED" for entry in data["entries"]))
        self.assertTrue(all(entry["active_claim"] is None for entry in data["entries"]))

    def test_validate_enforces_exact_historical_seed_invariant(self) -> None:
        base = seeded_data()
        cases: list[dict[str, object]] = []

        missing = json.loads(json.dumps(base))
        missing["entries"][0]["source"] = "dispatcher"
        cases.append(missing)

        extra = json.loads(json.dumps(base))
        extra["entries"].append(
            entry(
                "cluster-1/theme/paper-extra",
                state="ACCEPTED",
                operation="REVIEW",
                result="PASS",
                source="historical-v9-maintainer-accepted",
            )
        )
        extra["entries"].sort(key=lambda item: item["package_id"])
        cases.append(extra)

        invalid_state = json.loads(json.dumps(base))
        invalid_state["entries"][0]["state"] = "REVIEWED_REJECT"
        invalid_state["entries"][0]["result"] = "REJECT"
        cases.append(invalid_state)

        for index, invalid in enumerate(cases):
            with self.subTest(case=index):
                self.registry.write_text(
                    json.dumps(invalid, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8",
                )
                original = self.registry.read_bytes()
                process = run_cli(self.registry, "validate")
                self.assertNotEqual(process.returncode, 0)
                self.assertEqual(self.registry.read_bytes(), original)

    def test_validate_allows_nonhistorical_dispatcher_entries(self) -> None:
        self.make_registry(["cluster-1/theme/paper-future"])
        validated = result_json(run_cli(self.registry, "validate"))
        self.assertEqual(validated["entries"], 101)


if __name__ == "__main__":
    unittest.main()
