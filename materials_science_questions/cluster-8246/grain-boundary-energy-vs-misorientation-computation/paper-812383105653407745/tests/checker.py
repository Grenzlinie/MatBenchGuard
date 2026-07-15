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
    # Prepare shared constants for the checker
    return {
        'G': 100e9,        # Pa
        'nu': 0.3,
        'gamma': 0.6,      # J/m^2
        'b': 0.4e-9,       # m
        'L_m': 10e-9,      # m
        'L_nm': 10.0,      # nm
        'abs_tol': 1e-12,
        'rel_tol': 1e-8
    }


# === block: score_0 (check id='deltaW_value_check') ===
def score_0(artifact, step, ctx):
    def compute_deltaW(misfit, n, N, alpha_deg, alpha, sin_half, ctx):
        # Convert to meters
        L_m = ctx['L_m']
        L_nm = ctx['L_nm']
        b = ctx['b']
        G = ctx['G']
        nu = ctx['nu']
        gamma = ctx['gamma']
        B = n * b
        r0 = B
        # h_i in meters: (2*i-1)/2 * L_m * sin(alpha/2)
        def h_i(i):
            return (2.0*i - 1.0) / 2.0 * L_m * sin_half
        D = G / (2.0 * math.pi * (1.0 - nu))
        # Self-energy sum
        W_self = 0.0
        for i in range(1, N+1):
            h = h_i(i)
            num = 2.0*h - r0
            if num <= 0:
                continue
            term = math.log(num / r0) - 2.0*h*(h - r0) / (num * num)
            W_self += term
        # Interaction sum (over all i,j, i!=j)
        W_int = 0.0
        for i in range(1, N+1):
            hi = h_i(i)
            for j in range(1, N+1):
                if j == i:
                    continue
                hj = h_i(j)
                factor = math.cos(alpha/2.0)**2 + ((-1)**(i+j)) * math.sin(alpha/2.0)**2
                # Avoid division by zero
                diff = abs(hi - hj)
                if diff < 1e-20:
                    continue
                term = math.log((hi + hj) / diff) - 2.0*hi*hj / ((hi + hj)*(hi + hj))
                W_int += factor * term
        # Elastic energy Eq. (11): W_el = (D*B^2/2) * ( 2*W_int + W_self )
        W_el = D * B * B / 2.0 * (2.0 * W_int + W_self)
        # Surface energy Eq. (12): Ws = gamma * (N*L_m - H_m) where H_m = N*L_m*sin(alpha/2)
        H_m = N * L_m * sin_half
        Ws = gamma * (N * L_m - H_m)
        # Misfit coupling Eq. (15): Wf = -pi * D * B * (1+nu) * f * L_m * N^2 * sin(alpha)
        Wf = -math.pi * D * B * (1.0 + nu) * misfit * L_m * N * N * math.sin(alpha)
        return W_el + Ws + Wf

    # Tolerances relaxed to absorb double-precision variability
    abs_tol = 1e-8
    rel_tol = 1e-6

    correct = 0
    total = 0
    for row in artifact:
        try:
            misfit = float(row['misfit_parameter'])
            n = int(float(row['Burgers_vector_n']))
            H_nm = float(row['film_thickness_nm'])
            alpha_deg = float(row['angle_deg'])
            reported = float(row['delta_W_J'])
        except Exception:
            continue
        alpha = math.radians(alpha_deg)
        sin_half = math.sin(alpha / 2.0)
        L_nm = ctx['L_nm']
        L_sin_nm = L_nm * sin_half  # nm
        # Infer N from reported film thickness (allow both nominal and exact H)
        if L_sin_nm <= 0:
            continue
        N = int(round(H_nm / L_sin_nm))
        if N < 1:
            continue
        deltaW_comp = compute_deltaW(misfit, n, N, alpha_deg, alpha, sin_half, ctx)
        tol = max(abs_tol, rel_tol * abs(deltaW_comp))
        if abs(reported - deltaW_comp) <= tol:
            correct += 1
        total += 1
    if total == 0:
        return 0.0
    return correct / total


# === block: score_1 (check id='deltaW_trend_check') ===
def score_1(artifact, step, ctx):
    passes = 0
    checks = 0

    # Helper: monotonic non-increasing (value decreases or stays same)
    def is_mono_decreasing(vals, eps=1e-12):
        for a, b in zip(vals, vals[1:]):
            if b > a + eps:
                return False
        return True

    # Helper: monotonic non-decreasing
    def is_mono_increasing(vals, eps=1e-12):
        for a, b in zip(vals, vals[1:]):
            if b < a - eps:
                return False
        return True

    # Convert artifact to list of dicts with typed values
    rows = []
    for row in artifact:
        try:
            rows.append({
                'f': float(row['misfit_parameter']),
                'n': int(float(row['Burgers_vector_n'])),
                'H': float(row['film_thickness_nm']),
                'alpha': float(row['angle_deg']),
                'dW': float(row['delta_W_J'])
            })
        except Exception:
            continue

    # Trend 1: For each B (n), delta_W decreases with f (angle 90, H~707)
    # Filter rows with angle 90 and H near 707 (706-708 nm)
    def is_default_H(H):
        return 706.0 <= H <= 708.0

    def is_angle90(a):
        return abs(a - 90.0) < 0.1

    group1_rows = [r for r in rows if is_angle90(r['alpha']) and is_default_H(r['H'])]
    trend1_ok = True
    for n_val in [1,2,3]:
        subset = sorted([r for r in group1_rows if r['n'] == n_val], key=lambda x: x['f'])
        dw_vals = [r['dW'] for r in subset]
        if len(dw_vals) >= 2:
            if not is_mono_decreasing(dw_vals):
                trend1_ok = False
                break
    checks += 1
    if trend1_ok:
        passes += 1

    # Trend 2: For small f (0.001, 0.002), delta_W increases with B (angle 90, H~707)
    trend2_ok = True
    for f_val in [0.001, 0.002]:
        subset = sorted([r for r in group1_rows if abs(r['f'] - f_val) < 1e-6], key=lambda x: x['n'])
        dw_vals = [r['dW'] for r in subset]
        if len(dw_vals) >= 2:
            if not is_mono_increasing(dw_vals):
                trend2_ok = False
                break
    checks += 1
    if trend2_ok:
        passes += 1

    # Trend 3: For f=0.004, n=1, delta_W decreases with H (angle 90, varying H)
    # Filter rows with f=0.004, n=1, angle 90
    group3_rows = [r for r in rows if abs(r['f'] - 0.004) < 1e-6 and r['n'] == 1 and is_angle90(r['alpha'])]
    group3_sorted = sorted(group3_rows, key=lambda x: x['H'])
    dw_H = [r['dW'] for r in group3_sorted]
    if len(dw_H) >= 2:
        trend3_ok = is_mono_decreasing(dw_H)
    else:
        trend3_ok = True  # lack of rows? but should exist
    checks += 1
    if trend3_ok:
        passes += 1

    # Trend 4: Minimum in alpha not at endpoints for f=0.003, n=1, N=100 (H~707)
    group4_rows = [r for r in rows if abs(r['f'] - 0.003) < 1e-6 and r['n'] == 1 and is_default_H(r['H']) and r['alpha'] in {60.0,90.0,120.0,150.0}]
    if group4_rows:
        dw_map = {r['alpha']: r['dW'] for r in group4_rows}
        min_alpha = min(dw_map, key=lambda a: dw_map[a])
        if min_alpha not in (60.0, 150.0):
            trend4_ok = True
        else:
            trend4_ok = False
    else:
        trend4_ok = True
    checks += 1
    if trend4_ok:
        passes += 1

    if checks == 0:
        return 0.0
    return passes / checks


_SCORERS = {
    'deltaW_value_check': score_0,
    'deltaW_trend_check': score_1,
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
