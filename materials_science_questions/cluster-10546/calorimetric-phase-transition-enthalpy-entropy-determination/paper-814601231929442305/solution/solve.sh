#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: transition_temperatures.csv ===
python3 - <<PYEOF
import csv
data = [
    ("SolubilityExtrapolation", 93.29),
    ("DeltaHtr", 90.59),
    ("MeltingData", 108.37),
    ("GcPhase_eq19", 109.25),
    ("GcPhase_eq20", 109.28),
]
with open("$OUTDIR/transition_temperatures.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["method", "T_tr_C"])
    writer.writerows(data)
PYEOF
