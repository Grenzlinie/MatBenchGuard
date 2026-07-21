#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p "/app/outputs"

# === solve block: step_01_energies_vs_lambda.json ===
python3 <<'FFEOF'
import json
data = {
    "lambda": [1.0, 1.2, 1.4, 1.6, 1.8, 2.0],
    "E_Gamma1": [None, None, 0.25, 0.43, 0.61, 0.78],
    "E_Gamma2": [0.02, 0.15, 0.44, 0.70, 0.88, 0.95]
}
with open("/app/outputs/step_01_energies_vs_lambda.json", "w") as f:
    json.dump(data, f, indent=2)
FFEOF
