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
    return {}


# === block: score_0 (check id='s_b') ===
def score_0(artifact, step, ctx):
    T_ref = 10
    rows = artifact
    B0 = None
    for row in rows:
        if int(row['T']) == T_ref:
            B0 = float(row['B'])
            break
    if B0 is None:
        return 0.0
    points = []
    for row in rows:
        T_val = float(row['T'])
        B_val = float(row['B'])
        if B_val > 0:
            points.append({'T': T_val, 'lnr': math.log(B_val / B0)})
        else:
            return 0.0
    n = len(points)
    if n < 2:
        return 0.0
    sum_x = sum(p['T'] for p in points)
    sum_y = sum(p['lnr'] for p in points)
    sum_xy = sum(p['T'] * p['lnr'] for p in points)
    sum_x2 = sum(p['T']**2 for p in points)
    denom = n * sum_x2 - sum_x**2
    if denom == 0:
        return 0.0
    slope = (n * sum_xy - sum_x * sum_y) / denom
    abs_slope = abs(slope)
    target = step.get('reference', 3e-4)
    # The instructed Δn (0.03) differs from the paper’s Fig. 3 (Δn=0.033) whose slopes are used as gold.
    # Use a wider tolerance (1.5e-4) to accommodate this parameter discrepancy.
    tol = 1.5e-4
    return 1.0 if abs(abs_slope - target) <= tol else 0.0


# === block: score_1 (check id='s_tau') ===
def score_1(artifact, step, ctx):
    T_ref = 10
    rows = artifact
    B0 = None
    tau0 = None
    for row in rows:
        if int(row['T']) == T_ref:
            tau0 = float(row['tau'])
            break
    if tau0 is None:
        return 0.0
    points = []
    for row in rows:
        T_val = float(row['T'])
        tau_val = float(row['tau'])
        if tau_val > 0:
            points.append({'T': T_val, 'lnr': math.log(tau_val / tau0)})
        else:
            return 0.0
    n = len(points)
    if n < 2:
        return 0.0
    sum_x = sum(p['T'] for p in points)
    sum_y = sum(p['lnr'] for p in points)
    sum_xy = sum(p['T'] * p['lnr'] for p in points)
    sum_x2 = sum(p['T']**2 for p in points)
    denom = n * sum_x2 - sum_x**2
    if denom == 0:
        return 0.0
    slope = (n * sum_xy - sum_x * sum_y) / denom
    abs_slope = abs(slope)
    target = step.get('reference', 7e-4)
    tol = step.get('tolerance', 1e-4)
    return 1.0 if abs(abs_slope - target) <= tol else 0.0


_SCORERS = {
    's_b': score_0,
    's_tau': score_1,
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
