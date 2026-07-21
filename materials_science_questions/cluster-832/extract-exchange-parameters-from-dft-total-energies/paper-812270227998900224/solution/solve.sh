#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
export OUTDIR=/app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: parameter_scans.csv ===
python3 << 'EOF' > "$OUTDIR/parameter_scans.csv"
import sys, csv, math
import numpy as np
from scipy.optimize import fsolve

# Table I coefficients (i, a, b, c, d, p, q, r, u, v)
data1 = [
    [1, 24, 16, 0, 8, 4, 0, 2, 2, 0],
    [2, -24, 16, 0, -8, -4, 0, 2, 2, 0],
    [3, 48, 64, 0, 16, 2, 0, 0, 2, 0],
    [4, -48, 64, 0, -16, -2, 0, 0, 2, 0],
    [5, 0, 32, 0, 0, 0, 0, -2, 2, 0],
    [6, 0, 64, 0, 0, 0, 0, 0, 2, 0],
    [7, 0, -32, -24, -4, 4, 8, 0, 2, 8],
    [8, 0, -32, -24, 4, -4, 8, 0, 2, 8],
    [9, 0, -72, -54, -12, 3, 4, 0, 1.5, 4],
    [10, 0, -72, -54, 12, -3, 4, 0, 1.5, 4],
    [11, 0, -32, -24, -8, 2, 2, 0, 1, 2],
    [12, 0, -16, -12, -4, 2, 0, 0, 1, 0],
    [13, 0, -32, -24, -8, 2, 0, 0, 2, 8],
    [14, 0, -32, -24, 8, -2, 2, 0, 1, 2],
    [15, 0, -16, -12, 4, -2, 0, 0, 1, 0],
    [16, 0, -32, -24, 8, -2, 0, 0, 2, 8],
    [17, 0, -8, -6, -4, 1, 0, 0, 0.5, 0],
    [18, 0, -16, -12, -8, 1, 0, 0, 1.5, 4],
    [19, 0, -8, -6, -4, 1, -4, 0, 1.5, 4],
    [20, 0, -8, -6, 4, -1, 0, 0, 0.5, 0],
    [21, 0, -16, -12, 8, -1, 0, 0, 1.5, 4],
    [22, 0, -8, -6, 4, -1, -4, 0, 1.5, 4]
]

# Table II coefficients
data2 = [
    [1, 24, 16, 0, 8, 4, 0, 2, 2, 0],
    [2, 24, -16, 0, 8, -4, 0, 2, 2, 0],
    [3, 24, 32, 0, 8, 2, 0, 0, 2, 0],
    [4, 24, -32, 0, 8, -2, 0, 0, 2, 0],
    [5, 24, 0, 0, 8, 0, 0, 2, 0, 0],
    [6, 24, 0, 0, 8, 0, 0, 0, 0, 0],
    [7, 0, -32, -24, -4, 4, 8, 0, 2, 8],
    [8, 0, 32, 24, -4, -4, 8, 0, 2, 8],
    [9, 0, -96, -72, -16, 3, 4, 0, 1.5, 4],
    [10, 0, 96, 72, -16, -3, 4, 0, 1.5, 4],
    [11, 0, -64, -48, -16, 2, 2, 0, 1, 2],
    [12, 0, 64, 48, -16, -2, 2, 0, 1, 2],
    [13, 0, -32, -24, -8, 2, 0, 0, 1, 0],
    [14, 0, -64, -48, -16, 2, 0, 0, 2, 8],
    [15, 0, 32, 24, -8, -2, 0, 0, 1, 0],
    [16, 0, 64, 48, -16, -2, 0, 0, 2, 8],
    [17, 0, -32, -24, -16, 1, 0, 0, 0.5, 0],
    [18, 0, -64, -48, -32, 1, 0, 0, 1.5, 4],
    [19, 0, -32, -24, -16, 1, -4, 0, 1.5, 4],
    [20, 0, 32, 24, -16, -1, 0, 0, 0.5, 0],
    [21, 0, 64, 48, -32, -1, 0, 0, 1.5, 4],
    [22, 0, 32, 24, -16, -1, -4, 0, 1.5, 4],
    [23, 0, 0, 0, -32, 0, -2, 0, 1, 2],
    [24, 0, 0, 0, -16, 0, 0, 0, 1, 0],
    [25, 0, 0, 0, -16, 0, 0, 0, 2, 8],
    [26, 0, 0, 0, -8, 0, -8, 0, 2, 8],
    [27, 0, 0, 0, -4, 0, 0, 0, 0, 0]
]

arr1 = np.array(data1)
arr2 = np.array(data2)

def eq_residual(vars, J1p_ratio, J2p_ratio, J2_ratio, J3_ratio):
    t, R = vars
    if t <= 0:
        return np.array([1e10, 1e10])
    K1 = 1.0 / t
    K2 = J2_ratio * K1
    K3 = J3_ratio * K1
    K1p = J1p_ratio * K1
    K2p = J2p_ratio * K1

    args1 = (arr1[:,5]*K1 + arr1[:,6]*K2 + arr1[:,7]*K3 + arr1[:,8]*K1p + arr1[:,9]*K2p)
    args2 = (arr2[:,5]*K1 + arr2[:,6]*K2 + arr2[:,7]*K3 + arr2[:,8]*K1p + arr2[:,9]*K2p)

    max_arg1 = np.max(args1)
    max_arg2 = np.max(args2)

    coeff1 = (arr1[:,1]*K1 + arr1[:,2]*K2) + (arr1[:,3]*K1 + arr1[:,4]*K3)*R
    coeff2 = (arr2[:,1]*K1 + arr2[:,2]*K2) + (arr2[:,3]*K1 + arr2[:,4]*K3)*R

    sum1 = np.sum(coeff1 * np.exp(args1 - max_arg1))
    sum2 = np.sum(coeff2 * np.exp(args2 - max_arg2))
    return np.array([sum1, sum2])

def solve_for_Tc(J1p_ratio, J2p_ratio, J2_ratio, J3_ratio, initial_guess=None):
    if initial_guess is None:
        t0, R0 = 1.8, 1.0
    else:
        t0, R0 = initial_guess
    try:
        sol = fsolve(eq_residual, [t0, R0], args=(J1p_ratio, J2p_ratio, J2_ratio, J3_ratio),
                     maxfev=2000, xtol=1e-12, full_output=True)
        if sol[2] == 1:
            t, R = sol[0][0], sol[0][1]
            if t <= 1e-8:
                t, R = 0.0, 0.0
            return t, R
        else:
            alternatives = [(1.0, 1.0), (2.0, 0.5), (0.5, 0.5), (0.1, 0.1)]
            for t0_alt, R0_alt in alternatives:
                try:
                    sol = fsolve(eq_residual, [t0_alt, R0_alt], args=(J1p_ratio, J2p_ratio, J2_ratio, J3_ratio),
                                 maxfev=2000, xtol=1e-12)
                    t, R = sol[0], sol[1]
                    if t <= 1e-8:
                        t, R = 0.0, 0.0
                    return t, R
                except Exception:
                    continue
            return None
    except Exception:
        return None

def scan_parameter(param_name, values, J1p_func=None, J2p_func=None, J2_func=None, J3_func=None):
    results = []
    prev_sol = None
    for val in values:
        J1p = 0.0; J2p = 0.0; J2 = 0.0; J3 = 0.0
        if J1p_func: J1p = J1p_func(val)
        if J2p_func: J2p = J2p_func(val)
        if J2_func:  J2 = J2_func(val)
        if J3_func:  J3 = J3_func(val)
        sol = solve_for_Tc(J1p, J2p, J2, J3, initial_guess=prev_sol)
        if sol is not None:
            t, R = sol
        else:
            t, R = 0.0, 0.0
        results.append((param_name, val, t, R))
        if sol and t > 0:
            prev_sol = (t, R)
        else:
            prev_sol = None
    return results

all_results = []
# J1' scan: -2.0 to 2.0 step 0.05
j1p_vals = np.arange(-2.0, 2.0+0.05, 0.05)
all_results.extend(scan_parameter("J1'", j1p_vals, J1p_func=lambda x: x))
# J2' scan: step 0.1
j2p_vals = np.arange(-2.0, 2.0+0.1, 0.1)
all_results.extend(scan_parameter("J2'", j2p_vals, J2p_func=lambda x: x))
# J2 scan: step 0.05
j2_vals = np.arange(-1.0, 1.0+0.05, 0.05)
all_results.extend(scan_parameter("J2", j2_vals, J2_func=lambda x: x))
# J3 scan: step 0.2
j3_vals = np.arange(-2.0, 2.0+0.2, 0.2)
all_results.extend(scan_parameter("J3", j3_vals, J3_func=lambda x: x))

param_order = {"J1'":0, "J2'":1, "J2":2, "J3":3}
all_results.sort(key=lambda x: (param_order[x[0]], x[1]))

writer = csv.writer(sys.stdout)
writer.writerow(["parameter", "parameter_value", "kB_Tc_over_J1", "mu1_over_lambda1"])
for row in all_results:
    writer.writerow(row)
EOF

# === solve block: instability_point.csv ===
python3 /solution/compute_solve.py instability_point > "$OUTDIR/instability_point.csv"
