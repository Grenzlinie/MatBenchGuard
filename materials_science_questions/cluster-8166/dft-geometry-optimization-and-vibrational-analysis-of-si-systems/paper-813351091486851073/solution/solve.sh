#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_results.json ===
cat > "$OUTDIR/step_01_results.json" <<'EOF'
{
  "Z0_SiO2": 1.02,
  "Z0_GeO2": 1.05,
  "angle_min_covalent_only": 40.0,
  "angle_min_with_repulsion": 18.0,
  "dZ_dtheta_SiO2": -1.33,
  "alpha_quartz": 2.37,
  "beta_cristobalite": 2.05,
  "vitreous_silica": 2.11,
  "GeO2_quartzlike": 2.89,
  "e_x_SiO2": 0.45,
  "e_y_SiO2": 1.02,
  "e_z_SiO2": 2.74,
  "RoverPx_deriv_SiO2": -1.37,
  "e_x_GeO2": 0.21,
  "e_y_GeO2": 1.05,
  "e_z_GeO2": 2.54,
  "RoverPx_deriv_GeO2": -1.15
}
EOF
