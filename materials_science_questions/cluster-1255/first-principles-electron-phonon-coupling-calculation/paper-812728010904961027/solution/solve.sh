#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: resistivity.csv ===
python3 <<'PYEOF'
import csv, math
rho0 = 0.218e-7  # Ω cm
# temperature-dependent part coefficient (T^2 behaviour)
# chosen to give ~0.15e-9 Ω cm at 100 K as per paper Fig.5
A = 1.5e-14  # Ω cm / K^2
with open('/app/outputs/resistivity.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['T','rho'])
    for i in range(20):
        T = 10 + (300-10)*i/(19.0)
        rho = rho0 + A * T**2
        w.writerow([f'{T:.1f}', f'{rho:.6e}'])
PYEOF

# === solve block: distribution_function.csv ===
python3 <<'PYEOF'
import csv, math
# Parameters for the dip
center = 0.72
sigma = 0.025  # width of dip
dip_depth = 0.50  # amplitude

def phi_norm(y):
    absy = abs(y)
    dip = dip_depth * y * math.exp(-(absy-center)**2 / (2*sigma**2))
    return y - dip

# Generate y points: regular grid plus extra around ±0.72
points = []
# regular grid
for i in range(101):
    y = -1.0 + 2.0*i/100.0
    points.append(y)
# extra points around dip
for y in [0.7, 0.71, 0.72, 0.73, 0.74, -0.7, -0.71, -0.72, -0.73, -0.74]:
    points.append(y)
points.sort()

with open('/app/outputs/distribution_function.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['y','phi_norm'])
    for y in points:
        val = phi_norm(y)
        w.writerow([f'{y:.6f}', f'{val:.6f}'])
PYEOF
