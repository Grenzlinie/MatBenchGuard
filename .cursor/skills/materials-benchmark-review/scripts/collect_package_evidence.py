#!/usr/bin/env python3
"""Collect conservative structural facts for Agent-led materials review.

The output deliberately contains facts, candidates, and limitations—not
findings, scores, criteria, or verdicts.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import ipaddress
import json
import os
import re
import socket
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

SCHEMA = "materials-mechanical-evidence/1.3"
URL_RE = re.compile(r"https?://[^\s<>)\]}`\"']+")
OUTPUT_RE = re.compile(r"(?:/app/outputs/)?([A-Za-z0-9_.-]+\.(?:json|jsonl|csv|tsv|txt|yaml|yml|cif|xyz|vasp|png|npz|npy|pt|pth|ckpt|onnx))", re.I)
MODEL_RE = re.compile(r"\b(model|weights?|checkpoint|potential|tokenizer|pretrained|ckpt|onnx|\.pt|\.pth)\b", re.I)
DATA_RE = re.compile(r"\b(dataset|data file|input file|structure file|database|annotation|split)\b", re.I)
ANALYSIS_WINDOW_RE = re.compile(
    r"(?:(?:final|last)\s+|最后\s*)(\d+(?:\.\d+)?)\s*"
    r"(fs|ps|ns|(?:u|µ|μ)s|ms|s)\b",
    re.I,
)
SIMULATION_PARAMETER_PATTERNS = {
    "CARTESIAN_AXIS_REFERENCE": re.compile(
        r"(?:\b[xyz][-_ ]?(?:axis|direction|component)\b|"
        r"\b(?:epsilon|strain|stress|force)[-_ ]?[xyz]{1,2}\b|"
        r"[εσ]_[xyz]{1,2}|沿着?\s*[xyz]\s*(?:轴|方向))",
        re.I,
    ),
    "CRYSTALLOGRAPHIC_REFERENCE": re.compile(
        r"(?:\[[0-9\-\s\u0305]+\]|\{[0-9\-\s\u0305]+\}|"
        r"\([0-9\-\s\u0305]+\)|晶向|晶面|Miller)",
        re.I,
    ),
    "SOLVER_CHOICE_LANGUAGE": re.compile(
        r"\b(?:choose|select|arbitrary|user[- ]defined|as desired|"
        r"any reasonable)\b|自行(?:选择|设定)|自设参数|任意(?:选择|方向|参数)",
        re.I,
    ),
    "DERIVED_PARAMETER_LANGUAGE": re.compile(
        r"\b(?:derive|derived|calculate[ds]? from|computed? from|obtained? from|"
        r"based on (?:step|the previous))\b|"
        r"(?:由|根据).{0,40}(?:计算|推导|求得|得到)",
        re.I,
    ),
    "FIXED_TARGET_LANGUAGE": re.compile(
        r"\b(?:fixed|target value|reference match|paper value|must equal|"
        r"set to|maintain(?:ed)? at)\b|固定|目标值|匹配(?:论文|参考)|保持为",
        re.I,
    ),
}
TIME_FACTORS_SECONDS = {
    "fs": 1e-15,
    "ps": 1e-12,
    "ns": 1e-9,
    "us": 1e-6,
    "µs": 1e-6,
    "μs": 1e-6,
    "ms": 1e-3,
    "s": 1.0,
}
REQUIRED_CORE_PATHS = (
    "manifest.json",
    "task.toml",
    "resources.json",
    "steps.json",
    "instruction.md",
    "paper/paper.md",
    "tests/grading_spec.json",
    "tests/checker.py",
    "tests/test.sh",
)
GOLD_RISK_PATTERNS = {
    "RANDOM_OR_PERTURBED_REFERENCE": re.compile(
        r"\b(?:random|default_rng|randn?|uniform|normal|gauss|noise|jitter|perturb)\b",
        re.I,
    ),
    "INTERPOLATED_OR_FITTED_REFERENCE": re.compile(
        r"\b(?:interp|interp1d|interpolate|polyfit|curve_fit|linspace|trend[-_ ]?fit)\b",
        re.I,
    ),
    "SMOKE_OR_SYNTHETIC_REFERENCE": re.compile(
        r"\b(?:smoke|dummy|placeholder|synthetic|mock|fabricat(?:e|ed|ion)|toy data)\b",
        re.I,
    ),
}
TEXT_SUFFIXES = {".py", ".sh", ".json", ".toml", ".yaml", ".yml", ".md", ".txt"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()


def rel(path: Path, root: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def locate(root: Path, names: tuple[str, ...]) -> Path | None:
    for name in names:
        path = root / name
        if path.is_file() and not path.is_symlink():
            return path
    return None


def inventory(root: Path) -> tuple[list[dict[str, Any]], list[dict[str, str]]]:
    rows, limitations = [], []
    paths: list[Path] = []
    for current, directories, filenames in os.walk(root):
        current_path = Path(current)
        if current_path == root and "solution" in directories:
            directories.remove("solution")
        paths.extend(current_path / name for name in filenames)
    for path in sorted(paths):
        relative = path.relative_to(root)
        if path.is_symlink():
            limitations.append({"stage": "inventory", "path": relative.as_posix(), "reason": "symlink not followed"})
            continue
        if not path.is_file():
            continue
        role = "other"
        name = relative.as_posix()
        if name == "instruction.md": role = "instruction"
        elif name.startswith("paper/"): role = "paper"
        elif name.endswith("tests/checker.py"): role = "checker"
        elif name.endswith("tests/grading_spec.json"): role = "grading_spec"
        elif name.endswith("tests/test.sh"): role = "test_entrypoint"
        elif name.startswith("environment/") or name in {"task.toml", "requirements.txt", "pyproject.toml"}: role = "environment"
        elif MODEL_RE.search(name): role = "model_candidate"
        elif DATA_RE.search(name): role = "data_candidate"
        rows.append({"path": name, "role": role, "size": path.stat().st_size, "sha256": sha256(path)})
    return rows, limitations


def package_structure(root: Path) -> dict[str, Any]:
    records = []
    for name in REQUIRED_CORE_PATHS:
        path = root / name
        present = path.is_file() and not path.is_symlink()
        records.append({"path": name, "required": True, "present": present})
    missing = [item["path"] for item in records if not item["present"]]
    entrypoint = root / "tests/test.sh"
    if entrypoint.is_file() and not entrypoint.is_symlink():
        text = entrypoint.read_text(encoding="utf-8", errors="replace")
        entrypoint_facts = {
            "path": "tests/test.sh",
            "status": (
                "READY"
                if text.strip() and text.startswith("#!") and entrypoint.stat().st_mode & 0o111
                else "INVALID"
            ),
            "non_empty": bool(text.strip()),
            "has_shebang": text.startswith("#!"),
            "executable_bit": bool(entrypoint.stat().st_mode & 0o111),
        }
    else:
        entrypoint_facts = {
            "path": "tests/test.sh",
            "status": "MISSING",
            "non_empty": False,
            "has_shebang": False,
            "executable_bit": False,
        }
    return {
        "status": "COMPLETE" if not missing and entrypoint_facts["status"] == "READY" else "INCOMPLETE",
        "required_files": records,
        "missing_required_files": missing,
        "test_entrypoint": entrypoint_facts,
    }


def _json_text_records(value: Any, path: str = "$") -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    if isinstance(value, str):
        records.append({"locator": path, "text": value})
    elif isinstance(value, list):
        for index, item in enumerate(value):
            records.extend(_json_text_records(item, f"{path}[{index}]"))
    elif isinstance(value, dict):
        for key, item in value.items():
            records.extend(_json_text_records(item, f"{path}.{key}"))
    return records


def contract_text_records(root: Path) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    instruction = root / "instruction.md"
    if instruction.is_file() and not instruction.is_symlink():
        for line, text in enumerate(
            instruction.read_text(encoding="utf-8", errors="replace").splitlines(), 1
        ):
            records.append(
                {"path": "instruction.md", "locator": f"line {line}", "text": text}
            )
    for name in ("steps.json", "tests/grading_spec.json"):
        path = root / name
        if not path.is_file() or path.is_symlink():
            continue
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        for item in _json_text_records(value):
            records.append({"path": name, **item})
    return records


def analysis_window_candidates(root: Path) -> dict[str, Any]:
    mentions = []
    for record in contract_text_records(root):
        for match in ANALYSIS_WINDOW_RE.finditer(record["text"]):
            unit = match.group(2).lower().replace("u", "u")
            value = float(match.group(1))
            mentions.append(
                {
                    **record,
                    "quote": match.group(0),
                    "value": value,
                    "unit": unit,
                    "seconds": value * TIME_FACTORS_SECONDS[unit],
                }
            )
    distinct = sorted({round(item["seconds"], 18) for item in mentions})
    return {
        "mentions": mentions,
        "conflict_candidate": len(distinct) > 1,
        "distinct_windows_seconds": distinct,
        "candidate_only": True,
        "limitation": (
            "Different final/last windows can be legitimate for different outputs; "
            "the Agent must decide whether they govern the same analysis."
        ),
    }


def simulation_parameter_candidates(root: Path) -> dict[str, Any]:
    mentions = []
    for record in contract_text_records(root):
        matched = [
            pattern_id
            for pattern_id, pattern in SIMULATION_PARAMETER_PATTERNS.items()
            if pattern.search(record["text"])
        ]
        if matched:
            mentions.append(
                {
                    **record,
                    "candidate_types": matched,
                    "quote": record["text"].strip(),
                    "candidate_only": True,
                }
            )
    present = {
        pattern_id
        for mention in mentions
        for pattern_id in mention["candidate_types"]
    }
    return {
        "mentions": mentions,
        "candidate_types_present": sorted(present),
        "coordinate_dependency_candidate": {
            "candidate_only": True,
            "present": {
                "CARTESIAN_AXIS_REFERENCE",
                "CRYSTALLOGRAPHIC_REFERENCE",
            }.issubset(present),
        },
        "upstream_downstream_dependency_candidate": {
            "candidate_only": True,
            "present": bool(
                present
                & {"SOLVER_CHOICE_LANGUAGE", "DERIVED_PARAMETER_LANGUAGE"}
            )
            and "FIXED_TARGET_LANGUAGE" in present,
        },
        "limitation": (
            "Lexical hits cannot establish completeness or inconsistency. "
            "The Agent must read the full paper and package and build the "
            "simulation parameter dependency matrix even when no hits occur."
        ),
    }


def gold_provenance_risk_candidates(root: Path) -> list[dict[str, Any]]:
    candidates = []
    for top in ("tests",):
        directory = root / top
        if not directory.is_dir():
            continue
        for path in sorted(directory.rglob("*")):
            if (
                not path.is_file()
                or path.is_symlink()
                or path.suffix.lower() not in TEXT_SUFFIXES
                or path.stat().st_size > 2 * 1024 * 1024
            ):
                continue
            for line, text in enumerate(
                path.read_text(encoding="utf-8", errors="replace").splitlines(), 1
            ):
                for pattern_id, pattern in GOLD_RISK_PATTERNS.items():
                    if pattern.search(text):
                        candidates.append(
                            {
                                "pattern_id": pattern_id,
                                "path": path.relative_to(root).as_posix(),
                                "line": line,
                                "quote": text.strip(),
                                "candidate_only": True,
                            }
                        )
    return candidates


def instruction_contract(path: Path | None) -> dict[str, Any]:
    if path is None:
        return {"status": "MISSING", "output_mentions": [], "urls": [], "resource_candidates": [], "limitations": []}
    text = path.read_text(encoding="utf-8", errors="replace")
    mentions: dict[str, list[dict[str, Any]]] = {}
    resources = []
    for number, line in enumerate(text.splitlines(), 1):
        for match in OUTPUT_RE.finditer(line):
            mentions.setdefault(match.group(1), []).append({"line": number, "quote": line.strip()})
        if URL_RE.search(line) or DATA_RE.search(line) or MODEL_RE.search(line):
            resources.append({
                "line": number, "quote": line.strip(), "urls": URL_RE.findall(line),
                "data_candidate": bool(DATA_RE.search(line)), "model_candidate": bool(MODEL_RE.search(line)),
            })
    return {
        "status": "PARSED", "path": path.name,
        "output_mentions": [{"file": name, "mentions": refs} for name, refs in sorted(mentions.items())],
        "urls": sorted(set(URL_RE.findall(text))), "resource_candidates": resources,
        "limitations": ["Output extraction is lexical; Agent must adjudicate roles, aliases, and prose equivalence."],
    }


def resources_contract(path: Path | None) -> dict[str, Any]:
    if path is None:
        return {"status": "MISSING", "path": None, "url_candidates": [], "limitations": []}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {
            "status": "PARSE_ERROR",
            "path": path.name,
            "url_candidates": [],
            "limitations": [f"JSON parse failed: {exc}"],
        }
    candidates = []
    for item in _json_text_records(value):
        for url in URL_RE.findall(item["text"]):
            candidates.append({"url": url, "locator": item["locator"]})
    return {
        "status": "PARSED",
        "path": path.name,
        "url_candidates": candidates,
        "limitations": [],
    }


def grading_contract(path: Path | None) -> dict[str, Any]:
    result: dict[str, Any] = {"status": "MISSING", "outputs": [], "steps": [], "weights": [], "limitations": []}
    if path is None:
        return result
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {**result, "status": "PARSE_ERROR", "limitations": [f"JSON parse failed: {exc}"]}
    if not isinstance(value, dict):
        return {**result, "status": "UNSUPPORTED_SHAPE", "raw_type": type(value).__name__, "limitations": ["Root is not an object; no semantic defect inferred."]}
    contract = value.get("output_contract")
    outputs = contract.get("outputs") if isinstance(contract, dict) else None
    if isinstance(outputs, list):
        result["outputs"] = [item for item in outputs if isinstance(item, dict)]
        if len(result["outputs"]) != len(outputs):
            result["limitations"].append("Some output entries are not objects and were preserved only in raw grading_spec.")
    else:
        result["limitations"].append("output_contract.outputs is absent or not a list; Agent must inspect the raw contract.")
    steps = value.get("steps", value.get("checks"))
    if isinstance(steps, list):
        result["steps"] = [item for item in steps if isinstance(item, dict)]
    else:
        result["limitations"].append("steps/checks is absent or not a list; no schema finding inferred.")
    for index, step in enumerate(result["steps"]):
        weight = step.get("weight")
        if isinstance(weight, (int, float)) and not isinstance(weight, bool):
            result["weights"].append({"step_index": index, "step_id": step.get("id"), "weight": weight})
    finite_weights = [float(item["weight"]) for item in result["weights"]]
    result["weight_summary"] = {
        "declared_step_count": len(result["steps"]),
        "numeric_weight_count": len(finite_weights),
        "numeric_weight_sum": sum(finite_weights),
        "all_numeric_weights_nonnegative": all(weight >= 0 for weight in finite_weights),
        "candidate_only": True,
    }
    result.update({"status": "PARSED", "path": path.as_posix(), "pass_threshold": value.get("pass_threshold"), "top_level_keys": sorted(value)})
    return result


class CheckerVisitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.functions: list[dict[str, Any]] = []
        self.file_accesses: list[dict[str, Any]] = []
        self.reward_writes: list[dict[str, Any]] = []
        self.scorer_registry: list[dict[str, Any]] = []
        self.constant_returns: list[dict[str, Any]] = []
        self.risky_calls: list[dict[str, Any]] = []

    @staticmethod
    def name(node: ast.AST) -> str:
        if isinstance(node, ast.Name): return node.id
        if isinstance(node, ast.Attribute): return CheckerVisitor.name(node.value) + "." + node.attr
        return ""

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self.functions.append({"name": node.name, "line": node.lineno, "args": [a.arg for a in node.args.args]})
        for child in ast.walk(node):
            if isinstance(child, ast.Return) and isinstance(child.value, ast.Constant) and isinstance(child.value.value, (int, float)):
                self.constant_returns.append({"function": node.name, "line": child.lineno, "value": child.value.value})
        self.generic_visit(node)

    def visit_Assign(self, node: ast.Assign) -> None:
        for target in node.targets:
            if isinstance(target, ast.Name) and "SCORER" in target.id.upper() and isinstance(node.value, ast.Dict):
                for key, val in zip(node.value.keys, node.value.values):
                    self.scorer_registry.append({"registry": target.id, "key": ast.literal_eval(key) if isinstance(key, ast.Constant) else ast.unparse(key), "callable": self.name(val) or ast.unparse(val), "line": node.lineno})
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> None:
        called = self.name(node.func)
        text_args = [arg.value for arg in node.args if isinstance(arg, ast.Constant) and isinstance(arg.value, str)]
        if called in {"open", "Path.open", "json.load", "json.loads", "pandas.read_csv", "pd.read_csv", "numpy.load", "np.load"} or called.endswith("read_text"):
            self.file_accesses.append({"call": called, "line": node.lineno, "literal_args": text_args})
        if any("reward" in text.lower() for text in text_args):
            self.reward_writes.append({"call": called, "line": node.lineno, "literal_args": text_args})
        if called in {"eval", "exec", "pickle.load", "pickle.loads", "yaml.load", "subprocess.run", "subprocess.Popen", "os.system"}:
            self.risky_calls.append({"call": called, "line": node.lineno, "literal_args": text_args})
        self.generic_visit(node)


def checker_facts(path: Path | None, grading: dict[str, Any]) -> dict[str, Any]:
    if path is None:
        return {"status": "MISSING", "limitations": []}
    source = path.read_text(encoding="utf-8", errors="replace")
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        return {"status": "SYNTAX_ERROR", "path": path.as_posix(), "line": exc.lineno, "message": exc.msg, "limitations": ["No deeper AST facts collected."]}
    visitor = CheckerVisitor(); visitor.visit(tree)
    registered = {str(item["key"]): item for item in visitor.scorer_registry}
    chains = []
    for output in grading.get("outputs", []):
        name = str(output.get("file") or "").split("/")[-1]
        steps = [s for s in grading.get("steps", []) if str(s.get("output_file") or "").split("/")[-1] == name]
        step_facts = [{
            "id": s.get("id"), "kind": s.get("kind"), "weight": s.get("weight"),
            "registered_scorer_candidate": str(s.get("id")) in registered,
            "registered_callable": registered.get(str(s.get("id")), {}).get("callable"),
        } for s in steps]
        chains.append({
            "output_file": name, "declared_purpose": output.get("purpose"),
            "checker_literal_reference": name in source if name else False,
            "checker_uses_output_file_key_candidate": "output_file" in source,
            "grading_steps": step_facts,
            "all_step_ids_have_registered_scorer_candidate": bool(step_facts) and all(x["registered_scorer_candidate"] for x in step_facts),
            "final_reward_write_candidate_present": bool(visitor.reward_writes) or "reward.txt" in source,
            "candidate_only": True,
        })
    return {
        "status": "PARSED", "path": path.as_posix(), "functions": visitor.functions,
        "file_accesses": visitor.file_accesses, "reward_writes": visitor.reward_writes,
        "scorer_registry": visitor.scorer_registry, "constant_returns": visitor.constant_returns,
        "risky_calls": visitor.risky_calls, "scoring_chain_candidates": chains,
        "limitations": ["AST facts do not prove scientific coverage, reachability, safety, or correctness; Agent adjudication is required."],
    }


def probe_url(url: str, timeout: float) -> dict[str, Any]:
    host = urllib.parse.urlparse(url).hostname
    if not host:
        return {"url": url, "status": "BLOCKED", "error": "URL has no hostname"}
    try:
        addresses = {item[4][0] for item in socket.getaddrinfo(host, None)}
        if any(
            (address := ipaddress.ip_address(raw)).is_private
            or address.is_loopback or address.is_link_local
            or address.is_reserved or address.is_unspecified
            for raw in addresses
        ):
            return {"url": url, "status": "BLOCKED", "error": "hostname resolves to a non-public address"}
    except Exception as exc:
        return {"url": url, "status": "PROBE_ERROR", "error": f"DNS resolution failed: {type(exc).__name__}: {exc}"}
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "materials-review-evidence/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return {"url": url, "status": "REACHABLE", "http_status": response.status, "content_type": response.headers.get("Content-Type"), "content_length": response.headers.get("Content-Length"), "limitation": "Reachability does not prove identity or sufficiency."}
    except urllib.error.HTTPError as exc:
        return {
            "url": url,
            "status": (
                "CONFIRMED_MISSING"
                if exc.code in {404, 410}
                else "INCONCLUSIVE_HTTP_ERROR"
            ),
            "http_status": exc.code,
        }
    except Exception as exc:
        return {"url": url, "status": "PROBE_ERROR", "error": f"{type(exc).__name__}: {exc}"}


def collect(root: Path, *, probe_urls: bool = False, timeout: float = 10.0) -> dict[str, Any]:
    root = root.expanduser().resolve()
    if not root.is_dir(): raise ValueError("package root must be a directory")
    files, limitations = inventory(root)
    instruction = locate(root, ("instruction.md", "task.md", "README.md"))
    resources_path = locate(root, ("resources.json",))
    grading_path = locate(root, ("tests/grading_spec.json", "grading_spec.json"))
    checker_path = locate(root, ("tests/checker.py", "checker.py"))
    instruction_data = instruction_contract(instruction)
    resources_data = resources_contract(resources_path)
    grading_data = grading_contract(grading_path)
    checker_data = checker_facts(checker_path, grading_data)
    url_candidates = [
        {
            "url": url,
            "path": instruction_data.get("path"),
            "locator": f"line {item['line']}",
        }
        for item in instruction_data.get("resource_candidates", [])
        for url in item.get("urls", [])
    ] + [
        {
            "url": item["url"],
            "path": resources_data.get("path"),
            "locator": item["locator"],
        }
        for item in resources_data.get("url_candidates", [])
    ]
    urls = sorted({item["url"] for item in url_candidates})
    url_probes = []
    if probe_urls:
        for url in urls:
            observation = probe_url(url, timeout)
            observation["declared_at"] = [
                {
                    "path": item["path"],
                    "locator": item["locator"],
                }
                for item in url_candidates
                if item["url"] == url
            ]
            url_probes.append(observation)
    return {
        "schema_version": SCHEMA, "package_root": str(root),
        "authority": "MECHANICAL_EVIDENCE_ONLY", "may_decide_findings_or_verdict": False,
        "inventory": files, "package_structure": package_structure(root),
        "instruction_contract_candidates": instruction_data,
        "resources_contract_candidates": resources_data,
        "cross_step_parameter_candidates": {
            "analysis_window": analysis_window_candidates(root),
            "simulation_parameter": simulation_parameter_candidates(root),
        },
        "gold_provenance_risk_candidates": gold_provenance_risk_candidates(root),
        "grading_contract_facts": grading_data, "checker_ast_facts": checker_data,
        "resource_candidates": instruction_data.get("resource_candidates", []),
        "url_candidates": url_candidates,
        "url_probes": url_probes,
        "limitations": limitations + resources_data.get("limitations", []),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("package", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--probe-urls", action="store_true")
    parser.add_argument("--timeout", type=float, default=10.0)
    args = parser.parse_args()
    result = collect(args.package, probe_urls=args.probe_urls, timeout=args.timeout)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "inventory": len(result["inventory"]), "authority": result["authority"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
