from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tests.test_materials_benchmark_review_dual_lane import (
    REPO_ROOT,
    RUNNER,
    assessment as base_assessment,
    copy_source_package,
    external_audit_dir,
)
from tests.test_materials_safe_repair import safe_plan


VALIDATOR = (
    REPO_ROOT
    / ".cursor"
    / "skills"
    / "materials-benchmark-review"
    / "scripts"
    / "validate_skill_authoring.py"
)
FAMILIES = [
    (
        "dft",
        "电子结构",
        "DFT computes the electronic structure energy of a copper crystal.",
        "exact_match",
        "DETERMINISTIC_EXACT",
    ),
    (
        "md",
        "分子动力学与统计采样",
        "Molecular dynamics simulation computes a copper trajectory and material property.",
        "metric_recompute",
        "TOLERANCE_BASED",
    ),
    (
        "phase",
        "热力学与相稳定性",
        "CALPHAD computes a metal phase diagram and phase stability.",
        "set_match",
        "SET_VALUED",
    ),
    (
        "mechanics",
        "力学与弹性",
        "Compute the ranked elastic modulus and strength of a copper alloy.",
        "ranking",
        "RANKING_BASED",
    ),
    (
        "phonons",
        "声子与晶格动力学",
        "Phonopy computes crystal phonon evidence and a dispersion curve.",
        "structural_audit",
        "EVIDENCE_BASED",
    ),
    (
        "data",
        "数据驱动性质预测",
        "A numerical model predicts an open-ended copper material property.",
        "open_ended",
        "OPEN_ENDED",
    ),
]

VALID_SOLUTION = """#!/bin/sh
set -eu
output_dir="${OUTPUT_DIR:-/app/outputs}"
mkdir -p "$output_dir"
python3 - "$output_dir/dispersion_curves.csv" <<'PY'
import csv
import math
import sys

c11, c12, c44 = 1.68e12, 1.21e12, 0.75e12
rho, lattice = 8.96, 3.61
lattice_cm = lattice * 1e-8
epsilon = c11 - c12 - 2 * c44
factor8 = 8 / (rho * lattice_cm**2)
factor2 = 2 / (rho * lattice_cm**2)
limits = {
    "100": math.sqrt(2) * math.pi / lattice,
    "110": math.sqrt(5) * math.pi / lattice,
    "111": math.sqrt(3 / 2) * math.pi / lattice,
}

def frequency(direction, mode, k_value):
    if direction == "100":
        sin_sq = math.sin(lattice * k_value / (2 * math.sqrt(2))) ** 2
        omega_sq = factor8 * sin_sq * (c11 if mode == "L" else c44)
    elif direction == "110":
        sin_sq = math.sin(lattice * k_value / 4) ** 2
        if mode == "L":
            bracket = 2 * c11 - epsilon - (2 * c11 - c44 - epsilon) * sin_sq
        elif mode == "T1":
            bracket = epsilon + 2 * c44 - (c44 + epsilon) * sin_sq
        else:
            bracket = 2 * c44 - (2 * c44 - c11) * sin_sq
        omega_sq = factor8 * sin_sq * bracket
    else:
        sin_sq = math.sin(lattice * k_value / math.sqrt(6)) ** 2
        bracket = 3 * c11 - 2 * epsilon if mode == "L" else 3 * c44 + epsilon
        omega_sq = factor2 * sin_sq * bracket
    return math.sqrt(max(omega_sq, 0)) / 1e13

with open(sys.argv[1], "w", newline="", encoding="utf-8") as handle:
    writer = csv.writer(handle)
    writer.writerow(["direction", "mode", "k", "frequency"])
    for direction, k_max in limits.items():
        for mode in ("L", "T1", "T2"):
            for index in range(20):
                k_value = k_max * index / 19
                writer.writerow(
                    [direction, mode, k_value, frequency(direction, mode, k_value)]
                )
PY
"""


def taxonomy_assessment(
    task: str,
    quote: str,
    *,
    explicit_reproduction: bool = False,
) -> dict[str, object]:
    value = base_assessment()
    value.update({
        "schema_version": "0.1",
        "taxonomy": {
            "computation_task": [task],
            "research_domain": ["基础材料研究与材料发现"],
            "material_system": {
                "primary": "金属与合金",
                "secondary": [],
            },
        },
        "taxonomy_evidence": [
            {
                "dimension": "computation_task",
                "label": task,
                "package_file": "instruction.md",
                "package_quote": quote,
            },
            {
                "dimension": "research_domain",
                "label": "基础材料研究与材料发现",
                "package_file": "instruction.md",
                "package_quote": quote,
            },
            {
                "dimension": "material_system.primary",
                "label": "金属与合金",
                "package_file": "instruction.md",
                "package_quote": "This task focuses on face-centred cubic copper (Cu).",
            },
        ],
        "materials_qualification": {
            "classification": "MAT_CORE",
            "rationale": (
                "The public fixture defines a copper material, numerical "
                "inputs, domain operation, and scored endpoint."
            ),
            "evidence": [
                {
                    "axis": "object",
                    "package_file": "instruction.md",
                    "package_quote": "face-centred cubic copper (Cu)",
                },
                {
                    "axis": "data",
                    "package_file": "instruction.md",
                    "package_quote": "c11 = 1.68×10¹² dynes/cm²",
                },
                {
                    "axis": "operation",
                    "package_file": "instruction.md",
                    "package_quote": quote,
                },
                {
                    "axis": "endpoint",
                    "package_file": "instruction.md",
                    "package_quote": "dispersion_curves.csv",
                },
                {
                    "axis": "domain_dependence",
                    "package_file": "instruction.md",
                    "package_quote": quote,
                },
            ],
        },
    })
    return value


def solution_repair_plan(
    report: dict[str, object],
    finding: dict[str, object],
    assessment_path: Path,
) -> dict[str, object]:
    finding_id = str(finding["finding_id"])
    value = safe_plan(str(report["audit_id"]), finding_id)
    value["repair_class"] = "ASSISTED_FIX"
    value["justification"] = (
        "Restore the missing Oracle from the public constants, formulas, "
        "sampling rule, and output contract."
    )
    value["evidence"] = [
        {
            "id": "audit-finding",
            "source": f"benchmark_audit:{finding_id}",
            "quote": str(finding["title"]),
        },
        {
            "id": "public-inputs",
            "source": "instruction.md",
            "quote": "c11 = 1.68×10¹² dynes/cm²",
        },
        {
            "id": "public-formulas",
            "source": "instruction.md",
            "quote": "Evaluate the following formulas at each k value:",
        },
        {
            "id": "public-output-contract",
            "source": "instruction.md",
            "quote": "Each curve must contain at least 20 equally spaced k points.",
        },
    ]
    value["operations"][0]["content"] = VALID_SOLUTION
    value["operations"][0]["evidence_ids"] = [
        "audit-finding",
        "public-inputs",
        "public-formulas",
        "public-output-contract",
    ]
    value["regression_tests"] = [
        {"type": "file_exists", "file": "solution/solve.sh"},
        {"type": "file_executable", "file": "solution/solve.sh"},
    ]
    value["agent_assessment"] = str(assessment_path)
    return value


def configure_answer_type(package: Path, policy: str) -> None:
    path = package / "tests/grading_spec.json"
    specification = json.loads(path.read_text(encoding="utf-8"))
    output = specification["output_contract"]["outputs"][0]
    output["target_policy"] = policy
    specification["target_policies"] = {output["file"]: policy}
    path.write_text(json.dumps(specification), encoding="utf-8")


def correct_fixture_checker(package: Path) -> None:
    path = package / "tests/checker.py"
    checker = path.read_text(encoding="utf-8")
    checker = checker.replace(
        "bracket = (3*c11 - 2*eps) * sin_sq",
        "bracket = 3*c11 - 2*eps",
    ).replace(
        "bracket = (3*c44 + eps) * sin_sq",
        "bracket = 3*c44 + eps",
    ).replace(
        "omega_sq = factor * bracket",
        "omega_sq = factor * sin_sq * bracket",
    )
    path.write_text(checker, encoding="utf-8")


def run_taxonomy_review(
    package: Path, assessment_path: Path
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(RUNNER),
            str(package),
            "--agent-assessment",
            str(assessment_path),
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=120,
        check=False,
    )


class MaterialsPipelineFamilyTests(unittest.TestCase):
    def test_materials_families_cover_answer_contracts_end_to_end(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            observed: set[str] = set()
            for slug, task, quote, policy, answer_type in FAMILIES:
                with self.subTest(family=slug, answer_type=answer_type):
                    package = workspace / f"paper-{slug}"
                    copy_source_package(package)
                    correct_fixture_checker(package)
                    instruction = package / "instruction.md"
                    instruction.write_text(
                        instruction.read_text(encoding="utf-8")
                        + "\n"
                        + quote
                        + "\n",
                        encoding="utf-8",
                    )
                    configure_answer_type(package, policy)
                    assessment_path = workspace / f"{slug}-assessment.json"
                    assessment_path.write_text(
                        json.dumps(
                            taxonomy_assessment(
                                task,
                                quote,
                                explicit_reproduction=True,
                            ),
                            ensure_ascii=False,
                        ),
                        encoding="utf-8",
                    )

                    reviewed = run_taxonomy_review(package, assessment_path)

                    self.assertEqual(
                        reviewed.returncode,
                        0,
                        msg=reviewed.stderr,
                    )
                    report = json.loads(
                        (
                            external_audit_dir(package) / "audit_report.json"
                        ).read_text(encoding="utf-8")
                    )
                    self.assertEqual(
                        report["summary"]["disposition"],
                        "CONDITIONAL",
                    )
                    self.assertEqual(
                        report["summary"]["publication_route"],
                        "REPAIR_QUEUE",
                    )
                    self.assertEqual(
                        report["summary"]["answer_type"], answer_type
                    )
                    self.assertEqual(
                        report["taxonomy_labels"]["computation_task"], [task]
                    )
                    observed.add(answer_type)
            self.assertEqual(
                observed,
                {
                    "DETERMINISTIC_EXACT",
                    "TOLERANCE_BASED",
                    "SET_VALUED",
                    "RANKING_BASED",
                    "EVIDENCE_BASED",
                    "OPEN_ENDED",
                },
            )

    def test_boundary_non_material_routes_to_quarantine_without_repair(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "paper-boundary"
            copy_source_package(package)
            (package / "instruction.md").write_text(
                "Sort generic records and write /app/outputs/dispersion_curves.csv.\n",
                encoding="utf-8",
            )
            (package / "steps.json").write_text(
                json.dumps(
                    [
                        {
                            "id": "sort",
                            "output_file": "dispersion_curves.csv",
                            "description": "Sort generic records.",
                        }
                    ]
                ),
                encoding="utf-8",
            )
            (package / "resources.json").write_text(
                json.dumps({"version": 1, "resources": []}),
                encoding="utf-8",
            )
            (package / "manifest.json").write_text(
                json.dumps(
                    {
                        "cluster_id": 0,
                        "paper_id": "boundary",
                        "discipline": "generic software",
                    }
                ),
                encoding="utf-8",
            )
            # Classification is Agent-authoritative (no keyword prescreen); a
            # NON_MAT verdict is the only thing that fires the C01 Hard Gate.
            quote = (
                "Sort generic records and write "
                "/app/outputs/dispersion_curves.csv."
            )
            value = taxonomy_assessment("磁性与自旋", quote)
            for item in value["taxonomy_evidence"]:
                item["package_quote"] = quote
            value["materials_qualification"] = {
                "classification": "NON_MAT",
                "rationale": (
                    "The public task is generic record sorting with no "
                    "materials object, operation, endpoint, or domain "
                    "dependence."
                ),
                "evidence": [
                    {
                        "axis": axis,
                        "package_file": "instruction.md",
                        "package_quote": quote,
                    }
                    for axis in (
                        "object",
                        "operation",
                        "endpoint",
                        "domain_dependence",
                    )
                ],
            }
            value.pop("dimensions", None)
            value.pop("reproduction_type", None)
            assessment_path = Path(temporary) / "assessment.json"
            assessment_path.write_text(
                json.dumps(value, ensure_ascii=False), encoding="utf-8"
            )

            completed = run_taxonomy_review(package, assessment_path)

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            report = json.loads(
                (external_audit_dir(package) / "audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(report["summary"]["materials_class"], "NON_MAT")
            self.assertEqual(report["summary"]["disposition"], "REJECT")
            self.assertEqual(
                report["summary"]["publication_route"], "QUARANTINE"
            )
            c01_gate = next(
                gate
                for gate in report["hard_gates"]
                if gate["code"] == "NON_MATERIALS_TASK"
            )
            self.assertEqual(c01_gate["status"], "FAIL")
            self.assertEqual(c01_gate["dimension"], "C01")
            self.assertFalse(
                json.loads(
                    (
                        external_audit_dir(package) / "corpus_index_entry.json"
                    ).read_text(encoding="utf-8")
                )["publishable"]
            )

    def test_agent_materials_qualification_overrides_lexical_prescreen(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package = workspace / "paper-boundary-material"
            copy_source_package(package)
            quote = (
                "Use micromagnetic finite-element simulation of NdFeB grains "
                "with measured anisotropy and exchange data to calculate the "
                "coercive field that controls permanent-magnet performance."
            )
            (package / "instruction.md").write_text(quote + "\n", encoding="utf-8")
            value = taxonomy_assessment("磁性与自旋", quote)
            value["taxonomy_evidence"][2]["package_quote"] = quote
            value["materials_qualification"] = {
                "classification": "MAT_CORE",
                "rationale": "The public task couples a material object and data to a materials operation, endpoint, and domain-dependent interpretation.",
                "evidence": [
                    {
                        "axis": axis,
                        "package_file": "instruction.md",
                        "package_quote": quote,
                    }
                    for axis in (
                        "object",
                        "data",
                        "operation",
                        "endpoint",
                        "domain_dependence",
                    )
                ],
            }
            for dimension in value["dimensions"].values():
                for evidence in dimension["evidence"]:
                    evidence["package_file"] = "instruction.md"
                    evidence["package_quote"] = quote
            assessment_path = workspace / "assessment.json"
            assessment_path.write_text(
                json.dumps(value, ensure_ascii=False), encoding="utf-8"
            )

            completed = subprocess.run(
                [
                    sys.executable,
                    str(RUNNER),
                    str(package),
                    "--agent-assessment",
                    str(assessment_path),
                ],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                timeout=120,
                check=False,
            )

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            report = json.loads(
                (external_audit_dir(package) / "audit_report.json").read_text()
            )
            self.assertEqual(report["summary"]["materials_class"], "MAT_CORE")
            self.assertEqual(
                report["materials_qualification"]["prescreen"]["classification"],
                "NOT_PROVIDED",
            )
            self.assertTrue(report["materials_qualification"]["authoritative"])
            self.assertNotIn(
                "MATERIALS_ADMISSIBILITY_REQUIRES_ADJUDICATION",
                {finding["title"] for finding in report["findings"]},
            )
            self.assertEqual(
                {item["axis"] for item in report["materials_qualification"]["evidence"]},
                {"object", "data", "operation", "endpoint", "domain_dependence"},
            )
            self.assertFalse(
                any(
                    gate["status"] == "FAIL"
                    and gate["gate_id"] == "MATERIALS_TASK"
                    for gate in report["hard_gates"]
                )
            )
            self.assertFalse((package / "benchmark_repair").exists())

    def test_skill_authoring_contract_is_valid(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(VALIDATOR)],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
        self.assertEqual(
            completed.returncode,
            0,
            msg=f"{completed.stdout}\n{completed.stderr}",
        )
        result = json.loads(completed.stdout)
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["taxonomy_sources"], 1)
        self.assertEqual(
            set(result["skills"]),
            {"materials-benchmark-review", "materials-benchmark-repair"},
        )


if __name__ == "__main__":
    unittest.main()
