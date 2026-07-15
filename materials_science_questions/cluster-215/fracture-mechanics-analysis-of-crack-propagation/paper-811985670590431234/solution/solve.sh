#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: stress_curve.csv ===
python3 <<'PYEOF' > "$OUTDIR/stress_curve.csv"
import math

x0 = 1.22
sigma = 0.4
offset = 0.05
A = 0.70

n_points = 200
x_min = -2.0
x_max = 2.0
dx = (x_max - x_min) / (n_points - 1)

# Print header
print('x_over_l,stress_normalized')
for i in range(n_points):
    x = x_min + i * dx
    stress = offset + A * math.exp(-((x - x0) ** 2) / (2 * sigma ** 2))
    print(f'{x},{stress}')
PYEOF
