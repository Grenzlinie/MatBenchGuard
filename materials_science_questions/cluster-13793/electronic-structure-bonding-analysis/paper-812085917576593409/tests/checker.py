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
    gold_order = None
    gold_table = []
    for step in spec.get('steps', []):
        if step.get('id') == 'ordering':
            gold_order = step.get('gold_order')
        elif step.get('id') == 'griffith':
            gold_table = step.get('gold_table', [])
    return {'gold_order': gold_order, 'gold_table': gold_table}


# === block: score_0 (check id='ordering') ===
def score_0(artifact, step, ctx):
    gold_order = ctx['gold_order']
    if not isinstance(artifact, dict) or 'models' not in artifact:
        return 0.0

    agent_order = artifact['models']
    if not isinstance(agent_order, list) or len(agent_order) != len(gold_order):
        return 0.0

    if set(agent_order) != set(gold_order):
        return 0.0

    # Kendall tau rank correlation distance
    rank = {name: i for i, name in enumerate(gold_order)}
    n = len(gold_order)
    distance = 0
    for i in range(n):
        for j in range(i + 1, n):
            a, b = agent_order[i], agent_order[j]
            if rank[a] > rank[b]:
                distance += 1

    max_distance = n * (n - 1) // 2
    score = 1.0 - distance / max_distance if max_distance > 0 else 1.0
    return max(0.0, min(1.0, score))


# === block: score_1 (check id='griffith') ===
def score_1(artifact, step, ctx):
    gold_table = ctx['gold_table']
    if not gold_table:
        return 1.0

    # build gold lookup
    gold_lookup = {}
    for row in gold_table:
        key = (row['model'], row['region'])
        gold_lookup[key] = float(row['Griffith_work_J_m2'])

    # parse agent CSV rows (artifact is already loaded as list of dicts)
    agent_rows = artifact
    if not isinstance(agent_rows, list) or not agent_rows:
        return 0.0

    agent_values = {}
    tolerance = 0.3
    matched = 0
    for row in agent_rows:
        try:
            model = row.get('model')
            region = row.get('region')
            if model is None or region is None:
                continue
            val = float(row.get('Griffith_work_J_m2'))
        except (ValueError, TypeError):
            continue
        key = (model, region)
        agent_values[key] = val
        if key in gold_lookup and abs(val - gold_lookup[key]) <= tolerance:
            matched += 1

    num_total = len(gold_table)
    score_num = matched / num_total if num_total else 0.0

    # trend check: W(Ni(2)) > W(no-add) > W(Ni(1)) in region-1
    trend_ok = False
    try:
        w_ni2 = agent_values[('Ni(2)', 'region-1')]
        w_no = agent_values[('no-add', 'region-1')]
        w_ni1 = agent_values[('Ni(1)', 'region-1')]
        if w_ni2 > w_no and w_no > w_ni1:
            trend_ok = True
    except KeyError:
        pass

    trend_score = 0.2 if trend_ok else 0.0
    return min(0.8 * score_num + trend_score, 1.0)


_SCORERS = {
    'ordering': score_0,
    'griffith': score_1,
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
