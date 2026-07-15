#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: md_velocity_stress.csv ===
python3 -c "
import csv
stress_vel = [
    (50, 0.3),
    (100, 0.8),
    (200, 1.5),
    (500, 2.05),
    (1000, 2.1),
    (2000, 2.1)
]
with open('$OUTDIR/md_velocity_stress.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['stress_MPa', 'velocity_nm_ps'])
    w.writerows(stress_vel)
"

# === solve block: drag_coefficient_B.csv ===
python3 /solution/generate.py drag_coefficient_B.csv

# === solve block: ld_dispersion_curve.csv ===
python3 /solution/generate.py ld_dispersion_curve.csv

# === solve block: ld_limiting_velocity.csv ===
python3 /solution/generate.py ld_limiting_velocity.csv
