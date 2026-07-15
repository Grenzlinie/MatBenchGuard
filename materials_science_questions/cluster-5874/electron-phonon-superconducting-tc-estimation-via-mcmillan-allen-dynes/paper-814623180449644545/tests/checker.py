import os
import json
import csv

# === author imports / helpers ===
import math
import numpy as np
from scipy.special import digamma, polygamma
from scipy.optimize import brentq, curve_fit


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
    params = spec.get('common_parameters', spec['steps'][0]['parameters'])
    lam = params['lambda']
    ThetaD = params['Theta_D']
    epsilonF = params['epsilon_F']
    mustar = params['mu_star']
    mu = params['mu']
    t_grid = np.array(params['t_grid'])
    eftau_vals = params['epsilonFtau_values']

    huge = 1e12
    psi_half = digamma(0.5)
    g = lam - mustar

    # precompute D/D0 factor
    def D_over_D0(eftau):
        if eftau > 1e5:
            return 1.0
        return 1.0 - (3.0 * math.sqrt(3.0) / (4.0 * math.pi)) * (1.0 / eftau**2)

    # compute T_c/T_c0 from Eq.1b
    def compute_Tc_ratio(eftau):
        if eftau > 1e5:
            return 1.0  # clean limit
        tau = eftau / epsilonF  # tau in 1/eV
        tau_ThetaD = ThetaD * tau
        ln_eps_Th = math.log(epsilonF / ThetaD)
        ln_eps_ftau = math.log(eftau) if eftau > 0 else 0.0
        g_star_over_g = (1.0 + mu * ln_eps_Th) / (1.0 + mu * ln_eps_ftau)
        g_star = g_star_over_g * g
        # suppress
        term1 = (1.0 / g_star) ** 2
        term2 = 2.0 * math.pi * (1.0/g - (mustar/g)**2 * math.log(tau_ThetaD))
        exponent = - (3.0 * math.sqrt(3.0) / (8.0 * math.pi)) * (1.0 / eftau**2) * (term1 + term2)
        return math.exp(exponent)

    # FEM equation for given t, h, eftau
    def fem_eq_residual(h, t, eftau, suppress, D_over_D0):
        if t <= 0.0:
            return huge
        a0_term = (2.0 / math.pi) * h / t
        a_term = a0_term * D_over_D0
        lhs = math.log(t) - suppress
        rhs = psi_half - digamma(0.5 + a_term) + (math.sqrt(3.0) * a0_term / (2.0 * eftau**2 * t)) * polygamma(1, 0.5 + a0_term)
        return lhs - rhs

    def solve_h_FEM(t, eftau, suppress, D_over_D0):
        if t >= 1.0 - 1e-12:
            return 0.0
        # find h where residual=0, h>0, typical range
        try:
            # bracket: h in [0, 5]
            f = lambda h: fem_eq_residual(h, t, eftau, suppress, D_over_D0)
            # ensure sign change
            f0 = f(0.0)
            if abs(f0) < 1e-12:
                return 0.0
            f5 = f(5.0)
            for i in range(20):
                h_high = 5.0 + i*5.0
                fh = f(h_high)
                if f0 * fh <= 0:
                    root = brentq(f, 0.0, h_high, xtol=1e-12)
                    return root
            return 0.0
        except:
            return 0.0

    def compute_h_WHHM(t, alpha):
        if t >= 1.0 - 1e-12:
            return 0.0
        target = psi_half - math.log(t)
        # solve digamma(0.5 + alpha*h/t) = target
        def f(h):
            return digamma(0.5 + alpha * h / t) - target
        try:
            # bracket
            f0 = f(0.0)
            # find high bound
            for hmax in [2.0*alpha, 5.0*alpha, 10.0*alpha, 20.0*alpha]:
                if f(hmax) * f0 <= 0:
                    return brentq(f, 0.0, hmax, xtol=1e-12)
            return 0.0
        except:
            return 0.0

    # compute expected curves
    results = {}
    for eftau in eftau_vals:
        suppress = math.log(compute_Tc_ratio(eftau))
        dd = D_over_D0(eftau)
        h_full = []
        h_orig = []
        for t in t_grid:
            hf = solve_h_FEM(t, eftau, suppress, dd)
            h_full.append(hf)
            # original without last term (set delocal term to 0 by not adding term2)
            # we solve same equation but without term2; but easier: recompute with a flag
            # we'll compute using same fem_eq_residual but without the delocalization term
            # We'll implement a separate function
        # Better: compute h_orig by solving fem without last term
        # We'll compute separately
        pass

    # but we can compute h_orig by solving the WHHM equation for the disordered system:
    # that uses D_over_D0*h as variable
    # For each eftau, the original curve is solution of ln(t)-suppress = psi(1/2)-psi(1/2+ (2/pi)(dd*h)/t)
    # This is the same as WHHM with alpha_eff = (2/pi)*dd, but with suppressed T_c ratio
    # So we can compute h_orig(t) = compute_h_whhm_orig(t, dd, suppress)
    def compute_h_orig(t, dd, suppress):
        if t >= 1.0 - 1e-12:
            return 0.0
        target = psi_half - math.log(t) + suppress  # rearranged
        def f(h):
            return digamma(0.5 + (2.0/math.pi)*dd*h/t) - target
        f0 = f(0.0)
        for hmax in [1.0, 2.0, 3.0, 5.0, 10.0]:
            try:
                if f(hmax) * f0 <= 0:
                    return brentq(f, 0.0, hmax, xtol=1e-12)
            except:
                pass
        return 0.0

    # recompute all
    store = {}
    for eftau in eftau_vals:
        suppress = math.log(compute_Tc_ratio(eftau))
        dd = D_over_D0(eftau)
        h_full = [solve_h_FEM(t, eftau, suppress, dd) for t in t_grid]
        h_orig = [compute_h_orig(t, dd, suppress) for t in t_grid]
        # fit WHHM to h_full
        # use curve_fit with custom function that returns h_WHHM(t,alpha)
        def whhm_func(t_data, alpha):
            return np.array([compute_h_WHHM(ti, alpha) for ti in t_data])
        t_data = t_grid
        h_data = np.array(h_full)
        # initial guess for alpha
        alpha_guess = 1.0
        try:
            popt, _ = curve_fit(whhm_func, t_data, h_data, p0=[alpha_guess], bounds=(0.01, 100))
            alpha_fit = popt[0]
        except:
            alpha_fit = 1.0
        h_whhm_fit = [compute_h_WHHM(t, alpha_fit) for t in t_grid]
        # slopes at T_c (near t=1)
        # use h at t=0.95 and t=1.0 for numerical slope
        if len(t_grid) >= 2 and t_grid[-1] == 1.0:
            idx_near = len(t_grid)-2  # t=0.95
            dt = t_grid[-1] - t_grid[idx_near]
            if dt != 0:
                s_full = (h_full[-1] - h_full[idx_near]) / dt  # dh/dt
                s_orig = (h_orig[-1] - h_orig[idx_near]) / dt
                s_fit = (h_whhm_fit[-1] - h_whhm_fit[idx_near]) / dt
            else:
                s_full = s_orig = s_fit = 0.0
        else:
            s_full = s_orig = s_fit = 0.0
        # alpha ratio = s_orig / s_fit (since alpha prop to 1/slope)
        if abs(s_fit) > 1e-12:
            alpha_ratio = s_orig / s_fit
        else:
            alpha_ratio = 1.0
        dTc_ratio = 1.0 - compute_Tc_ratio(eftau)
        # max rel diff
        max_rel_diff = 0.0
        for hf, hw in zip(h_full, h_whhm_fit):
            if hf > 1e-12:
                diff = abs(hf - hw) / hf
                if diff > max_rel_diff:
                    max_rel_diff = diff
        store[eftau] = {
            'h_full': h_full,
            'h_whhm_fit': h_whhm_fit,
            'alpha_ratio': alpha_ratio,
            'dTc_ratio': dTc_ratio,
            'max_rel_diff': max_rel_diff
        }

    ctx = {'store': store, 't_grid': t_grid, 'eftau_vals': eftau_vals}


# === block: score_0 (check id='score_h_vs_t') ===
def score_0(artifact, step, ctx):
    import math
    import numpy as np
    from scipy.special import digamma, polygamma
    from scipy.optimize import brentq, curve_fit

    par = step['parameters']
    tol_h = par.get('tolerance_h', 0.02)
    lam = par['lambda']
    ThetaD = par['Theta_D']
    epsilonF = par['epsilon_F']
    mustar = par['mu_star']
    mu = par['mu']
    t_grid = np.array(par['t_grid'])
    eftau_vals = par['epsilonFtau_values']

    psi_half = digamma(0.5)
    g = lam - mustar

    def D_over_D0(eftau):
        if eftau > 1e5:
            return 1.0
        return 1.0 - (3.0 * math.sqrt(3.0) / (4.0 * math.pi)) * (1.0 / eftau**2)

    def compute_Tc_ratio(eftau):
        if eftau > 1e5:
            return 1.0
        tau = eftau / epsilonF
        tau_ThetaD = ThetaD * tau
        ln_eps_Th = math.log(epsilonF / ThetaD)
        ln_eps_ftau = math.log(eftau) if eftau > 0 else 0.0
        g_star_over_g = (1.0 + mu * ln_eps_Th) / (1.0 + mu * ln_eps_ftau)
        g_star = g_star_over_g * g
        term1 = (1.0 / g_star) ** 2
        term2 = 2.0 * math.pi * (1.0/g - (mustar/g)**2 * math.log(tau_ThetaD))
        exponent = - (3.0 * math.sqrt(3.0) / (8.0 * math.pi)) * (1.0 / eftau**2) * (term1 + term2)
        return math.exp(exponent)

    def fem_residual(h, t, eftau, suppress, dd):
        if t <= 0.0:
            return 1e12
        a0_term = (2.0 / math.pi) * h / t
        a_term = a0_term * dd
        lhs = math.log(t) - suppress
        # corrected last term: no division by t
        rhs = psi_half - digamma(0.5 + a_term) + (math.sqrt(3.0) * a0_term / (2.0 * eftau**2)) * polygamma(1, 0.5 + a0_term)
        return lhs - rhs

    def solve_h_FEM(t, eftau, suppress, dd):
        if t >= 1.0 - 1e-12:
            return 0.0
        try:
            f = lambda h: fem_residual(h, t, eftau, suppress, dd)
            f0 = f(0.0)
            if abs(f0) < 1e-12:
                return 0.0
            for i in range(20):
                h_high = 5.0 + i * 5.0
                fh = f(h_high)
                if f0 * fh <= 0:
                    return brentq(f, 0.0, h_high, xtol=1e-12)
            return 0.0
        except:
            return 0.0

    def compute_h_WHHM(t, alpha):
        if t >= 1.0 - 1e-12:
            return 0.0
        target = psi_half - math.log(t)
        def f(h):
            return digamma(0.5 + alpha * h / t) - target
        try:
            f0 = f(0.0)
            for hmax in [2.0*alpha, 5.0*alpha, 10.0*alpha, 20.0*alpha]:
                if f(hmax) * f0 <= 0:
                    return brentq(f, 0.0, hmax, xtol=1e-12)
            return 0.0
        except:
            return 0.0

    # Build expected references
    ref = {}
    for eftau in eftau_vals:
        tc_ratio = compute_Tc_ratio(eftau)
        suppress = math.log(tc_ratio)
        dd = D_over_D0(eftau)
        h_full = [solve_h_FEM(t, eftau, suppress, dd) for t in t_grid]
        t_data = t_grid
        h_data = np.array(h_full)
        try:
            popt, _ = curve_fit(lambda x, alpha: np.array([compute_h_WHHM(ti, alpha) for ti in x]),
                                t_data, h_data, p0=[1.0], bounds=(0.01, 100))
            alpha_fit = popt[0]
        except:
            alpha_fit = 1.0
        h_whhm_fit = [compute_h_WHHM(t, alpha_fit) for t in t_grid]
        ref[eftau] = {'h_full': h_full, 'h_whhm_fit': h_whhm_fit}

    rows = artifact
    total = 0
    passed = 0
    for row in rows:
        total += 1
        try:
            eftau = float(row['epsilonFtau'])
            t = float(row['t'])
            h_fem_sub = float(row['h_FEM'])
            h_whhm_sub = float(row['h_WHHM_fit'])
        except:
            continue
        mapped = 1000000.0 if eftau > 1e5 else eftau
        if mapped not in ref:
            continue
        exp = ref[mapped]
        idx = (np.abs(t_grid - t)).argmin()
        if abs(h_fem_sub - exp['h_full'][idx]) <= tol_h and abs(h_whhm_sub - exp['h_whhm_fit'][idx]) <= tol_h:
            passed += 1
    if total == 0:
        return 0.0
    return passed / total


# === block: score_1 (check id='score_ratios') ===
def score_1(artifact, step, ctx):
    store = ctx['store']
    eftau_vals = ctx['eftau_vals']
    tol_alpha = 0.05
    tol_dTc = 0.05
    tol_max_rel = 0.01
    indistinguishable_vals = ctx.get('indistinguishable_vals', [1000000.0, 2.0])
    max_rel_threshold = 0.015
    rows = artifact  # list of dicts: epsilonFtau, alpha_H_over_alpha_0, dTc_over_Tc0, max_rel_diff...
    total_rows = 0
    passed_rows = 0
    for row in rows:
        total_rows += 1
        try:
            eftau = float(row['epsilonFtau'])
            alpha_sub = float(row['alpha_H_over_alpha_0'])
            dTc_sub = float(row['dTc_over_Tc0'])
            max_rel_sub = float(row['max_rel_diff_h_vs_WHHM_fit'])
        except:
            continue
        # map large value
        mapped = 1000000.0 if eftau > 1e5 else eftau
        if mapped not in store:
            continue
        exp = store[mapped]
        alpha_exp = exp['alpha_ratio']
        dTc_exp = exp['dTc_ratio']
        max_rel_exp = exp['max_rel_diff']
        ok_alpha = abs(alpha_sub - alpha_exp) <= tol_alpha
        ok_dTc = abs(dTc_sub - dTc_exp) <= tol_dTc
        ok_max_rel = abs(max_rel_sub - max_rel_exp) <= tol_max_rel
        # additional indistinguishability check
        indist_ok = True
        if mapped in indistinguishable_vals:
            if max_rel_sub > max_rel_threshold:
                indist_ok = False
        if ok_alpha and ok_dTc and ok_max_rel and indist_ok:
            passed_rows += 1
    if total_rows == 0:
        return 0.0
    return passed_rows / total_rows


_SCORERS = {
    'score_h_vs_t': score_0,
    'score_ratios': score_1,
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
