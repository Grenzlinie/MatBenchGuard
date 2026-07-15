import os
import json
import csv

# === author imports / helpers ===
import csv, os
import numpy as np

def recompute_exponent_and_r2(data_path, T0):
    """Load data.csv, filter T>T0, perform log-log linear regression.
    Returns (exponent, r_squared) or (None, None) if insufficient data."""
    if not os.path.exists(data_path):
        return None, None
    with open(data_path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    if not rows:
        return None, None
    # validate columns
    required = {'condition','temperature','ISD_min','delta'}
    if not required.issubset(rows[0].keys()):
        return None, None
    # filter T > T0
    x_log, y_log = [], []
    for r in rows:
        if not r['temperature'] or not r['ISD_min'] or not r['delta']:
            continue
        T = float(r['temperature'])
        isd = float(r['ISD_min'])
        d = float(r['delta'])
        if T > T0 and isd > 0 and d > 0:
            x_log.append(np.log(isd))
            y_log.append(np.log(d))
    if len(x_log) < 2:
        return None, None
    coeffs = np.polyfit(x_log, y_log, 1)
    exponent = float(coeffs[0])
    y_pred = np.polyval(coeffs, x_log)
    y_arr = np.array(y_log)
    ss_res = np.sum((y_arr - y_pred) ** 2)
    ss_tot = np.sum((y_arr - np.mean(y_arr)) ** 2)
    r_squared = float(1 - ss_res / ss_tot) if ss_tot > 0 else 0.0
    return exponent, r_squared


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
    return {
        'T0': 0.27,
        'ref_exponent': 2.02,
        'exponent_tolerance': 0.1,
        'consistency_tolerance': 0.02,
        'r_squared_min': 0.9
    }


# === block: score_0 (check id='step_03_data_collection') ===
def score_0(artifact, step, ctx):
    if artifact is None or not isinstance(artifact, list):
        return 0.0
    # shape checks
    if len(artifact) < 10:
        return 0.0
    conditions = set()
    for row in artifact:
        if all(k in row for k in ('condition','temperature','ISD_min','delta')):
            c = row.get('condition','').strip()
            if c:
                conditions.add(c)
    if len(conditions) < 2:
        return 0.0
    # recompute exponent
    data_path = os.path.join('/app/outputs', 'data.csv')
    exp, _ = recompute_exponent_and_r2(data_path, ctx['T0'])
    if exp is None:
        return 0.0
    # compare to reference
    ref = ctx['ref_exponent']
    tol = ctx['exponent_tolerance']
    if abs(exp - ref) <= tol:
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='step_04_fit_powerlaw') ===
def score_1(artifact, step, ctx):
    if artifact is None or not isinstance(artifact, dict):
        return 0.0
    exponent_b = artifact.get('exponent_b')
    r_sq = artifact.get('R_squared')
    if exponent_b is None or r_sq is None:
        return 0.0
    if not isinstance(exponent_b, (int, float)) or not isinstance(r_sq, (int, float)):
        return 0.0
    # recompute exponent from data.csv
    data_path = os.path.join('/app/outputs', 'data.csv')
    exp_recomputed, _ = recompute_exponent_and_r2(data_path, ctx['T0'])
    if exp_recomputed is None:
        return 0.0
    # consistency: exponent_b close to recomputed and R_squared plausible
    if abs(exponent_b - exp_recomputed) <= ctx['consistency_tolerance'] and r_sq >= ctx['r_squared_min']:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'step_03_data_collection': score_0,
    'step_04_fit_powerlaw': score_1,
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
