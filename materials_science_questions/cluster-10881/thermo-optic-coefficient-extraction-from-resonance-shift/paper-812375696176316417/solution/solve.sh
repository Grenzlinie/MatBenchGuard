#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: thermal_focal_length.csv ===
python3 << 'PYEOF'
import numpy as np
from scipy.optimize import root_scalar
from scipy.special import jv
import csv

a = 1.0
d = 0.5
k = 0.037
beta = 0.012
n0 = 3.30
gamma = 18.7e-5
alpha = 5.7e-6
T0 = 298.0
Tn = 298.1
g = (Tn - T0) / d

powers = list(range(0, 2100, 100))
rows = []

for P in powers:
    Tc = T0 + 2e-4 * P
    if P == 0:
        f_th = float('inf')
    else:
        I = P / (np.pi * a**2)
        ratio = T0 / Tc
        sol = root_scalar(lambda x: jv(0, x) - ratio,
                          bracket=[0.0, 2.4048], method='bisect')
        term = T0 * d + 0.5 * g * d**2 + (beta * I) / (6.0 * k) * d**3
        Delta_L = (alpha + gamma) * n0 * term * (1.0 / ratio - 1.0)
        if Delta_L <= 0.0:
            f_th = float('inf')
        else:
            f_th = a**2 / (2.0 * Delta_L * (n0 - 1.0))
    rows.append((P, f_th))

outpath = '/app/outputs/thermal_focal_length.csv'
with open(outpath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['P', 'f_th'])
    for P, fth in rows:
        writer.writerow([P, fth])
PYEOF
