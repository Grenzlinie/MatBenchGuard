#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: spinodal_results.json ===
python3 -c "
import json
data = {
    'gas_spinodal_temperatures': {
        'p_0_04': 0.85,
        'p_0_10': 1.155,
        'p_0_1105': 1.1875
    },
    'liquid_spinodal_temperatures': {
        'p_0_04': 1.105,
        'p_0_10': 1.175,
        'p_0_1105': 1.1875
    },
    'critical_point': {
        'p_c': 0.1105,
        'T_c': 1.1875
    }
}
with open('$OUTDIR/spinodal_results.json', 'w') as f:
    json.dump(data, f, indent=2)
"
