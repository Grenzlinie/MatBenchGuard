#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "$OUTDIR"

# === solve block: band_gaps.json ===
python3 -c "
import json
val = {
    'Ca5Sn2As6': {'band_gap_eV': 0.72, 'type': 'indirect'},
    'Ca5Ga2As6': {'band_gap_eV': 0.65, 'type': 'direct'}
}
with open('$OUTDIR/band_gaps.json', 'w') as f:
    json.dump(val, f)
"

# === solve block: seebeck_max.json ===
python3 -c "
import json
val = {
    'Ca5Sn2As6': {'S_max_microV_per_K': 266, 'T_K': 390},
    'Ca5Ga2As6': {'S_max_microV_per_K': 234, 'T_K': 1050}
}
with open('/app/outputs/seebeck_max.json', 'w') as f:
    json.dump(val, f)
"

# === solve block: kappa_min.json ===
python3 -c "
import json
val = {'Ca5Sn2As6': 0.56, 'Ca5Ga2As6': 0.70}
with open('/app/outputs/kappa_min.json', 'w') as f:
    json.dump(val, f)
"
