#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: crossover_and_ratio.csv ===
python3 << 'PYEOF'
import csv

data = [
    ["InSb", 3.4, 300/3.4, "cubic"],
    ["InAs", 13.4, 300/13.4, "cubic"],
    ["GaSb", 121, 300/121, "cubic"],
    ["In0.53Ga0.47As", 76, 300/76, "cubic"],
    ["InP", 304, 300/304, "equal"],
    ["In0.52Al0.48As", 507, 300/507, "quadratic"],
    ["GaAs", 306, 300/306, "equal"],
    ["CdTe", 310, 300/310, "equal"]
]

with open("/app/outputs/crossover_and_ratio.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["material", "T_star_K", "ratio_300K", "dominant_at_300K"])
    for row in data:
        writer.writerow(row)
PYEOF
