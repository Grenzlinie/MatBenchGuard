import os
import json
import csv

# === author imports / helpers ===
import json, math


import os as _ff_os
import json as _ff_json


def _ff_validate_output_contract():
    """Return a list of shape violations against grading_spec['output_contract']."""
    spec_path = "/tests/grading_spec.json"
    if not _ff_os.path.exists(spec_path):
        return []
    with open(spec_path) as _f:
        _spec = _ff_json.load(_f)
    contract = _spec.get("output_contract", {}) or {}
    outputs = contract.get("outputs", []) or []
    out_dir = "/app/outputs"
    violations = []
    for out in outputs:
        base = str(out.get("file", "")).split("/")[-1]
        if not base:
            continue
        path = _ff_os.path.join(out_dir, base)
        if not _ff_os.path.isfile(path):
            violations.append("missing output_contract file: " + base)
            continue
        fmt = out.get("format", "")
        schema = out.get("schema", {}) or {}
        if fmt == "json":
            try:
                data = _ff_json.load(open(path))
            except Exception as exc:  # noqa: BLE001
                violations.append(base + ": invalid JSON (" + str(exc) + ")")
                continue
            required = schema.get("required", {})
            fields = required.keys() if isinstance(required, dict) else (required or [])
            if isinstance(data, dict):
                for field in fields:
                    if field not in data:
                        violations.append(base + ": missing JSON field '" + str(field) + "'")
        elif fmt in ("csv", "tsv"):
            import csv as _ff_csv
            delim = "\t" if fmt == "tsv" else ","
            try:
                with open(path, newline="") as _f:
                    cols = set((_ff_csv.reader(_f, delimiter=delim).__next__() or []))
            except StopIteration:
                cols = set()
            except Exception as exc:  # noqa: BLE001
                violations.append(base + ": cannot read table (" + str(exc) + ")")
                continue
            required_cols = schema.get("required_columns", []) or []
            for col in required_cols:
                name = col.get("name") if isinstance(col, dict) else col
                if name and name not in cols:
                    violations.append(base + ": missing table column '" + str(name) + "'")
    return violations


def _ff_contract_gate():
    """Zero the reward and exit if the submission violates the output_contract shape."""
    violations = _ff_validate_output_contract()
    if not violations:
        return
    _ff_os.makedirs("/logs/verifier", exist_ok=True)
    with open("/logs/verifier/reward.txt", "w") as _f:
        _f.write("0.0")
    with open("/logs/verifier/breakdown.json", "w") as _f:
        _ff_json.dump({"output_contract_violations": violations}, _f, indent=2)
    raise SystemExit(0)


def load_artifact(path):
    if not path or not os.path.exists(path):
        return None
    if path.endswith(".json"):
        try:
            with open(path) as f:
                return json.load(f)
        except Exception:  # noqa: BLE001
            return None
    if path.endswith(".csv") or path.endswith(".tsv"):
        delim = "\t" if path.endswith(".tsv") else ","
        with open(path, newline="") as f:
            return list(csv.DictReader(f, delimiter=delim))
    with open(path) as f:
        return f.read()


def prepare(outputs_dir, spec):
    spec = json.load(open('/tests/grading_spec.json'))
    step = spec['steps'][0]
    return {"gold": step['gold'], "tolerances": step['tolerances']}


# === block: score_0 (check id='step_11') ===
def score_0(artifact, step, ctx):
    def count_leaves(node):
        if isinstance(node, dict):
            return sum(count_leaves(v) for v in node.values())
        elif isinstance(node, list):
            return sum(count_leaves(item) for item in node)
        else:
            return 1

    def get_tolerance(top_key, path_parts):
        tol_conf = ctx['tolerances'].get(top_key, 0.1)
        if isinstance(tol_conf, dict):
            for p in path_parts:
                if isinstance(p, str) and p in tol_conf:
                    return tol_conf[p]
            return 0.1
        else:
            return tol_conf

    def compare_trees(gold_node, art_node, path_parts, top_key):
        scores = []
        totals = []
        if isinstance(gold_node, dict):
            for k, v in gold_node.items():
                art_sub = art_node.get(k) if isinstance(art_node, dict) else None
                if art_sub is None:
                    scores.append(0)
                    totals.append(count_leaves(v))
                else:
                    sub_score, sub_total = compare_trees(v, art_sub, path_parts + [k], top_key)
                    scores.append(sub_score)
                    totals.append(sub_total)
        elif isinstance(gold_node, list):
            if not isinstance(art_node, list):
                scores.append(0)
                totals.append(count_leaves(gold_node))
            else:
                for idx, g_val in enumerate(gold_node):
                    art_val = art_node[idx] if idx < len(art_node) else None
                    if art_val is None:
                        scores.append(0)
                        totals.append(1)
                    else:
                        tol = get_tolerance(top_key, path_parts)
                        if isinstance(g_val, (int, float)) and isinstance(art_val, (int, float)):
                            if abs(art_val - g_val) <= tol:
                                scores.append(1)
                            else:
                                scores.append(0)
                        else:
                            scores.append(0)
                        totals.append(1)
        else:
            art_val = art_node
            if art_val is None:
                scores.append(0)
                totals.append(1)
            else:
                tol = get_tolerance(top_key, path_parts)
                if isinstance(gold_node, (int, float)) and isinstance(art_val, (int, float)):
                    if abs(art_val - gold_node) <= tol:
                        scores.append(1)
                    else:
                        scores.append(0)
                else:
                    scores.append(0)
                totals.append(1)
        return sum(scores), sum(totals)

    gold = ctx['gold']
    total_score = 0
    total_count = 0
    for prop, gold_val in gold.items():
        art_val = artifact.get(prop)
        if art_val is None:
            total_count += count_leaves(gold_val)
        else:
            sc, cnt = compare_trees(gold_val, art_val, [], prop)
            total_score += sc
            total_count += cnt
    if total_count == 0:
        return 0.0
    return total_score / total_count


_SCORERS = {
    'step_11': score_0,
}


def _step_id(step, index):
    sid = str(step.get("id", "")).strip()
    if sid:
        return sid
    output = str(step.get("output_file", "")).split("/")[-1].rsplit(".", 1)[0]
    kind = str(step.get("kind") or step.get("metric") or "score").strip()
    base = "_".join(part for part in (output, kind) if part).strip("_")
    return base or ("check_" + str(index))


def main():
    _ff_contract_gate()
    with open("/tests/grading_spec.json") as f:
        spec = json.load(f)
    outputs_dir = "/app/outputs"
    ctx = prepare(outputs_dir, spec)
    steps = spec.get("steps", spec.get("checks", [])) or []
    breakdown = {}
    total = 0.0
    for index, step in enumerate(steps):
        sid = _step_id(step, index)
        output_file = str(step.get("output_file", "")).split("/")[-1]
        weight = float(step.get("weight", 0.0))
        artifact = load_artifact(os.path.join(outputs_dir, output_file)) if output_file else None
        fn = _SCORERS.get(sid)
        if fn is None:
            score = 0.0
        else:
            try:
                score = float(fn(artifact, step, ctx))
            except Exception as exc:  # noqa: BLE001
                score = 0.0
                breakdown.setdefault("_errors", {})[sid] = repr(exc)
        score = max(0.0, min(1.0, score))
        breakdown[sid or output_file] = {"score": score, "weight": weight}
        total += score * weight
    os.makedirs("/logs/verifier", exist_ok=True)
    with open("/logs/verifier/reward.txt", "w") as f:
        f.write(str(round(total, 6)))
    with open("/logs/verifier/breakdown.json", "w") as f:
        json.dump(breakdown, f, indent=2)


if __name__ == "__main__":
    main()
