#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_grain_refinement_strength.json ===
python3 -c "import math, json; k=2.4; d_mm=2e-3; d0_mm=8e-3; dsi=k*(d_mm**(-0.5) - d0_mm**(-0.5)); json.dump({'delta_sigma_i': dsi}, open('/app/outputs/step_01_grain_refinement_strength.json','w'))"

# === solve block: step_02_dislocation_strength.json ===
python3 -c "import json; json.dump({'delta_sigma_p': 200.0}, open('/app/outputs/step_02_dislocation_strength.json','w'))"
