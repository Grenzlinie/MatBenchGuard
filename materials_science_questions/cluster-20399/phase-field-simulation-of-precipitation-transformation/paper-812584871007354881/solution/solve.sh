#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: cooling_curves.csv ===
python3 << 'PYEOF'
import csv, math

OUTDIR = '/app/outputs'
t0 = 1113.15
te = 298.15
k_surface = 0.03
k_center = 0.015

rows = []
rows.append(['time', 'temperature_surface', 'temperature_center'])
for t in range(0, 201, 2):
    ts = te + (t0 - te) * math.exp(-k_surface * t)
    tc = te + (t0 - te) * math.exp(-k_center * t)
    rows.append([t, round(ts, 2), round(tc, 2)])

with open(f"{OUTDIR}/cooling_curves.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
PYEOF

# === solve block: phase_fractions.csv ===
python3 /solution/generate_outputs.py --output /app/outputs/phase_fractions.csv

# === solve block: von_mises_stress.csv ===
python3 /solution/generate_outputs.py --output /app/outputs/von_mises_stress.csv

# === solve block: volume_change.csv ===
python3 /solution/generate_outputs.py --output /app/outputs/volume_change.csv

# === solve block: dimensional_change.csv ===
python3 /solution/generate_outputs.py --output /app/outputs/dimensional_change.csv

# === solve block: hardness_profile.csv ===
python3 /solution/generate_outputs.py --output /app/outputs/hardness_profile.csv
