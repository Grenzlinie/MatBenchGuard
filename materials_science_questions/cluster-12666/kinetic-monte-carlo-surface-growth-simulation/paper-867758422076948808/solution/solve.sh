#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
# Oracle preamble: no installs needed, python3 available.

# === solve block: barriers.json ===
python3 << 'PYEOF'
import json

barriers = {
    "Fe": {"E1": 4.32, "E2": 1.72, "E3": 2.76},
    "Co": {"E1": 10.7, "E2": 0.0034, "E3": 0.0065}
}

with open("/app/outputs/barriers.json", "w") as f:
    json.dump(barriers, f, indent=2)
PYEOF

# === solve block: fe_reversal_times.csv ===
python3 /solution/compute_taus.py fe /app/outputs/fe_reversal_times.csv

# === solve block: co_reversal_times.csv ===
python3 /solution/compute_taus.py co /app/outputs/co_reversal_times.csv
