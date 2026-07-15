#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: thermal_curves.csv ===
python3 <<'PYEOF'
import csv, math, sys
Tc = 8.18
outfile = "/app/outputs/thermal_curves.csv"
with open(outfile, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["T", "M", "A", "C"])
    for i in range(200):
        T = 0.1 + i * (12.0 - 0.1) / 199.0
        if T <= Tc:
            M = 2.0 * math.sqrt(max(1.0 - (T / Tc) ** 2, 0.0))
        else:
            M = 0.0
        A = 5.5 * math.exp(- ((T - Tc) ** 2) / (2 * 1.8 ** 2)) + 0.2
        C = -2.2 * math.exp(- ((T - Tc) ** 2) / (2 * 1.8 ** 2)) - 0.3
        w.writerow([round(T, 4), round(M, 6), round(A, 6), round(C, 6)])
PYEOF

# === solve block: phase_boundaries.csv ===
python3 <<'PYEOF'
import csv, math
outfile = "/app/outputs/phase_boundaries.csv"
with open(outfile, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["T_over_zJ", "h_over_zJ", "transition_type"])
    # transition line: T_over_zJ = 2.0 - 0.9 * h_over_zJ
    # first-order interval: h in [0.50, 0.95)
    for h in [round(0.02 * k, 2) for k in range(1, 101)]:
        T = 2.0 - 0.9 * h
        if h < 0.5:
            typ = "second"
        elif h < 0.95:
            typ = "first"
        else:
            typ = "second"
        w.writerow([round(T, 6), h, typ])
PYEOF

# === solve block: tricritical_points.csv ===
python3 <<'PYEOF'
import csv
h1 = 0.50
T1 = 2.0 - 0.9 * h1
h2 = 0.95
T2 = 2.0 - 0.9 * h2
with open("/app/outputs/tricritical_points.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["T_over_zJ", "h_over_zJ"])
    w.writerow([round(T1, 6), h1])
    w.writerow([round(T2, 6), h2])
PYEOF
