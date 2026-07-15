import os
import json
import csv

# === author imports / helpers ===
import csv
import numpy as np
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
    return {'gold_ternary': [0.51451255, 0.30433924, 0.61999649], 'pure_methane': 18.0, 'pure_ethane': 20.0}


# === block: score_0 (check id='s02') ===
def score_0(artifact, step, ctx):
    M = 1.0; K_A = 2.0; K_B = 10.0; K_C = 20.0
    Pt = 1.0
    tol = float(step.get("tolerance", 0.02))
    max_err = 0.0
    for row in artifact:
        xA = float(row['xA']); xB = float(row['xB']); xC = float(row['xC'])
        pA = xA*Pt; pB = xB*Pt; pC = xC*Pt
        denom = 1.0 + K_A*pA + K_B*pB + K_C*pC
        true_A = M * (K_A*pA) / denom
        true_B = M * (K_B*pB) / denom
        true_C = M * (K_C*pC) / denom
        pred_A = float(row['predicted_loading_A'])
        pred_B = float(row['predicted_loading_B'])
        pred_C = float(row['predicted_loading_C'])
        err_A = abs(pred_A - true_A) / max(true_A, 1e-6)
        err_B = abs(pred_B - true_B) / max(true_B, 1e-6)
        err_C = abs(pred_C - true_C) / max(true_C, 1e-6)
        row_err = max(err_A, err_B, err_C)
        if row_err > max_err: max_err = row_err
    if max_err <= tol: return 1.0
    penalty_width = tol * 10.0
    return max(0.0, 1.0 - (max_err - tol) / penalty_width)


# === block: score_1 (check id='s04') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows: return 0.0
    for row in rows:
        total = float(row['total_loading'])
        ch4 = float(row['predicted_loading_CH4'])
        c2h6 = float(row['predicted_loading_C2H6'])
        if abs(total - ch4 - c2h6) > 1e-6: return 0.0
    sorted_rows = sorted(rows, key=lambda r: float(r['y_ethane']))
    ch4_vals = [float(r['predicted_loading_CH4']) for r in sorted_rows]
    c2h6_vals = [float(r['predicted_loading_C2H6']) for r in sorted_rows]
    y_vals = [float(r['y_ethane']) for r in sorted_rows]
    mono_score = 1.0
    for i in range(1, len(y_vals)):
        if ch4_vals[i] > ch4_vals[i-1] + 0.01: mono_score = 0.0; break
    for i in range(1, len(y_vals)):
        if c2h6_vals[i] < c2h6_vals[i-1] - 0.01: mono_score = 0.0; break
    endpoint_score = 0.0
    if y_vals:
        if y_vals[0] <= 0.001:
            if abs(ch4_vals[0] - 18.0) <= 2.0 and abs(c2h6_vals[0]) <= 0.1:
                endpoint_score += 0.5
        if y_vals[-1] >= 0.999:
            if abs(c2h6_vals[-1] - 20.0) <= 2.0 and abs(ch4_vals[-1]) <= 0.1:
                endpoint_score += 0.5
    return 0.4 * mono_score + 0.5 * endpoint_score + 0.1


# === block: score_2 (check id='s05') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows: return 0.0
    sorted_rows = sorted(rows, key=lambda r: float(r['x_ethane']))
    y_vals = [float(r['required_y_ethane']) for r in sorted_rows]
    x_vals = [float(r['x_ethane']) for r in sorted_rows]
    ch4_vals = [float(r['predicted_loading_CH4']) for r in sorted_rows]
    c2h6_vals = [float(r['predicted_loading_C2H6']) for r in sorted_rows]
    mono_score = 1.0
    for i in range(1, len(y_vals)):
        if y_vals[i] < y_vals[i-1] - 0.01: mono_score = 0.0; break
    for i in range(1, len(ch4_vals)):
        if ch4_vals[i] > ch4_vals[i-1] + 0.01: mono_score = 0.0; break
    for i in range(1, len(c2h6_vals)):
        if c2h6_vals[i] < c2h6_vals[i-1] - 0.01: mono_score = 0.0; break
    endpoint_score = 0.0
    if x_vals:
        if x_vals[0] <= 0.001:
            if abs(y_vals[0]) <= 0.001 and abs(ch4_vals[0] - 18.0) <= 2.0 and abs(c2h6_vals[0]) <= 0.1:
                endpoint_score += 0.5
        if x_vals[-1] >= 0.999:
            if abs(y_vals[-1] - 1.0) <= 0.001 and abs(c2h6_vals[-1] - 20.0) <= 2.0 and abs(ch4_vals[-1]) <= 0.1:
                endpoint_score += 0.5
    return 0.4 * mono_score + 0.4 * endpoint_score + 0.2


# === block: score_3 (check id='s07') ===
def score_3(artifact, step, ctx):
    gold = ctx['gold_ternary']
    row = artifact[0]
    pred_CO2 = float(row['predicted_loading_CO2'])
    pred_N2 = float(row['predicted_loading_N2'])
    pred_H2O = float(row['predicted_loading_H2O'])
    errs = [abs(pred_CO2 - gold[0]), abs(pred_N2 - gold[1]), abs(pred_H2O - gold[2])]
    max_err = max(errs)
    if max_err <= 0.02: return 1.0
    return max(0.0, 1.0 - (max_err - 0.02)/0.2)


_SCORERS = {
    's02': score_0,
    's04': score_1,
    's05': score_2,
    's07': score_3,
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
