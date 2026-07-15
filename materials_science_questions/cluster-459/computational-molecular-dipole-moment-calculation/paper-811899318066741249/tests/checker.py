import os
import json
import csv

# === author imports / helpers ===
import subprocess
import sys
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--quiet', '--no-cache-dir', 'numpy', 'scipy'])
import numpy as np
from scipy.stats import linregress
import math
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
    import numpy as np
    from scipy.stats import linregress
    import math
    import csv

    # Hidden gold parameters and thermo reference table
    ctx = {}
    ctx['mu_gas'] = 2.340  # D
    ctx['D2Cm'] = 3.33564e-30
    ctx['N0'] = 6.02214076e23
    ctx['eps0'] = 8.854187817e-12
    ctx['kB'] = 1.380649e-23

    # Thermo gold coefficients
    ctx['a1'] = -3928.0
    ctx['a2'] = -0.0102
    ctx['a3'] = 6.4656
    ctx['b2'] = 0.16450
    ctx['b3'] = -28.678

    # Compute expected alpha and kappa for each thermo point
    thermo_points = spec['steps'][3]['thermo_points']  # hardcoded reference
    ref_alpha = {}
    ref_kappa = {}
    for pt in thermo_points:
        T_n = pt['T_n']
        P = pt['P']
        rho = pt['rho']
        # alpha = (a1 + a3*rho) / (T_n**2 * rho * (a2 + a3/T_n))
        num_alpha = ctx['a1'] + ctx['a3'] * rho
        den_alpha = (T_n ** 2) * rho * (ctx['a2'] + ctx['a3'] / T_n)
        alpha_val = num_alpha / den_alpha
        # kappa = (b2 + b3/T_n) / (rho * (a2 + a3/T_n))
        num_kappa = ctx['b2'] + ctx['b3'] / T_n
        den_kappa = rho * (ctx['a2'] + ctx['a3'] / T_n)
        kappa_val = num_kappa / den_kappa
        key = (T_n, P)
        ref_alpha[key] = alpha_val
        ref_kappa[key] = kappa_val
    ctx['ref_alpha'] = ref_alpha
    ctx['ref_kappa'] = ref_kappa
    return ctx


# === block: score_0 (check id='dielectric_coeffs') ===
def score_0(artifact, step, ctx):
    import json
    fn = f'/app/outputs/dielectric_eqn_coefficients.json'
    with open(fn) as f:
        artifact = json.load(f)
    gold = step['gold']
    tols = step['tolerances']
    def within(val, target, tol):
        if isinstance(tol, dict):
            if 'rel' in tol:
                return abs(val - target) <= tol['rel'] * abs(target) + 1e-12
            if 'abs' in tol:
                return abs(val - target) <= tol['abs']
        return abs(val - target) <= tol
    fields = ['a1','a2','a3','b0','b1','b2','b3']
    score = 0.0
    for fname in fields:
        if fname in artifact and within(artifact[fname], gold[fname], tols.get(fname, 0)):
            score += 1.0/len(fields)
    return score


# === block: score_1 (check id='kirkwood_dipole') ===
def score_1(artifact, step, ctx):
    import json
    fn = f'/app/outputs/kirkwood_results.json'
    with open(fn) as f:
        artifact = json.load(f)
    kf = artifact.get('kirkwood_function', [])
    if not kf or len(kf) < 3:
        return 0.0
    T_vals = np.array([pt['T_n'] for pt in kf])
    K1_vals = np.array([pt['K1'] for pt in kf])
    invT = 1.0 / T_vals
    slope, intercept, r_val, p_val, std_err = linregress(invT, K1_vals)
    mu2 = slope * 9.0 * step['eps0'] * step['kB'] / step['N0']
    mu_K_star = math.sqrt(mu2) / step['D2Cm']
    diff = abs(mu_K_star - step['mu_gold'])
    if diff <= step['mu_tolerance']:
        return 1.0
    else:
        return max(0.0, 1.0 - diff / (step['mu_tolerance']*2))


# === block: score_2 (check id='kf_dipole') ===
def score_2(artifact, step, ctx):
    import json
    fn = f'/app/outputs/kf_results.json'
    with open(fn) as f:
        artifact = json.load(f)
    kf = artifact.get('kf_function', [])
    if not kf or len(kf) < 3:
        return 0.0
    T_vals = np.array([pt['T_n'] for pt in kf])
    KFF_vals = np.array([pt['KFF'] for pt in kf])
    invT = 1.0 / T_vals
    slope, intercept, r_val, p_val, std_err = linregress(invT, KFF_vals)
    mu2 = slope * 9.0 * step['eps0'] * step['kB'] / step['N0']
    mu_KF_star = math.sqrt(mu2) / step['D2Cm']
    diff = abs(mu_KF_star - step['mu_gold'])
    if diff <= step['mu_tolerance']:
        return 1.0
    else:
        return max(0.0, 1.0 - diff / (step['mu_tolerance']*2))


# === block: score_3 (check id='thermo_props') ===
def score_3(artifact, step, ctx):
    # Gold αP and κT are computed in prepare() from the paper’s Table 3 coefficients
    # and the experimental ρ values, per Eqs. (2),(3),(10),(11).
    import csv
    fn = f'/app/outputs/thermodynamic_properties.csv'
    with open(fn) as f:
        rows = list(csv.DictReader(f))
    if not rows:
        return 0.0
    alpha_scores = []
    kappa_scores = []
    for row in rows:
        try:
            T_n = float(row['T_n'])
            P = float(row['P'])
            alpha = float(row['alpha_P'])
            kappa = float(row['kappa_T'])
        except (KeyError, ValueError):
            continue
        key = (T_n, P)
        ref_alpha = ctx['ref_alpha'].get(key, None)
        ref_kappa = ctx['ref_kappa'].get(key, None)
        if ref_alpha is None:
            continue
        # alpha deviation
        if ref_alpha != 0:
            dev_alpha = abs(alpha - ref_alpha) / abs(ref_alpha)
        else:
            dev_alpha = abs(alpha - ref_alpha) * 1e6
        if dev_alpha <= step['alpha_tolerance']:
            a_score = 1.0
        else:
            a_score = max(0.0, 1.0 - (dev_alpha - step['alpha_tolerance']) / 0.2)
        alpha_scores.append(a_score)
        # kappa deviation
        if ref_kappa != 0:
            dev_kappa = abs(kappa - ref_kappa) / abs(ref_kappa)
        else:
            dev_kappa = abs(kappa - ref_kappa) * 1e6
        if dev_kappa <= step['kappa_tolerance']:
            k_score = 1.0
        else:
            k_score = max(0.0, 1.0 - (dev_kappa - step['kappa_tolerance']) / 0.4)
        kappa_scores.append(k_score)
    if not alpha_scores or not kappa_scores:
        return 0.0
    mean_alpha = sum(alpha_scores) / len(alpha_scores)
    mean_kappa = sum(kappa_scores) / len(kappa_scores)
    return 0.5 * mean_alpha + 0.5 * mean_kappa


_SCORERS = {
    'dielectric_coeffs': score_0,
    'kirkwood_dipole': score_1,
    'kf_dipole': score_2,
    'thermo_props': score_3,
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
