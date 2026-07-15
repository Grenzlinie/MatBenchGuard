#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.json ===
python3 -c "
import json
with open('$OUTDIR/results.json', 'w') as f:
    json.dump({
        'activation_barrier_gamma': 2.2,
        'activation_barrier_eta': 5.0,
        'subsurface_energy_gain_gamma': 1.5
    }, f)
"
