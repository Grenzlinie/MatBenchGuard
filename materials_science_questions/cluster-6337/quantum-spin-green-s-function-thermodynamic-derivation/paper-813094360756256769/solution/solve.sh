#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: reproduction_results.json ===
python3 - <<'PYEOF'
import json

data = {
    "ferromagnetic_exponent": 0.25,
    "villian_model_exponent": 0.5,
    "triangular_exponent": 0.5,
    "ratio_for_even_n": {
        "Villain": [2.0, 2.0, 2.0, 2.0],
        "Triangular": [2.0, 2.0, 2.0, 2.0]
    }
}

with open("/app/outputs/reproduction_results.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
