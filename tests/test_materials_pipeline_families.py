from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tests.test_materials_benchmark_review_paper_grounded import (
    REPO_ROOT,
    RUNNER,
    copy_source_package,
)
from tests.test_materials_safe_repair import (
    INLINE_QUOTE,
    run_repair,
    write_plan,
)


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


def taxonomy_assessment(task: str, quote: str) -> dict[str, object]:
    return {
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
    }


def configure_answer_type(package: Path, policy: str) -> None:
    path = package / "tests/grading_spec.json"
    specification = json.loads(path.read_text(encoding="utf-8"))
    output = specification["output_contract"]["outputs"][0]
    output["target_policy"] = policy
    specification["target_policies"] = {output["file"]: policy}
    path.write_text(json.dumps(specification), encoding="utf-8")


def run_taxonomy_review(
    package: Path, assessment_path: Path
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(RUNNER),
            str(package),
            "--paper-mode",
            "no_paper",
            "--execution-level",
            "E1",
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
                            taxonomy_assessment(task, quote),
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
                            package / "benchmark_audit/audit_report.json"
                        ).read_text(encoding="utf-8")
                    )
                    self.assertEqual(
                        report["summary"]["disposition"], "REPAIR_QUEUE"
                    )
                    self.assertEqual(
                        report["summary"]["answer_type"], answer_type
                    )
                    self.assertEqual(
                        report["taxonomy_labels"]["computation_task"], [task]
                    )
                    finding = next(
                        item
                        for item in report["findings"]
                        if item["title"]
                        == "RESOURCE_VERIFICATION_INSUFFICIENT"
                    )
                    plan = workspace / f"{slug}-repair.json"
                    write_plan(plan, report["audit_id"], finding["finding_id"])
                    plan_value = json.loads(plan.read_text(encoding="utf-8"))
                    plan_value["agent_assessment"] = str(assessment_path)
                    plan.write_text(
                        json.dumps(plan_value, ensure_ascii=False),
                        encoding="utf-8",
                    )

                    repaired = run_repair(package, plan)

                    self.assertEqual(
                        repaired.returncode,
                        0,
                        msg=f"{repaired.stdout}\n{repaired.stderr}",
                    )
                    final_report = json.loads(
                        (
                            package / "benchmark_audit/audit_report.json"
                        ).read_text(encoding="utf-8")
                    )
                    self.assertEqual(
                        final_report["summary"]["disposition"],
                        "PUBLISH_CANDIDATE",
                    )
                    self.assertEqual(
                        final_report["summary"]["answer_type"], answer_type
                    )
                    self.assertEqual(
                        final_report["taxonomy_labels"]["computation_task"],
                        [task],
                    )
                    self.assertFalse(
                        final_report["scope"]["solution_content_inspected"]
                    )
                    self.assertTrue((package / "solution").is_dir())
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

            completed = subprocess.run(
                [sys.executable, str(RUNNER), str(package)],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                timeout=120,
                check=False,
            )

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            report = json.loads(
                (package / "benchmark_audit/audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(report["summary"]["materials_class"], "NON_MAT")
            self.assertEqual(report["summary"]["disposition"], "QUARANTINE")
            self.assertFalse(
                json.loads(
                    (
                        package
                        / "benchmark_audit/corpus_index_entry.json"
                    ).read_text(encoding="utf-8")
                )["publishable"]
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
        self.assertTrue(INLINE_QUOTE)


if __name__ == "__main__":
    unittest.main()
