import os
import json
import csv


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
    return {}


# === block: score_0 (check id='diamond_accuracy') ===
def score_0(artifact, step, ctx):
    d = artifact.get('bulk_diamond', {})
    gold_a0 = step.get('params', {}).get('gold_a0', 3.572)
    tol_a0 = step.get('params', {}).get('tolerance_a0', 0.01)
    gold_B0 = step.get('params', {}).get('gold_B0', 434.6)
    tol_B0 = step.get('params', {}).get('tolerance_B0', 10.0)
    gold_k = step.get('params', {}).get('gold_k_direct', 465.7)
    tol_k = step.get('params', {}).get('tolerance_k_direct', 10.0)
    score_a0 = 1.0 if isinstance(d.get('a0'), (int, float)) and abs(d['a0'] - gold_a0) <= tol_a0 else 0.0
    score_B0 = 1.0 if isinstance(d.get('B0'), (int, float)) and abs(d['B0'] - gold_B0) <= tol_B0 else 0.0
    score_k = 1.0 if isinstance(d.get('k_direct'), (int, float)) and abs(d['k_direct'] - gold_k) <= tol_k else 0.0
    return (score_a0 + score_B0 + score_k) / 3.0


# === block: score_1 (check id='graphene_accuracy') ===
def score_1(artifact, step, ctx):
    d = artifact.get('graphene', {})
    gold_a0 = step.get('params', {}).get('gold_a0', 2.468)
    tol_a0 = step.get('params', {}).get('tolerance_a0', 0.01)
    gold_k = step.get('params', {}).get('gold_k_direct', 719.1)
    tol_k = step.get('params', {}).get('tolerance_k_direct', 10.0)
    score_a0 = 1.0 if isinstance(d.get('a0'), (int, float)) and abs(d['a0'] - gold_a0) <= tol_a0 else 0.0
    score_k = 1.0 if isinstance(d.get('k_direct'), (int, float)) and abs(d['k_direct'] - gold_k) <= tol_k else 0.0
    return (score_a0 + score_k) / 2.0


# === block: score_2 (check id='trends_ordering') ===
def score_2(artifact, step, ctx):
    conditions = step.get('params', {}).get('conditions', [])
    if not conditions:
        return 0.0
    field = 'k_direct'
    count = 0
    for cond in conditions:
        left_key = cond.get('left')
        right_key = cond.get('right')
        op = cond.get('op')
        left_val = artifact.get(left_key, {}).get(field)
        right_val = artifact.get(right_key, {}).get(field)
        if left_val is None or right_val is None:
            continue
        if op == '>' and left_val > right_val:
            count += 1
        elif op == '<' and left_val < right_val:
            count += 1
        elif op == '>=' and left_val >= right_val:
            count += 1
        elif op == '<=' and left_val <= right_val:
            count += 1
        elif op == '==' and left_val == right_val:
            count += 1
    return count / len(conditions)


# === block: score_3 (check id='ratio_bounds') ===
def score_3(artifact, step, ctx):
    systems = step.get('params', {}).get('systems', [])
    field = step.get('params', {}).get('field', 'ratio_k')
    min_val = step.get('params', {}).get('min', 0.9)
    max_val = step.get('params', {}).get('max', 1.1)
    if not systems:
        return 0.0
    count = 0
    for sys in systems:
        val = artifact.get(sys, {}).get(field)
        if isinstance(val, (int, float)) and min_val <= val <= max_val:
            count += 1
    return count / len(systems)


_SCORERS = {
    'diamond_accuracy': score_0,
    'graphene_accuracy': score_1,
    'trends_ordering': score_2,
    'ratio_bounds': score_3,
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
