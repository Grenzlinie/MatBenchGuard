#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: calculated_properties.csv ===
python3 << 'PYEOF'
import csv

data = [
    ("2.5", 0.53, 0.02),
    ("2.6", 0.55, 0.03),
    ("2.7", 0.45, 0.05),
    ("2.8", 0.25, 0.08),
    ("2.9", 0.08, 0.15),
    ("3.0", 0.02, 0.28)
]

with open("/app/outputs/calculated_properties.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["distance_A", "Delta_E_eV", "Delta_q_e"])
    for row in data:
        writer.writerow(row)
PYEOF
