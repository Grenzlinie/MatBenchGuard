import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import quad
import csv, os, json


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
    R = 8.314
    theta_E = 269.2
    a = -1.085e-3
    b = -1.1835e-7
    A = 229615.89
    B = 12.73
    C = -1.1274e-2

    def solve_yva(T):
        if T <= 0:
            return 0.0
        Gva = 0.2 * R * T
        Omega = A + B*T + C*T**2
        def f(y):
            return y - np.exp(-(Gva + Omega * (1.0 - y)**2) / (R*T))
        # If f(0) >= 0 the root is essentially zero (exponential underflow)
        if f(0.0) >= 0.0:
            return 0.0
        return brentq(f, 0.0, 1.0, xtol=1e-14)

    def compute_cp_pure(T):
        x = theta_E / T
        einstein = 3*R * x**2 * np.exp(x) / (np.exp(x)-1)**2
        return einstein + a*T + b*T**2

    def compute_cp_and_h(T):
        yva = solve_yva(T)
        h = 0.01  # small delta for numerical derivative
        yva_p = solve_yva(T+h)
        yva_m = solve_yva(T-h)
        dyva_dT = (yva_p - yva_m)/(2*h)
        cp_pure = compute_cp_pure(T)
        cp = cp_pure - 2*C*T*yva + (A - C*T**2)*dyva_dT

        # integrate Cp from 298.15 to T for heat content
        if T >= 298.15:
            # numerical integration with caching to avoid repeated solves
            def integrand(t):
                y = solve_yva(t)
                cp_p = compute_cp_pure(t)
                # reuse dyva? compute total cp directly
                # We recompute dyva numerically inside but it's okay
                # Use same approach
                f_h = 0.01
                yp = solve_yva(t+f_h) if t+f_h <= 3800 else yva
                ym = solve_yva(t-f_h) if t-f_h > 0 else yva
                dydt = (yp - ym)/(2*f_h) if (t-f_h>0 and t+f_h<=3800) else 0.0
                cp_t = cp_p - 2*C*t*y + (A - C*t**2)*dydt
                return cp_t
            H_diff, _ = quad(integrand, 298.15, T, limit=200, epsabs=1e-6, epsrel=1e-6)
        else:
            def integrand(t):
                y = solve_yva(t)
                cp_p = compute_cp_pure(t)
                f_h = 0.01
                yp = solve_yva(t+f_h) if t+f_h <= 3800 else yva
                ym = solve_yva(t-f_h) if t-f_h > 0 else yva
                dydt = (yp - ym)/(2*f_h) if (t-f_h>0 and t+f_h<=3800) else 0.0
                cp_t = cp_p - 2*C*t*y + (A - C*t**2)*dydt
                return cp_t
            val, _ = quad(integrand, T, 298.15, limit=200, epsabs=1e-6, epsrel=1e-6)
            H_diff = -val
        return yva, cp, H_diff

    # Collect all temperatures from scoring steps
    spec = json.load(open('/tests/grading_spec.json'))
    temps = set()
    for step in spec['steps']:
        if 'temperatures' in step:
            temps.update(step['temperatures'])
    temps = sorted(temps)

    ref = {}
    for T in temps:
        yva, cp, h = compute_cp_and_h(T)
        ref[T] = {'yva': yva, 'cp': cp, 'h_diff': h}

    return {'ref': ref}


# === block: score_0 (check id='check_cp_values') ===
def score_0(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list) or len(artifact)==0:
        return 0.0
    try:
        T_agent = np.array([float(r['T']) for r in artifact])
        Cp_agent = np.array([float(r['Cp']) for r in artifact])
    except:
        return 0.0
    temps = step['temperatures']
    ref = ctx['ref']
    tol = step['relative_tol']
    scores = []
    for T in temps:
        ref_cp = ref[T]['cp']
        idx = np.argmin(np.abs(T_agent - T))
        cp_val = Cp_agent[idx]
        rel_err = abs(cp_val - ref_cp) / max(abs(ref_cp), 1e-9)
        scores.append(1.0 if rel_err <= tol else 0.0)
    return float(np.mean(scores))


# === block: score_1 (check id='check_heat_content_values') ===
def score_1(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list) or len(artifact)==0:
        return 0.0
    try:
        T_agent = np.array([float(r['T']) for r in artifact])
        H_agent = np.array([float(r['H_minus_H298']) for r in artifact])
    except:
        return 0.0
    temps = step['temperatures']
    ref = ctx['ref']
    tol = step['relative_tol']
    scores = []
    for T in temps:
        ref_h = ref[T]['h_diff']
        idx = np.argmin(np.abs(T_agent - T))
        h_val = H_agent[idx]
        rel_err = abs(h_val - ref_h) / max(abs(ref_h), 1e-9)
        scores.append(1.0 if rel_err <= tol else 0.0)
    return float(np.mean(scores))


# === block: score_2 (check id='check_yva_values') ===
def score_2(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list) or len(artifact)==0:
        return 0.0
    try:
        T_agent = np.array([float(r['T']) for r in artifact])
        y_agent = np.array([float(r['y_va']) for r in artifact])
    except:
        return 0.0
    temps = step['temperatures']
    ref = ctx['ref']
    tol = step['absolute_tol']
    scores = []
    for T in temps:
        ref_y = ref[T]['yva']
        idx = np.argmin(np.abs(T_agent - T))
        y_val = y_agent[idx]
        abs_err = abs(y_val - ref_y)
        scores.append(1.0 if abs_err <= tol else 0.0)
    return float(np.mean(scores))


# === block: score_3 (check id='structural_audit') ===
def score_3(artifact, step, ctx):
    base = '/app/outputs'
    files = {
        'cp': 'heat_capacity.csv',
        'heat': 'heat_content.csv',
        'yva': 'vacancy_concentration.csv'
    }
    data = {}
    for key, fname in files.items():
        path = os.path.join(base, fname)
        if not os.path.exists(path):
            return 0.0
        with open(path, newline='') as f:
            rows = list(csv.DictReader(f))
        if not rows:
            return 0.0
        try:
            T = np.array([float(r['T']) for r in rows])
            if key == 'cp':
                vals = np.array([float(r['Cp']) for r in rows])
            elif key == 'heat':
                vals = np.array([float(r['H_minus_H298']) for r in rows])
            else:
                vals = np.array([float(r['y_va']) for r in rows])
        except:
            return 0.0
        data[key] = (T, vals)

    # Monotonic checks
    for key in ['cp', 'heat']:
        _, vals = data[key]
        if not np.all(np.diff(vals) >= -1e-6):
            return 0.0

    # Curvature check for vacancy Arrhenius plot
    T_y, yva = data['yva']
    mask = yva > 1e-6
    if np.sum(mask) < 3:
        return 0.0
    x = 10000.0 / T_y[mask]
    y_log = np.log10(yva[mask])
    coeffs = np.polyfit(x, y_log, 2)
    # second derivative non-zero => curvature
    if abs(coeffs[0]) < 1e-10:
        return 0.0
    return 1.0


_SCORERS = {
    'check_cp_values': score_0,
    'check_heat_content_values': score_1,
    'check_yva_values': score_2,
    'structural_audit': score_3,
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
