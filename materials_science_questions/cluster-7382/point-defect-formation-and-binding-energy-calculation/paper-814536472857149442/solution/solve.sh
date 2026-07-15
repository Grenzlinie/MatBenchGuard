#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: interaction_energies.json ===
python3 -c "
import json
data = {
    'Al-Al': [0.13, 0.13, 0.01],
    'Cu-Cu': [-0.22, -0.06, -0.01],
    'S-S': [-0.54, -0.23, 0.09],
    'Al-Cu': [0.21, 0.09, 0.02],
    'Al-Vac': [-0.26, 0.0, -0.03],
    'Cu-Vac': [-0.23, -0.21, -0.05],
    'S-Vac': [-0.53, -0.39, 0.0]
}
with open('$OUTDIR/interaction_energies.json','w') as f:
    json.dump(data, f, indent=2)
"
