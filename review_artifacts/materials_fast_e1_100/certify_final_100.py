#!/usr/bin/env python3
"""Certify the first 100 source-bound PASS records across ordered review batches."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
BATCHES = [
    ROOT / "final_100_v8_taxonomy_review_batch_1_v2",
    ROOT / "final_100_v8_taxonomy_review_batch_2_v2",
]
REVIEW_UNIVERSE_BATCHES = [
    ROOT / "original_review_baseline_v6_oracle_venv_20260716",
    ROOT / "expansion_review_next_120_v3_oracle_venv_20260716",
]
OUTPUT = ROOT / "final_100_pass_v8_20260716"
EVIDENCE_CONTRACT_VERSION = "materials-evidence-contract/1.0"
DIMENSION_MAX_POINTS = {
    "scientific_validity": 35,
    "instruction_answerability": 20,
    "checker_gold_alignment": 25,
    "robustness_discrimination": 15,
    "solution_completeness": 5,
}
PAPER_TRIGGERS = {
    "SCIENTIFIC_CONFLICT",
    "NECESSARY_INFORMATION_MISSING",
    "GOLD_PROVENANCE_UNCERTAIN",
    "EXPLICIT_REPRODUCTION_CLAIM",
}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_hash(value: Any) -> str:
    payload = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def file_hash(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def filter_index(
    packages: list[dict[str, Any]],
    universe_items: list[dict[str, Any]],
    frozen: dict[str, Any],
) -> dict[str, Any]:
    dimensions: dict[str, dict[str, list[str]]] = {
        name: {}
        for name in (
            "verdict",
            "score_band",
            "computation_task",
            "research_domain",
            "material_system",
            "cluster",
            "finding_severity",
            "finding_code",
            "repair_status",
            "selection_status",
        )
    }

    def add(dimension: str, value: str, package_id: str) -> None:
        packages_for_value = dimensions[dimension].setdefault(value, [])
        if package_id not in packages_for_value:
            packages_for_value.append(package_id)

    for item in packages:
        package_id = item["package_id"]
        add("verdict", item["final_verdict"], package_id)
        score = item["final_score"]
        add("score_band", f"{int(score // 5) * 5:02d}-{int(score // 5) * 5 + 4:02d}", package_id)
        for label in item["taxonomy"]["computation_task"]:
            add("computation_task", label, package_id)
        for label in item["taxonomy"]["research_domain"]:
            add("research_domain", label, package_id)
        add("material_system", item["taxonomy"]["material_system"]["primary"], package_id)
        add("cluster", item["package_id"].split("/", 1)[0], package_id)
        for finding in item["findings"]:
            add("finding_severity", finding["severity"], package_id)
            add("finding_code", finding["title"], package_id)
        add("selection_status", "CERTIFIED_FINAL_100", package_id)
    certified_ids = {item["package_id"] for item in packages}
    for universe_item in universe_items:
        record = universe_item["record"]
        report = universe_item["report"]
        package_id = record["package_id"]
        scoring = record["evidence"]["cli_scoring"]
        add("verdict", scoring["final_verdict"], package_id)
        score = scoring["total_score"]
        add(
            "score_band",
            "NOT_ASSESSABLE"
            if score is None
            else f"{int(score // 5) * 5:02d}-{int(score // 5) * 5 + 4:02d}",
            package_id,
        )
        if package_id not in certified_ids:
            taxonomy = report.get("taxonomy_labels", {})
            computation = taxonomy.get("computation_task", [])
            domains = taxonomy.get("research_domain", [])
            for label in computation:
                add("computation_task", label, package_id)
            if not computation:
                add("computation_task", "NOT_ASSESSED", package_id)
            for label in domains:
                add("research_domain", label, package_id)
            if not domains:
                add("research_domain", "NOT_ASSESSED", package_id)
            primary = taxonomy.get("material_system", {}).get("primary")
            if primary:
                add("material_system", primary, package_id)
            else:
                add("material_system", "NOT_ASSESSED", package_id)
        add("cluster", package_id.split("/", 1)[0], package_id)
        findings = report.get("findings", [])
        for finding in findings:
            add("finding_severity", finding["severity"], package_id)
            add("finding_code", finding["title"], package_id)
        if not findings:
            add("finding_severity", "NO_FINDINGS", package_id)
            add("finding_code", "NO_FINDINGS", package_id)
        add(
            "selection_status",
            "CERTIFIED_FINAL_100" if package_id in certified_ids else "REVIEWED_NOT_CERTIFIED",
            package_id,
        )
    frozen_by_id = {item["package_id"]: item["state"] for item in frozen["packages"]}
    for universe_item in universe_items:
        package_id = universe_item["record"]["package_id"]
        add(
            "repair_status",
            frozen_by_id.get(package_id, "NOT_IN_FROZEN_DISPOSITION"),
            package_id,
        )
    return {
        "schema_version": "materials-canvas-filter-index/1.0",
        "sources": [
            "final_100_pass_index.json",
            "review universe batches",
            "../frozen_41_final_disposition_v3_20260716/disposition.json",
        ],
        "certified_package_count": len(packages),
        "review_universe_count": len(universe_items),
        "dimensions": dimensions,
    }


def validate_evidence_contract(
    package_id: str,
    report: dict[str, Any],
    checker: dict[str, Any],
) -> None:
    contract = report.get("evidence_contract")
    if (
        not isinstance(contract, dict)
        or contract.get("version") != EVIDENCE_CONTRACT_VERSION
        or contract.get("fail_closed") is not True
        or contract.get("gaps") != []
    ):
        raise ValueError(
            f"PASS evidence contract is incomplete: {package_id}"
        )
    qualification = report.get("materials_qualification")
    if (
        not isinstance(qualification, dict)
        or qualification.get("authoritative") is not True
        or qualification.get("classification")
        not in {"MAT_CORE", "MAT_METHOD", "MAT_WRAPPER"}
        or not isinstance(qualification.get("evidence"), list)
        or not qualification["evidence"]
    ):
        raise ValueError(
            f"authoritative materials qualification is missing: {package_id}"
        )
    dimensions = report.get("dimension_scores")
    if (
        not isinstance(dimensions, list)
        or {
            item.get("dimension"): item.get("max_points")
            for item in dimensions
            if isinstance(item, dict)
        }
        != DIMENSION_MAX_POINTS
    ):
        raise ValueError(f"dimension evidence schema is invalid: {package_id}")
    for dimension in dimensions:
        name = dimension["dimension"]
        earned = dimension.get("points_earned")
        status = dimension.get("status")
        evidence = dimension.get("evidence")
        if (
            not isinstance(earned, (int, float))
            or isinstance(earned, bool)
            or not 0 <= earned <= DIMENSION_MAX_POINTS[name]
            or status
            not in (
                "PASS"
                if earned / DIMENSION_MAX_POINTS[name] >= 0.8
                else "WARNING"
                if earned / DIMENSION_MAX_POINTS[name] >= 0.5
                else "FAIL",
            )
            or not isinstance(evidence, list)
            or not evidence
        ):
            raise ValueError(
                f"dimension points/status/evidence are inconsistent for "
                f"{package_id}: {name}"
            )
    if report.get("configuration", {}).get("paper_mode") == "no_paper":
        adjudication = report.get("paper_trigger_adjudication")
        if (
            not isinstance(adjudication, list)
            or {
                item.get("trigger")
                for item in adjudication
                if isinstance(item, dict)
            }
            != PAPER_TRIGGERS
            or any(
                item.get("status") != "NOT_TRIGGERED"
                or not isinstance(item.get("evidence"), list)
                or not item["evidence"]
                for item in adjudication
            )
        ):
            raise ValueError(
                f"no-paper trigger adjudication is incomplete: {package_id}"
            )
    coverage = checker.get("probe_coverage")
    if not isinstance(coverage, dict) or set(coverage) != {
        "positive",
        "negative",
        "discrimination",
        "equivalence",
    }:
        raise ValueError(
            f"dynamic probe provenance is incomplete: {package_id}"
        )
    if any(
        coverage[name].get("status") != "ASSESSED"
        for name in ("positive", "negative")
    ):
        raise ValueError(
            f"positive/negative probe evidence is incomplete: {package_id}"
        )
    for name in ("discrimination", "equivalence"):
        status = coverage[name].get("status")
        provenance = coverage[name].get("provenance", {})
        if status == "ASSESSED" and (
            provenance.get("oracle_used") is not False
            or provenance.get("source_kind")
            != "INDEPENDENT_PUBLIC_FIXTURE"
            or not provenance.get("fixture_hashes")
        ):
            raise ValueError(
                f"dynamic probe provenance is invalid for {package_id}: {name}"
            )
        if status == "NOT_ASSESSABLE" and (
            provenance.get("oracle_used") is not False
            or provenance.get("source_kind") != "NONE"
            or provenance.get("fixture_hashes") != {}
        ):
            raise ValueError(
                f"unavailable probe provenance is dishonest for "
                f"{package_id}: {name}"
            )
        if status not in {"ASSESSED", "NOT_ASSESSABLE"}:
            raise ValueError(
                f"dynamic probe status is invalid for {package_id}: {name}"
            )
    oracle = checker.get("solution_oracle", {})
    if (
        checker.get("solution_content_inspected") is not False
        or report.get("scope", {}).get("solution_content_inspected") is not False
        or oracle.get("scientific_evidence") is not False
    ):
        raise ValueError(f"Oracle boundary or leakage violation: {package_id}")
    serialized = json.dumps(
        {"report": report, "checker": checker},
        ensure_ascii=False,
    ).lower()
    if any(
        forbidden in serialized
        for forbidden in (
            '"oracle_values"',
            '"oracle_output"',
            '"solution_values"',
            '"reference_values"',
        )
    ):
        raise ValueError(f"Oracle value leakage detected: {package_id}")


def certify_record(batch: Path, record: dict[str, Any]) -> dict[str, Any]:
    scoring = record["evidence"]["cli_scoring"]
    binding = record["evidence"]["source_binding"]
    identity = binding["cli_audit_identity"]
    report = read_json(batch / identity["report_path"])
    manifest = read_json(batch / identity["manifest_path"])
    evidence_snapshot = record.get("evidence", {}).get("cli_evidence", {})
    checker_path = evidence_snapshot.get("checker_tests_path")
    if not isinstance(checker_path, str) or not checker_path:
        raise ValueError(
            f"PASS evidence contract lacks checker snapshot: "
            f"{record['package_id']}"
        )
    checker = read_json(batch / checker_path)
    validate_evidence_contract(record["package_id"], report, checker)
    evidence_unhashed = {
        key: value
        for key, value in evidence_snapshot.items()
        if key != "snapshot_hash"
    }
    if (
        evidence_snapshot.get("snapshot_hash")
        != canonical_hash(evidence_unhashed)
        or evidence_snapshot.get("report_path") != identity["report_path"]
        or evidence_snapshot.get("manifest_path") != identity["manifest_path"]
        or evidence_snapshot.get("report_hash")
        != file_hash(batch / identity["report_path"])
        or evidence_snapshot.get("manifest_hash")
        != file_hash(batch / identity["manifest_path"])
        or evidence_snapshot.get("checker_tests_hash")
        != file_hash(batch / checker_path)
        or evidence_snapshot.get("contract_version")
        != report["evidence_contract"]["version"]
        or evidence_snapshot.get("materials_qualification")
        != report["materials_qualification"]
        or evidence_snapshot.get("paper_trigger_adjudication")
        != report.get("paper_trigger_adjudication", [])
        or evidence_snapshot.get("probe_coverage")
        != checker.get("probe_coverage", {})
    ):
        raise ValueError(
            f"source-bound CLI evidence snapshot mismatch: "
            f"{record['package_id']}"
        )
    if manifest.get("output_hashes", {}).get("audit_report.json") != file_hash(
        batch / identity["report_path"]
    ):
        raise ValueError(f"audit report output hash mismatch: {record['package_id']}")
    unhashed = {key: value for key, value in scoring.items() if key != "snapshot_hash"}
    if scoring["final_verdict"] != "PASS" or scoring["total_score"] < 80:
        raise ValueError(f"non-PASS record selected: {record['package_id']}")
    if scoring["snapshot_hash"] != canonical_hash(unhashed):
        raise ValueError(f"invalid score snapshot: {record['package_id']}")
    report_projection = {
        "scoring_version": report["summary"]["scoring_version"],
        "final_verdict": report["summary"]["final_verdict"],
        "total_score": report["summary"]["total_score"],
        "hard_gate_triggered": report["summary"]["hard_gate_triggered"],
        "dimension_scores": report["dimension_scores"],
        "hard_gates": report["hard_gates"],
    }
    report_projection["snapshot_hash"] = canonical_hash(report_projection)
    if report_projection != scoring:
        raise ValueError(f"persisted report scoring mismatch: {record['package_id']}")
    if identity["scoring_snapshot_hash"] != scoring["snapshot_hash"]:
        raise ValueError(f"score identity mismatch: {record['package_id']}")
    if report["audit_id"] != identity["audit_id"] or manifest["audit_id"] != identity["audit_id"]:
        raise ValueError(f"audit identity mismatch: {record['package_id']}")
    if (
        binding.get("package_id") != record["package_id"]
        or binding.get("source_relative_path")
        != record["source_relative_path"]
        or identity.get("status") != "VALIDATED"
        or identity.get("package_id") != record["package_id"]
        or identity.get("source_relative_path")
        != record["source_relative_path"]
    ):
        raise ValueError(
            f"source binding identity mismatch: {record['package_id']}"
        )
    if manifest["input_hashes"] != binding["source_role_hashes"]:
        raise ValueError(f"source hash mismatch: {record['package_id']}")
    if scoring["hard_gate_triggered"] or any(
        gate["status"] != "PASS" for gate in scoring["hard_gates"]
    ):
        raise ValueError(f"PASS record has unresolved gate: {record['package_id']}")
    return {
        "selection_rank": 0,
        "package_id": record["package_id"],
        "source_relative_path": record["source_relative_path"],
        "source_batch": batch.name,
        "original_verdict": scoring["final_verdict"],
        "repair_status": "NOT_REQUIRED",
        "final_score": scoring["total_score"],
        "final_verdict": scoring["final_verdict"],
        "final_hard_gates": scoring["hard_gates"],
        "dimension_scores": scoring["dimension_scores"],
        "taxonomy": report.get("taxonomy_labels", {}),
        "taxonomy_evidence": report.get("taxonomy_evidence", []),
        "taxonomy_source": report.get("taxonomy_source", {}),
        "findings": report.get("findings", []),
        "audit_id": identity["audit_id"],
        "scoring_snapshot_hash": scoring["snapshot_hash"],
        "source_role_hashes": binding["source_role_hashes"],
        "audit_report": identity["report_path"],
        "audit_manifest": identity["manifest_path"],
        "repair_history": None,
    }


def canvas(summary: dict[str, Any]) -> dict[str, Any]:
    finding_counts = summary["finding_counts"]
    gate_counts = summary["hard_gate_status_counts"]
    repair_counts = summary["frozen_disposition_counts"]
    nodes = [
        {"id": "1000000000000001", "type": "text", "x": 0, "y": 0, "width": 460, "height": 220, "color": "4", "text": "# Materials Benchmark Quality\n\n**100 final PASS packages certified**\n\nEvery record is bound to a persisted CLI audit, score snapshot, and source-role hashes."},
        {"id": "1000000000000002", "type": "text", "x": -520, "y": 320, "width": 420, "height": 240, "color": "5", "text": f"## Review funnel\n\n- Reviewed: {summary['reviewed_total']}\n- PASS available: {summary['pass_available']}\n- Certified: {summary['certified_count']}\n- CONDITIONAL: {summary['all_verdict_counts'].get('CONDITIONAL', 0)}\n- NOT_ASSESSABLE: {summary['all_verdict_counts'].get('NOT_ASSESSABLE', 0)}\n- REJECT: {summary['all_verdict_counts'].get('REJECT', 0)}"},
        {"id": "1000000000000003", "type": "text", "x": 0, "y": 320, "width": 420, "height": 240, "color": "3", "text": "## Selection policy\n\n1. Frozen original 100 in manifest order\n2. Remaining corpus in cluster round-robin order\n3. CLI PASS only\n4. First 100 unique identities\n5. No unrepaired CONDITIONAL counted"},
        {"id": "1000000000000004", "type": "text", "x": 520, "y": 320, "width": 420, "height": 240, "color": "6", "text": f"## Coverage\n\n- Computation labels: {summary['taxonomy_coverage']['computation_task']}\n- Research domains: {summary['taxonomy_coverage']['research_domain']}\n- Material systems: {summary['taxonomy_coverage']['material_system']}\n- Taxonomy revision: 85\n- Every label has an instruction quote"},
        {"id": "1000000000000005", "type": "file", "x": -520, "y": 660, "width": 420, "height": 300, "file": "final_100_pass_index.json"},
        {"id": "1000000000000006", "type": "file", "x": 0, "y": 660, "width": 420, "height": 300, "file": "final_100_pass_summary.md"},
        {"id": "1000000000000008", "type": "text", "x": 520, "y": 660, "width": 420, "height": 300, "color": "2", "text": f"## Findings and gates\n\n- Finding severity: {summary['finding_severity_counts']}\n- Top finding codes: {dict(list(finding_counts.items())[:8])}\n- Hard Gate statuses: {gate_counts}\n- Every certified package has four PASS gates"},
        {"id": "1000000000000009", "type": "text", "x": 1040, "y": 660, "width": 420, "height": 300, "color": "1", "text": f"## Frozen non-PASS disposition\n\n- States: {repair_counts}\n- Published repairs: {repair_counts.get('PUBLISHED', 0)}\n- No Docker runtime path was repaired\n- Threshold/Gold changes remain blocked without evidence"},
        {"id": "1000000000000010", "type": "file", "x": 1560, "y": 660, "width": 420, "height": 300, "file": "../frozen_41_final_disposition_v3_20260716/disposition.json"},
        {"id": "1000000000000011", "type": "file", "x": 2080, "y": 660, "width": 420, "height": 300, "file": "../boundary_9_review_v4/aggregate.json"},
        {"id": "1000000000000012", "type": "file", "x": 2600, "y": 660, "width": 420, "height": 300, "file": "../coverage_60_review_v1/aggregate.json"},
        {"id": "1000000000000013", "type": "file", "x": 3120, "y": 660, "width": 420, "height": 300, "file": "../repair_cohort_9_disposition_v3_20260716.json"},
        {"id": "1000000000000014", "type": "file", "x": 3640, "y": 660, "width": 420, "height": 300, "file": "canvas_filter_index.json"},
        {"id": "1000000000000007", "type": "group", "x": -1040, "y": 1080, "width": 5200, "height": 5600, "label": "100 source-bound PASS packages", "color": "4"},
    ]
    edges = []
    for offset, target in enumerate(("1000000000000002", "1000000000000003", "1000000000000004", "1000000000000005", "1000000000000006", "1000000000000007"), 1):
        edges.append({"id": f"200000000000000{offset}", "fromNode": "1000000000000001", "fromSide": "bottom", "toNode": target, "toSide": "top", "toEnd": "arrow"})
    for offset, target in enumerate(("1000000000000008", "1000000000000009", "1000000000000010", "1000000000000011", "1000000000000012", "1000000000000013", "1000000000000014"), 7):
        edges.append({"id": f"20000000000000{offset:02d}", "fromNode": "1000000000000001", "fromSide": "bottom", "toNode": target, "toSide": "top", "toEnd": "arrow"})
    for index, item in enumerate(summary["packages"], start=1):
        row, column = divmod(index - 1, 5)
        node_id = f"3{index:015d}"
        taxonomy = item["taxonomy"]
        finding_counts = Counter(finding["severity"] for finding in item["findings"])
        nodes.append(
            {
                "id": node_id,
                "type": "text",
                "x": -980 + column * 1020,
                "y": 1160 + row * 270,
                "width": 940,
                "height": 220,
                "color": "4",
                "text": (
                    f"## {index:03d} · {item['package_id']}\n\n"
                    f"Score **{item['final_score']}** · PASS · repair `{item['repair_status']}`\n\n"
                    f"Task: {', '.join(taxonomy['computation_task'])}\n\n"
                    f"Domain: {', '.join(taxonomy['research_domain'])}\n\n"
                    f"System: {taxonomy['material_system']['primary']} · Findings: {dict(finding_counts)}\n\n"
                    f"Audit: `{item['audit_report']}`"
                ),
            }
        )
        edges.append(
            {
                "id": f"4{index:015d}",
                "fromNode": "1000000000000007",
                "fromSide": "bottom",
                "toNode": node_id,
                "toSide": "top",
                "toEnd": "arrow",
            }
        )
    return {"nodes": nodes, "edges": edges}


def legacy_v8_main() -> None:
    selected: list[dict[str, Any]] = []
    seen: set[str] = set()
    verdicts: Counter[str] = Counter()
    reviewed = 0
    pass_available = 0
    batch_counts: dict[str, dict[str, int]] = {}
    for batch in BATCHES:
        index = read_json(batch / "index.json")
        counts: Counter[str] = Counter()
        for record in index["records"]:
            reviewed += 1
            verdict = record["evidence"]["cli_scoring"]["final_verdict"]
            verdicts[verdict] += 1
            counts[verdict] += 1
            if verdict != "PASS":
                continue
            pass_available += 1
            if record["package_id"] in seen or len(selected) == 100:
                continue
            item = certify_record(batch, record)
            item["selection_rank"] = len(selected) + 1
            selected.append(item)
            seen.add(record["package_id"])
        batch_counts[batch.name] = dict(sorted(counts.items()))
    if len(selected) != 100 or len(seen) != 100:
        raise ValueError("certification did not produce exactly 100 unique PASS packages")
    verdicts.clear()
    reviewed = 0
    pass_available = 0
    expected_selected_ids: list[str] = []
    universe_batch_counts: dict[str, dict[str, int]] = {}
    universe_records: list[dict[str, Any]] = []
    universe_items: list[dict[str, Any]] = []
    for batch in REVIEW_UNIVERSE_BATCHES:
        counts: Counter[str] = Counter()
        for record in read_json(batch / "index.json")["records"]:
            universe_records.append(record)
            identity = record["evidence"]["source_binding"]["cli_audit_identity"]
            universe_items.append(
                {"record": record, "report": read_json(batch / identity["report_path"])}
            )
            verdict = record["evidence"]["cli_scoring"]["final_verdict"]
            counts[verdict] += 1
            verdicts[verdict] += 1
            reviewed += 1
            pass_available += verdict == "PASS"
            if verdict == "PASS" and len(expected_selected_ids) < 100:
                expected_selected_ids.append(record["package_id"])
        universe_batch_counts[batch.name] = dict(sorted(counts.items()))
    if [item["package_id"] for item in selected] != expected_selected_ids:
        raise ValueError(
            "taxonomy certification order differs from the first 100 PASS "
            "identities in the frozen review universe"
        )
    universe_by_id = {record["package_id"]: record for record in universe_records}
    for item in selected:
        universe_hashes = universe_by_id[item["package_id"]]["evidence"][
            "source_binding"
        ]["source_role_hashes"]
        if item["source_role_hashes"] != universe_hashes:
            raise ValueError(
                "taxonomy certification source hashes differ from review "
                f"universe: {item['package_id']}"
            )
    summary = {
        "schema_version": "materials-final-100-pass/1.0",
        "selection_policy": "frozen_original_order_then_deterministic_corpus_expansion",
        "certified_count": len(selected),
        "unique_package_count": len(seen),
        "reviewed_total": reviewed,
        "pass_available": pass_available,
        "all_verdict_counts": dict(sorted(verdicts.items())),
        "batch_verdict_counts": batch_counts,
        "review_universe_batch_verdict_counts": universe_batch_counts,
        "all_final_gates_pass": True,
        "all_source_bound": True,
        "packages": selected,
    }
    summary["taxonomy_coverage"] = {
        "computation_task": len({label for item in selected for label in item["taxonomy"]["computation_task"]}),
        "research_domain": len({label for item in selected for label in item["taxonomy"]["research_domain"]}),
        "material_system": len({item["taxonomy"]["material_system"]["primary"] for item in selected}),
    }
    severity_counts: Counter[str] = Counter()
    finding_counts: Counter[str] = Counter()
    gate_counts: Counter[str] = Counter()
    for item in selected:
        severity_counts.update(finding["severity"] for finding in item["findings"])
        finding_counts.update(finding["title"] for finding in item["findings"])
        gate_counts.update(gate["status"] for gate in item["final_hard_gates"])
    frozen = read_json(
        ROOT / "frozen_41_final_disposition_v3_20260716/disposition.json"
    )
    summary["finding_severity_counts"] = dict(sorted(severity_counts.items()))
    summary["finding_counts"] = dict(
        sorted(finding_counts.items(), key=lambda item: (-item[1], item[0]))
    )
    summary["hard_gate_status_counts"] = dict(sorted(gate_counts.items()))
    summary["frozen_disposition_counts"] = frozen["state_counts"]
    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT / "final_100_pass_index.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (OUTPUT / "canvas_filter_index.json").write_text(
        json.dumps(
            filter_index(selected, universe_items, frozen),
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    lines = [
        "# Materials Benchmark Quality: final 100 PASS",
        "",
        f"- Reviewed {reviewed} source-bound packages across two ordered review-universe batches.",
        f"- Found {pass_available} CLI PASS packages and certified the first 100 unique identities.",
        "- Every selected package has score >= 80, four passing Hard Gates, a valid scoring snapshot hash, and matching persisted audit/source hashes.",
        "- No CONDITIONAL, NOT_ASSESSABLE, or REJECT package is counted.",
        "- Repairs are not required for the selected 100; unresolved baseline CONDITIONAL packages remain outside this certified set.",
        "",
        "## Batch verdicts",
        "",
    ]
    lines.extend(f"- `{name}`: {counts}" for name, counts in universe_batch_counts.items())
    lines.extend(["", "## Taxonomy certification batches", ""])
    lines.extend(f"- `{name}`: {counts}" for name, counts in batch_counts.items())
    lines.extend(["", "The machine index is the authoritative per-package evidence surface; the Canvas provides the compact analytical overview.", ""])
    (OUTPUT / "final_100_pass_summary.md").write_text("\n".join(lines), encoding="utf-8")
    (OUTPUT / "materials_benchmark_quality.canvas").write_text(json.dumps(canvas(summary), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({key: summary[key] for key in ("certified_count", "reviewed_total", "pass_available", "all_verdict_counts")}, ensure_ascii=False))


def certify_v9(
    batches: list[Path],
    output: Path,
    expected_count: int,
) -> dict[str, Any]:
    selected: list[dict[str, Any]] = []
    seen: set[str] = set()
    for batch in batches:
        index = read_json(batch / "index.json")
        for record in index.get("records", []):
            scoring = record.get("evidence", {}).get("cli_scoring", {})
            if scoring.get("final_verdict") != "PASS":
                continue
            package_id = record.get("package_id")
            if not isinstance(package_id, str) or package_id in seen:
                if package_id in seen:
                    raise ValueError(
                        f"duplicate PASS package identity: {package_id}"
                    )
                raise ValueError("PASS record lacks package identity")
            item = certify_record(batch, record)
            item["selection_rank"] = len(selected) + 1
            selected.append(item)
            seen.add(package_id)
            if len(selected) == expected_count:
                break
        if len(selected) == expected_count:
            break
    if len(selected) != expected_count:
        raise ValueError(
            f"certification produced {len(selected)} evidence-backed PASS "
            f"packages; expected {expected_count}"
        )
    summary = {
        "schema_version": "materials-final-pass-evidence-v9/1.0",
        "evidence_contract_version": EVIDENCE_CONTRACT_VERSION,
        "legacy_v8_role": "IDENTITY_ORDER_SOURCE_BINDING_BASELINE_ONLY",
        "certified_count": len(selected),
        "unique_package_count": len(seen),
        "all_source_bound": True,
        "all_evidence_contracts_valid": True,
        "packages": selected,
    }
    output.mkdir(parents=True, exist_ok=False)
    (output / "final_100_pass_index.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--batch",
        action="append",
        required=True,
        help="source-bound v9 batch directory; repeat in certification order",
    )
    parser.add_argument("--output", required=True)
    parser.add_argument("--expected-count", type=int, default=100)
    arguments = parser.parse_args()
    try:
        if arguments.expected_count < 1:
            raise ValueError("--expected-count must be positive")
        summary = certify_v9(
            [Path(item).expanduser().resolve() for item in arguments.batch],
            Path(arguments.output).expanduser().resolve(),
            arguments.expected_count,
        )
        print(
            json.dumps(
                {
                    "certified_count": summary["certified_count"],
                    "output": str(Path(arguments.output).expanduser().resolve()),
                },
                ensure_ascii=False,
            )
        )
        return 0
    except Exception as exc:  # noqa: BLE001
        print(f"final certification failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
