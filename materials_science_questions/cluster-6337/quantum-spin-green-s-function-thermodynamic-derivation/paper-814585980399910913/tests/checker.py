import os
import json
import csv

# === author imports / helpers ===
import subprocess
import sys

# Helper to ensure required packages are installed (checker may pip-install its deps)
def _ensure_pkg(pkg_name, import_as=None):
    try:
        __import__(import_as or pkg_name)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q",
                               "--no-cache-dir", "-i",
                               "https://pypi.tuna.tsinghua.edu.cn/simple",
                               pkg_name])
        __import__(import_as or pkg_name)

_ensure_pkg("numpy")
_ensure_pkg("scipy")

import numpy as np
from scipy import integrate, optimize
import csv
import math
import os
import json as json


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
    spec = json.load(open('/tests/grading_spec.json'))
    params = spec['steps'][1]['config']['params']
    tolerances = spec['steps'][1]['config']['tolerances']
    return {'params': params, 'tolerances': tolerances}


# === block: score_0 (check id='shape_check') ===
def score_0(artifact, step, ctx):
    # artifact is list of dicts
    if artifact is None or not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    required = step.get('config', {}).get('required_columns', [])
    expected_rows = step.get('config', {}).get('expected_rows', 0)
    if set(required).issubset(artifact[0].keys()) and len(artifact) == expected_rows:
        return 1.0
    return 0.0


# === block: score_1 (check id='values_check') ===
def score_1(artifact, step, ctx):
    # artifact: list of dicts
    params = ctx['params']
    tolerances = ctx['tolerances']
    rho_s = params['rho_s']
    hc = params['hc']
    Lambda = params['Lambda']
    N = params['N_components']

    def xi0(Ly):
        xi_J = hc / rho_s
        return (np.e / 8) * (xi_J / (2*np.pi)) * np.exp(2*np.pi * Ly / xi_J) * (1 - xi_J / (4*np.pi * Ly))

    def compute_gap0(Ly):
        xi0_val = xi0(Ly)
        return hc / xi0_val

    def compute_ta0_inv(Ly):
        xi0_val = xi0(Ly)
        Delta0 = hc / xi0_val
        mu0 = Delta0 / hc
        I0_val = (1/(2*np.pi)) * np.log((Lambda + np.sqrt(Lambda**2 + mu0**2))/mu0)
        return N * I0_val / 2.0

    def temperature_correction(Ly, beta):
        # sum over p = 2π m / Ly, m != 0
        Mmax = int(np.floor(Ly * Lambda / (2*np.pi)))
        if Mmax < 1:
            return 0.0
        integral_sum = 0.0
        for m in range(1, Mmax+1):
            p = 2*np.pi * m / Ly
            def integrand(k):
                e = np.sqrt(k**2 + p**2)
                denom = np.exp(beta * hc * e) - 1.0
                if denom <= 0:
                    return 0.0
                return 1.0 / (e * denom)
            res, _ = integrate.quad(integrand, 0, Lambda, limit=200)
            integral_sum += res
        # factor 2 for positive and negative m
        delta = -2 * integral_sum
        return delta

    def solve_gap(ta_inv, Ly, beta):
        # solve for mu = Delta/hc
        def equation(mu):
            if mu <= 0:
                return 1e6
            # integral I(mu)
            def I_func():
                def integrand(k):
                    e_k = np.sqrt(k**2 + mu**2)
                    arg = beta * hc * e_k / 2.0
                    if arg > 100:
                        coth = 1.0
                    else:
                        coth = np.cosh(arg)/np.sinh(arg)
                    return coth / (2 * e_k)
                res, _ = integrate.quad(integrand, 0, Lambda, limit=200)
                return res / (2*np.pi)
            I_val = I_func()
            return (N / ta_inv) * I_val - 1.0  # actually equation N * (1/ta) * I? Wait: Eq. (28): N t_a * I = 1 => I = 1/(N t_a). We have t_a = 1/ta_inv. So N * (1/ta_inv) * I = 1. So condition: N * I / ta_inv = 1 => I * N = ta_inv. So F = I * N - ta_inv.
            # But careful: Eq (28) is N t_a I = 1, so I = 1/(N t_a) = ta_inv / N. Thus ta_inv - N * I = 0.
            # Actually t_a = 1/ta_inv? We defined ta_inv = 1/t_a. So equation is N * I / ta_inv = 1 => N * I = ta_inv. So we solve for mu such that N*I - ta_inv = 0.
            return N * I_val - ta_inv
        # bracket search
        mu_low, mu_high = 1e-6, 10.0
        f_low = equation(mu_low)
        f_high = equation(mu_high)
        if f_low * f_high > 0:
            # try expand
            while equation(mu_high) * f_low > 0 and mu_high < 1e6:
                mu_high *= 2
            if mu_high > 1e5 and equation(mu_high)*equation(mu_low) > 0:
                raise ValueError("No root found")
        mu_root = optimize.brentq(equation, mu_low, mu_high, xtol=1e-8)
        return mu_root

    def expected_values(Ly, T):
        if T == 0:
            xi = xi0(Ly)
            gap = compute_gap0(Ly)
            return xi, gap
        beta = 1.0 / T
        ta_inv_0 = compute_ta0_inv(Ly)
        delta = temperature_correction(Ly, beta)
        ta_inv = ta_inv_0 + delta
        if ta_inv <= 0:
            return None, None
        mu = solve_gap(ta_inv, Ly, beta)
        gap = mu * hc
        xi = hc / gap
        return xi, gap

    rows = artifact
    if not rows:
        return 0.0
    tol_T0 = tolerances['T0']
    tol_T = tolerances['finite_T']
    score_sum = 0.0
    n = 0
    for row in rows:
        try:
            legs = int(row['legs'])
            T = float(row['temperature'])
            corr_len = float(row['correlation_length'])
            gap_str = row.get('gap', '')
            gap_val = float(gap_str) if gap_str and gap_str.lower() != 'nan' else None
            exp_xi, exp_gap = expected_values(legs, T)
            if exp_xi is None:
                score_row = 0.0
            else:
                rel_err_xi = abs(corr_len - exp_xi) / max(abs(exp_xi), 1.0)
                tol_rel = tol_T0 if T == 0 else tol_T
                score_xi = max(0.0, 1.0 - rel_err_xi / tol_rel)
                score_gap = 1.0
                if gap_val is not None and exp_gap is not None:
                    rel_err_gap = abs(gap_val - exp_gap) / max(abs(exp_gap), 1.0)
                    score_gap = max(0.0, 1.0 - rel_err_gap / tol_rel)
                score_row = 0.5 * score_xi + 0.5 * score_gap
            score_sum += score_row
            n += 1
        except Exception:
            n += 1
    if n == 0:
        return 0.0
    return score_sum / n


# === block: score_2 (check id='monotonicity_check') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    # Build dicts
    by_leg = {}
    for row in rows:
        try:
            legs = int(row['legs'])
            T = float(row['temperature'])
            corr = float(row['correlation_length'])
            if legs not in by_leg:
                by_leg[legs] = {}
            by_leg[legs][T] = corr
        except:
            pass
    # Checks
    checks = 0
    passed = 0
    # leg monotonic: for each T, legs order: corr should increase
    Ts = sorted(set(by_leg[2].keys()) | set(by_leg[4].keys()) | set(by_leg[6].keys()))
    legs_list = [2, 4, 6]
    for T in Ts:
        vals = []
        for l in legs_list:
            if l in by_leg and T in by_leg[l]:
                vals.append(by_leg[l][T])
        if len(vals) >= 2:
            for i in range(len(vals)-1):
                checks += 1
                if vals[i] <= vals[i+1] * 1.001:  # allow tiny non monotonic from noise
                    passed += 1
    # T monotonic: for each leg, corr should decrease with T
    for l in legs_list:
        if l in by_leg:
            temps = sorted(by_leg[l].keys(), reverse=False)
            for i in range(len(temps)-1):
                checks += 1
                if by_leg[l][temps[i]] >= by_leg[l][temps[i+1]] * 0.999:
                    passed += 1
    if checks == 0:
        return 1.0
    return passed / checks


_SCORERS = {
    'shape_check': score_0,
    'values_check': score_1,
    'monotonicity_check': score_2,
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
