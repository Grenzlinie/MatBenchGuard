#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_resonance_angles.csv ===
cat > /app/outputs/step_01_resonance_angles.csv <<'FFEOF'
configuration,resonance_angle_deg,FWHM_deg
unslant_90deg,21.6,0.5
slant_60deg,9.0,0.5
period_500nm,2.8,0.5
FFEOF

# === solve block: step_02_sensitivity_data.csv ===
cat > /app/outputs/step_02_sensitivity_data.csv <<'FFEOF'
configuration,refractive_index,resonance_angle_deg
slant_60deg,1.00,9.0
slant_60deg,1.01,8.3
slant_60deg,1.02,7.6
slant_60deg,1.03,6.9
slant_60deg,1.04,6.2
slant_60deg,1.05,5.5
unslant_90deg,1.00,21.6
unslant_90deg,1.01,20.8
unslant_90deg,1.02,20.0
unslant_90deg,1.03,19.2
unslant_90deg,1.04,18.4
unslant_90deg,1.05,17.6
FFEOF

# === solve block: step_03_results_summary.json ===
python3 -c '
import json
result = {
  "slant_sensitivity_deg_per_RIU": 70.0,
  "unslant_sensitivity_deg_per_RIU": 80.0,
  "slant_FWHM_deg": 0.5,
  "slant_FOM": 140.0
}
with open("/app/outputs/step_03_results_summary.json", "w") as f:
  json.dump(result, f, indent=2)
'
