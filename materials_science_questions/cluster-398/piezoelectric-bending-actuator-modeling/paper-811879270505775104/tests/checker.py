import os
import json
import csv

# === author imports / helpers ===
import math
import os


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
    return {"outputs_dir": outputs_dir}


# === block: score_0 (check id='peak_coefficients') ===
def score_0(artifact, step, ctx):
    targets = step.get('targets', {})
    if not targets:
        return 0.0
    total = 0.0
    count = 0
    for key, tdef in targets.items():
        if key not in artifact:
            continue
        try:
            val = float(artifact[key])
        except:
            continue
        gold = tdef['value']
        tol_type = tdef['tol_type']
        tol = tdef['tol']
        if tol_type == 'absolute':
            ok = abs(val - gold) <= tol
        else:
            ok = abs(val - gold) <= tol * max(abs(gold), abs(val))
        total += 1.0 if ok else 0.0
        count += 1
    return total / count if count > 0 else 0.0


# === block: score_1 (check id='voltage_dependence') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    required = {'V_m', 'P_ell', 'dP_dV', 'alpha', 'c11', 'c12', 'c22', 'k'}
    if not required.issubset(rows[0].keys()):
        return 0.0
    n = len(rows)
    try:
        V_m = [float(r['V_m']) for r in rows]
        P_ell = [float(r['P_ell']) for r in rows]
        dP_dV_agent = [float(r['dP_dV']) for r in rows]
        alpha_agent = [float(r['alpha']) for r in rows]
        c11 = [float(r['c11']) for r in rows]
        c12 = [float(r['c12']) for r in rows]
        c22 = [float(r['c22']) for r in rows]
        k_agent = [float(r['k']) for r in rows]
    except (ValueError, KeyError):
        return 0.0

    config = step.get('config', {})
    min_rows = config.get('expected_rows_min', 180)
    deriv_tol = config.get('derivative_tolerance', 1e-6)
    alpha_tol = config.get('alpha_tolerance', 1e-4)
    k_tol = config.get('k_tolerance', 1e-4)

    row_score = 1.0 if n >= min_rows else 0.0

    mono = all(P_ell[i] <= P_ell[i+1] + 1e-12 for i in range(n-1))
    mono_score = 1.0 if mono else 0.0

    V_volts = [v / 1000.0 for v in V_m]
    dP_dV_comp = []
    for i in range(n):
        if i == 0:
            dV = V_volts[1] - V_volts[0]
            if dV == 0: dV = 1e-9
            dP_dV_comp.append((P_ell[1] - P_ell[0]) / dV)
        elif i == n - 1:
            dV = V_volts[-1] - V_volts[-2]
            if dV == 0: dV = 1e-9
            dP_dV_comp.append((P_ell[-1] - P_ell[-2]) / dV)
        else:
            dV = (V_volts[i+1] - V_volts[i-1]) / 2.0
            if dV == 0: dV = 1e-9
            dP_dV_comp.append((P_ell[i+1] - P_ell[i-1]) / dV)
    max_abs_diff = max(abs(dP_dV_agent[i] - dP_dV_comp[i]) for i in range(n))
    deriv_score = 1.0 if max_abs_diff < deriv_tol else max(0.0, 1.0 - (max_abs_diff - deriv_tol) / deriv_tol)

    # get b2 from peak coefficients JSON
    b2_val = 0.27
    try:
        peak_path = os.path.join(ctx['outputs_dir'], 'step_01_coefficients.json')
        import json
        with open(peak_path) as f:
            peak_data = json.load(f)
            if 'b2' in peak_data:
                b2_val = float(peak_data['b2'])
    except:
        pass

    alpha_comp = [1.0 / (1.0 + b2_val * p * (1.0 - p)) for p in P_ell]
    max_alpha_diff = max(abs(alpha_agent[i] - alpha_comp[i]) for i in range(n))
    alpha_score = 1.0 if max_alpha_diff < alpha_tol else max(0.0, 1.0 - (max_alpha_diff - alpha_tol) / alpha_tol)

    k_comp = []
    for i in range(n):
        if c11[i] > 0 and c22[i] > 0:
            k_comp.append(abs(c12[i]) / math.sqrt(c11[i] * c22[i]))
        else:
            k_comp.append(0.0)
    max_k_diff = max(abs(k_agent[i] - k_comp[i]) for i in range(n))
    k_score = 1.0 if max_k_diff < k_tol else max(0.0, 1.0 - (max_k_diff - k_tol) / k_tol)

    idx_half = min(range(n), key=lambda i: abs(P_ell[i] - 0.5))
    window = 5
    start = max(0, idx_half - window)
    end = min(n, idx_half + window + 1)
    peak_val = dP_dV_agent[idx_half]
    peak_is_max = all(peak_val >= dP_dV_agent[i] - 1e-12 for i in range(start, end))
    ok_peak = peak_val > 1e-12 and peak_is_max
    left_avg = sum(dP_dV_agent[start:idx_half]) / (idx_half - start) if idx_half > start else peak_val
    right_avg = sum(dP_dV_agent[idx_half+1:end]) / (end - idx_half - 1) if end > idx_half+1 else peak_val
    bell_shape = left_avg < peak_val and right_avg < peak_val
    peak_score = 1.0 if (ok_peak and bell_shape) else 0.0

    w_row = 0.05
    w_mono = 0.1
    w_deriv = 0.25
    w_alpha = 0.2
    w_k = 0.2
    w_peak = 0.2
    return w_row * row_score + w_mono * mono_score + w_deriv * deriv_score + w_alpha * alpha_score + w_k * k_score + w_peak * peak_score


_SCORERS = {
    'peak_coefficients': score_0,
    'voltage_dependence': score_1,
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
