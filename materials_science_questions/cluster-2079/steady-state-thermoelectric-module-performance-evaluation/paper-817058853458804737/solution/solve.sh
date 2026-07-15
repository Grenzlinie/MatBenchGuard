#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: theta_thv_vs_I.csv ===
python3 - << 'EOF' "$OUTDIR"
import csv, sys, os
outdir = sys.argv[1]
path = os.path.join(outdir, 'theta_thv_vs_I.csv')
S = 0.0027
R = 1.035
theta_th = 102
T_j = 353
theta_a = 50
Q = 0.5
T_c = T_j - theta_a * Q
rows = []
for i in range(1, 16):  # 0.1 A to 1.5 A
    I = i / 10.0
    dT = theta_th * (S * I * T_c - 0.5 * I**2 * R - Q)
    P = S * I * dT + I**2 * R
    A = P / I**2 - R
    B = A + (0.5 * S * I * R - S**2 * T_c) * theta_th
    thv = (A * theta_th) / B
    rows.append((I, thv))
with open(path, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['I_tec', 'theta_thv'])
    w.writerows(rows)
EOF

# === solve block: minimum_theta_thv.json ===
python3 /solution/compute_curve.py /app/outputs
