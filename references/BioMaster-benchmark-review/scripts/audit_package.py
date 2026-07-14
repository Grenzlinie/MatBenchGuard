#!/usr/bin/env python3
"""Deterministic static audit for biology benchmark packages.

This script intentionally ignores solution directories and reference answers.
It produces evidence for a model reviewer; it does not replace scientific judgment.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path
from typing import Any

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover
    tomllib = None

CORE_FILES = [
    "task.toml",
    "manifest.json",
    "instruction.md",
    "steps.json",
    "resources.json",
    "tests/grading_spec.json",
    "tests/checker.py",
]

BIO_TERMS = {
    "organism": [
        "gene", "genome", "protein", "cell", "tissue", "organism", "strain",
        "metabolite", "pathway", "transcript", "variant", "phenotype", "microbiome",
        "dna", "rna", "rapamycin", "bacteria", "yeast", "plant", "human",
    ],
    "data": [
        "fastq", "bam", "sam", "vcf", "fasta", "bed", "gff", "gtf", "pdb",
        "sbml", "expression matrix", "count matrix", "metabolic model", "sequencing",
        "single-cell", "single cell", "mass spectrometry", "microscopy",
    ],
    "method": [
        "alignment", "assembly", "differential expression", "variant calling",
        "annotation", "phylogen", "flux balance", "fba", "moma", "metabolic model",
        "peak calling", "clustering", "gene set", "pathway enrichment", "structure prediction",
    ],
    "endpoint": [
        "growth rate", "yield", "function", "interaction", "expression", "fitness",
        "cell type", "lineage", "disease", "response", "production", "activity",
        "binding", "structure", "phenotype",
    ],
}

ACCESSION_RE = re.compile(
    r"^(?:GCA|GCF)_\d+\.\d+$|^(?:GSE|GSM|GPL|SRR|SRP|SRS|SRX|ERP|ERR|ERS|ERX)\d+$|"
    r"^(?:ENCSR|ENCFF)\w+$|^[A-Za-z0-9]{4}$|^[OPQ][0-9][A-Z0-9]{3}[0-9]$"
)


def safe_extract(zpath: Path, dest: Path) -> None:
    with zipfile.ZipFile(zpath) as zf:
        for member in zf.infolist():
            target = (dest / member.filename).resolve()
            if not str(target).startswith(str(dest.resolve()) + os.sep):
                raise ValueError(f"unsafe zip path: {member.filename}")
        zf.extractall(dest)


def locate_root(path: Path) -> tuple[Path, tempfile.TemporaryDirectory[str] | None]:
    temp: tempfile.TemporaryDirectory[str] | None = None
    if path.is_file() and path.suffix.lower() == ".zip":
        temp = tempfile.TemporaryDirectory(prefix="bio_benchmark_audit_")
        dest = Path(temp.name)
        safe_extract(path, dest)
        path = dest
    if not path.exists():
        raise FileNotFoundError(path)
    if path.is_file():
        raise ValueError("input must be a benchmark directory or zip archive")

    candidates: list[tuple[int, int, Path]] = []
    for p in [path, *path.rglob("*")]:
        if not p.is_dir() or "__MACOSX" in p.parts or "solution" in p.parts:
            continue
        count = sum((p / rel).exists() for rel in CORE_FILES)
        if count:
            candidates.append((-count, len(p.parts), p))
    if not candidates:
        raise ValueError("could not locate a benchmark root")
    candidates.sort()
    return candidates[0][2], temp


def read_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def basename(value: Any) -> str:
    return str(value or "").replace("\\", "/").split("/")[-1]


def add_issue(issues: list[dict[str, Any]], severity: str, code: str, message: str, evidence: Any = None) -> None:
    item: dict[str, Any] = {"severity": severity, "code": code, "message": message}
    if evidence is not None:
        item["evidence"] = evidence
    issues.append(item)


def biological_prescreen(text: str) -> dict[str, Any]:
    low = text.lower()

    def has_term(term: str) -> bool:
        if " " in term or "-" in term or len(term) > 4:
            return term in low
        return re.search(r"(?<![a-z0-9])" + re.escape(term) + r"(?![a-z0-9])", low) is not None

    evidence: dict[str, list[str]] = {}
    score = 0
    for axis, terms in BIO_TERMS.items():
        hits = sorted({term for term in terms if has_term(term)})
        evidence[axis] = hits[:12]
        if hits:
            score += 2 if axis in {"method", "endpoint"} else 1
    if score >= 6:
        classification = "BIO_LIKELY"
    elif score >= 3:
        classification = "AMBIGUOUS"
    else:
        classification = "NON_BIO_LIKELY"
    return {"classification": classification, "lexical_score": score, "evidence": evidence}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="benchmark directory or zip")
    parser.add_argument("--output", default="audit_static.json")
    args = parser.parse_args()

    issues: list[dict[str, Any]] = []
    parse_status: dict[str, Any] = {}
    temp = None
    try:
        root, temp = locate_root(Path(args.input).expanduser().resolve())

        for rel in CORE_FILES:
            p = root / rel
            if not p.exists():
                sev = "FATAL" if rel in {"instruction.md", "tests/checker.py", "tests/grading_spec.json"} else "HIGH"
                add_issue(issues, sev, "MISSING_FILE", f"missing expected file: {rel}")
                parse_status[rel] = "missing"
                continue
            try:
                if rel.endswith(".json"):
                    read_json(p)
                elif rel.endswith(".toml"):
                    if tomllib is None:
                        raise RuntimeError("tomllib unavailable")
                    with p.open("rb") as f:
                        tomllib.load(f)
                else:
                    read_text(p)
                parse_status[rel] = "ok"
            except Exception as exc:  # noqa: BLE001
                parse_status[rel] = f"error: {exc}"
                add_issue(issues, "FATAL", "PARSE_ERROR", f"cannot parse {rel}", repr(exc))

        instruction = read_text(root / "instruction.md") if (root / "instruction.md").exists() else ""
        checker = read_text(root / "tests/checker.py") if (root / "tests/checker.py").exists() else ""
        steps = read_json(root / "steps.json") if (root / "steps.json").exists() else []
        resources = read_json(root / "resources.json") if (root / "resources.json").exists() else {}
        spec = read_json(root / "tests/grading_spec.json") if (root / "tests/grading_spec.json").exists() else {}
        manifest = read_json(root / "manifest.json") if (root / "manifest.json").exists() else {}

        combined = "\n".join([instruction, json.dumps(steps), json.dumps(resources), json.dumps(manifest)])
        biology = biological_prescreen(combined)
        if biology["classification"] == "NON_BIO_LIKELY":
            add_issue(issues, "FATAL", "NON_BIO_PRESCREEN", "package lacks clear biological objects, methods, and endpoints")
        elif biology["classification"] == "AMBIGUOUS":
            add_issue(issues, "HIGH", "BIOLOGY_AMBIGUOUS", "biological relevance requires model adjudication")

        step_outputs = {basename(s.get("output_file")) for s in steps if basename(s.get("output_file"))}
        step_evidence = {basename(s.get("evidence")) for s in steps if basename(s.get("evidence"))}
        contract_outputs = {
            basename(o.get("file"))
            for o in (spec.get("output_contract", {}) or {}).get("outputs", [])
            if basename(o.get("file"))
        }
        checker_outputs = {
            basename(s.get("output_file"))
            for s in (spec.get("steps", spec.get("checks", [])) or [])
            if basename(s.get("output_file"))
        }
        instruction_outputs = set(re.findall(r"/app/outputs/([A-Za-z0-9_.-]+)", instruction))

        for name in sorted(step_outputs - contract_outputs):
            add_issue(issues, "HIGH", "OUTPUT_NOT_CONTRACTED", f"step output is absent from output contract: {name}")
        for name in sorted(contract_outputs - checker_outputs):
            add_issue(issues, "HIGH", "OUTPUT_NOT_SCORED", f"contract output is not referenced by grading steps: {name}")
        for name in sorted(step_evidence - contract_outputs):
            sev = "FATAL" if name and name.lower() in instruction.lower() and ("must" in instruction.lower() or "required" in instruction.lower()) else "HIGH"
            add_issue(issues, sev, "EVIDENCE_NOT_ENFORCED", f"declared evidence is absent from output contract: {name}")
        for name in sorted(instruction_outputs - (contract_outputs | step_evidence | step_outputs)):
            add_issue(issues, "MEDIUM", "INSTRUCTION_ONLY_OUTPUT", f"instruction names an output not represented elsewhere: {name}")

        weights = []
        for st in spec.get("steps", spec.get("checks", [])) or []:
            try:
                weights.append(float(st.get("weight", 0)))
            except (TypeError, ValueError):
                add_issue(issues, "HIGH", "INVALID_WEIGHT", "non-numeric grading weight", st.get("weight"))
        if weights and abs(sum(weights) - 1.0) > 1e-6:
            add_issue(issues, "HIGH", "WEIGHTS_NOT_ONE", "grading weights do not sum to 1", sum(weights))

        policies = {
            str(o.get("target_policy", ""))
            for o in (spec.get("output_contract", {}) or {}).get("outputs", [])
        }
        checker_low = checker.lower()
        model_mentions = [name for name in step_evidence if name and name.lower() in checker_low]
        recompute_claim = "metric_recompute" in policies or "recompute" in json.dumps(spec).lower() or "recompute" in instruction.lower()
        hardcoded_compare = any(token in checker for token in ["target_value", "expected_entries", "fph_gold"])
        scientific_engine = any(token in checker_low for token in ["cobra", "sbml", "pysam", "scanpy", "anndata", "biopython", "bedtools", "vcf", "samtools"])
        if recompute_claim and hardcoded_compare and not scientific_engine:
            add_issue(
                issues,
                "FATAL",
                "RECOMPUTE_CLAIM_MISMATCH",
                "package claims metric recomputation, but checker appears to compare submitted values to hard-coded targets",
                {"policies": sorted(policies), "scientific_engine_detected": scientific_engine},
            )
        if step_evidence and not model_mentions:
            add_issue(
                issues,
                "FATAL",
                "LOAD_BEARING_EVIDENCE_IGNORED",
                "checker does not reference declared supporting evidence",
                sorted(step_evidence),
            )

        load_bearing_process = [
            s for s in steps
            if str(s.get("role", "")).lower() == "process" and not bool(s.get("load_bearing", False))
            and basename(s.get("evidence"))
        ]
        if load_bearing_process:
            add_issue(
                issues,
                "HIGH",
                "PROCESS_MARKED_NON_LOAD_BEARING",
                "a process that produces required downstream evidence is marked non-load-bearing",
                [s.get("id") for s in load_bearing_process],
            )

        expected_count = 0
        for st in spec.get("steps", spec.get("checks", [])) or []:
            if isinstance(st.get("expected_entries"), list):
                expected_count += len(st["expected_entries"])
        full_list_claim = any(x in instruction.lower() for x in ["full list", "every reaction", "all reactions", "for each reaction"])
        if full_list_claim and expected_count and expected_count < 10:
            add_issue(
                issues,
                "FATAL",
                "SPARSE_CHECKER_COVERAGE",
                "instruction requires a full result set but checker verifies only a small fixed subset",
                {"checked_entries": expected_count},
            )

        pass_threshold = spec.get("pass_threshold")
        if isinstance(pass_threshold, (int, float)) and weights:
            largest = max(weights)
            if largest >= float(pass_threshold):
                add_issue(
                    issues,
                    "HIGH",
                    "SINGLE_COMPONENT_CAN_PASS",
                    "one grading component can meet the pass threshold by itself",
                    {"largest_weight": largest, "pass_threshold": pass_threshold},
                )

        homepage_resources = []
        unspecified_packages = []
        for r in resources.get("resources", []) if isinstance(resources, dict) else []:
            access = r.get("access", {}) or {}
            method = str(access.get("method", ""))
            if method == "url":
                url = str(access.get("url", ""))
                if re.match(r"^https?://[^/]+/?$", url):
                    homepage_resources.append({"id": r.get("id"), "url": url})
            elif method == "accession":
                acc = str(access.get("accession", "")).strip()
                if not acc or not ACCESSION_RE.match(acc):
                    add_issue(issues, "HIGH", "ACCESSION_UNRESOLVED_FORMAT", "accession is absent or not recognized", acc)
            elif method == "package":
                pkg = str(access.get("package", "")).strip()
                if pkg and not any(k in access for k in ["version", "ecosystem", "install"]):
                    unspecified_packages.append(pkg)
        if homepage_resources:
            add_issue(
                issues,
                "HIGH",
                "DATABASE_HOMEPAGE_ONLY",
                "database homepages do not identify exact downloadable inputs or versions",
                homepage_resources,
            )
        if unspecified_packages:
            add_issue(
                issues,
                "MEDIUM",
                "UNPINNED_PACKAGES",
                "package resources lack ecosystem and version pins",
                sorted(unspecified_packages),
            )

        difficulty = (manifest.get("difficulty", {}) or {}).get("compute_estimate", {}) if isinstance(manifest, dict) else {}
        if difficulty and not any(k in difficulty for k in ["assumptions", "range", "lower_bound", "upper_bound"]):
            add_issue(issues, "LOW", "POINT_ESTIMATE_ONLY", "compute estimate is a point estimate without an uncertainty range")

        severity_rank = {"FATAL": 4, "HIGH": 3, "MEDIUM": 2, "LOW": 1}
        max_sev = max((severity_rank[i["severity"]] for i in issues), default=0)
        static_verdict = "REJECT" if max_sev >= 4 else "CONDITIONAL" if max_sev >= 2 else "PASS"

        result = {
            "schema_version": "1.0",
            "benchmark_root": str(root),
            "solution_content_inspected": False,
            "parse_status": parse_status,
            "biology_prescreen": biology,
            "cross_file_sets": {
                "step_outputs": sorted(step_outputs),
                "step_evidence": sorted(step_evidence),
                "contract_outputs": sorted(contract_outputs),
                "grading_outputs": sorted(checker_outputs),
                "instruction_outputs": sorted(instruction_outputs),
            },
            "issues": sorted(issues, key=lambda x: (-severity_rank[x["severity"]], x["code"])),
            "static_verdict": static_verdict,
            "limitations": [
                "biology classification is a lexical prescreen and requires model adjudication",
                "network reachability is not tested by this script",
                "paper fidelity is not tested by this script",
                "task-specific checker attacks require domain-aware probes",
            ],
        }
        Path(args.output).write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
        print(json.dumps({"static_verdict": static_verdict, "issue_count": len(issues), "output": args.output}, indent=2))
        return 0
    except Exception as exc:  # noqa: BLE001
        print(f"audit failed: {exc}", file=sys.stderr)
        return 2
    finally:
        if temp is not None:
            temp.cleanup()


if __name__ == "__main__":
    raise SystemExit(main())
