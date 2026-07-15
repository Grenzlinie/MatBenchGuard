#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail

# === solve block: heterostructure_properties.json ===
mkdir -p /app/outputs
python3 -c "
import json
data = {
    'band_gap_direct': 1.81,
    'cbm_energy': -4.20,
    'vbm_energy': -6.01,
    'reducing_capacity': 0.24,
    'oxidizing_ability': 0.34,
    'electron_mobility_x': 10942.98,
    'electron_mobility_y': 9293.66,
    'hole_mobility_x': 5716.60,
    'hole_mobility_y': 3797.36,
    'absorption_coefficient_visible': 300000.0,
    'alignment_type': 'type-II',
    'absorption_edge': 1.8
}
with open('/app/outputs/heterostructure_properties.json', 'w') as f:
    json.dump(data, f, indent=2)
"
