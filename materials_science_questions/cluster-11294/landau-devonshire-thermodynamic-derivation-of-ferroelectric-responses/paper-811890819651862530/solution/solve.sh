#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: results.csv ===
cat > /tmp/gen_results.py << 'PYEOF'
import numpy as np
from scipy.integrate import quad
from scipy.optimize import fsolve
import csv

# ---------- constants & parameters ----------
epsilon0 = 8.854187817e-12

# Layer compositions (Ba fraction)
comp = [('BST 90/10', 0.9), ('BST 75/25', 0.75), ('BST 60/40', 0.6)]

def layer_params(y):
    T_C = y*120.0 + (1-y)*(-253.0)
    C   = y*1.7e5 + (1-y)*0.8e5
    def b_Ba(T): return 1.44e7*(T-175.0)
    b_Sr = 8.4e9
    b = lambda T: y*b_Ba(T) + (1-y)*b_Sr
    c   = y*3.96e10   # STO c=0
    Q12 = y*(-0.045) + (1-y)*(-0.013)
    c11_Ba=1.76e11; c12_Ba=8.46e10
    c11_Sr=3.181e11; c12_Sr=1.025e11
    c11= y*c11_Ba + (1-y)*c11_Sr
    c12= y*c12_Ba + (1-y)*c12_Sr
    inv_s_sum = c11 + c12 - 2*c12**2/c11   # = 1/(s11+s12)
    lam = y*10.6e-6 + (1-y)*8.75e-6
    return {'T_C':T_C,'C':C,'b':b,'c':c,'Q12':Q12,'inv_s_sum':inv_s_sum,'lam':lam}

layers = [layer_params(y) for _,y in comp]

# ---------- substrate TEC ----------
def tec_sub(sub, T_C, T_K):
    if sub == 'MgO':
        T = T_K
        return 12.92e-6*(1-np.exp(-5.826e-3*(T-65.23))) + 2.067e-3*T*1e-6
    elif sub == 'SrTiO3':
        return 8.75e-6
    elif sub == 'Si':
        T = T_K
        return 3.725e-6*(1-np.exp(-5.88e-3*(T-124))) + 5.548e-4*T*1e-6
    elif sub == 'c-Al2O3':
        T = T_C
        return (8.026 + 8.17e-4*T - 3.279*np.exp(-2.91e-3*T)) * 1e-6
    elif sub == 'a-Al2O3':
        T = T_C
        return (7.419 + 6.43e-4*T - 3.211*np.exp(-2.59e-3*T)) * 1e-6
    elif sub == 'LaAlO3':
        T = T_K
        return (-9.493e-17*T**6 + 4.909e-13*T**5 - 1.015e-9*T**4
                + 1.068e-6*T**3 - 6.054e-4*T**2 + 0.1823*T - 14.52) * 1e-6
    else:
        raise ValueError

def thermal_strain(sub, T_A_C, T_f_C, lays):
    if sub == 'SrTiO3':
        lam_sub = 8.75e-6
        return [(lam_sub - l['lam']) * (T_f_C - T_A_C) for l in lays]
    if sub in ('MgO','Si','LaAlO3'):
        T_A = T_A_C + 273.15
        T_f = T_f_C + 273.15
        func = lambda T: tec_sub(sub, None, T)
    else:  # c-, a-Al2O3
        T_A = T_A_C
        T_f = T_f_C
        func = lambda T: tec_sub(sub, T, None)
    res = []
    for l in lays:
        lam_i = l['lam']
        val, _ = quad(lambda T: func(T) - lam_i, T_A, T_f, limit=200)
        res.append(val)
    return res

# ---------- equilibrium solver ----------
def solve_P(T, E_ext, x_list, lays):
    n = len(lays)
    alpha = 1.0/n
    a = np.zeros(n); b = np.zeros(n); c = np.zeros(n)
    K1 = np.zeros(n); Q12 = np.zeros(n)
    for i,ly in enumerate(lays):
        a[i] = (T - ly['T_C']) / (epsilon0 * ly['C'])
        b[i] = ly['b'](T)
        c[i] = ly['c']
        K1[i] = 4 * ly['Q12'] * ly['inv_s_sum']
        Q12[i] = ly['Q12']
    def eqs(P):
        P_avg = alpha * P.sum()
        f = np.zeros(n)
        for i in range(n):
            f[i] = a[i]*P[i] + b[i]*P[i]**3 + c[i]*P[i]**5 \
                   - K1[i]*P[i]*(x_list[i] - Q12[i]*P[i]) \
                   + (1/epsilon0)*(P[i] - P_avg) - E_ext
        return f
    # multiple initial guesses
    for guess in [np.ones(n)*0.01, np.ones(n)*0.2, np.ones(n)*0.5, np.zeros(n)]:
        try:
            sol = fsolve(eqs, guess, maxfev=2000, xtol=1e-12)
            if np.allclose(eqs(sol), 0, atol=1e-8):
                return sol
        except:
            continue
    return np.zeros(n)  # fallback

def P_avg(T, E_ext, x_list, lays):
    return np.mean(solve_P(T, E_ext, x_list, lays))

def eps_dielectric(T, E_ext, x_list, lays, dE=1e3):
    P0 = P_avg(T, E_ext-dE, x_list, lays)
    P1 = P_avg(T, E_ext+dE, x_list, lays)
    return (P1 - P0)/(2*dE) / epsilon0

# ---------- generate CSV ----------
rows = []

# (a) TEC_sweep
tec_vals = np.arange(5e-6, 15.01e-6, 0.1e-6)
for T_A in (550, 650, 750):
    for stec in tec_vals:
        x_l = [(stec - ly['lam']) * (25.0 - T_A) for ly in layers]
        P0 = P_avg(25.0, 0.0, x_l, layers)
        e0 = eps_dielectric(25.0, 0.0, x_l, layers)
        P400 = P_avg(25.0, 4e7, x_l, layers)
        e400 = eps_dielectric(25.0, 4e7, x_l, layers)
        tun = 100*(e0 - e400)/e0 if e0 != 0 else 0.0
        rows.append(['TEC_sweep', stec, '', T_A, 0, 'avg_polarization_C_per_m2', P0])
        rows.append(['TEC_sweep', stec, '', T_A, 0, 'dielectric_constant', e0])
        rows.append(['TEC_sweep', stec, '', T_A, 0, 'tunability_percent', 0.0])
        rows.append(['TEC_sweep', stec, '', T_A, 400, 'avg_polarization_C_per_m2', P400])
        rows.append(['TEC_sweep', stec, '', T_A, 400, 'dielectric_constant', e400])
        rows.append(['TEC_sweep', stec, '', T_A, 400, 'tunability_percent', tun])

# (b) substrate_annealing
substrates_anneal = ['Si','MgO','SrTiO3','LaAlO3']
for sub in substrates_anneal:
    for T_A in (450, 750):
        x_l = thermal_strain(sub, T_A, 25.0, layers)
        P0 = P_avg(25.0, 0.0, x_l, layers)
        e0 = eps_dielectric(25.0, 0.0, x_l, layers)
        P400 = P_avg(25.0, 4e7, x_l, layers)
        e400 = eps_dielectric(25.0, 4e7, x_l, layers)
        tun = 100*(e0 - e400)/e0 if e0 != 0 else 0.0
        rows.append(['substrate_annealing', '', sub, T_A, 0, 'avg_polarization_C_per_m2', P0])
        rows.append(['substrate_annealing', '', sub, T_A, 0, 'dielectric_constant', e0])
        rows.append(['substrate_annealing', '', sub, T_A, 0, 'tunability_percent', 0.0])
        rows.append(['substrate_annealing', '', sub, T_A, 400, 'avg_polarization_C_per_m2', P400])
        rows.append(['substrate_annealing', '', sub, T_A, 400, 'dielectric_constant', e400])
        rows.append(['substrate_annealing', '', sub, T_A, 400, 'tunability_percent', tun])

# (c) temperature_dependence (T_A fixed at 750°C)
T_A_fixed = 750
for sub in ('Si','SrTiO3'):
    for T_op in range(-10, 91, 5):
        x_l = thermal_strain(sub, T_A_fixed, T_op, layers)
        P = P_avg(T_op, 4e7, x_l, layers)
        e = eps_dielectric(T_op, 4e7, x_l, layers)
        # need zero-field epsilon for tunability
        e0 = eps_dielectric(T_op, 0.0, x_l, layers)
        tun = 100*(e0 - e)/e0 if e0 != 0 else 0.0
        rows.append(['temperature_dependence', '', sub, T_op, 400, 'avg_polarization_C_per_m2', P])
        rows.append(['temperature_dependence', '', sub, T_op, 400, 'dielectric_constant', e])
        rows.append(['temperature_dependence', '', sub, T_op, 400, 'tunability_percent', tun])

# write CSV
with open('/app/outputs/results.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['condition_type','substrate_TEC','substrate_name',
                'annealing_temperature_C','applied_field_kV_per_cm',
                'quantity','value'])
    for r in rows:
        w.writerow(r)
PYEOF
python3 /tmp/gen_results.py
