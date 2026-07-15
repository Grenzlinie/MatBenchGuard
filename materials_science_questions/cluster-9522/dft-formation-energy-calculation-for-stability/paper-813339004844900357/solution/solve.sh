#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
mkdir -p /app/outputs

# === solve block: results.json ===
python3 <<'PYEOF'
import json
import numpy as np
from scipy.optimize import minimize_scalar

C_conv = 6.242

def delta_W_12_min(G, a, g_b6_110, g_b6_112):
    g110_b12 = g_b6_110 / 2.0
    g112_b12 = g_b6_112 / 2.0
    elastic_pre = 11.0 * G * a * a * C_conv / (128.0 * np.pi)
    gsfe_coeff = 6.0 * (g110_b12 + g112_b12) * C_conv
    
    def func(r):
        arg = (4 * r**2) / (3 * a**2)
        if arg <= 0:
            arg = 1e-10
        return -elastic_pre * (np.log(arg) + 2) + gsfe_coeff * r
    
    lb = 0.01 * a
    ub = 10.0 * a
    res = minimize_scalar(func, bounds=(lb, ub), method='bounded')
    if res.success:
        return res.fun
    else:
        return float('nan')

compositions = {
    "pure_Nb": {
        "bcc_hcp_energy_difference": -0.06,
        "C_prime": 60.0,
        "gamma_us_112": 0.781,
        "gamma_us_110": 0.678,
        "gamma_b3": 0.36,
        "gamma_b6": 0.12,
        "G": 40.0,
        "lattice_constant_a": 0.330,
        "gamma_b6_112": 0.10
    },
    "Ti75Nb": {
        "bcc_hcp_energy_difference": -0.03,
        "C_prime": 40.0,
        "gamma_us_112": 0.534,
        "gamma_us_110": 0.494,
        "gamma_b3": 0.30,
        "gamma_b6": 0.088235,
        "G": 30.0,
        "lattice_constant_a": 0.329,
        "gamma_b6_112": 0.08
    },
    "Ti50Nb": {
        "bcc_hcp_energy_difference": -0.01,
        "C_prime": 20.0,
        "gamma_us_112": 0.371,
        "gamma_us_110": 0.329,
        "gamma_b3": 0.225,
        "gamma_b6": 0.06081,
        "G": 20.0,
        "lattice_constant_a": 0.327,
        "gamma_b6_112": 0.05
    },
    "Ti25Nb": {
        "bcc_hcp_energy_difference": 0.0,
        "C_prime": 0.0,
        "gamma_us_112": 0.296,
        "gamma_us_110": 0.307,
        "gamma_b3": 0.096,
        "gamma_b6": 0.024,
        "G": 13.97,
        "lattice_constant_a": 0.3253,
        "gamma_b6_112": 0.019
    }
}

output = {}
for comp, d in compositions.items():
    gb6_110 = d["gamma_b6"]
    gb6_112 = d["gamma_b6_112"]
    dw = delta_W_12_min(d["G"], d["lattice_constant_a"], gb6_110, gb6_112)
    ratio = d["gamma_b3"] / (2 * d["gamma_b6"])
    output[comp] = {
        "bcc_hcp_energy_difference": d["bcc_hcp_energy_difference"],
        "C_prime": d["C_prime"],
        "gamma_us_112": d["gamma_us_112"],
        "gamma_us_110": d["gamma_us_110"],
        "gamma_b3": d["gamma_b3"],
        "gamma_b6": d["gamma_b6"],
        "ratio_gamma_b3_to_2gamma_b6": round(ratio, 6),
        "G": d["G"],
        "lattice_constant_a": d["lattice_constant_a"],
        "Delta_W_min": round(dw, 6) if np.isfinite(dw) else 0.0
    }

with open("/app/outputs/results.json", "w") as f:
    json.dump(output, f, indent=2)

print("results.json written successfully")
PYEOF
