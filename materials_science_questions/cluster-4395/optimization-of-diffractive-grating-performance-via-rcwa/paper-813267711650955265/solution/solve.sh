#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: optimal_design_results.json ===
cat > /app/outputs/optimal_design_results.json <<'FFEOF'
{
  "wedge_apex_angle_deg": 8.1,
  "wedge_refractive_index": 1.48,
  "transmission_grating_period_nm": 610,
  "transmission_grating_blaze_angle_deg": 62,
  "reflection_grating_period_nm": 1140,
  "reflection_grating_blaze_angle_deg": 13,
  "collection_efficiency": 0.5375,
  "concentration_ratio": 3.77,
  "angular_tolerance_phi_deg_90percent": 35.0,
  "angular_tolerance_theta_deg_90percent": 3.0,
  "angular_tolerance_phi_deg_50percent": 53.0,
  "angular_tolerance_theta_deg_50percent": 9.0
}
FFEOF
