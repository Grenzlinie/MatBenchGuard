#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: constants.json ===
python3 -c "
import json
data = {
    'cation_A': 5.3,
    'cation_B': 4.7,
    'anion_A': 4.6,
    'anion_B': 19.0
}
with open('$OUTDIR/constants.json', 'w') as f:
    json.dump(data, f)
"
