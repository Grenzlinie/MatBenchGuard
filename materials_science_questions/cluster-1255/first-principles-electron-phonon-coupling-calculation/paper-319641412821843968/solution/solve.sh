#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results.json ===
python3 -c "
import json
results = {
    'V0_Tc': 11.1,
    'V0.85_Tc': 4.9,
    'V0.70_Tc': 0.98,
    'V0_lambda_ac': 0.71,
    'V0_lambda_op': 0.21
}
with open('/app/outputs/results.json','w') as f:
    json.dump(results, f, indent=2)
"
