import os
import json
import csv

# === author imports / helpers ===
import csv, os


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
    def prepare(outputs_dir, spec):
        ctx = {}
        path1 = os.path.join(outputs_dir, 'table1.csv')
        if os.path.exists(path1):
            with open(path1, newline='') as f:
                reader = csv.DictReader(f)
                ctx['table1'] = list(reader)
        else:
            ctx['table1'] = []
        path2 = os.path.join(outputs_dir, 'table2.csv')
        if os.path.exists(path2):
            with open(path2, newline='') as f:
                reader = csv.DictReader(f)
                ctx['table2'] = list(reader)
        else:
            ctx['table2'] = []
        return ctx


# === block: score_0 (check id='table1_values') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0
    gold = step.get('gold', [])
    tol_partial = step.get('tolerance_partial', 0.03)
    tol_n_out = step.get('tolerance_n_out', 0.05)
    cols = ['n_s', 'n_p', 'n_d', 'n_f', 'n_g', 'n_out']
    gold_map = {}
    for g in gold:
        calc = g.get('calculation', '').strip()
        gold_map[calc] = g
    total_checks = 0
    passed = 0
    for row in artifact:
        calc = row.get('calculation', '').strip()
        g = gold_map.get(calc)
        if g is None:
            continue
        for col in cols:
            total_checks += 1
            try:
                val = float(row[col])
            except (ValueError, KeyError):
                continue
            gold_val = float(g[col])
            tol = tol_n_out if col == 'n_out' else tol_partial
            if abs(val - gold_val) <= tol:
                passed += 1
    if total_checks == 0:
        return 0.0
    return passed / total_checks


# === block: score_1 (check id='table1_trends') ===
def score_1(artifact, step, ctx):
    if not artifact:
        return 0.0
    rows = {}
    for row in artifact:
        calc = row.get('calculation', '').strip()
        rows[calc] = row
    if 'APW' not in rows or 'RAPW' not in rows:
        return 0.0
    apw = rows['APW']
    rapw = rows['RAPW']
    checks = 0
    passed = 0
    try:
        if float(rapw['n_s']) > float(apw['n_s']):
            passed += 1
    except:
        pass
    checks += 1
    try:
        if float(rapw['n_p']) > float(apw['n_p']):
            passed += 1
    except:
        pass
    checks += 1
    try:
        if float(rapw['n_d']) < float(apw['n_d']):
            passed += 1
    except:
        pass
    checks += 1
    if checks == 0:
        return 0.0
    return passed / checks


# === block: score_2 (check id='table2_values') ===
def score_2(artifact, step, ctx):
    if not artifact:
        return 0.0
    gold = step.get('gold', [])
    tol_partial = step.get('tolerance_partial', 0.03)
    tol_n_out = step.get('tolerance_n_out', 0.05)
    gold_map = {}
    for g in gold:
        state = g.get('state', '').strip()
        gold_map[state] = float(g['n_state'])
    total_checks = 0
    passed = 0
    for row in artifact:
        state = row.get('state', '').strip()
        if state not in gold_map:
            continue
        total_checks += 1
        try:
            val = float(row['n_state'])
        except (ValueError, KeyError):
            continue
        gold_val = gold_map[state]
        tol = tol_n_out if state == 'n_out' else tol_partial
        if abs(val - gold_val) <= tol:
            passed += 1
    if total_checks == 0:
        return 0.0
    return passed / total_checks


# === block: score_3 (check id='table2_consistency') ===
def score_3(artifact, step, ctx):
    table1 = ctx.get('table1', [])
    if not artifact or not table1:
        return 0.0
    rapw = None
    for row in table1:
        if row.get('calculation', '').strip() == 'RAPW':
            rapw = row
            break
    if rapw is None:
        return 0.0
    t2 = {}
    for row in artifact:
        state = row.get('state', '').strip()
        try:
            t2[state] = float(row['n_state'])
        except:
            pass
    checks = []
    p_sum = t2.get('p3/2', 0) + t2.get('p1/2', 0)
    checks.append(abs(p_sum - float(rapw.get('n_p', 0))) <= 0.02)
    d_sum = t2.get('d5/2', 0) + t2.get('d3/2', 0)
    checks.append(abs(d_sum - float(rapw.get('n_d', 0))) <= 0.02)
    f_sum = t2.get('f7/2', 0) + t2.get('f5/2', 0)
    checks.append(abs(f_sum - float(rapw.get('n_f', 0))) <= 0.02)
    g_sum = t2.get('g9/2', 0) + t2.get('g7/2', 0)
    checks.append(abs(g_sum - float(rapw.get('n_g', 0))) <= 0.02)
    checks.append(abs(t2.get('s1/2', 0) - float(rapw.get('n_s', 0))) <= 0.02)
    checks.append(abs(t2.get('n_out', 0) - float(rapw.get('n_out', 0))) <= 0.02)
    if not checks:
        return 0.0
    return sum(checks) / len(checks)


_SCORERS = {
    'table1_values': score_0,
    'table1_trends': score_1,
    'table2_values': score_2,
    'table2_consistency': score_3,
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
