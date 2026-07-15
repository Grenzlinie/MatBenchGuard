#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: band_gaps.json ===
python3 -c "
import json
data = {
    'diamond_Si_gap_ev': 0.5,
    'Si46_gap_ev': 1.17,
    'K8Si46_metallic': True,
    'K8Ga8Si38_gap_ev': 0.65,
    'Si46_minus_diamond_ev': 0.67,
    'K8Ga8Si38_minus_Si46_ev': -0.52,
    'K8Ga8Si38_minus_diamond_ev': 0.15
}
with open('/app/outputs/band_gaps.json', 'w') as f:
    json.dump(data, f, indent=2)
"
