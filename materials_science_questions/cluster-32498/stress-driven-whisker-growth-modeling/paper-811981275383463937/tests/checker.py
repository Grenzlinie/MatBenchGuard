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
    steps = spec.get('steps', [])
    table1_gold = []
    hstar_ratios = {}
    hstar_tol = 0.01
    table2_gold = []
    tau_rel_tol = 0.01
    tau_log_tol = 0.5
    tau_thresh = 3600
    table2_rel_tol = 0.01
    for step in steps:
        if step['id'] == 'tau_match':
            table1_gold = step['params']['gold_data']
            tau_rel_tol = step['params']['rel_tolerance']
            tau_log_tol = step['params']['log10_tolerance']
            tau_thresh = step['params']['tau_threshold_3600']
        if step['id'] == 'h_star_ratio':
            hstar_ratios = step['params']['expected_ratios']
            hstar_tol = step['params']['tolerance']
        if step['id'] == 'table2_match':
            table2_gold = step['params']['gold_data']
            table2_rel_tol = step['params']['rel_tolerance']
    return {
        'tau_gold': table1_gold,
        'hstar_ratios': hstar_ratios,
        'hstar_tol': hstar_tol,
        'tau_rel_tol': tau_rel_tol,
        'tau_log_tol': tau_log_tol,
        'tau_thresh': tau_thresh,
        'table2_gold': table2_gold,
        'table2_rel_tol': table2_rel_tol
    }


# === block: score_0 (check id='table1_shape') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    req_cols = ['Orientation', 'R', 'tau', 'c_star', 'h_star', 'omega']
    if not all(c in rows[0] for c in req_cols):
        return 0.0
    orients = set()
    for r in rows:
        try:
            o = float(r.get('Orientation', -1))
            orients.add(round(o, 2))
        except:
            continue
    if 0.0 not in orients and 0 not in orients:
        return 0.0
    if 35.25 not in orients:
        return 0.0
    if len(rows) != 6:
        return 0.0
    return 1.0


# === block: score_1 (check id='h_star_ratio') ===
def score_1(artifact, step, ctx):
    expected = ctx.get('hstar_ratios', {})
    tol = ctx.get('hstar_tol', 0.01)
    rows = artifact
    if not rows:
        return 0.0
    passed = 0
    for row in rows:
        try:
            orient = float(row['Orientation'])
            R = float(row['R'])
            h = float(row['h_star'])
        except:
            continue
        ratio = h / R if R != 0 else 0
        orient_key = str(round(orient, 2))
        exp_ratio = expected.get(orient_key)
        if exp_ratio is None:
            continue
        if abs(ratio - exp_ratio) <= tol:
            passed += 1
    return passed / len(rows) if rows else 0.0


# === block: score_2 (check id='tau_match') ===
def score_2(artifact, step, ctx):
    import math
    gold = ctx.get('tau_gold', [])
    rel_tol = ctx.get('tau_rel_tol', 0.01)
    log_tol = ctx.get('tau_log_tol', 0.5)
    thresh = ctx.get('tau_thresh', 3600)
    rows = artifact
    if not rows or not gold:
        return 0.0
    passed = 0
    for row in rows:
        try:
            orient = float(row['Orientation'])
            R_agent = float(row['R'])
            tau_agent = float(row['tau'])
        except:
            continue
        gold_row = None
        for g in gold:
            if abs(float(g['Orientation']) - orient) < 0.1 and abs(float(g['R']) - R_agent) < 1e-12:
                gold_row = g
                break
        if gold_row is None:
            continue
        gold_tau = float(gold_row['tau'])
        if gold_tau <= thresh:
            if abs((tau_agent - gold_tau) / gold_tau) <= rel_tol:
                passed += 1
        else:
            if abs(math.log10(tau_agent) - math.log10(gold_tau)) <= log_tol:
                passed += 1
    return passed / len(rows) if rows else 0.0


# === block: score_3 (check id='table2_match') ===
def score_3(artifact, step, ctx):
    gold = ctx.get('table2_gold', [])
    rel_tol = ctx.get('table2_rel_tol', 0.01)
    rows = artifact
    if not rows or not gold:
        return 0.0
    passed = 0
    for row in rows:
        try:
            R_agent = float(row['R'])
            se = float(row['sigma_e'])
            ss = float(row['sigma_s'])
        except:
            continue
        gold_row = None
        for g in gold:
            if abs(float(g['R']) - R_agent) < 1e-12:
                gold_row = g
                break
        if gold_row is None:
            continue
        gold_se = float(gold_row['sigma_e'])
        gold_ss = float(gold_row['sigma_s'])
        if abs((se - gold_se) / gold_se) <= rel_tol and abs((ss - gold_ss) / gold_ss) <= rel_tol:
            passed += 1
    return passed / len(rows) if rows else 0.0


_SCORERS = {
    'table1_shape': score_0,
    'h_star_ratio': score_1,
    'tau_match': score_2,
    'table2_match': score_3,
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
