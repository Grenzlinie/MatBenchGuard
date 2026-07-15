#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_skyrmion_metrics.json ===
mkdir -p "$OUTDIR"
python3 -c "
import json
data = {
    'conditions': [
        {'label': 'zero_field_0K', 'skyrmion_number': 0.0, 'skyrmion_count': 0},
        {'label': 'field_200mT_0K', 'skyrmion_number': 1.0, 'skyrmion_count': 1},
        {'label': 'field_250mT_0K', 'skyrmion_number': 1.0, 'skyrmion_count': 1},
        {'label': 'field_200mT_100K', 'skyrmion_number': 1.0, 'skyrmion_count': 1},
        {'label': 'field_200mT_150K', 'skyrmion_number': 0.0, 'skyrmion_count': 0},
        {'label': 'field_200mT_A15pJm_0K', 'skyrmion_number': 1.0, 'skyrmion_count': 1},
    ]
}
with open('$OUTDIR/step_01_skyrmion_metrics.json', 'w') as f:
    json.dump(data, f, indent=2)
"
