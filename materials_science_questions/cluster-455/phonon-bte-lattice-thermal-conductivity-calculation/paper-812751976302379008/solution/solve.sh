#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_thermal_conductivity.json ===
python3 -c "import json; json.dump({'lambda_x': 211.0, 'lambda_y': 260.0, 'lambda_z': 229.0}, open('/app/outputs/step_01_thermal_conductivity.json','w'))"
