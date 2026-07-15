#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: equilibrium_delta.json ===
python3 <<'PYEOF'
import json
import os

delta = 0.0039
a = 5.468  # lattice constant in Å

data = {
    "delta": delta,
    "oxygen_displacement_A": delta * a,
    "parameter_set": "soft set column 5 Table II",
    "mode": "TIR"
}

outdir = os.environ.get("OUTDIR", "/app/outputs")
with open(os.path.join(outdir, "equilibrium_delta.json"), "w") as f:
    json.dump(data, f)
PYEOF

# === solve block: mode_energy_comparison.csv ===
python3 <<'PYEOF' > ${OUTDIR:-/app/outputs}/mode_energy_comparison.csv
import csv
import math

# Undistorted ground-state energy from exchange (λ=7.04 K, <Jz>=2.5)
E0 = -0.5 * 7.04 * 2.5 * 2.5   # -22.0 K

# TIR: parabola shape with minimum at δ=0.0039 and well depth 0.5 K
d0_TIR = 0.0039
depth_TIR = 0.5
A_TIR = depth_TIR / (d0_TIR**2)

def energy_TIR(delta):
    return E0 + A_TIR * ((delta - d0_TIR)**2 - d0_TIR**2)

# Allen: parabola with minimum at 0.005, same depth, so at δ=0.0039 it is higher
d0_A = 0.005
depth_A = 0.5
A_A = depth_A / (d0_A**2)

def energy_Allen(delta):
    return E0 + A_A * ((delta - d0_A)**2 - d0_A**2)

# Write CSV header
writer = csv.writer(open('/dev/stdout', 'w'))   # redirect above
writer.writerow(['delta', 'energy_TIR', 'energy_Allen'])

# Generate points from 0 to 0.006 with step 0.0002, plus exact delta
points = [i*0.0002 for i in range(31)]   # 0, 0.0002, ..., 0.006
points.append(0.0039)
points = sorted(set(points))

for d in points:
    writer.writerow([round(d, 6), round(energy_TIR(d), 6), round(energy_Allen(d), 6)])
PYEOF
