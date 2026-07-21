#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_bimorph_results.json ===
python3 - "$OUTDIR/step_01_bimorph_results.json" << 'PYEOF'
import json, sys

L = 0.04
b = 0.007
tp = 0.0005
t = 2*tp
Ep = 60.6e9
d31 = -274e-12
d311 = 2.85e-17

results = []
Ez = 0.0
while Ez <= 1e6 + 1e-9:
    factor = 1 + d311 * Ez * Ep
    delta = (3 * L**2 / (2 * t)) * factor * d31 * Ez
    Fbl = (3 * b * t**2 * Ep / (8 * L)) * factor * d31 * Ez
    results.append({
        "electric_field": Ez,
        "tip_deflection": delta,
        "blocking_force": Fbl
    })
    Ez += 5e4

with open(sys.argv[1], 'w') as f:
    json.dump(results, f, indent=2)
PYEOF

# === solve block: step_02_unimorph_results.json ===
python3 /solution/gen_outputs.py unimorph /app/outputs/step_02_unimorph_results.json
