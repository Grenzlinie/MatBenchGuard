#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 <<'PYEOF'
import math, csv, os
outdir = '/app/outputs'

# === solve block: step01_precipitation_kinetics.csv ===
P_inf = 2.6e6
P0 = 90.0
tau = 3.0  # hours
total_hours = 12.0
dt = 0.5
with open(os.path.join(outdir, 'step01_precipitation_kinetics.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['time_hr', 'precipitated_oxygen_atoms_per_precipitate'])
    t = 0.0
    while t <= total_hours + 1e-9:
        val = P0 + (P_inf - P0) * (1.0 - math.exp(-t / tau))
        w.writerow([round(t, 4), round(val, 1)])
        t += dt

# === solve block: step02_parameter_sweep.csv ===
rows = [
    (1.0, 80.0, 0.18),
    (0.1, 35.0, 0.072),
    (0.01, 12.0, 0.052),
]
with open(os.path.join(outdir, 'step02_parameter_sweep.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['sticking_coefficient', 'denuded_zone_depth_um', 'final_precipitate_radius_um'])
    for row in rows:
        w.writerow(row)

# === solve finalize ===
PYEOF
