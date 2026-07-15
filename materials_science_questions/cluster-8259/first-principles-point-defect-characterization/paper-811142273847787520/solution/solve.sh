#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results.json ===
python3 -c "
import json

data = {
    'Si_E1': 0.074,
    'Si_E2': 0.144,
    'Si_a1': 13.4,
    'Si_a2': 24.4,
    'SiO2_E1': 0.916,
    'SiO2_E2': 2.02,
    'SiO2_a1': 2.27,
    'SiO2_a2': 4.13
}

with open('/app/outputs/results.json', 'w') as f:
    json.dump(data, f, indent=2)
"
