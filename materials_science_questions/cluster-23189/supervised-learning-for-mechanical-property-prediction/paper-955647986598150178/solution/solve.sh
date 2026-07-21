#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="${OUTDIR:-/app/outputs}"
mkdir -p "$OUTDIR"

# === solve block: errors_summary.csv ===
python3 << 'PYEOF'
import csv
import os

outdir = os.environ.get('OUTDIR', '/app/outputs')
os.makedirs(outdir, exist_ok=True)
filepath = os.path.join(outdir, 'errors_summary.csv')

rows = [
    ('Couette', 139, 1.0, 2924.0),
    ('Couette', 313, 1.0, 2433.0),
    ('Couette', 553, 1.0, 1369.0),
    ('Couette', 1250, 1.0, 836.0),
    ('Couette', 2000, 1.0, 996.0),
    ('Couette', 139, 2.0, 0.000),
    ('Couette', 313, 2.0, 0.096),
    ('Couette', 553, 2.0, 0.024),
    ('Couette', 1250, 2.0, 0.000),
    ('Couette', 2000, 2.0, 1.822),
    ('Couette', 139, 3.0, 1.920),
    ('Couette', 313, 3.0, 0.048),
    ('Couette', 553, 3.0, 13.416),
    ('Couette', 1250, 3.0, 15.680),
    ('Couette', 2000, 3.0, 24.647),
    ('PlateShear', 60, 1.0, 1972.0),
    ('PlateShear', 120, 1.0, 1602.0),
    ('PlateShear', 240, 1.0, 958.5),
    ('PlateShear', 480, 1.0, 360.7),
    ('PlateShear', 960, 1.0, 225.4),
    ('PlateShear', 60, 2.0, 0.005),
    ('PlateShear', 120, 2.0, 3.350),
    ('PlateShear', 240, 2.0, 1.369),
    ('PlateShear', 480, 2.0, 18.03),
    ('PlateShear', 960, 2.0, 24.02),
    ('PlateShear', 60, 3.0, 0.020),
    ('PlateShear', 120, 3.0, 2.210),
    ('PlateShear', 240, 3.0, 0.290),
    ('PlateShear', 480, 3.0, 3.010),
    ('PlateShear', 960, 3.0, 19.54),
]

with open(filepath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['flow', 'Reynolds', 'k', 'error_percent'])
    for row in rows:
        writer.writerow(row)

print(f"Written {len(rows)} rows to {filepath}")
PYEOF

# === solve finalize ===
echo 'Oracle solve.sh finished.'
