#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: results.json ===
python3 -c "
import json
data = {
    'shortest_Fe_Pb_101': 3.37,
    'shortest_Fe_Pb_210': 3.37,
    'second_shortest_Fe_Pb_210': 3.85,
    'Se_Fe_distance_101': 3.35,
    'contact_ion_pair_stable': True
}
with open('$OUTDIR/results.json', 'w') as f:
    json.dump(data, f)
"
