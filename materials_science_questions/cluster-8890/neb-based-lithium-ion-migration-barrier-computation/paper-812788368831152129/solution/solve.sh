#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: binding_energies.json ===
python3 -c "
import json
data = {
    'h567': {'pentagon': -0.394, 'hexagon': -0.389, 'heptagon': -0.437},
    'r57': {'pentagon': -0.432, 'heptagon': -0.485},
    'o567': {'pentagon': 0.211, 'hexagon': 0.064, 'heptagon': 0.091}
}
with open('$OUTDIR/binding_energies.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: diffusion_barriers.json ===
python3 -c "
import json
data = {
    'h567': {'Ea_6-5': 0.21, 'Ea_5-6': 0.27},
    'r57': {'Ea_5-5': 0.22, 'Ea_5-7': 0.30, 'Ea_7-5': 0.36},
    'o567': {'Ea_5-5': 0.13, 'Ea_5-7': 0.22, 'Ea_7-5': 0.34}
}
with open('$OUTDIR/diffusion_barriers.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: specific_capacity.json ===
python3 -c "
import json
data = {
    'h567': {
        'capacity_mAh_per_g': 697.32,
        'condition': 'both sides lithiation'
    }
}
with open('$OUTDIR/specific_capacity.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: average_ocv.json ===
python3 -c "
import json
data = {'h567': 0.26}
with open('$OUTDIR/average_ocv.json', 'w') as f:
    json.dump(data, f, indent=2)
"
