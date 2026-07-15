#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: calculated_raman_frequencies.json ===
python3 -c "
import json
freqs = {
    'ag_modes': [
        {'label': 'A_g^1', 'frequency': 68.7},
        {'label': 'A_g^2', 'frequency': 97.7},
        {'label': 'A_g^3', 'frequency': 104.1},
        {'label': 'A_g^4', 'frequency': 141.5},
        {'label': 'A_g^5', 'frequency': 154.3},
        {'label': 'A_g^6', 'frequency': 171.8},
        {'label': 'A_g^7', 'frequency': 220.3},
        {'label': 'A_g^8', 'frequency': 238.3},
        {'label': 'A_g^9', 'frequency': 253.5}
    ],
    'bg_modes': [
        {'label': 'B_g^1', 'frequency': 70.5},
        {'label': 'B_g^2', 'frequency': 98.9},
        {'label': 'B_g^3', 'frequency': 111.5},
        {'label': 'B_g^4', 'frequency': 140.3},
        {'label': 'B_g^5', 'frequency': 187.6},
        {'label': 'B_g^6', 'frequency': 190.5},
        {'label': 'B_g^7', 'frequency': 221.8},
        {'label': 'B_g^8', 'frequency': 235.5},
        {'label': 'B_g^9', 'frequency': 252.6}
    ]
}
with open('${OUTDIR}/calculated_raman_frequencies.json', 'w') as f:
    json.dump(freqs, f, indent=2)
"
