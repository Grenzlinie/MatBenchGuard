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
    try:
        step = spec['steps'][0]
        gold = step.get('params', {}).get('gold', {})
        tols = step.get('params', {}).get('tols', {})
        return {'gold': gold, 'tols': tols}
    except Exception:
        return {'gold': {}, 'tols': {}}


# === block: score_0 (check id='water_dynamics') ===
def score_0(artifact, step, ctx):
    gold = ctx['gold']
    tols = ctx['tols']
    score = 0.0
    bulk_row = None
    cylinder_row = None
    for row in artifact:
        m = row.get('model', '').strip().lower()
        if m == 'bulk':
            bulk_row = row
        elif m == 'cylinder':
            cylinder_row = row
    if bulk_row is None or cylinder_row is None:
        return 0.0
    def val(key, row):
        try:
            return float(row[key])
        except Exception:
            return None
    vals_ok = 0
    for model, row in [('bulk', bulk_row), ('cylinder', cylinder_row)]:
        for prop in ['D', 'tau1_inv', 'tau2_inv', 'mu_z']:
            expected = gold.get(f'{model}_{prop}')
            tolerance = tols.get(f'{prop}_tol')
            actual = val(prop, row)
            if actual is not None and expected is not None and tolerance is not None and abs(actual - expected) <= tolerance:
                vals_ok += 1
    score += 0.1 * vals_ok
    trends_ok = 0
    d_bulk = val('D', bulk_row)
    d_cyl = val('D', cylinder_row)
    if d_bulk is not None and d_cyl is not None and d_bulk > d_cyl:
        trends_ok += 1
    tau1_bulk = val('tau1_inv', bulk_row)
    tau1_cyl = val('tau1_inv', cylinder_row)
    if tau1_bulk is not None and tau1_cyl is not None and tau1_bulk > tau1_cyl:
        trends_ok += 1
    tau2_bulk = val('tau2_inv', bulk_row)
    tau2_cyl = val('tau2_inv', cylinder_row)
    if tau2_bulk is not None and tau2_cyl is not None and tau2_bulk > tau2_cyl:
        trends_ok += 1
    score += (0.2 / 3) * trends_ok
    return min(score, 1.0)


_SCORERS = {
    'water_dynamics': score_0,
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
