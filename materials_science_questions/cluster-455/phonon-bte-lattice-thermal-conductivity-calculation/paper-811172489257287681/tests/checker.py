import os
import json
import csv

# === author imports / helpers ===
import csv
import math


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
    ctx = {}
    for step in spec.get('steps', []):
        oid = step['id']
        if 'gold_table' in step:
            ctx[oid] = {'gold_table': step['gold_table'], 'tolerance_relative': step.get('tolerance_relative', 0.2), 'metric_column': step.get('metric_column', None)}
        if 'expected_lines' in step:
            ctx[oid] = {'expected_lines': step['expected_lines']}
    return ctx


# === block: score_0 (check id='step_02') ===
def score_0(artifact, step, ctx):
    # artifact is list of dicts from CSV
    step_id = step['id']
    gold_info = ctx.get(step_id, {})
    gold_table = gold_info.get('gold_table', [])
    tol = gold_info.get('tolerance_relative', 0.2)
    gold_map = {}
    for row in gold_table:
        gold_map[row['Material']] = row['kappa_l_WmK']
    rows_found = 0
    total_score = 0.0
    for row in artifact:
        mat = row.get('Material')
        if mat not in gold_map:
            continue
        gold_val = gold_map[mat]
        try:
            agent_val = float(row['kappa_l_WmK'])
        except (ValueError, TypeError):
            continue
        rel_err = abs(agent_val - gold_val) / max(1e-12, abs(gold_val))
        score = 1.0 if rel_err <= tol else max(0.0, 1.0 - (rel_err - tol) / (2 * tol))
        total_score += score
        rows_found += 1
    if rows_found == 0:
        return 0.0
    return total_score / rows_found


# === block: score_1 (check id='step_03') ===
def score_1(artifact, step, ctx):
    # artifact is list of dicts; compare Optimal_ZT to gold thresholds
    step_id = step['id']
    gold_info = ctx.get(step_id, {})
    gold_table = gold_info.get('gold_table', [])
    metric_col = gold_info.get('metric_column', 'Optimal_ZT')
    tol = gold_info.get('tolerance_relative', 0.2)
    gold_map = {}
    for row in gold_table:
        key = (row['Material'], row['DopingType'], int(row['Temperature_K']))
        gold_map[key] = row[metric_col]
    if not gold_map:
        return 0.0
    rows_scored = 0
    total_score = 0.0
    for row in artifact:
        try:
            mat = row['Material']
            dop = row['DopingType']
            temp = int(row['Temperature_K'])
        except (KeyError, ValueError):
            continue
        key = (mat, dop, temp)
        if key not in gold_map:
            continue
        gold_val = gold_map[key]
        try:
            agent_val = float(row[metric_col])
        except (ValueError, TypeError):
            continue
        if agent_val >= gold_val:
            score = 1.0
        else:
            deficit = gold_val - agent_val
            max_deficit = tol * gold_val
            score = max(0.0, 1.0 - deficit / max_deficit)
        total_score += score
        rows_scored += 1
    if rows_scored == 0:
        return 0.0
    return total_score / rows_scored


# === block: score_2 (check id='step_04') ===
def score_2(artifact, step, ctx):
    # artifact is a string (the whole text file)
    step_id = step['id']
    expected = ctx.get(step_id, {}).get('expected_lines', [])
    text = artifact.strip()
    lines = [l.strip() for l in text.splitlines()]
    if len(lines) != len(expected):
        return 0.0
    score = 0.0
    for i, exp in enumerate(expected):
        if lines[i] == exp:
            score += 1.0
    return score / len(expected)


_SCORERS = {
    'step_02': score_0,
    'step_03': score_1,
    'step_04': score_2,
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
