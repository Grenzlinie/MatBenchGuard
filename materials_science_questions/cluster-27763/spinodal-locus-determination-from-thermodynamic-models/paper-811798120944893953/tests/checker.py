import os
import json
import csv

# === author imports / helpers ===
# helper imports used by prepare and scorers
import numpy as np
from scipy.special import erfc
import math

def debye(k, N, Rg):
    x = k * Rg
    res = np.ones_like(k) * N
    mask = x > 1e-12
    xm = x[mask]
    res[mask] = 2*N * (np.exp(-xm**2) - 1 + xm**2) / (xm**4)
    return res

def inv_sine(h_k, k, r):
    """Inverse sine transform: (1/(2π² r)) ∫ k sin(kr) h_k dk"""
    integrand_base = k * h_k
    vals = np.zeros_like(r)
    for i, ri in enumerate(r):
        sin_kr = np.sin(k * ri)
        # use trapezoidal integration on the k-array
        integral = np.trapz(integrand_base * sin_kr, k)
        vals[i] = integral / (2 * np.pi**2 * ri)
    return vals

# Bhatia-Thornton S_phi_phi from h_cc table used in structure_factor scorer
def compute_S_phi_phi(k_vals, r_arr, hAA, hAB, hBB, phi, rho_ch):
    """Compute concentration fluctuation structure factor for given k values."""
    N = len(k_vals)
    S_phi_phi = np.zeros(N)
    for idx, k in enumerate(k_vals):
        kr = k * r_arr
        mask = kr > 1e-12
        sinc = np.ones_like(kr)
        sinc[mask] = np.sin(kr[mask]) / kr[mask]
        integ_AA = r_arr**2 * sinc * hAA
        integ_BB = r_arr**2 * sinc * hBB
        integ_AB = r_arr**2 * sinc * hAB
        S_AA = phi + 4*np.pi * phi**2 * rho_ch * np.trapz(integ_AA, r_arr)
        S_BB = (1-phi) + 4*np.pi * (1-phi)**2 * rho_ch * np.trapz(integ_BB, r_arr)
        S_AB = 4*np.pi * phi * (1-phi) * rho_ch * np.trapz(integ_AB, r_arr)
        S_phi_phi[idx] = (1-phi)**2 * S_AA + phi**2 * S_BB - 2*phi*(1-phi)*S_AB
    return S_phi_phi


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
    # Precompute analytical reference curves for h_cc and effective potentials
    import numpy as np
    from math import sqrt, pi

    # System parameters (hhPP/PE blend from paper Table 1)
    N = 96
    RgA = 12.32          # Å
    gamma = 1.34
    rho = 0.0332          # sites/Å³
    phi = 0.5

    sigma_A = RgA / sqrt(N/6.0)
    sigma_B = gamma * sigma_A
    sigma_AB2 = phi * sigma_B**2 + (1-phi) * sigma_A**2   # actually 0.5*(sigma_A^2+sigma_B^2)
    sigma_A2 = sigma_A**2
    sigma_B2 = sigma_B**2

    chi_s = 1.0/(2*N*phi) + 1.0/(2*N*(1-phi))   # ~0.0208333

    RgB = sqrt(N/6.0) * sigma_B
    xi_cA = RgA / sqrt(2)
    xi_cB = RgB / sqrt(2)

    # Correlation hole length for AB pair
    xi_c_AB = sqrt((RgA**2 + RgB**2) / 8.0)

    # Density correlation lengths for each pair
    xi_rho_AA_inv = pi*rho*sigma_A2/3.0 + 1.0/xi_cA
    xi_rho_AA = 1.0/xi_rho_AA_inv

    xi_rho_BB_inv = pi*rho*sigma_B2/3.0 + 1.0/xi_cB
    xi_rho_BB = 1.0/xi_rho_BB_inv

    xi_rho_AB_inv = pi*rho*sigma_AB2/3.0 + 1.0/xi_c_AB
    xi_rho_AB = 1.0/xi_rho_AB_inv

    # Wavevector grid for discrete transforms (log-spaced for accuracy)
    k_max = 10.0
    nk = 2048
    k_arr = np.logspace(np.log10(1e-4), np.log10(k_max), nk)

    # Real-space output grid
    r_max = 40.0
    nr = 200
    r_arr = np.linspace(0.1, r_max, nr)

    chi_ratios = {'athermal': 0.0, 'chi0.1': 0.1, 'chi0.5': 0.5, 'chi0.7': 0.7}
    curves = {}

    # Form factors precomputed (independent of chi)
    omega_cm_A = N * np.exp(-k_arr**2 * RgA**2 / 6.0)
    omega_cm_B = N * np.exp(-k_arr**2 * RgB**2 / 6.0)
    omega_mm_A = debye(k_arr, N, RgA)
    omega_mm_B = debye(k_arr, N, RgB)

    for cond, crat in chi_ratios.items():
        # xi_phi for this reduced temperature
        denom = 24 * phi * (1-phi) * chi_s * (1.0 - crat)
        if denom <= 0:
            xi_phi = 1e6   # very large, avoid divergence
        else:
            xi_phi = sqrt(sigma_AB2 / denom)   # sigma_AB = length, so sqrt ok
        xi_phi2 = xi_phi**2

        # Compute monomer-level h_mm(k) for the three pairs
        def h_mm_AA_k(k):
            pref = 12.0 / (rho * sigma_AB2)
            t1 = (1-phi)/phi / (k**2 + 1.0/xi_phi2)
            t2 = gamma**2 / (k**2 + 1.0/xi_rho_AA**2)
            t3 = -(1.0/phi) * (sigma_AB2/sigma_A2) / (k**2 + 1.0/xi_cA**2)
            return pref * (t1 + t2 + t3)

        def h_mm_BB_k(k):
            pref = 12.0 / (rho * sigma_AB2)
            t1 = phi/(1-phi) / (k**2 + 1.0/xi_phi2)
            t2 = gamma**-2 / (k**2 + 1.0/xi_rho_BB**2)
            t3 = -(1.0/(1-phi)) * (sigma_AB2/sigma_B2) / (k**2 + 1.0/xi_cB**2)
            return pref * (t1 + t2 + t3)

        def h_mm_AB_k(k):
            pref = 12.0 / (rho * sigma_AB2)
            t1 = -1.0 / (k**2 + 1.0/xi_phi2)
            t2 = 1.0 / (k**2 + 1.0/xi_rho_AB**2)
            return pref * (t1 + t2)

        hAAk = h_mm_AA_k(k_arr)
        hBBk = h_mm_BB_k(k_arr)
        hABk = h_mm_AB_k(k_arr)

        # Map to center-of-mass level (eq 3)
        hAA_cc = (omega_cm_A / omega_mm_A) * hAAk
        hBB_cc = (omega_cm_B / omega_mm_B) * hBBk
        hAB_cc = (omega_cm_B / omega_mm_B) * hABk   # eq 3 for AB

        # Inverse sine transform to real space (using np.trapezoid instead of deprecated np.trapz)
        def inv_sine_fixed(h_k, k, r):
            integrand_base = k * h_k
            vals = np.zeros_like(r)
            for i, ri in enumerate(r):
                sin_kr = np.sin(k * ri)
                integral = np.trapezoid(integrand_base * sin_kr, k)
                vals[i] = integral / (2 * np.pi**2 * ri)
            return vals

        hAA_r = inv_sine_fixed(hAA_cc, k_arr, r_arr)
        hBB_r = inv_sine_fixed(hBB_cc, k_arr, r_arr)
        hAB_r = inv_sine_fixed(hAB_cc, k_arr, r_arr)

        curves[cond] = {
            'r': r_arr.copy(),
            'h_AA': hAA_r,
            'h_AB': hAB_r,
            'h_BB': hBB_r
        }

        # --- Effective potentials via HNC ---
        rho_ch = rho / N
        S_AA = phi + phi**2 * rho_ch * hAA_cc
        S_BB = (1-phi) + (1-phi)**2 * rho_ch * hBB_cc
        S_AB = phi * (1-phi) * rho_ch * hAB_cc
        det = np.maximum(S_AA * S_BB - S_AB**2, 1e-30)

        rho_cA = phi * rho / N
        rho_cB = (1-phi) * rho / N
        rho_total_c = rho_cA + rho_cB

        c_AA_k = 1.0/rho_cA - S_BB / (rho_total_c * det)
        c_BB_k = 1.0/rho_cB - S_AA / (rho_total_c * det)
        c_AB_k = S_AB / (rho_total_c * det)

        # Use the same fixed inv_sine for direct correlation functions
        c_AA_r = inv_sine_fixed(c_AA_k, k_arr, r_arr)
        c_BB_r = inv_sine_fixed(c_BB_k, k_arr, r_arr)
        c_AB_r = inv_sine_fixed(c_AB_k, k_arr, r_arr)

        # HNC closure (eq 13): v = h - ln(1+h) - c
        log_arg_AA = np.maximum(1.0 + hAA_r, 1e-12)
        v_AA = hAA_r - np.log(log_arg_AA) - c_AA_r
        log_arg_BB = np.maximum(1.0 + hBB_r, 1e-12)
        v_BB = hBB_r - np.log(log_arg_BB) - c_BB_r
        log_arg_AB = np.maximum(1.0 + hAB_r, 1e-12)
        v_AB = hAB_r - np.log(log_arg_AB) - c_AB_r

        curves[cond]['v_AA'] = v_AA
        curves[cond]['v_AB'] = v_AB
        curves[cond]['v_BB'] = v_BB

    return {
        'curves': curves,
        'outputs_dir': '/app/outputs',
        'params': {'N':N, 'rho':rho, 'phi':phi, 'RgA':RgA}
    }


# === block: score_0 (check id='analytical_hcc') ===
def score_0(artifact, step, ctx):
    import numpy as np

    curves = ctx['curves']
    tol_rel = step['tolerance']['rel_tol']
    tol_abs = step['tolerance']['abs_floor']
    conditions = ['athermal', 'chi0.1', 'chi0.5', 'chi0.7']
    scores = []

    for cond in conditions:
        exp = curves.get(cond)
        if exp is None:
            scores.append(0.0)
            continue
        rows = [row for row in artifact if row.get('condition') == cond]
        if not rows:
            scores.append(0.0)
            continue
        r_agent = np.array([float(row['r']) for row in rows])
        hAA_agent = np.array([float(row['h_AA']) for row in rows])
        hAB_agent = np.array([float(row['h_AB']) for row in rows])
        hBB_agent = np.array([float(row['h_BB']) for row in rows])

        hAA_exp = np.interp(r_agent, exp['r'], exp['h_AA'])
        hAB_exp = np.interp(r_agent, exp['r'], exp['h_AB'])
        hBB_exp = np.interp(r_agent, exp['r'], exp['h_BB'])

        # pointwise weighted relative L1 error
        denom = np.abs(hAA_exp) + np.abs(hAB_exp) + np.abs(hBB_exp) + tol_abs
        err_point = (np.abs(hAA_agent - hAA_exp) + np.abs(hAB_agent - hAB_exp) + np.abs(hBB_agent - hBB_exp)) / denom
        avg_err = np.mean(err_point)

        if avg_err <= tol_rel:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (avg_err - tol_rel) / (2.0 * tol_rel)))

    return np.mean(scores) if scores else 0.0


# === block: score_1 (check id='effective_potentials') ===
def score_1(artifact, step, ctx):
    import numpy as np

    curves = ctx['curves']
    tol_rel = step['tolerance']['rel_tol']
    tol_abs = step['tolerance']['abs_floor']
    conditions = ['athermal', 'chi0.1', 'chi0.5', 'chi0.7']
    scores = []

    for cond in conditions:
        exp = curves.get(cond)
        if exp is None:
            scores.append(0.0)
            continue
        rows = [row for row in artifact if row.get('condition') == cond]
        if not rows:
            scores.append(0.0)
            continue
        r_agent = np.array([float(row['r']) for row in rows])
        vAA_agent = np.array([float(row['v_AA']) for row in rows])
        vAB_agent = np.array([float(row['v_AB']) for row in rows])
        vBB_agent = np.array([float(row['v_BB']) for row in rows])

        vAA_exp = np.interp(r_agent, exp['r'], exp['v_AA'])
        vAB_exp = np.interp(r_agent, exp['r'], exp['v_AB'])
        vBB_exp = np.interp(r_agent, exp['r'], exp['v_BB'])

        denom = np.abs(vAA_exp) + np.abs(vAB_exp) + np.abs(vBB_exp) + tol_abs
        err_point = (np.abs(vAA_agent - vAA_exp) + np.abs(vAB_agent - vAB_exp) + np.abs(vBB_agent - vBB_exp)) / denom
        avg_err = np.mean(err_point)

        if avg_err <= tol_rel:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (avg_err - tol_rel) / (2.0 * tol_rel)))

    return np.mean(scores) if scores else 0.0


# === block: score_2 (check id='md_simulation_athermal') ===
def score_2(artifact, step, ctx):
    import numpy as np

    curves = ctx['curves']
    exp = curves['athermal']
    rows = artifact
    if not rows:
        return 0.0
    r_agent = np.array([float(row['r']) for row in rows])
    hAA_sim = np.array([float(row['h_AA_sim']) for row in rows])
    hAB_sim = np.array([float(row['h_AB_sim']) for row in rows])
    hBB_sim = np.array([float(row['h_BB_sim']) for row in rows])

    hAA_exp = np.interp(r_agent, exp['r'], exp['h_AA'])
    hAB_exp = np.interp(r_agent, exp['r'], exp['h_AB'])
    hBB_exp = np.interp(r_agent, exp['r'], exp['h_BB'])

    r_min = step['tolerance']['r_min']
    mask = r_agent > r_min
    if not np.any(mask):
        return 0.0

    max_err = max(
        np.max(np.abs(hAA_sim[mask] - hAA_exp[mask])),
        np.max(np.abs(hAB_sim[mask] - hAB_exp[mask])),
        np.max(np.abs(hBB_sim[mask] - hBB_exp[mask]))
    )
    tol = step['tolerance']['abs_tol']

    score = max(0.0, 1.0 - max_err / tol) if tol > 0 else 0.0
    return score


# === block: score_3 (check id='structure_factor') ===
def score_3(artifact, step, ctx):
    import csv, os, numpy as np
    from math import pi

    outputs_dir = ctx['outputs_dir']
    params = ctx['params']
    phi = params['phi']
    rho_ch = params['rho'] / params['N']

    hcc_path = os.path.join(outputs_dir, 'analytical_hcc.csv')
    if not os.path.exists(hcc_path):
        return 0.0

    with open(hcc_path, newline='') as f:
        reader = csv.DictReader(f)
        hcc_data = list(reader)

    tol_rel = step['tolerance']['rel_tol']
    abs_floor = step['tolerance']['abs_floor']
    conditions = set(row['condition'] for row in artifact if row.get('condition'))
    scores = []

    for cond in conditions:
        sf_rows = [row for row in artifact if row.get('condition') == cond]
        if not sf_rows:
            continue
        hcc_rows = [row for row in hcc_data if row.get('condition') == cond]
        if not hcc_rows:
            scores.append(0.0)
            continue

        r_vals = np.array([float(row['r']) for row in hcc_rows])
        hAA = np.array([float(row['h_AA']) for row in hcc_rows])
        hAB = np.array([float(row['h_AB']) for row in hcc_rows])
        hBB = np.array([float(row['h_BB']) for row in hcc_rows])

        k_vals = np.array([float(row['k']) for row in sf_rows])
        S_phi_phi_agent = np.array([float(row['S_phi_phi']) for row in sf_rows])

        # recompute S_phi_phi from h_cc using the Bhatia-Thornton integral
        S_phi_phi_calc = compute_S_phi_phi(k_vals, r_vals, hAA, hAB, hBB, phi, rho_ch)

        max_S = np.max(np.abs(S_phi_phi_calc))
        if max_S < 1e-12:
            scores.append(1.0 if np.max(np.abs(S_phi_phi_agent)) < 1e-3 else 0.0)
            continue

        rel_err = np.max(np.abs(S_phi_phi_agent - S_phi_phi_calc)) / (max_S + abs_floor)
        if rel_err <= tol_rel:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (rel_err - tol_rel) / tol_rel))

    return np.mean(scores) if scores else 0.0


_SCORERS = {
    'analytical_hcc': score_0,
    'effective_potentials': score_1,
    'md_simulation_athermal': score_2,
    'structure_factor': score_3,
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
