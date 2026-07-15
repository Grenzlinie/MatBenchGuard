#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: alpha_values.json ===
python3 - <<'PYEOF'
import json

data = [
    {"structure": "fcc",     "alpha_min": 0.458, "alpha_max": 0.592, "alpha_avg": 0.561},
    {"structure": "hcp",     "alpha_min": 0.458, "alpha_max": 0.582, "alpha_avg": None},
    {"structure": "bcc",     "alpha_min": 0.445, "alpha_max": 0.630, "alpha_avg": 0.546},
    {"structure": "diamond", "alpha_min": 0.289, "alpha_max": 0.500, "alpha_avg": 0.433},
    {"structure": "sc",      "alpha_min": 0.333, "alpha_max": 0.577, "alpha_avg": 0.500},
]

with open("/app/outputs/alpha_values.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
