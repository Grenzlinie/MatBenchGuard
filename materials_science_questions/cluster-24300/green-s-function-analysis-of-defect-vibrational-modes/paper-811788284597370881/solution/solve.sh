#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: zpl_quantities.json ===
python3 << PYEOF
import json, os
import numpy as np
from scipy.integrate import quad

a = 1.0
b_vals = [-0.2, 0.0, 0.16]
T_vals = [0.0, 0.1, 0.5]

def ImG(w):
    if w <= 0.0 or w > 1.0:
        return 0.0
    return 16.0 * w**3 * np.sqrt(1.0 - w**2)

def ReG(w):
    return -2.0 - 8.0 * w**2 + 16.0 * w**4

def n_bose(w, T):
    if T == 0.0 or w == 0.0:
        return 0.0
    return 1.0 / (np.exp(w / T) - 1.0)

def D(w, T):
    return ReG(w) + 1j * (ImG(w) * (1.0 + 2.0 * n_bose(w, T)))

def D_tilde(w, b, T):
    dv = D(w, T)
    return dv / (1.0 - b * dv)

def integrand_S_abs(w, b, T):
    if w <= 0.0:
        return 0.0
    return np.imag(D_tilde(w, b, T)) / (w * w)

def integrand_S_lum(w, b, T):
    if w <= 0.0:
        return 0.0
    G = ReG(w) + 1j * ImG(w)
    factor = np.abs(1.0 - b * G)**2
    return np.imag(D_tilde(w, b, T)) * factor / (w * w)

def integrand_lngamma(w, b, T):
    if w <= 0.0:
        # limit: D(0,T) = ReG(0) = -2  =>  1 - b*D(0,T) = 1 + 2b
        return np.log(1.0 + 2.0 * b)
    return np.log(1.0 - b * D(w, T))

results = []
for b in b_vals:
    for T in T_vals:
        # Stokes shift
        D0 = D(0.0, T)
        Dt0 = D0 / (1.0 - b * D0)
        delta_L = (a*a / (2.0 * np.pi)) * np.real(Dt0)

        # S_L absorption
        S_abs, _ = quad(integrand_S_abs, 0.0, 1.0, args=(b, T), limit=500,
                        epsabs=1e-15, epsrel=1e-15)
        S_abs *= a*a / np.pi

        # S_L luminescence
        S_lum, _ = quad(integrand_S_lum, 0.0, 1.0, args=(b, T), limit=500,
                        epsabs=1e-15, epsrel=1e-15)
        S_lum *= a*a / np.pi

        # gamma and delta_Q
        Z, _ = quad(integrand_lngamma, 0.0, 1.0, args=(b, T), limit=500,
                    epsabs=1e-15, epsrel=1e-15)
        gamma = np.real(Z) / (2.0 * np.pi)
        delta_Q = -np.imag(Z) / (2.0 * np.pi)

        results.append({
            "b": b,
            "T": T,
            "delta_L": delta_L,
            "S_L_absorption": S_abs,
            "S_L_luminescence": S_lum,
            "gamma": gamma,
            "delta_Q": delta_Q
        })

output = {
    "b_values": b_vals,
    "T_values": T_vals,
    "results": results
}

outdir = os.environ.get("OUTDIR", "/app/outputs")
path = os.path.join(outdir, "zpl_quantities.json")
with open(path, "w") as f:
    json.dump(output, f, indent=2)

print("zpl_quantities.json written successfully")
PYEOF
