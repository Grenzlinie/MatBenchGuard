#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: bridge_factors.json ===
python3 -c '
import json
result = {
    "w": 2/3,
    "f_expression": "2*h/9",
    "hetero_f_for_m0": 0.5,
    "condition": "h < 9/4"
}
with open("/app/outputs/bridge_factors.json", "w") as f:
    json.dump(result, f, indent=2)
'
