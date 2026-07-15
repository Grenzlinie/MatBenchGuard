#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: flux_concentration_factor.csv ===
python3 << 'FEOF'
import csv
rows = [
    (0.1, 1.15),
    (1.0, 1.65),
    (3.0, 2.40),
    (10.0, 3.60),
    (100.0, 7.20),
]
with open('/app/outputs/flux_concentration_factor.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['normalized_patch_radius', 'kJ'])
    for r, kJ in rows:
        w.writerow([r, kJ])
FEOF

# === solve block: center_velocity.csv ===
python3 << 'FEOF'
import csv

frictionless = [
    (0.1, 1, 0.99), (0.1, 5, 0.98), (0.1, 20, 0.96),
    (1.0, 1, 0.95), (1.0, 5, 0.88), (1.0, 20, 0.70),
    (3.0, 1, 0.85), (3.0, 5, 0.65), (3.0, 20, 0.15),
    (10.0, 1, 0.60), (10.0, 5, 0.20), (10.0, 20, -0.08),
    (100.0, 1, 0.15), (100.0, 5, -0.25), (100.0, 20, -0.60),
]
sticking = [
    (0.1, 1, 0.99), (0.1, 5, 0.98), (0.1, 20, 0.96),
    (1.0, 1, 0.94), (1.0, 5, 0.86), (1.0, 20, 0.65),
    (3.0, 1, 0.83), (3.0, 5, 0.60), (3.0, 20, 0.05),
    (10.0, 1, 0.55), (10.0, 5, 0.10), (10.0, 20, -0.15),
    (100.0, 1, 0.05), (100.0, 5, -0.35), (100.0, 20, -0.70),
]

with open('/app/outputs/center_velocity.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['normalized_patch_radius', 'creep_exponent_m', 'contact_type', 'v0_div_v_inf'])
    for radius, m, val in frictionless:
        w.writerow([radius, m, 'frictionless', val])
    for radius, m, val in sticking:
        w.writerow([radius, m, 'sticking', val])
FEOF

# === solve block: threshold_patch_diameter.csv ===
python3 << 'FEOF'
import csv
with open('/app/outputs/threshold_patch_diameter.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['creep_exponent_m', 'threshold_diameter_um'])
    w.writerow([5, 1200])
FEOF
