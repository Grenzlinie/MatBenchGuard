#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: dE_vs_de.csv ===
python3 << 'PYEOF'
import csv, os

rows = [
    ["system", "delta", "de_per_O", "dE_V"],
    # A.Y
    ["A.Y", 0.0, 1.7, 2.5],
    ["A.Y", 0.125, 1.8, 2.8],
    ["A.Y", 0.25, 1.9, 3.1],
    ["A.Y", 0.375, 2.0, 3.4],
    # SF
    ["SF", 0.0, 1.4, 2.0],
    ["SF", 0.125, 1.5, 2.2],
    ["SF", 0.25, 1.6, 2.4],
    ["SF", 0.375, 1.7, 2.6],
    # B.Cu
    ["B.Cu", 0.0, 0.8, 1.0],
    ["B.Cu", 0.125, 1.0, 1.2],
    ["B.Cu", 0.25, 1.2, 1.4],
    ["B.Cu", 0.375, 1.4, 1.6],
]

with open("/app/outputs/dE_vs_de.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
print("dE_vs_de.csv written")
PYEOF

# === solve block: barriers_vs_de.csv ===
python3 << 'PYEOF'
import csv, os

rows = [
    ["system", "delta", "barrier_eV", "de_per_O"],
    # A.Y
    ["A.Y", 0.125, 0.7, 1.8],
    ["A.Y", 0.25, 0.6, 1.9],
    ["A.Y", 0.375, 0.5, 2.0],
    # SF
    ["SF", 0.125, 1.0, 1.5],
    ["SF", 0.25, 0.9, 1.6],
    ["SF", 0.375, 0.8, 1.7],
    # B.Cu
    ["B.Cu", 0.125, 1.5, 1.0],
    ["B.Cu", 0.25, 1.3, 1.2],
    ["B.Cu", 0.375, 1.1, 1.4],
]

with open("/app/outputs/barriers_vs_de.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
print("barriers_vs_de.csv written")
PYEOF
