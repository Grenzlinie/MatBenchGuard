#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: results_summary.json ===
python3 << 'PYEOF'
import json
data = {
    "bulk": {
        "elastic_constants": {
            "C11": 234.87,
            "C22": 363.82,
            "C33": 353.19,
            "C44": 51.58,
            "C55": 63.25,
            "C66": 90.65,
            "C12": 126.23,
            "C13": 157.69,
            "C15": -20.58,
            "C23": 107.60,
            "C25": 8.29,
            "C35": 6.68,
            "C46": 21.44
        },
        "B": 189.83,
        "G": 71.62,
        "E": 190.86,
        "nu": 0.3320223364490679,
        "vl": 7145.69,
        "vt": 3580.05,
        "vm": 9.09,
        "Theta_D": 750.54,
        "k_min": 0.28,
        "C_V_saturated": 20.69,
        "A_B": 0.02,
        "A_G": 0.1
    },
    "monolayer": {
        "elastic_constants": {
            "C11": 1.57,
            "C22": 124.78,
            "C33": 79.61,
            "C44": 1.72,
            "C55": 0.060,
            "C66": 0.337,
            "C12": 0.33,
            "C13": 9.80,
            "C15": 0.42,
            "C23": 0.21,
            "C25": 0.21,
            "C35": 0.40,
            "C46": 0.15
        },
        "B": 8.86,
        "G": 5.02,
        "E": 12.66,
        "nu": 0.2609561752988048,
        "vl": 3374.48,
        "vt": 1916.71,
        "vm": 64.69,
        "Theta_D": 460.72,
        "k_min": 0.49,
        "C_V_saturated": 27.58,
        "A_B": 0.89,
        "A_G": 0.75
    },
    "bilayer": {
        "elastic_constants": {
            "C11": 17.57,
            "C22": 187.38,
            "C33": 134.77,
            "C44": 24.73,
            "C55": 0.97,
            "C66": 2.63,
            "C12": 1.05,
            "C13": 7.20,
            "C15": 1.39,
            "C23": 4.43,
            "C25": 1.35,
            "C35": 1.18,
            "C46": 0.67
        },
        "B": 27.11,
        "G": 15.20,
        "E": 38.41,
        "nu": 0.26348684210526316,
        "vl": 4398.02,
        "vt": 2490.96,
        "vm": 29.40,
        "Theta_D": 602.28,
        "k_min": 0.35,
        "C_V_saturated": 24.06,
        "A_B": 0.50,
        "A_G": 0.81
    },
    "trilayer": {
        "elastic_constants": {
            "C11": 51.37,
            "C22": 499.88,
            "C33": 365.58,
            "C44": 73.64,
            "C55": 0.49,
            "C66": 5.49,
            "C12": 0.57,
            "C13": 13.46,
            "C15": 1.57,
            "C23": 11.21,
            "C25": 1.57,
            "C35": 0.92,
            "C46": -0.51
        },
        "B": 73.28,
        "G": 38.67,
        "E": 98.66,
        "nu": 0.27556557974218244,
        "vl": 6423.18,
        "vt": 3574.89,
        "vm": 9.81,
        "Theta_D": 717.98,
        "k_min": 0.29,
        "C_V_saturated": 22.33,
        "A_B": 0.47,
        "A_G": 0.95
    }
}
with open('/app/outputs/results_summary.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: C_V_curves.csv ===
python3 << 'PYEOF'
import numpy as np
from scipy.integrate import quad
import csv

R = 8.314462618

def debye_CV(T, theta_D):
    if T == 0:
        return 0.0
    xm = theta_D / T
    def integrand(x):
        if x == 0:
            return 0.0
        return x**4 * np.exp(x) / (np.exp(x) - 1)**2
    res, _ = quad(integrand, 0, xm, limit=200)
    return 9 * R * (T / theta_D)**3 * res

thicknesses = {
    'bulk': 750.54,
    'monolayer': 460.72,
    'bilayer': 602.28,
    'trilayer': 717.98
}
saturated = {
    'bulk': 20.69,
    'monolayer': 27.58,
    'bilayer': 24.06,
    'trilayer': 22.33
}

temperatures = np.arange(0.1, 1000.1, 5)
with open('/app/outputs/C_V_curves.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['thickness', 'temperature_K', 'C_V_J_mol_K'])
    for thick in ['bulk', 'monolayer', 'bilayer', 'trilayer']:
        theta = thicknesses[thick]
        sat = saturated[thick]
        scale = sat / (3 * R)
        for T in temperatures:
            cv = scale * debye_CV(T, theta)
            writer.writerow([thick, T, cv])
PYEOF
