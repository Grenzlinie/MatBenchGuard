import os
import json
import csv

# === author imports / helpers ===
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
    rows = load_artifact(os.path.join(outputs_dir, 'step_3_results.csv'))
    if rows is None:
        return {}
    avgs = {}
    for m in ['quenched', '25ns']:
        frows = [r for r in rows if r.get('model', '').strip() == m]
        if not frows:
            return {}
        d = {}
        for col in ['failure_strain','failure_stress','fracture_energy','number_of_PFCs','strain_first_nanocrack','stress_first_nanocrack']:
            try:
                vals = [float(r[col]) for r in frows]
                d[col + '_mean'] = sum(vals) / len(vals)
            except Exception:
                d[col + '_mean'] = None
        avgs[m] = d
    return {'averages': avgs}


# === block: score_0 (check id='csv_shape') ===
def score_0(artifact, step, ctx):
    req_cols = ['model','direction','failure_strain','failure_stress','fracture_energy','number_of_PFCs','strain_first_nanocrack','stress_first_nanocrack']
    if not isinstance(artifact, list) or len(artifact) != 10:
        return 0.0
    for row in artifact:
        for c in req_cols:
            if c not in row:
                return 0.0
    for r in artifact:
        if r.get('direction','').strip() != 'y':
            return 0.0
        if r.get('model','').strip() not in ('quenched','25ns'):
            return 0.0
    return 1.0


# === block: score_1 (check id='quenched_avg_failure_strain') ===
def score_1(artifact, step, ctx):
    avg = ctx.get('averages',{}).get('quenched',{}).get('failure_strain_mean')
    if avg is None:
        return 0.0
    target = step['target']
    tol = step['tolerance_relative']
    threshold = target * (1 - tol)
    if avg >= threshold:
        return 1.0
    deficit = threshold - avg
    max_deficit = target * tol
    if deficit >= max_deficit:
        return 0.0
    return (max_deficit - deficit) / max_deficit


# === block: score_2 (check id='quenched_avg_failure_stress') ===
def score_2(artifact, step, ctx):
    avg = ctx.get('averages',{}).get('quenched',{}).get('failure_stress_mean')
    if avg is None:
        return 0.0
    target = step['target']
    tol = step['tolerance_relative']
    threshold = target * (1 - tol)
    if avg >= threshold:
        return 1.0
    deficit = threshold - avg
    max_deficit = target * tol
    if deficit >= max_deficit:
        return 0.0
    return (max_deficit - deficit) / max_deficit


# === block: score_3 (check id='quenched_avg_fracture_energy') ===
def score_3(artifact, step, ctx):
    avg = ctx.get('averages',{}).get('quenched',{}).get('fracture_energy_mean')
    if avg is None:
        return 0.0
    target = step['target']
    tol = step['tolerance_relative']
    threshold = target * (1 - tol)
    if avg >= threshold:
        return 1.0
    deficit = threshold - avg
    max_deficit = target * tol
    if deficit >= max_deficit:
        return 0.0
    return 1.0 - deficit / max_deficit


# === block: score_4 (check id='quenched_avg_number_of_PFCs') ===
def score_4(artifact, step, ctx):
    avg = ctx.get('averages',{}).get('quenched',{}).get('number_of_PFCs_mean')
    if avg is None:
        return 0.0
    target = step['target']
    tol = step['tolerance_relative']
    threshold = target * (1 - tol)
    if avg >= threshold:
        return 1.0
    deficit = threshold - avg
    max_deficit = target * tol
    if deficit >= max_deficit:
        return 0.0
    return (max_deficit - deficit) / max_deficit


# === block: score_5 (check id='quenched_avg_strain_first_nanocrack') ===
def score_5(artifact, step, ctx):
    avg = ctx.get('averages',{}).get('quenched',{}).get('strain_first_nanocrack_mean')
    if avg is None:
        return 0.0
    target = step['target']
    rel_tol = step['tolerance_relative']
    rel_err = abs(avg - target) / abs(target)
    if rel_err <= rel_tol:
        return 1.0
    elif rel_err >= 2*rel_tol:
        return 0.0
    else:
        return (2*rel_tol - rel_err) / rel_tol


# === block: score_6 (check id='quenched_avg_stress_first_nanocrack') ===
def score_6(artifact, step, ctx):
    avg = ctx.get('averages',{}).get('quenched',{}).get('stress_first_nanocrack_mean')
    if avg is None:
        return 0.0
    target = step['target']
    rel_tol = step['tolerance_relative']
    rel_err = abs(avg - target) / abs(target)
    if rel_err <= rel_tol:
        return 1.0
    elif rel_err >= 2*rel_tol:
        return 0.0
    else:
        return (2*rel_tol - rel_err) / rel_tol


# === block: score_7 (check id='25ns_avg_failure_strain') ===
def score_7(artifact, step, ctx):
    avg = ctx.get('averages',{}).get('25ns',{}).get('failure_strain_mean')
    if avg is None:
        return 0.0
    target = step['target']
    tol = step['tolerance_relative']
    threshold = target * (1 - tol)
    if avg >= threshold:
        return 1.0
    deficit = threshold - avg
    max_deficit = target * tol
    if deficit >= max_deficit:
        return 0.0
    return (max_deficit - deficit) / max_deficit


# === block: score_8 (check id='25ns_avg_failure_stress') ===
def score_8(artifact, step, ctx):
    avg = ctx.get('averages',{}).get('25ns',{}).get('failure_stress_mean')
    if avg is None:
        return 0.0
    target = step['target']
    tol = step['tolerance_relative']
    threshold = target * (1 - tol)
    if avg >= threshold:
        return 1.0
    deficit = threshold - avg
    max_deficit = target * tol
    if deficit >= max_deficit:
        return 0.0
    return (max_deficit - deficit) / max_deficit


# === block: score_9 (check id='25ns_avg_fracture_energy') ===
def score_9(artifact, step, ctx):
    avg = ctx.get('averages',{}).get('25ns',{}).get('fracture_energy_mean')
    if avg is None:
        return 0.0
    target = step['target']
    tol = step['tolerance_relative']
    threshold = target * (1 - tol)
    if avg >= threshold:
        return 1.0
    deficit = threshold - avg
    max_deficit = target * tol
    if deficit >= max_deficit:
        return 0.0
    return 1.0 - deficit / max_deficit


# === block: score_10 (check id='25ns_avg_number_of_PFCs') ===
def score_10(artifact, step, ctx):
    avg = ctx.get('averages',{}).get('25ns',{}).get('number_of_PFCs_mean')
    if avg is None:
        return 0.0
    target = step['target']
    tol = step['tolerance_relative']
    threshold = target * (1 - tol)
    if avg >= threshold:
        return 1.0
    deficit = threshold - avg
    max_deficit = target * tol
    if deficit >= max_deficit:
        return 0.0
    return (max_deficit - deficit) / max_deficit


# === block: score_11 (check id='25ns_avg_strain_first_nanocrack') ===
def score_11(artifact, step, ctx):
    avg = ctx.get('averages',{}).get('25ns',{}).get('strain_first_nanocrack_mean')
    if avg is None:
        return 0.0
    target = step['target']
    rel_tol = step['tolerance_relative']
    rel_err = abs(avg - target) / abs(target)
    if rel_err <= rel_tol:
        return 1.0
    elif rel_err >= 2*rel_tol:
        return 0.0
    else:
        return (2*rel_tol - rel_err) / rel_tol


# === block: score_12 (check id='25ns_avg_stress_first_nanocrack') ===
def score_12(artifact, step, ctx):
    avg = ctx.get('averages',{}).get('25ns',{}).get('stress_first_nanocrack_mean')
    if avg is None:
        return 0.0
    target = step['target']
    rel_tol = step['tolerance_relative']
    rel_err = abs(avg - target) / abs(target)
    if rel_err <= rel_tol:
        return 1.0
    elif rel_err >= 2*rel_tol:
        return 0.0
    else:
        return (2*rel_tol - rel_err) / rel_tol


# === block: score_13 (check id='trend_energy') ===
def score_13(artifact, step, ctx):
    avg_q = ctx.get('averages',{}).get('quenched',{}).get('fracture_energy_mean')
    avg_25 = ctx.get('averages',{}).get('25ns',{}).get('fracture_energy_mean')
    if avg_q is None or avg_25 is None:
        return 0.0
    return 1.0 if avg_q > avg_25 else 0.0


# === block: score_14 (check id='trend_pfc') ===
def score_14(artifact, step, ctx):
    avg_q = ctx.get('averages',{}).get('quenched',{}).get('number_of_PFCs_mean')
    avg_25 = ctx.get('averages',{}).get('25ns',{}).get('number_of_PFCs_mean')
    if avg_q is None or avg_25 is None:
        return 0.0
    return 1.0 if avg_q > avg_25 else 0.0


_SCORERS = {
    'csv_shape': score_0,
    'quenched_avg_failure_strain': score_1,
    'quenched_avg_failure_stress': score_2,
    'quenched_avg_fracture_energy': score_3,
    'quenched_avg_number_of_PFCs': score_4,
    'quenched_avg_strain_first_nanocrack': score_5,
    'quenched_avg_stress_first_nanocrack': score_6,
    '25ns_avg_failure_strain': score_7,
    '25ns_avg_failure_stress': score_8,
    '25ns_avg_fracture_energy': score_9,
    '25ns_avg_number_of_PFCs': score_10,
    '25ns_avg_strain_first_nanocrack': score_11,
    '25ns_avg_stress_first_nanocrack': score_12,
    'trend_energy': score_13,
    'trend_pfc': score_14,
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
