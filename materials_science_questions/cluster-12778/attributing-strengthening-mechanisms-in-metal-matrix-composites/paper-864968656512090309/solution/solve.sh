#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_prediction.json ===
cat > /app/outputs/step_01_prediction.json <<'FFEOF'
{
  "yield_strength_MPa": 1266,
  "interface_strengthening_MPa": 421,
  "dislocation_strengthening_MPa": 120,
  "solid_solution_strengthening_MPa": 280,
  "precipitation_strengthening_MPa": 445
}
FFEOF
