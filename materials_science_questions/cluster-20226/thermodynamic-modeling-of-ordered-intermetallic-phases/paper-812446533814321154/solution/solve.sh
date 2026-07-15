#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy numpy
mkdir -p /app/outputs

# === solve block: occupation_and_intensity.csv ===
python3 << 'PYEOF' > "$OUTDIR/occupation_and_intensity.csv"
import numpy as np
from scipy.optimize import minimize, Bounds
from scipy.interpolate import CubicSpline
import warnings
warnings.filterwarnings('ignore')

V = 1.22
# Energy per cluster configuration (i for A, j for B, k for C) - pair only
E = np.zeros(8)
for idx in range(8):
    i = (idx >> 2) & 1
    j = (idx >> 1) & 1
    k = idx & 1
    E[idx] = i*j*1.0 + i*k*V + j*k*V

i_arr = np.array([(idx>>2)&1 for idx in range(8)])
j_arr = np.array([(idx>>1)&1 for idx in range(8)])
k_arr = np.array([idx&1 for idx in range(8)])

def independent_rho(PA, PB, PC):
    rho = np.where(i_arr, PA, 1-PA) * np.where(j_arr, PB, 1-PB) * np.where(k_arr, PC, 1-PC)
    return rho / rho.sum()

def eq_constraint(x, theta):
    rho = x[:8]
    PA, PB, PC = x[8], x[9], x[10]
    PA_calc = rho[i_arr==1].sum()
    PB_calc = rho[j_arr==1].sum()
    PC_calc = rho[k_arr==1].sum()
    return np.array([rho.sum() - 1.0,
                     PA - PA_calc,
                     PB - PB_calc,
                     PC - PC_calc,
                     (PA+PB+PC)/3.0 - theta])

def obj_fun(x, tau):
    rho = x[:8]
    log_rho = np.where(rho>1e-15, np.log(rho), 0.0)
    ent = np.dot(rho, log_rho)
    en = np.dot(E, rho)
    return en + tau * ent

def random_start(theta):
    for _ in range(50):
        PA = np.random.rand()
        PB = np.random.rand()
        PC = 3*theta - PA - PB
        if 0 <= PC <= 1:
            break
    else:
        PA = PB = PC = theta
    rho0 = independent_rho(PA, PB, PC)
    return np.concatenate([rho0, [PA, PB, PC]])

def solve_one(theta, tau, x0=None, n_starts=8):
    bounds = Bounds([1e-12]*8 + [0,0,0], [1]*8 + [1,1,1])
    cons = {'type': 'eq', 'fun': eq_constraint, 'args': (theta,)}
    if x0 is not None:
        starts = [x0] + [random_start(theta) for _ in range(max(0, n_starts-1))]
    else:
        starts = [random_start(theta) for _ in range(n_starts)]
    best_fun = np.inf
    best_x = None
    for x0i in starts:
        try:
            res = minimize(obj_fun, x0i, args=(tau,), method='SLSQP',
                           bounds=bounds, constraints=cons,
                           options={'maxiter': 2000, 'ftol': 1e-14})
            if res.success and res.fun < best_fun:
                best_fun = res.fun
                best_x = res.x
        except:
            continue
    if best_x is None:
        x0f = np.concatenate([independent_rho(theta, theta, theta), [theta]*3])
        try:
            res = minimize(obj_fun, x0f, args=(tau,), method='SLSQP', bounds=bounds, constraints=cons)
            if res.success:
                best_x = res.x
        except:
            pass
    if best_x is None:
        return theta, theta, theta, 0.0, None
    PA, PB, PC = best_x[8], best_x[9], best_x[10]
    I = ((PA - PB)/2.0 - PC)**2
    return PA, PB, PC, I, best_x

# Phase 1: estimate energy scale by matching Tc_max = 270 K
theta_coarse = np.linspace(0.15, 0.70, 12)
tau_vals = np.linspace(0.05, 3.0, 100)
tau_c_list = []
for th in theta_coarse:
    x0 = None
    I_vals = []
    taus_used = []
    for tau in reversed(tau_vals):
        _, _, _, I, x = solve_one(th, tau, x0=x0, n_starts=5)
        I_vals.append(I)
        taus_used.append(tau)
        if x is not None:
            x0 = x
    taus_used = np.array(taus_used[::-1])
    I_vals = np.array(I_vals[::-1])
    try:
        cs = CubicSpline(taus_used, I_vals)
        d2 = cs.derivative(2)(taus_used)
        signs = np.sign(d2)
        cross = np.where(np.diff(signs) != 0)[0]
        for ci in cross:
            if I_vals[ci] > 1e-5 and I_vals[ci+1] < I_vals[ci]:
                tau_c_list.append(taus_used[ci])
                break
    except:
        pass

if tau_c_list:
    tau_c_max = max(tau_c_list)
    T0 = 270.0 / tau_c_max
else:
    T0 = 270.0

# Phase 2: produce the required CSV
theta_vals = np.arange(0.10, 0.76, 0.05)
T_vals = np.arange(50, 310, 10)

rows = []
for th in theta_vals:
    x0 = None
    for T in sorted(T_vals, reverse=True):
        tau = T / T0
        PA, PB, PC, I, x = solve_one(th, tau, x0=x0, n_starts=5)
        if x is not None:
            x0 = x
        I = max(I, 0.0)
        rows.append((th, T, PA, PB, PC, I))

# Write in ascending theta and T order
rows.sort(key=lambda r: (r[0], r[1]))
with open('/app/outputs/occupation_and_intensity.csv', 'w') as f:
    f.write('theta,T,PA,PB,PC,I\n')
    for th, T, PA, PB, PC, I in rows:
        f.write(f'{th:.4f},{T:.1f},{PA:.8f},{PB:.8f},{PC:.8f},{I:.8e}\n')
PYEOF
