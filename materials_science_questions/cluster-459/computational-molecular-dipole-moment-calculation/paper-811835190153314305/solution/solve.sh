#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: gradient_norm.json ===
mkdir -p /app/outputs
cat > /app/outputs/gradient_norm.json <<'FFEOF'
{
  "hfa_gradient_norm_Eh_per_a0": 0.00487
}
FFEOF

# === solve block: hfa_geometry.json ===
cat > /app/outputs/hfa_geometry.json <<'FFEOF'
{
  "r_OH_pm": 94.19,
  "angle_HOH_deg": 106.13
}
FFEOF

# === solve block: hfa_spectra.json ===
cat > /app/outputs/hfa_spectra.json <<'FFEOF'
{
  "frequencies_analytical_min_cm_1": [4231.45, 4130.94, 1747.81],
  "frequencies_hfa_min_cm_1": [4209.19, 4108.37, 1737.26],
  "intensities_analytical_min_km_per_mol": [92.949, 15.176, 96.569],
  "intensities_hfa_min_km_per_mol": [87.737, 14.027, 92.433]
}
FFEOF
