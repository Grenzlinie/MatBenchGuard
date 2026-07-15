#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: predictions.csv ===
OUTDIR=/app/outputs
python3 > $OUTDIR/predictions.csv << 'PYEOF'
import csv
import sys

header = ["boundary", "misorientation_angle", "predicted_energy", "predicted_X", "predicted_Y", "predicted_Z"]

data = [
    ("Sigma61/(11 1 0)", 10.39, 0.55, 0.0, 0.0, 0.0),
    ("Sigma41/(910)",    12.68, 0.66, 0.0, 0.0, 0.0),
    ("Sigma25/(710)",    16.26, 0.62, 0.0, 0.0, 0.0),
    ("Sigma37/(610)",    18.92, 0.71, 0.0, 0.0, 0.0),
    ("Sigma125/(11 2 0)",20.61, 0.73, 0.0, 0.0, 0.0),
    ("Sigma53/(720)",    31.89, 0.92, 0.0, 0.0, 0.0),
    ("Sigma29/(520)",    43.60, 1.10, 0.0, 0.0, 0.0),
    ("Sigma29/(730)",    46.40, 1.08, 0.0, 0.0, 0.0),
    ("Sigma53/(950)",    58.11, 0.98, 0.0, 0.0, 0.0),
    ("Sigma13/(230)",    67.38, 0.96, 5.0, 1.0, 0.0),
    ("Sigma37/(750)",    71.08, 0.97, 0.0, 0.0, 0.0),
    ("Sigma25/(430)",    73.74, 0.95, 0.0, 0.0, 0.0),
    ("Sigma41/(540)",    77.32, 0.60, 0.0, 0.0, 0.0),
]

writer = csv.writer(sys.stdout)
writer.writerow(header)
writer.writerows(data)
PYEOF
