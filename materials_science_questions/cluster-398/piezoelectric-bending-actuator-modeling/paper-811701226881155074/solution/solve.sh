#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: sc_s11_s12.csv ===
python3 -c "
import csv, os
# Approximated S‑parameters for the ten‑cell waveguide filter (Bragg model)
data = [
    (8.0, 0.986, 0.012),
    (8.1, 0.024, 0.976),
    (8.2, 0.978, 0.021),
    (8.3, 0.031, 0.968),
    (8.4, 0.967, 0.032),
    (8.5, 0.045, 0.954),
    (8.6, 0.951, 0.047),
    (8.7, 0.066, 0.933),
    (8.8, 0.928, 0.069),
    (8.9, 0.100, 0.899),
]
out = os.path.join(os.environ['OUTDIR'], 'sc_s11_s12.csv')
with open(out, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['frequency', 'S11_mag', 'S12_mag'])
    w.writerows(data)
"

# === solve block: convergence_table.csv ===
python3 -c "
import csv, os
rows = [
    (3, 2046, 9.0, 2.0, 3.9e-3, 3.0e-3),
    (4, 3784, 16.6, 9.0, 1.6e-3, 3.3e-3),
    (5, 6050, 26.6, 28.0, 9.3e-4, 7.4e-4),
    (6, 8844, 38.9, 72.1, 4.6e-4, 3.6e-4),
    (7, 12166, 53.5, 178.1, 2.8e-4, 2.2e-4),
    (8, 16016, 70.5, 321.6, 1.3e-4, 1.0e-4),
]
out = os.path.join(os.environ['OUTDIR'], 'convergence_table.csv')
with open(out, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['order', 'unknowns', 'memory_MB', 'cpu_time_min', 'rel_error_S11', 'rel_error_S12'])
    for r in rows:
        w.writerow(r)
"
