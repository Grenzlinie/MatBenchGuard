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
import re
import socket
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

SCHEMA = "materials-mechanical-evidence/1.0"
URL_RE = re.compile(r"https?://[^\s<>)\]}`\"']+")
OUTPUT_RE = re.compile(r"(?:/app/outputs/)?([A-Za-z0-9_.-]+\.(?:json|jsonl|csv|tsv|txt|yaml|yml|cif|xyz|vasp|png|npz|npy|pt|pth|ckpt|onnx))", re.I)
MODEL_RE = re.compile(r"\b(model|weights?|checkpoint|potential|tokenizer|pretrained|ckpt|onnx|\.pt|\.pth)\b", re.I)
DATA_RE = re.compile(r"\b(dataset|data file|input file|structure file|database|annotation|split)\b", re.I)


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
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            limitations.append({"stage": "inventory", "path": path.relative_to(root).as_posix(), "reason": "symlink not followed"})
            continue
        if not path.is_file():
            continue
        role = "other"
        name = path.relative_to(root).as_posix()
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
        return {"url": url, "status": "HTTP_ERROR", "http_status": exc.code}
    except Exception as exc:
        return {"url": url, "status": "PROBE_ERROR", "error": f"{type(exc).__name__}: {exc}"}


def collect(root: Path, *, probe_urls: bool = False, timeout: float = 10.0) -> dict[str, Any]:
    root = root.expanduser().resolve()
    if not root.is_dir(): raise ValueError("package root must be a directory")
    files, limitations = inventory(root)
    instruction = locate(root, ("instruction.md", "task.md", "README.md"))
    grading_path = locate(root, ("tests/grading_spec.json", "grading_spec.json"))
    checker_path = locate(root, ("tests/checker.py", "checker.py"))
    instruction_data = instruction_contract(instruction)
    grading_data = grading_contract(grading_path)
    checker_data = checker_facts(checker_path, grading_data)
    urls = instruction_data.get("urls", [])
    return {
        "schema_version": SCHEMA, "package_root": str(root),
        "authority": "MECHANICAL_EVIDENCE_ONLY", "may_decide_findings_or_verdict": False,
        "inventory": files, "instruction_contract_candidates": instruction_data,
        "grading_contract_facts": grading_data, "checker_ast_facts": checker_data,
        "resource_candidates": instruction_data.get("resource_candidates", []),
        "url_probes": [probe_url(url, timeout) for url in urls] if probe_urls else [],
        "limitations": limitations + ([{"stage": "url_probe", "reason": "URL probing not requested."}] if urls and not probe_urls else []),
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
