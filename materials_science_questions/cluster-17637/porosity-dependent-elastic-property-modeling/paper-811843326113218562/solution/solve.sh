#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: wave_speeds.json ===
python3 <<'PYEOF'
import json
data = {
    "two_elastic_solids": {
        "P_wave_1": 5.94,
        "P_wave_2": 4.36,
        "S_wave_1": 4.92,
        "S_wave_2": 3.28
    },
    "porous_medium": {
        "P_wave_1": 3.35,
        "P_wave_2": 0.55,
        "S_wave": 1.26,
        "porosity_wave": 2.92
    }
}
with open("/app/outputs/wave_speeds.json", "w") as f:
    json.dump(data, f)
PYEOF
