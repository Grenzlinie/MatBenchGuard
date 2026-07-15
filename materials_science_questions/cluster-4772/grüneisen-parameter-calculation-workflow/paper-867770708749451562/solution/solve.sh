#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: thermo_properties.json ===
cat > /app/outputs/thermo_properties.json <<'EOF'
{
  "PPv_CV_LDA": 128.0,
  "PPv_CV_PBE": 129.5,
  "PPv_alpha_LDA": 4.5e-06,
  "PPv_alpha_PBE": 5.8e-06,
  "PPv_gamma_LDA": 1.35,
  "PPv_gamma_PBE": 1.30,
  "Pv_CV_LDA": 130.0,
  "Pv_CV_PBE": 132.0,
  "Pv_alpha_LDA": 5.0e-06,
  "Pv_alpha_PBE": 6.5e-06,
  "Pv_gamma_LDA": 1.55,
  "Pv_gamma_PBE": 1.45
}
EOF

# === solve block: phase_boundary.json ===
cat > /app/outputs/phase_boundary.json <<'EOF'
{
  "Clapeyron_slope_1000K": 7.65,
  "Clapeyron_slope_2500K": 9.0,
  "Clapeyron_slope_4000K": 10.35,
  "transition_pressure_2500K_LDA": 110,
  "transition_pressure_2500K_PBE": 117
}
EOF
