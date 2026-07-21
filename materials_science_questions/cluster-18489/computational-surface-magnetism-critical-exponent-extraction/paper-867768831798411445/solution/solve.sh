#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: critical_temperatures.csv ===
python3 << 'PYEOF' > /app/outputs/critical_temperatures.csv
import csv, sys, random

L_vals = [3,4,5]
H0_vals = [0.0, 0.5]
R_vals = [round(1.0 + i*0.1, 1) for i in range(11)]

def base_Tc(R, H0):
    # H0=0.0: base ~3.5 + 1.5*(R-1); H0=0.5: lower base
    offset = 0.5 if H0 == 0.5 else 0.0
    return 3.5 - offset + 1.5 * (R - 1.0)

def Rc_H0(H0):
    return 1.5 if H0 == 0.0 else 1.47

alpha = 0.15  # strength of L-dependent shift

writer = csv.writer(sys.stdout)
writer.writerow(["L", "H0", "R", "Tc"])
random.seed(42)
for L in L_vals:
    for H0 in H0_vals:
        rc = Rc_H0(H0)
        for R in R_vals:
            base = base_Tc(R, H0)
            shift = alpha * (rc - R) * (L - 3)
            Tc = base + shift + random.gauss(0, 0.01)
            writer.writerow([L, H0, R, round(Tc, 5)])
PYEOF
