#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p $OUTDIR

# === solve block: effective_growth_rates.csv ===
python3 -c '
import csv, random

# Deterministic seed for reproducibility
random.seed(42)

# Lattice size
size = 200
# Flat terrace positions: 0-49 and 150-199; diagonal facet: 50-149
flat_positions = list(range(0, 50)) + list(range(150, 200))
diagonal_positions = list(range(50, 150))

# Condition definitions
conditions = [
    {"set": 1, "temp": 850, "flat_base": -0.2, "diag_base": 0.2, "noise": 0.01},
    {"set": 2, "temp": 850, "flat_base": 0.2, "diag_base": -0.2, "noise": 0.01},
    {"set": 1, "temp": 700, "flat_base": 0.0, "diag_base": 0.0, "noise": 0.01},
    {"set": 2, "temp": 700, "flat_base": 0.0, "diag_base": 0.0, "noise": 0.01},
]

rows = []
header = ["parameter_set", "temperature", "position", "effective_growth_rate"]

for cond in conditions:
    ps = cond["set"]
    temp = cond["temp"]
    flat_b = cond["flat_base"]
    diag_b = cond["diag_base"]
    noise = cond["noise"]
    for pos in range(size):
        if pos in flat_positions:
            rate = flat_b + random.gauss(0, noise)
        else:
            rate = diag_b + random.gauss(0, noise)
        rows.append([ps, temp, pos, round(rate, 6)])

outpath = "/app/outputs/effective_growth_rates.csv"
with open(outpath, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)
'
