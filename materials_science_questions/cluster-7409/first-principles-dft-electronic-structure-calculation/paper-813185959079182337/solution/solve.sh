#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: lattice_parameters.json ===
python3 -c "
import json
data = {
    'pristine': {'a': 3.782, 'c': 9.496, 'volume': 543.34},
    'Ag_6.25': {'a': 3.800, 'c': 9.528, 'volume': 550.40},
    'Ag_12.5': {'a': 3.818, 'c': 9.572, 'volume': 557.08},
    'Ag_18.75': {'a': 3.845, 'c': 9.586, 'volume': 561.11}
}
with open('/app/outputs/lattice_parameters.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: pristine_band_gap.txt ===
echo "3.16" > /app/outputs/pristine_band_gap.txt
