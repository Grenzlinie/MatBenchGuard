#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: activation_barriers.json ===
python3 -c "
import json

barriers = {
    'low_coverage': {
        'Ni4/TiO2': 1.037,
        'Ni4/CeO2': 0.824,
        'Ni4/BNO': 0.798
    },
    'high_coverage': {
        'Ni4/TiO2': 0.475,
        'Ni4/CeO2': 0.352,
        'Ni4/BNO': 0.320
    }
}

with open('/app/outputs/activation_barriers.json', 'w') as f:
    json.dump(barriers, f, indent=2)
"
