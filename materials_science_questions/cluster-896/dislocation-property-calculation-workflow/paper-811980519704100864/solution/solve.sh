#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: relaxed_shear_stress.csv ===
python3 -c '
import sys, math
def series_sum(x):
    s = 16.0/15.0 * x
    t = 1
    while True:
        term = float(2*t+2)/((2*t+1)*(2*t+3)*(2*t+5)) * math.pow(x, 2*t+1)
        if term < 1e-8:
            break
        s += term
        t += 1
    return s
print("x_over_R,p_rθ_over_F")
for x in [i/10.0 for i in range(11)]:
    print("{:.1f},{:.12f}".format(x, series_sum(x)))
' > /app/outputs/relaxed_shear_stress.csv

# === solve block: equilibrium_spacing.txt ===
python3 -c '
import math
b = 1.0
R = 1.0
eps = 0.01
X = math.sqrt(15 * b * R / (32 * eps))
print("X = {:.10f}".format(X))
' > /app/outputs/equilibrium_spacing.txt
