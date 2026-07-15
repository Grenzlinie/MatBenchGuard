#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: step_01_heat_capacity_comparison.csv ===
python3 << 'PYEOF'
import numpy as np
from scipy.integrate import quad
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
import csv
import math

R = 1.987  # cal/mol·K
# Experimental cV data from Table 2 (columns 1 and 2)
exp_data = {
    1.0: 0.000026,
    2.0: 0.000211,
    3.0: 0.000712,
    4.0: 0.001688,
    5.0: 0.003298,
    7.5: 0.0112,
    10.0: 0.0262,
    12.5: 0.0496,
    15.0: 0.0825,
    17.5: 0.124,
    20.0: 0.174,
    30.0: 0.449,
    40.0: 0.757,
    50.0: 1.100,
    60.0: 1.398,
    70.0: 1.647,
    80.0: 1.866,
    90.0: 2.070,
    100.0: 2.261,
    110.0: 2.435,
    120.0: 2.599,
    130.0: 2.760,
    140.0: 2.919,
    150.0: 3.068,
    160.0: 3.234,
    170.0: 3.379,
    180.0: 3.542,
    190.0: 3.684,
    200.0: 3.825
}

T_exp = np.array(sorted(exp_data.keys()))
cV_exp = np.array([exp_data[t] for t in T_exp])

# Integration tolerance
eps = 1e-12

# Precompute full integrals I(infinity) = Gamma(n+1)*zeta(n+1)
from scipy.special import gamma, zeta
I_inf = {}
for n in [0.5, 1, 3]:
    I_inf[n] = gamma(n+1) * zeta(n+1)

# Scalar integration helper
def _I_n(n, y):
    if y <= 0:
        return 0.0
    if y > 20:
        return I_inf[n]
    res, _ = quad(lambda x: x**n / (np.exp(x)-1.0), 0, y, limit=200, epsabs=eps, epsrel=eps)
    return res

# Scalar Debye function D_n(y)
def _D_n(n, y):
    if y <= 0:
        return np.nan
    I_y = _I_n(n, y)
    term1 = n * (n+1) * y**(-n) * I_y
    term2 = n * y / (np.exp(y) - 1.0)
    return term1 - term2

# Vectorized D_n that accepts array y while keeping n fixed
D_n = np.vectorize(_D_n, excluded=['n'])

# Debye model
def cV_debye(T, Theta3):
    y = Theta3 / T
    D3 = D_n(3, y)
    return 3.0 * R * D3

# Tarasov model (Eq 13)
def cV_tarasov(T, Theta1, Theta3):
    y1 = Theta1 / T
    y3 = Theta3 / T
    D1_1 = D_n(1, y1)
    D3_3 = D_n(3, y3)
    D1_3 = D_n(1, y3)
    return 3.0 * R * (D1_1 + (Theta3 / Theta1) * (D3_3 - D1_3))

# Modified model (Eqs 46-49)
def cV_modified(T, Theta3s, Theta1s, Theta3b, Theta1b):
    # stretching
    y1s = Theta1s / T
    y3s = Theta3s / T
    D1_1s = D_n(1, y1s)
    D3_3s = D_n(3, y3s)
    D1_3s = D_n(1, y3s)
    cV_s = R * (D1_1s + (Theta3s / Theta1s) * (D3_3s - D1_3s))
    # bending
    y1b = Theta1b / T
    y3b = Theta3b / T
    D12_1b = D_n(0.5, y1b)
    D3_3b = D_n(3, y3b)
    D12_3b = D_n(0.5, y3b)
    cV_b = 2.0 * R * (D12_1b + (Theta3b / Theta1b)**0.5 * (D3_3b - D12_3b))
    return cV_s + cV_b

# Fit Tarasov parameters
p0 = [500.0, 200.0]
def tarasov_fit(T, Theta1, Theta3):
    return cV_tarasov(T, Theta1, Theta3)

params, pcov = curve_fit(tarasov_fit, T_exp, cV_exp, p0=p0, maxfev=10000)
Theta1_fit, Theta3_fit = params
print(f"Fitted Tarasov: Theta1={Theta1_fit:.2f}, Theta3={Theta3_fit:.2f}")

# Interpolate experimental cV to integer 1..200
interp_lin = interp1d(T_exp, cV_exp, kind='linear', fill_value='extrapolate')
T_int = np.arange(1, 201, dtype=int)
cV_exp_int = interp_lin(T_int)

# Compute model cV and deviations
Debye_cV = np.array([cV_debye(t, 260.0) for t in T_int])
Tarasov_cV = np.array([cV_tarasov(t, Theta1_fit, Theta3_fit) for t in T_int])
Modified_cV = np.array([cV_modified(t, 996.6, 996.9, 188.7, 910.9) for t in T_int])

Debye_dev = 100.0 * (Debye_cV - cV_exp_int) / cV_exp_int
Tarasov_dev = 100.0 * (Tarasov_cV - cV_exp_int) / cV_exp_int
Modified_dev = 100.0 * (Modified_cV - cV_exp_int) / cV_exp_int

# Write CSV
with open('/app/outputs/step_01_heat_capacity_comparison.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['T','exp_cV','Debye_cV','Debye_dev_percent','Tarasov_cV','Tarasov_dev_percent','Modified_cV','Modified_dev_percent'])
    for i, t in enumerate(T_int):
        exp = cV_exp_int[i]
        deb = Debye_cV[i]
        dev_deb = Debye_dev[i]
        tar = Tarasov_cV[i]
        dev_tar = Tarasov_dev[i]
        mod = Modified_cV[i]
        dev_mod = Modified_dev[i]
        writer.writerow([int(t), f"{exp:.6f}", f"{deb:.6f}", f"{dev_deb:.2f}", f"{tar:.6f}", f"{dev_tar:.2f}", f"{mod:.6f}", f"{dev_mod:.2f}"])
print("CSV written.")
PYEOF
