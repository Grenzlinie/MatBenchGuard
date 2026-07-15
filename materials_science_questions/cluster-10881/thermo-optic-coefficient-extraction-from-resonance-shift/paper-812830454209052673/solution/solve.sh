#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: chi_t_60.txt ===
OUTDIR=/app/outputs && printf '%s\n' -2.92 > "$OUTDIR/chi_t_60.txt"

# === solve block: chi_t_temperature.csv ===
python3 << 'PYEOF'
import csv

rows = [
    [23.0, 34.35, -6.52, -7.14, -7.18, -2.84, -2.84, -2.87],
    [61.2, 35.6,  -7.07, -7.66, -7.73, -2.88, -2.89, -2.91],
    [125.2, 37.7, -7.71, -8.29, -8.43, -3.00, -3.02, -3.03],
    [177.0, 39.35, -8.73, -9.33, -9.44, -2.99, -3.01, -3.02],
    [227.5, 41.1, -9.52, -10.12, -10.30, -3.05, -3.00, -3.06],
    [275, 42.65, -11.06, -11.78, -11.91, -2.91, -2.90, -2.90],
    [328, 44.7, -13.48, -14.19, -14.27, -2.66, -2.63, -2.65],
    [385, 47.3, -17.53, -18.40, -18.57, -2.15, -2.05, -2.03],
    [435, 49.95, -21.49, -22.53, -22.75, -1.66, -1.49, -1.46],
]

header = [
    "temperature_C", "gamma_t_1e6",
    "dn_e_dt_4358_1e6", "dn_e_dt_5893_1e6", "dn_e_dt_6563_1e6",
    "chi_t_4358", "chi_t_5893", "chi_t_6563"
]

with open("/app/outputs/chi_t_temperature.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)
PYEOF
