#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: results.json ===
python3 - <<'PYEOF'
import numpy as np
import json
from scipy.stats import linregress

k     = 0.0137
gamma = 0.49
gamma_p = 0.8
nu_m = 276.31
V_m  = 21.61
c_base = -10.47
a1 = -0.858
a2 = 0.344
dVc_dT = -0.0316

# melting pressure slope (kbar/K) evaluated at T
def dPm_dT_kbar(T):
    T0 = 195.48
    A = 5.886
    B = 3.96
    return A * B / T0 * (T / T0) ** (B - 1)

def V_c_func(T):
    return 27.79 - 0.0316 * T

configs = [
    {"key": "0kbar",    "P_kbar": 0.0,  "Tm": 192.5},
    {"key": "1.93kbar", "P_kbar": 1.93, "Tm": 210.0},
    {"key": "3.07kbar", "P_kbar": 3.07, "Tm": 217.34},
]

result = {}
for cfg in configs:
    key = cfg["key"]
    P_kbar = cfg["P_kbar"]
    Tm = cfg["Tm"]

    # constant DPM/DT at the melting point (kbar/K)
    dPm_dT_cst = dPm_dT_kbar(Tm)

    # temperature range from Tm-5 K to just below Tm
    T_arr = np.linspace(Tm - 5.0, Tm - 0.02, 500)
    delta_T = Tm - T_arr

    Vc = V_c_func(T_arr)

    # solid volume Eq. (2.10) with constant dPm/dT
    exponent = -k / (1.0 - gamma) * (dPm_dT_cst ** (1.0 - gamma)) * (delta_T ** (1.0 - gamma))
    Vs = Vc * np.exp(exponent)

    # thermal expansivity Eq. (2.12)  (kbar^-1?? no, it's K^-1, but formulas are consistent)
    alpha_p = k * (dPm_dT_cst ** (1.0 - gamma)) * (delta_T ** (-gamma)) + dVc_dT / Vc

    # isothermal compressibility Eq. (2.13) (kbar^-1)
    kappa_T = k * (dPm_dT_cst ** (-gamma)) * (delta_T ** (-gamma))

    # specific heat (kbar·cm³/mol/K)
    Cp_kbar_cm3 = T_arr * Vs * alpha_p**2 / kappa_T
    # convert to J/(mol·K) (1 kbar·cm³ = 100 J)
    Cp = 100.0 * Cp_kbar_cm3

    # Raman frequency Eq. (2.5) with Vp = Vs
    c0 = c_base + a1 * P_kbar + a2 * (P_kbar**2)
    nu_p = c0 + nu_m * (Vs / V_m) ** (-gamma_p)

    # frequency‑shift variable  X = (1/ν) dν/dT
    dnu_dT = np.gradient(nu_p, T_arr)
    X = dnu_dT / nu_p

    # linear regression of C_p vs X
    slope, intercept, r_value, p_value, std_err = linregress(X, Cp)

    # extract dPm/dT from slope   (bar/K)
    Vc_Tm = V_c_func(Tm)
    dPm_dT_bar_fit = -10.0 * slope * gamma_p / (Tm * Vc_Tm)

    # intercept: (dS/dT)_m = intercept / T_m   (J/(mol·K²))
    dS_dT_m_fit = intercept / Tm

    result[key] = {
        "temperatures": T_arr.tolist(),
        "C_p": Cp.tolist(),
        "X": X.tolist(),
        "dPm_dT": dPm_dT_bar_fit,
        "dS_dT_m": dS_dT_m_fit,
    }

import os
os.makedirs("/app/outputs", exist_ok=True)
with open("/app/outputs/results.json", "w") as f:
    json.dump(result, f, indent=2)
PYEOF
