#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: optimum_parameters.json ===
python3 - <<'PYEOF'
import json
data = {
    "optimum_parameters": {
        "tool_passes": 1,
        "rotational_speed": 965.20,
        "transverse_speed": 23.69
    },
    "predicted_tensile_strength": 170.90
}
with open("/app/outputs/optimum_parameters.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: model_comparison.json ===
python3 - <<'PYEOF'
import json
predicted = 170.90
experimental = 162.89
base = 135.0
deviation = (predicted - experimental) / predicted * 100
improvement = (experimental - base) / base * 100
data = {
    "experimental_tensile_strength": experimental,
    "predicted_tensile_strength": predicted,
    "deviation_percentage": round(deviation, 2),
    "improvement_percentage": round(improvement, 2)
}
with open("/app/outputs/model_comparison.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
