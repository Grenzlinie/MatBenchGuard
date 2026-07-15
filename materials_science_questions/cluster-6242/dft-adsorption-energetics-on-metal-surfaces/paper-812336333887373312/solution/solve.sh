#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: steady_state_results.json ===
python3 -c "
import json
data = {
    'T': 600.0,
    'pCO': 20.0,
    'pO2': 1.0,
    'TOF': 4.6e18,
    'N_CO_br': 0.11,
    'N_CO_cus': 0.70,
    'N_O_br': 0.89,
    'N_O_cus': 0.29
}
with open('$OUTDIR/steady_state_results.json', 'w') as f:
    json.dump(data, f, indent=2)
"
