#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_02_ICOHP_values.json ===
python3 -c "
import json
data = {
    'B_Ir_ICOHP': -2.06,
    'Zr_Ir_ICOHP': -0.99,
    'Ir_Ir_empty_ICOHP': -0.74,
    'Ir_Ir_filled_ICOHP': -0.37
}
with open('/app/outputs/step_02_ICOHP_values.json', 'w') as f:
    json.dump(data, f, indent=2)
"
