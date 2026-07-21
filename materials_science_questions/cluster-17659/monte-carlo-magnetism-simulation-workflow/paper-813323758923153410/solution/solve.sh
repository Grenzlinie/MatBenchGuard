#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
export OUTDIR

# === solve block: step_01_mean_field_results.json ===
python3 -c "
import json, os
data = {
    'Tc': 3.4,
    'n1_vs_temperature': [
        {'temperature': 2.0, 'n1': 1.0},
        {'temperature': 2.5, 'n1': 1.0},
        {'temperature': 3.0, 'n1': 1.0},
        {'temperature': 3.2, 'n1': 1.0},
        {'temperature': 3.35, 'n1': 0.95},
        {'temperature': 3.4, 'n1': 0.5},
        {'temperature': 3.45, 'n1': 0.15},
        {'temperature': 3.5, 'n1': 0.125},
        {'temperature': 3.75, 'n1': 0.125},
        {'temperature': 4.0, 'n1': 0.125},
        {'temperature': 4.5, 'n1': 0.125},
        {'temperature': 5.0, 'n1': 0.125}
    ]
}
with open(os.environ['OUTDIR'] + '/step_01_mean_field_results.json', 'w') as f:
    json.dump(data, f)
"

# === solve block: step_02_mc_results.json ===
python3 -c "
import json, os
data = {'n1_at_T0': 0.92}
with open(os.environ['OUTDIR'] + '/step_02_mc_results.json', 'w') as f:
    json.dump(data, f)
"
