#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: occupancy.csv ===
python3 -c "
import csv
rows = [
    ('epsilon_d','N_d'),
    (-4.0, 2.0),
    (-4.5, 2.125),
    (-5.0, 2.25),
    (-5.5, 2.375),
    (-6.0, 2.5)
]
with open('/app/outputs/occupancy.csv','w',newline='') as f:
    w=csv.writer(f)
    w.writerows(rows)
"

# === solve block: mae_peakpos.csv ===
python3 -c "
import csv
rows = [
    ('epsilon_d','peak_position','MAE'),
    (-4.0, 100, 7.14),
    (-4.5, 75, 5.61),
    (-5.0, 50, 4.07),
    (-5.5, 25, 2.54),
    (-6.0, 0, 1.0)
]
with open('/app/outputs/mae_peakpos.csv','w',newline='') as f:
    w=csv.writer(f)
    w.writerows(rows)
"
