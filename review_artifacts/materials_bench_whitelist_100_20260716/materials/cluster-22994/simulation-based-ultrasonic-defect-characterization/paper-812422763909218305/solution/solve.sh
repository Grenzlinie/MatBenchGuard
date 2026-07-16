#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: optimized_lens_parameters.json ===
python3 << 'PYEOF'
import json

data = {
    "Fx_in": 2.25,
    "Fy_in": 2.58,
    "waterpath_in": 1.61
}
with open('/app/outputs/optimized_lens_parameters.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF
