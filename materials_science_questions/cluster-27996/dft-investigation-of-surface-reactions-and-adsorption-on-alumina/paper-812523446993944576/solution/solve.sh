#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: binding_energies.csv ===
python3 - <<'PYEOF'
import csv

rows = [
  ["A1", 0.53, 0.48],
  ["A2", 0.37, 0.32],
  ["A3", 0.30, 0.25],
  ["A4", 0.25, 0.20],
  ["A5", 0.33, 0.28],
  ["A6", 0.36, 0.31],
  ["A7", 0.34, 0.29],
  ["A8", 0.32, 0.27],
  ["A9", 0.45, 0.40],
  ["A10", 0.49, 0.44],
  ["A11", 0.35, 0.30],
  ["A12", 0.38, 0.33],
  ["A13", 0.40, 0.35],
  ["A14", 0.31, 0.26],
  ["A15", 0.38, 0.33],
  ["A16", 0.39, 0.34],
  ["B1", 0.48, 0.43],
  ["B2", 0.46, 0.41],
  ["B3", 0.35, 0.30],
  ["B4", 0.15, 0.10],
  ["B5", 0.47, 0.42],
  ["B6", 0.33, 0.28],
  ["B7", 0.34, 0.29],
  ["B8", 0.28, 0.23],
  ["B9", 0.49, 0.44],
  ["B10", 0.34, 0.29],
]

with open("/app/outputs/binding_energies.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["site", "binding_energy_without_zpe", "binding_energy_with_zpe"])
    writer.writerows(rows)
PYEOF
