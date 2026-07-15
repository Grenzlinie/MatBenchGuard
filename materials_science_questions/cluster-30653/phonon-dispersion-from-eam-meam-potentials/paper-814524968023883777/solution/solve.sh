#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p "/app/outputs"

# === solve block: tp_melting_curve.csv ===
python3 -c "
import csv, math

# Generate melting curve points from Simon equation
# Tm = Tm0 * (P/a + 1)^b  with Tm0=1250 K, a=28.25 GPa, b=0.59
Tm0, a, b = 1250.0, 28.25, 0.59
pressures = [i*15 for i in range(11)]  # 0 to 150 GPa
rows = []
for p in pressures:
    tm = Tm0 * (p / a + 1)**b
    rows.append((p, round(tm, 2)))

with open('$OUTDIR/tp_melting_curve.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['pressure_GPa', 'melting_temperature_K'])
    for p, t in rows:
        w.writerow([p, t])
"

# === solve block: sm_melting_curve.csv ===
python3 /solution/generate.py sm_melting_curve.csv

# === solve block: simon_fit.json ===
python3 /solution/generate.py simon_fit.json
