import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import scipy.integrate as integrate
import json, csv, os, math


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
    # Global physical parameters
    ctx = {}
    ctx['sigma_A'] = 1.0             # J/m^2
    ctx['xi_A'] = 0.5e-9            # m, half-width (2xi_A=1nm)
    ctx['omega_A'] = 1e9            # J/m^3  (sigma_A / (2*xi_A))
    beta_omega_A = 1.0              # given, beta*omega_A = 1.0
    ctx['beta_omega_A'] = beta_omega_A
    # beta = 1e-9 (makes product 1)
    ctx['beta'] = 1e-9

    def u_g_e_from_u_m_e(u_m_e, alpha):
        r = u_m_e / (1.0 - u_m_e) * math.exp(alpha * ctx['beta_omega_A'])
        return r / (1.0 + r)

    def compute_critical_compositions(alpha):
        e1 = math.exp(ctx['beta_omega_A'])
        ea = math.exp(alpha * ctx['beta_omega_A'])
        u_m_ct = (e1 - 1.0) / (ea - 1.0)
        u_g_ct = ea * (e1 - 1.0) / (e1 * (ea - 1.0))
        return u_m_ct, u_g_ct

    def g_phi(phi):
        return 4.0 * phi * (1.0 - phi)

    def u_profile(phi, u_m_e, alpha):
        # u/(1-u) = (u_m_e/(1-u_m_e)) * exp(alpha*beta_omega_A * g(phi))
        r = u_m_e / (1.0 - u_m_e) * math.exp(alpha * ctx['beta_omega_A'] * g_phi(phi))
        return r / (1.0 + r)

    def omega1_integrand(phi, u_m_e, alpha):
        u = u_profile(phi, u_m_e, alpha)
        # Omega1(phi) from Eq. (61) scaled by 1/omega_A?  Actually Eq. (62) uses sqrt(g+ (1/(beta*omega_A)) ln((1-u)/(1-u_m_e)) )
        # So integrand is sqrt( g(phi) + (1/(beta*omega_A))*ln((1-u)/(1-u_m_e)) )
        # But (1/(beta*omega_A)) = 1/ctx['beta_omega_A'] = 1.0  (since beta_omega_A=1)
        term = g_phi(phi) + (1.0 / ctx['beta_omega_A']) * math.log((1.0 - u) / (1.0 - u_m_e))
        return math.sqrt(max(term, 0.0))

    def compute_model1_sigma(u_m_e, alpha):
        # Numerical integration from 0 to 1, but profile is symmetric, integrate from 0 to 0.5 and double? Actually Eq. (62): σ = (4/π) σ_A ∫_0^1 sqrt(Ω1/ω_A) dφ = (4/π) σ_A ∫_0^1 integrand.
        # The integrand we defined is sqrt( g + (1/(βω_A)) ln(...) ), which equals sqrt(Ω1/ω_A) because Ω1 = ω_A * [g + (1/(βω_A)) ln(...)]? Wait Eq. (62): σ = (4/π) σ_A ∫_0^1 sqrt( g(φ) + (1/(β ω_A)) ln((1-u)/(1-u_m^e)) ) dφ. So directly integrand is that. So we integrate from 0 to 1.
        result, _ = integrate.quad(omega1_integrand, 0.0, 1.0, args=(u_m_e, alpha), limit=200)
        return (4.0/math.pi) * ctx['sigma_A'] * result

    def compute_omega_e(u_m_e, alpha):
        u_g_e = u_g_e_from_u_m_e(u_m_e, alpha)
        return ctx['omega_A'] + (1.0 / ctx['beta']) * math.log((1.0 - u_g_e) / (1.0 - u_m_e))

    def compute_model2_sigma(u_m_e, alpha):
        omega_e = compute_omega_e(u_m_e, alpha)
        return ctx['sigma_A'] * math.sqrt(omega_e / ctx['omega_A'])

    def compute_classical_sigma(u_m_e, alpha):
        omega_e = compute_omega_e(u_m_e, alpha)
        return ctx['sigma_A'] * (omega_e / ctx['omega_A'])

    ctx['u_g_e_from_u_m_e'] = u_g_e_from_u_m_e
    ctx['compute_critical_compositions'] = compute_critical_compositions
    ctx['compute_model1_sigma'] = compute_model1_sigma
    ctx['compute_model2_sigma'] = compute_model2_sigma
    ctx['compute_classical_sigma'] = compute_classical_sigma
    return ctx


# === block: score_0 (check id='step_02_common_gb_composition') ===
def score_0(artifact, step, ctx):
    import math
    artifact = step['artifact']  # list of dicts from csv
    params = step['params']
    alphas = params['alphas']
    test_points = params['test_points']
    tol_rel = params['tolerance_rel']
    func = ctx[params['reference_function']]

    # build mapping per alpha: (float u_m_e) -> float u_g_e
    data = {}
    for row in artifact:
        try:
            a = int(row['alpha'])
            um = float(row['u_m_e'])
            ug = float(row['u_g_e'])
        except:
            continue
        data.setdefault(a, {})[um] = ug

    total_checks = 0
    passed = 0
    for a in alphas:
        if a not in data:
            continue
        for um in test_points:
            # find closest u_m_e in data
            best = None
            min_diff = float('inf')
            for key in data[a]:
                diff = abs(key - um)
                if diff < 1e-10:
                    best = key
                    break
                if diff < min_diff:
                    min_diff = diff
                    best = key
            if best is None:
                continue
            reported = data[a][best]
            expected = func(um, a)
            if abs(reported - expected) <= tol_rel * abs(expected):
                passed += 1
            total_checks += 1
    if total_checks == 0:
        return 0.0
    return passed / total_checks


# === block: score_1 (check id='step_03_modeli_energy') ===
def score_1(artifact, step, ctx):
    import math
    artifact = step['artifact']
    params = step['params']
    alphas = params['alphas']
    test_points_per_alpha = params['test_points_per_alpha']
    tol_rel = params['tolerance_rel']
    func_sigma = ctx[params['reference_function_sigma']]
    func_bounds = ctx[params['reference_function_bounds']]
    check_columns = params['check_columns']

    # build mapping per alpha: dict of u_m_e -> {sigma, u_m_ct, u_g_ct}
    data = {}
    for row in artifact:
        try:
            a = int(row['alpha'])
            um = float(row['u_m_e'])
            sigma = float(row['sigma'])
            u_m_ct = float(row['u_m_ct'])
            u_g_ct = float(row['u_g_ct'])
        except:
            continue
        data.setdefault(a, []).append((um, sigma, u_m_ct, u_g_ct))

    # Check bounds for each alpha: compare u_m_ct and u_g_ct to expected
    passed = 0
    total = 0
    for a in alphas:
        if a not in data:
            continue
        # get bounds from first row (same per alpha)
        _, _, u_m_ct_report, u_g_ct_report = data[a][0]
        u_m_ct_exp, u_g_ct_exp = func_bounds(a)
        if abs(u_m_ct_report - u_m_ct_exp) <= 1e-6 and abs(u_g_ct_report - u_g_ct_exp) <= 1e-6:
            passed += 1
        total += 1

    # Check sigma at specific u_m_e
    for a_str, um_list in test_points_per_alpha.items():
        a = int(a_str)
        if a not in data:
            continue
        # build dict for quick lookup
        lookup = {}
        for um, sig, _, _ in data[a]:
            lookup[um] = sig
        for um_test in um_list:
            # find closest
            best = None
            min_diff = float('inf')
            for key in lookup:
                diff = abs(key - um_test)
                if diff < 1e-10:
                    best = key
                    break
                if diff < min_diff:
                    min_diff = diff
                    best = key
            if best is None:
                continue
            reported = lookup[best]
            expected = func_sigma(um_test, a)
            if abs(reported - expected) <= tol_rel * abs(expected):
                passed += 1
            total += 1

    if total == 0:
        return 0.0
    return passed / total


# === block: score_2 (check id='step_04_modelii_energy') ===
def score_2(artifact, step, ctx):
    import math
    artifact = step['artifact']
    params = step['params']
    alphas = params['alphas']
    test_points_per_alpha = params['test_points_per_alpha']
    tol_rel = params['tolerance_rel']
    func = ctx[params['reference_function']]

    # build mapping per alpha: (float u_m_e) -> float sigma
    data = {}
    for row in artifact:
        try:
            a = int(row['alpha'])
            um = float(row['u_m_e'])
            sigma = float(row['sigma'])
        except:
            continue
        data.setdefault(a, {})[um] = sigma

    total = 0
    passed = 0
    for a_str, um_list in test_points_per_alpha.items():
        a = int(a_str)
        if a not in data:
            continue
        for um_test in um_list:
            best = None
            min_diff = float('inf')
            for key in data[a]:
                diff = abs(key - um_test)
                if diff < 1e-10:
                    best = key
                    break
                if diff < min_diff:
                    min_diff = diff
                    best = key
            if best is None:
                continue
            reported = data[a][best]
            expected = func(um_test, a)
            if abs(reported - expected) <= tol_rel * abs(expected):
                passed += 1
            total += 1
    if total == 0:
        return 0.0
    return passed / total


# === block: score_3 (check id='step_05_classical_energy') ===
def score_3(artifact, step, ctx):
    import math
    artifact = step['artifact']
    params = step['params']
    alphas = params['alphas']
    test_points_per_alpha = params['test_points_per_alpha']
    tol_rel = params['tolerance_rel']
    func = ctx[params['reference_function']]

    data = {}
    for row in artifact:
        try:
            a = int(row['alpha'])
            um = float(row['u_m_e'])
            sigma = float(row['sigma'])
        except:
            continue
        data.setdefault(a, {})[um] = sigma

    total = 0
    passed = 0
    for a_str, um_list in test_points_per_alpha.items():
        a = int(a_str)
        if a not in data:
            continue
        for um_test in um_list:
            best = None
            min_diff = float('inf')
            for key in data[a]:
                diff = abs(key - um_test)
                if diff < 1e-10:
                    best = key
                    break
                if diff < min_diff:
                    min_diff = diff
                    best = key
            if best is None:
                continue
            reported = data[a][best]
            expected = func(um_test, a)
            if abs(reported - expected) <= tol_rel * abs(expected):
                passed += 1
            total += 1
    if total == 0:
        return 0.0
    return passed / total


# === block: score_4 (check id='step_06_analytic_results') ===
def score_4(artifact, step, ctx):
    import json
    artifact = step['artifact']  # a dict
    params = step['params']
    tol = params['tolerance_abs']

    # Compute expected values
    sigma_A = params['expected_sigma_A']
    xi_A = params['expected_xi_A']
    epsilon = (4.0 / math.pi) * math.sqrt(xi_A * sigma_A)
    omega_A = params['expected_omega_A']
    # For u_m_e = 0.09, alpha = 3
    um = params['u_m_e_sample']
    alpha = params['alpha_sample']
    u_g = ctx['u_g_e_from_u_m_e'](um, alpha)
    omega_e = omega_A + (1.0 / ctx['beta']) * math.log((1.0 - u_g) / (1.0 - um))
    sigma_expected = sigma_A * math.sqrt(omega_e / omega_A)
    sigma_over_sigma_A = sigma_expected / sigma_A
    xi_omega = xi_A * omega_e  # note: we need 2ξ * ω^e? The formula is σ/(2ξ ω^e) = 1, but we only have xi_A half-width. Actually 2ξ = 2*xi_A, so σ/(2ξ ω^e) = sigma_expected / (2.0 * xi_A * omega_e) = 1.0.
    # But in task, they ask sigma_over_xi_omega = σ/(2ξ ω^e). So compute directly.
    xi_full = 2.0 * xi_A
    sigma_over_xi_omega = sigma_expected / (xi_full * omega_e)

    # Compare each required key
    required = ['sigma_A', 'xi_A', 'epsilon', 'omega_A', 'sigma', 'sigma_over_sigma_A', 'sigma_over_xi_omega']
    expected_vals = {
        'sigma_A': sigma_A,
        'xi_A': xi_A,
        'epsilon': epsilon,
        'omega_A': omega_A,
        'sigma': sigma_expected,
        'sigma_over_sigma_A': sigma_over_sigma_A,
        'sigma_over_xi_omega': sigma_over_xi_omega
    }
    passed = 0
    total = len(required)
    for key in required:
        if key not in artifact:
            continue
        val = artifact[key]
        exp = expected_vals[key]
        if abs(val - exp) <= tol * max(1.0, abs(exp)):
            passed += 1
    return passed / total


_SCORERS = {
    'step_02_common_gb_composition': score_0,
    'step_03_modeli_energy': score_1,
    'step_04_modelii_energy': score_2,
    'step_05_classical_energy': score_3,
    'step_06_analytic_results': score_4,
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
