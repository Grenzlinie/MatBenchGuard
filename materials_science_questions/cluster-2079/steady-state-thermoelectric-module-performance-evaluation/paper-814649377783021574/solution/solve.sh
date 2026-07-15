#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_temperature_differences.json ===
python3 -c "import json; json.dump({'A1_deltaT': 26.22, 'B5_deltaT': 17.21}, open('/app/outputs/step_01_temperature_differences.json','w'))"
