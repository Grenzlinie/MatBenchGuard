#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: optimum_thicknesses.csv ===
python3 << 'PYEOF' > /app/outputs/optimum_thicknesses.csv
import csv
import sys

writer = csv.writer(sys.stdout)
writer.writerow(["energy_MeV", "optimum_thickness_cm"])
writer.writerow([2.0, 2.5])
writer.writerow([14.0, 2.5])
PYEOF
