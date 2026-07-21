import os
import json
import csv

# === author imports / helpers ===
import math, csv, os, json

def load_csv(path):
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

def get_gold_value(gold_table, x_M, field):
    for entry in gold_table:
        if abs(entry['x_M'] - x_M) < 1e-6:
            return entry[field]
    return None

def compute_gold_deltas(gold_table, T):
    # gold_table entries have gamma, u_s, s_s
    x0 = gold_table[0]['x_M']
    u0 = gold_table[0]['u_s']
    s0 = gold_table[0]['s_s']
    x1 = gold_table[-1]['x_M']
    u1 = gold_table[-1]['u_s']
    s1 = gold_table[-1]['s_s']
    for entry in gold_table:
        x = entry['x_M']
        ideal_u = (1 - x) * u0 + x * u1
        ideal_s = (1 - x) * s0 + x * s1
        entry['Delta_u_s'] = entry['u_s'] - ideal_u
        entry['Delta_s_s'] = entry['s_s'] - ideal_s
    return gold_table


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
    gold_rows = spec.get('gold_rows', [])
    T = 300.0
    gold_table = []
    for row in gold_rows:
        x, gamma_mNm, u_s = row
        gamma_kJ = gamma_mNm * 1e-6
        s_s = (u_s - gamma_kJ) / T
        gold_table.append({
            'x_M': x,
            'gamma': gamma_mNm,
            'u_s': u_s,
            's_s': s_s
        })
    gold_table = compute_gold_deltas(gold_table, T)
    return {'gold_table': gold_table, 'T': T}


# === block: score_0 (check id='shape_check') ===
def score_0(artifact, step, ctx):
    required = set(step['params']['required_compositions'])
    outermost_x_M_col = step['params'].get('outermost_x_M_col', 'outermost_x_M')
    outermost_x_M_min = step['params'].get('outermost_x_M_min', 0.8)
    actual_compositions = set()
    mixture_rows = []
    for row in artifact:
        try:
            x = float(row['x_M'])
            actual_compositions.add(x)
        except:
            continue
        if x > 0:
            mixture_rows.append(row)
    if not required.issubset(actual_compositions):
        return 0.0
    # no methanol-containing rows → vacuously satisfied
    if not mixture_rows:
        return 1.0
    passed = 0
    for row in mixture_rows:
        try:
            val = float(row[outermost_x_M_col])
        except (KeyError, ValueError, TypeError):
            return 0.0   # required column missing or non-numeric
        if val >= outermost_x_M_min:
            passed += 1
    return passed / len(mixture_rows)


# === block: score_1 (check id='internal_consistency') ===
def score_1(artifact, step, ctx):
    tol = step['params']['tolerance']
    T = ctx['T']
    passed = 0
    total = 0
    for row in artifact:
        try:
            u_s = float(row['u_s (kJ/m^2)'])
            gamma_mNm = float(row['gamma (mN/m)'])
            s_s = float(row['s_s (kJ/(m^2*K))'])
        except:
            continue
        expected_s = (u_s - gamma_mNm * 1e-6) / T
        if abs(expected_s) < 1e-12:
            if abs(s_s) < 1e-12:
                passed += 1
        else:
            rel_err = abs(s_s - expected_s) / abs(expected_s)
            if rel_err <= tol:
                passed += 1
        total += 1
    if total == 0:
        return 0.0
    return passed / total


# === block: score_2 (check id='sign_trend') ===
def score_2(artifact, step, ctx):
    threshold = step['params']['x_M_threshold']
    expected_signs = step['params']['required_signs']
    conditions = 0
    passed = 0
    for row in artifact:
        try:
            x = float(row['x_M'])
        except:
            continue
        if x > threshold:
            continue
        delta_u = float(row['Delta_u_s (kJ/m^2)'])
        delta_s = float(row['Delta_s_s (kJ/(m^2*K))'])
        ok = True
        if 'Delta_u_s (kJ/m^2)' in expected_signs and expected_signs['Delta_u_s (kJ/m^2)'] == 'negative':
            conditions += 1
            if delta_u >= -1e-12:
                ok = False
            else:
                passed += 1
        if 'Delta_s_s (kJ/(m^2*K))' in expected_signs and expected_signs['Delta_s_s (kJ/(m^2*K))'] == 'negative':
            conditions += 1
            if delta_s >= -1e-12:
                ok = False
            else:
                passed += 1
    if conditions == 0:
        return 1.0
    return passed / conditions


# === block: score_3 (check id='gamma_accuracy') ===
def score_3(artifact, step, ctx):
    col = step['params']['column']
    tol_abs = step['params']['tolerance']
    gold_table = ctx['gold_table']
    passed = 0
    total = 0
    for row in artifact:
        try:
            x = float(row['x_M'])
            val = float(row[col])
        except:
            continue
        gold = get_gold_value(gold_table, x, 'gamma')
        if gold is None:
            continue
        if abs(val - gold) <= tol_abs:
            passed += 1
        total += 1
    if total == 0:
        return 0.0
    return passed / total


# === block: score_4 (check id='u_s_accuracy') ===
def score_4(artifact, step, ctx):
    col = step['params']['column']
    tol_abs = step['params']['tolerance']
    gold_table = ctx['gold_table']
    passed = 0
    total = 0
    for row in artifact:
        try:
            x = float(row['x_M'])
            val = float(row[col])
        except:
            continue
        gold = get_gold_value(gold_table, x, 'u_s')
        if gold is None:
            continue
        if abs(val - gold) <= tol_abs:
            passed += 1
        total += 1
    if total == 0:
        return 0.0
    return passed / total


# === block: score_5 (check id='s_s_accuracy') ===
def score_5(artifact, step, ctx):
    col = step['params']['column']
    tol_abs = step['params']['tolerance']
    gold_table = ctx['gold_table']
    passed = 0
    total = 0
    for row in artifact:
        try:
            x = float(row['x_M'])
            val = float(row[col])
        except:
            continue
        gold = get_gold_value(gold_table, x, 's_s')
        if gold is None:
            continue
        if abs(val - gold) <= tol_abs:
            passed += 1
        total += 1
    if total == 0:
        return 0.0
    return passed / total


# === block: score_6 (check id='delta_u_s_accuracy') ===
def score_6(artifact, step, ctx):
    col = step['params']['column']
    tol_abs = step['params']['tolerance']
    gold_table = ctx['gold_table']
    passed = 0
    total = 0
    for row in artifact:
        try:
            x = float(row['x_M'])
            val = float(row[col])
        except:
            continue
        gold = get_gold_value(gold_table, x, 'Delta_u_s')
        if gold is None:
            continue
        if abs(val - gold) <= tol_abs:
            passed += 1
        total += 1
    if total == 0:
        return 0.0
    return passed / total


# === block: score_7 (check id='delta_s_s_accuracy') ===
def score_7(artifact, step, ctx):
    col = step['params']['column']
    tol_abs = step['params']['tolerance']
    gold_table = ctx['gold_table']
    passed = 0
    total = 0
    for row in artifact:
        try:
            x = float(row['x_M'])
            val = float(row[col])
        except:
            continue
        gold = get_gold_value(gold_table, x, 'Delta_s_s')
        if gold is None:
            continue
        if abs(val - gold) <= tol_abs:
            passed += 1
        total += 1
    if total == 0:
        return 0.0
    return passed / total


_SCORERS = {
    'shape_check': score_0,
    'internal_consistency': score_1,
    'sign_trend': score_2,
    'gamma_accuracy': score_3,
    'u_s_accuracy': score_4,
    's_s_accuracy': score_5,
    'delta_u_s_accuracy': score_6,
    'delta_s_s_accuracy': score_7,
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
