import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.optimize import fsolve


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
    T = 1873.0
    R = 8.314462618
    NA = 6.02214076e23
    NA13 = NA ** (1/3)
    M_Co = 58.933
    M_Cr = 51.996
    M_Ni = 58.693
    rho_Co = 7.75
    rho_Cr = 6.3
    rho_Ni = 7.9

    def molar_surface_area(M, rho):
        V = M / rho
        S_cm2 = 1.091 * NA13 * (V ** (2/3))
        return S_cm2 * 1e-4

    S_Co = molar_surface_area(M_Co, rho_Co)
    S_Cr = molar_surface_area(M_Cr, rho_Cr)
    S_Ni = molar_surface_area(M_Ni, rho_Ni)

    sigma_Co0 = 866.0 - 0.15 * (T - 933)
    sigma_Cr0 = 1672.0 - 0.20 * (T - 2178)
    sigma_Ni0 = 1838.0 - 0.42 * (T - 1728)

    CoCr_A0, CoCr_B0 = -12008.6239, 2.2019
    CoCr_A1, CoCr_B1 = -5836.4696, 1.1402
    CrNi_A0, CrNi_B0 = 318, -7.33
    CrNi_A1, CrNi_B1 = 16941, -6.37
    CoNi_A0, CoNi_B0 = 1331, 0.0

    ctx = dict(
        T=T, R=R,
        S=dict(Co=S_Co, Cr=S_Cr, Ni=S_Ni),
        sigma_pure=dict(Co=sigma_Co0, Cr=sigma_Cr0, Ni=sigma_Ni0),
        binary=dict(
            CoCr=dict(A=[CoCr_A0, CoCr_A1], B=[CoCr_B0, CoCr_B1]),
            CrNi=dict(A=[CrNi_A0, CrNi_A1], B=[CrNi_B0, CrNi_B1]),
            CoNi=dict(A=[CoNi_A0], B=[CoNi_B0])
        ),
        beta_tilde=0.75
    )
    return ctx


# === block: score_0 (check id='surface_properties') ===
def score_0(artifact, step, ctx):
    def compute_G_xs(x_arr, ctx):
        x_Co, x_Cr, x_Ni = float(x_arr[0]), float(x_arr[1]), float(x_arr[2])
        T = ctx['T']
        G = 0.0
        if x_Co > 1e-12 and x_Cr > 1e-12:
            d = x_Co - x_Cr
            a0, a1 = ctx['binary']['CoCr']['A']
            b0, b1 = ctx['binary']['CoCr']['B']
            L0 = a0 + b0 * T
            L1 = a1 + b1 * T
            G += x_Co * x_Cr * (L0 + L1 * d)
        if x_Cr > 1e-12 and x_Ni > 1e-12:
            d = x_Cr - x_Ni
            a0, a1 = ctx['binary']['CrNi']['A']
            b0, b1 = ctx['binary']['CrNi']['B']
            L0 = a0 + b0 * T
            L1 = a1 + b1 * T
            G += x_Cr * x_Ni * (L0 + L1 * d)
        if x_Co > 1e-12 and x_Ni > 1e-12:
            a0 = ctx['binary']['CoNi']['A'][0]
            b0 = ctx['binary']['CoNi']['B'][0]
            L0 = a0 + b0 * T
            G += x_Co * x_Ni * L0
        return G

    def partial_G_xs(comp, idx, ctx, beta=1.0):
        x = np.array([comp['Co'], comp['Cr'], comp['Ni']])
        eps = 1e-7
        dx = np.zeros(3)
        dx[idx] = 1.0
        other = [j for j in range(3) if j != idx]
        for j in other:
            dx[j] = -0.5
        x_plus = x + eps * dx
        x_minus = x - eps * dx
        G_plus = compute_G_xs(x_plus, ctx)
        G_minus = compute_G_xs(x_minus, ctx)
        return beta * (G_plus - G_minus) / (2.0 * eps)

    def butler_residuals(X, bulk, ctx):
        X_Cr_s, X_Ni_s, sigma = X
        X_Co_s = 1.0 - X_Cr_s - X_Ni_s
        if X_Co_s < -1e-9 or X_Cr_s < -1e-9 or X_Ni_s < -1e-9:
            return np.array([1e6, 1e6, 1e6])
        xs = {'Co': X_Co_s, 'Cr': X_Cr_s, 'Ni': X_Ni_s}
        xb = {'Co': bulk['X_Co'], 'Cr': bulk['X_Cr'], 'Ni': bulk['X_Ni']}
        T = ctx['T']
        R = ctx['R']
        S = ctx['S']
        sigma_pure = ctx['sigma_pure']
        bt = ctx['beta_tilde']
        res = []
        comp_keys = ['Co', 'Cr', 'Ni']
        for i, comp in enumerate(comp_keys):
            ln_term = np.log(max(xs[comp], 1e-12) / max(xb[comp], 1e-12))
            Gibbs_b = partial_G_xs(xb, i, ctx, beta=1.0)
            Gibbs_s = partial_G_xs(xs, i, ctx, beta=bt)
            term = sigma_pure[comp] + 1000.0 * (R * T / S[comp]) * ln_term + 1000.0 * (1.0 / S[comp]) * (Gibbs_s - Gibbs_b)
            res.append(term - sigma)
        return np.array(res)

    tol_tension = step.get('tolerances', {}).get('tension_abs', 10.0)
    tol_compo = step.get('tolerances', {}).get('composition_abs', 0.02)
    tension_min = step.get('tolerances', {}).get('tension_min', 1720)
    tension_max = step.get('tolerances', {}).get('tension_max', 1850)

    rows = artifact
    N = len(rows)
    if N == 0:
        return 0.0

    ok_recompute = 0
    seg_ok = 0
    tension_vals = []
    for row in rows:
        try:
            xc = float(row['bulk_X_Cr'])
            xn = float(row['bulk_X_Ni'])
            xco = float(row['bulk_X_Co'])
        except Exception:
            continue
        bulk = {'X_Cr': xc, 'X_Ni': xn, 'X_Co': xco}
        try:
            sf_t = float(row['surface_tension_mN_per_m'])
            sf_xcr = float(row['surface_X_Cr'])
            sf_xn = float(row['surface_X_Ni'])
            sf_xco = float(row['surface_X_Co'])
        except Exception:
            continue
        tension_vals.append(sf_t)
        sigma_guess1 = (ctx['sigma_pure']['Co'] + ctx['sigma_pure']['Cr'] + ctx['sigma_pure']['Ni']) / 3.0
        initial_guesses = [
            [xc, xn, sigma_guess1],
            [0.25, 0.25, 1.8],
        ]
        sol_success = False
        for guess in initial_guesses:
            try:
                sol, info, ier, msg = fsolve(lambda X: butler_residuals(X, bulk, ctx),
                                             guess,
                                             full_output=True,
                                             maxfev=5000,
                                             xtol=1e-8)
                if ier == 1:
                    X_cr_s_opt = sol[0]
                    X_ni_s_opt = sol[1]
                    sigma_opt = sol[2]
                    if (X_cr_s_opt >= -1e-6 and X_ni_s_opt >= -1e-6
                            and sigma_opt > 0):
                        X_co_s_opt = 1.0 - X_cr_s_opt - X_ni_s_opt
                        if X_co_s_opt >= -1e-6:
                            sol_success = True
                            break
            except Exception:
                pass
        if not sol_success:
            continue
        if abs(sf_t - sigma_opt) <= tol_tension and \
           abs(sf_xcr - X_cr_s_opt) <= tol_compo and \
           abs(sf_xn - X_ni_s_opt) <= tol_compo and \
           abs(sf_xco - X_co_s_opt) <= tol_compo:
            ok_recompute += 1
        if sf_xcr > xc:
            seg_ok += 1

    recompute_score = ok_recompute / N if N > 0 else 0.0
    seg_score = seg_ok / N if N > 0 else 0.0

    min_t = min(tension_vals) if tension_vals else 0.0
    max_t = max(tension_vals) if tension_vals else 0.0
    range_ok = 1.0 if (min_t >= tension_min and max_t <= tension_max) else 0.0

    cuts = step.get('cuts', [])
    mono_score = 0.0
    if cuts:
        cut_scores = []
        for cut in cuts:
            points = cut.get('points', [])
            x_vals = []
            y_vals = []
            for pt in points:
                x_cr_pt, x_ni_pt, x_co_pt = pt
                for r in rows:
                    try:
                        if abs(float(r['bulk_X_Cr']) - x_cr_pt) < 1e-9 and \
                           abs(float(r['bulk_X_Ni']) - x_ni_pt) < 1e-9 and \
                           abs(float(r['bulk_X_Co']) - x_co_pt) < 1e-9:
                            x_vals.append(x_cr_pt)
                            y_vals.append(float(r['surface_tension_mN_per_m']))
                            break
                    except Exception:
                        continue
            if len(x_vals) >= 2:
                corr = np.corrcoef(x_vals, y_vals)[0, 1]
                if np.isnan(corr):
                    cs = 0.0
                elif corr <= -0.85:
                    cs = 1.0
                elif corr < 0.0:
                    cs = max(0.0, 1.0 + corr / 0.85)
                else:
                    cs = 0.0
                cut_scores.append(cs)
        if cut_scores:
            mono_score = sum(cut_scores) / len(cut_scores)

    w_recompute = 0.6
    w_seg = 0.15
    w_range = 0.05
    w_mono = 0.2
    total = w_recompute * recompute_score + w_seg * seg_score + w_range * range_ok + w_mono * mono_score
    return float(total)


_SCORERS = {
    'surface_properties': score_0,
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
