#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: phase_diagram_data.json ===
python3 <<'PYEOF'
import numpy as np
from scipy.optimize import fsolve
import json, os

def safe_log(x):
    if x <= 0 or x >= 1:
        return 0.0
    return x * np.log(x)

def phi(t, c, Pi, Lambda, eta_c, eta_cc):
    eps = eta_c * c + 0.5 * eta_cc * c**2
    term1 = t * (safe_log(c) + safe_log(1 - c)) if 0 < c < 1 else 0.0
    return term1 + 2 * c * (1 - c) - 4.5 * Pi**2 + 3 * np.sqrt(Lambda) * eps * Pi

def dphi_dc(t, c, Pi, Lambda, eta_c, eta_cc):
    # derivative of 2*c*(1-c) is 2 - 4*c (was previously 4 - 8*c)
    return t * np.log(c / (1 - c)) + 2 - 4*c + 3 * np.sqrt(Lambda) * Pi * (eta_c + eta_cc * c)

def dphi_dPi(t, c, Pi, Lambda, eta_c, eta_cc):
    eps = eta_c * c + 0.5 * eta_cc * c**2
    return -9 * Pi + 3 * np.sqrt(Lambda) * eps

def omega(t, c, Pi, Lambda, eta_c, eta_cc):
    M = dphi_dc(t, c, Pi, Lambda, eta_c, eta_cc)
    dP = dphi_dPi(t, c, Pi, Lambda, eta_c, eta_cc)
    return phi(t, c, Pi, Lambda, eta_c, eta_cc) - M * c - Pi * dP

def spinodal(c, Lambda, eta_c, eta_cc, Pi):
    return c * (1 - c) * (4 - Lambda * (eta_c + eta_cc * c)**2 - 3 * eta_cc * np.sqrt(Lambda) * Pi)

def critical_equations(vars, Lambda, eta_c, eta_cc, Pi):
    t, c = vars
    s = spinodal(c, Lambda, eta_c, eta_cc, Pi)
    crit = (c * (1 - c))**2 / (1 - 2 * c) * 3 * Lambda * eta_cc * (eta_c + eta_cc * c)
    return [s - t, crit - t]

def make_eq_left(t, Pi_o, Lambda, eta_c, eta_cc):
    def eq_left(vars):
        c_a, c_b, Pi_b = vars
        M_a = dphi_dc(t, c_a, Pi_o, Lambda, eta_c, eta_cc)
        M_b = dphi_dc(t, c_b, Pi_b, Lambda, eta_c, eta_cc)
        dP_a = dphi_dPi(t, c_a, Pi_o, Lambda, eta_c, eta_cc)
        dP_b = dphi_dPi(t, c_b, Pi_b, Lambda, eta_c, eta_cc)
        oa = omega(t, c_a, Pi_o, Lambda, eta_c, eta_cc)
        ob = omega(t, c_b, Pi_b, Lambda, eta_c, eta_cc)
        return [M_a - M_b, dP_a - dP_b, oa - ob]
    return eq_left

def make_eq_right(t, Pi_o, Lambda, eta_c, eta_cc):
    def eq_right(vars):
        c_a, Pi_a, c_b = vars
        M_a = dphi_dc(t, c_a, Pi_a, Lambda, eta_c, eta_cc)
        M_b = dphi_dc(t, c_b, Pi_o, Lambda, eta_c, eta_cc)
        dP_a = dphi_dPi(t, c_a, Pi_a, Lambda, eta_c, eta_cc)
        dP_b = dphi_dPi(t, c_b, Pi_o, Lambda, eta_c, eta_cc)
        oa = omega(t, c_a, Pi_a, Lambda, eta_c, eta_cc)
        ob = omega(t, c_b, Pi_o, Lambda, eta_c, eta_cc)
        return [M_a - M_b, dP_a - dP_b, oa - ob]
    return eq_right

def make_five_eq(t, Pi_o, c_o, Lambda, eta_c, eta_cc):
    def five_eq(vars):
        c_a, c_b, Pi_a, Pi_b, z = vars
        M_a = dphi_dc(t, c_a, Pi_a, Lambda, eta_c, eta_cc)
        M_b = dphi_dc(t, c_b, Pi_b, Lambda, eta_c, eta_cc)
        dP_a = dphi_dPi(t, c_a, Pi_a, Lambda, eta_c, eta_cc)
        dP_b = dphi_dPi(t, c_b, Pi_b, Lambda, eta_c, eta_cc)
        oa = omega(t, c_a, Pi_a, Lambda, eta_c, eta_cc)
        ob = omega(t, c_b, Pi_b, Lambda, eta_c, eta_cc)
        eq1 = M_a - M_b
        eq2 = dP_a - dP_b
        eq3 = oa - ob
        eq4 = Pi_o - (z * Pi_b + (1 - z) * Pi_a)
        eq5 = c_o - (z * c_b + (1 - z) * c_a)
        return [eq1, eq2, eq3, eq4, eq5]
    return five_eq

def trace_binodal(Lambda, eta_c, eta_cc, Pi_o, t_start, t_end, n_pts=60):
    ts = np.linspace(t_start, t_end, n_pts)
    c_a_list = []
    c_b_list = []
    t_list = []
    guess_left = [0.1, 0.9, Pi_o]
    guess_right = [0.1, Pi_o, 0.9]
    for t in ts:
        try:
            sl = fsolve(make_eq_left(t, Pi_o, Lambda, eta_c, eta_cc), guess_left, maxfev=2000, factor=0.1)
            c_a, _, _ = sl
            if not (0.01 < c_a < 0.99):
                continue
            sr = fsolve(make_eq_right(t, Pi_o, Lambda, eta_c, eta_cc), guess_right, maxfev=2000, factor=0.1)
            _, _, c_b = sr
            if not (0.01 < c_b < 0.99):
                continue
            c_a_list.append(c_a)
            c_b_list.append(c_b)
            t_list.append(t)
            guess_left = sl
            guess_right = sr
        except Exception:
            continue
    return np.array(t_list), np.array(c_a_list), np.array(c_b_list)

param_sets = [
    ('L100_eta_c_-0.05_eta_cc_0.04', 100, -0.05, 0.04),
    ('L100_eta_c_-0.03_eta_cc_0',   100, -0.03, 0.0),
    ('L100_eta_c_-0.01_eta_cc_-0.04', 100, -0.01, -0.04),
    ('L350_eta_c_-0.05_eta_cc_0.05', 350, -0.05, 0.05)
]

Pi_ref = 0.1
results = {}

for key, L, ec, ecc in param_sets:
    Lambda = L
    eta_c = ec
    eta_cc = ecc

    cs = np.linspace(0.001, 0.999, 300)
    t_spin = spinodal(cs, Lambda, eta_c, eta_cc, Pi_ref)
    mask = t_spin > 0
    spinodal_pts = {'t': t_spin[mask].tolist(), 'c': cs[mask].tolist()}

    if eta_cc == 0:
        c_c = 0.5
        t_c = 1.0 - Lambda * eta_c**2 / 4.0
    else:
        guess_c = 0.4 if eta_cc * (eta_c + 0.5*eta_cc) > 0 else 0.6
        guess_t = spinodal(guess_c, Lambda, eta_c, eta_cc, Pi_ref)
        try:
            t_c, c_c = fsolve(lambda v: critical_equations(v, Lambda, eta_c, eta_cc, Pi_ref),
                              [guess_t, guess_c], maxfev=2000, factor=0.1)
        except Exception:
            t_c, c_c = 1.0, 0.5
    crit_pt = {'t_c': float(t_c), 'c_c': float(c_c)}

    t_min = 0.01
    t_max_use = max(t_c - 0.01, t_min + 0.01)
    t_arr, c_a_arr, c_b_arr = trace_binodal(Lambda, eta_c, eta_cc, Pi_ref, t_min, t_max_use, 60)
    order = np.argsort(t_arr)
    pb = { 't': t_arr[order].tolist(),
           'c_alpha': c_a_arr[order].tolist(),
           'c_beta': c_b_arr[order].tolist() }

    t_tie = 0.8
    try:
        gg_l = fsolve(make_eq_left(t_tie, Pi_ref, Lambda, eta_c, eta_cc), [0.25, 0.75, Pi_ref], maxfev=2000)
        gg_r = fsolve(make_eq_right(t_tie, Pi_ref, Lambda, eta_c, eta_cc), [0.25, Pi_ref, 0.75], maxfev=2000)
        c_a_ref = gg_l[0]
        c_b_ref = gg_r[2]
    except Exception:
        c_a_ref = 0.3
        c_b_ref = 0.7

    c_o_vals = np.linspace(c_a_ref + 0.02, c_b_ref - 0.02, 20)
    tie_lines = []
    for c_o in c_o_vals:
        guess_z = (c_b_ref - c_o) / (c_b_ref - c_a_ref)
        guess = [c_a_ref, c_b_ref, Pi_ref, Pi_ref, guess_z]
        try:
            sol = fsolve(make_five_eq(t_tie, Pi_ref, c_o, Lambda, eta_c, eta_cc),
                         guess, maxfev=2000, factor=0.1)
            c_a_s, c_b_s, Pi_a_s, Pi_b_s, z_s = sol
            if 0.01 < z_s < 0.99 and c_a_s < c_b_s:
                tie_lines.append({'c_alpha': float(c_a_s), 'Pi_alpha': float(Pi_a_s),
                                  'c_beta': float(c_b_s), 'Pi_beta': float(Pi_b_s)})
        except Exception:
            pass

    t_eff = 0.8
    Pi_ls = np.linspace(0.0, 0.5, 30)
    gap = []
    for Pi in Pi_ls:
        try:
            sl = fsolve(make_eq_left(t_eff, Pi, Lambda, eta_c, eta_cc), [0.2, 0.8, Pi], maxfev=2000)
            sr = fsolve(make_eq_right(t_eff, Pi, Lambda, eta_c, eta_cc), [0.2, Pi, 0.8], maxfev=2000)
            if sl[0] < sr[2]:
                gap.append(float(sr[2] - sl[0]))
            else:
                gap.append(float('nan'))
        except Exception:
            gap.append(float('nan'))

    results[key] = {
        'critical_point': crit_pt,
        'phase_boundary_at_Pi_0_1': pb,
        'spinodal_at_Pi_0_1': spinodal_pts,
        'tie_lines_at_t_0_8': tie_lines,
        'effect_of_Pi': {'t': t_eff, 'Pi': Pi_ls.tolist(), 'gap_width': gap}
    }

outdir = os.environ.get('OUTDIR', '/app/outputs')
with open(os.path.join(outdir, 'phase_diagram_data.json'), 'w') as f:
    json.dump(results, f, indent=2)
print('phase_diagram_data.json written')
PYEOF

# === solve finalize ===
echo "Oracle complete."
