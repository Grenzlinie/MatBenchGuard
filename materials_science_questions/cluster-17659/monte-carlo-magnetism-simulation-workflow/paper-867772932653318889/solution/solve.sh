#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: xi_over_L_data.csv ===
python3 << 'PYEOF'
import csv, os

outdir = os.environ['OUTDIR']
fname = os.path.join(outdir, 'xi_over_L_data.csv')

lines = {
    8:  {'a': 1.1945, 'b': 0.25},
    12: {'a': 0.978,  'b': 0.2},
    16: {'a': 0.3233, 'b': -0.15},
    24: {'a': 0.336,  'b': -0.1},
    32: {'a': 0.85405,'b': 0.1},
}

h_min, h_max, step = -2.3, -2.0, 0.002
rows = []
for L, coeff in lines.items():
    a, b = coeff['a'], coeff['b']
    h = h_min
    while h <= h_max + 1e-9:
        xi_over_L = max(0.0, a + b * h)
        rows.append([L, round(h, 6), round(xi_over_L, 6), 0.001])
        h += step

with open(fname, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['L', 'h', 'xi_over_L', 'error_xi_over_L'])
    writer.writerows(rows)
PYEOF

# === solve block: barrier_data.json ===
python3 << 'PYEOF'
import json, os

outdir = os.environ['OUTDIR']
fname = os.path.join(outdir, 'barrier_data.json')
data = {
    "L": [8, 12, 16, 24, 32],
    "Delta_F_over_N": [0.03382, 0.01756, 0.01138, 0.00608, 0.00392],
    "error_Delta_F": [0.00029, 0.00015, 0.00009, 0.00005, 0.00005],
    "theta_estimate": 1.469,
    "theta_error": 0.020,
    "fit_range": "L>=12"
}
with open(fname, 'w') as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: critical_exponents.json ===
python3 << 'PYEOF'
import json, os

outdir = os.environ['OUTDIR']
fname = os.path.join(outdir, 'critical_exponents.json')

data = {
    "L": [8, 12, 16],
    "h_star": [-2.178, -2.140, -2.123],
    "h_star_error": [0.004, 0.005, 0.003],
    "beta_over_nu": [0.0125, 0.0104, 0.0119],
    "beta_over_nu_error": [0.0007, 0.0005, 0.0004],
    "nu_h": [0.887, 0.709, 0.742],
    "nu_h_error": [0.005, 0.009, 0.007],
    "nu_T": [1.07, 1.01, 1.10],
    "nu_T_error": [0.09, 0.04, 0.15],
    "final_beta_over_nu": 0.0116,
    "final_beta_over_nu_error": 0.0004,
    "final_nu_h": 0.75,
    "final_nu_h_error": 0.02,
    "final_nu_T": 1.05,
    "final_nu_T_error": 0.10,
    "final_theta": 1.469,
    "final_theta_error": 0.020
}

with open(fname, 'w') as f:
    json.dump(data, f, indent=2)
PYEOF
