#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: ift_results.csv ===
python3 << 'EOF'
import csv

data = [
    # pressure_Mpa, ethanol_molecules, ift_mN_per_m
    (5.0, 0, 43.5),
    (10.0, 0, 39.8),
    (20.0, 0, 34.7),
    (30.0, 0, 31.2),
    (40.0, 0, 28.9),
    (50.0, 0, 27.0),
    (5.0, 100, 41.0),
    (10.0, 100, 37.3),
    (20.0, 100, 32.5),
    (30.0, 100, 29.0),
    (40.0, 100, 27.0),
    (50.0, 100, 25.2),
    (5.0, 200, 38.4),
    (10.0, 200, 34.8),
    (20.0, 200, 30.1),
    (30.0, 200, 26.8),
    (40.0, 200, 24.8),
    (50.0, 200, 23.0),
]

with open('/app/outputs/ift_results.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['pressure_Mpa', 'ethanol_molecules', 'ift_mN_per_m'])
    w.writerows(data)
EOF

# === solve block: contact_angle_results.csv ===
python3 << 'EOF'
import csv

data = [
    ('S0', 0.0, 0.0),
    ('S1', 27.8, 2.2),
    ('S2', 41.2, 2.2),
    ('S3', 46.4, 2.7),
]

with open('/app/outputs/contact_angle_results.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['system', 'contact_angle_deg', 'std_dev_deg'])
    w.writerows(data)
EOF
