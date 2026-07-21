#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_modal_coefficients.json ===
cat > /app/outputs/step_01_modal_coefficients.json <<'FFEOF'
{
  "A": [9.17e11, -6.91e11, 4.27e11, -2.17e10],
  "B": [9.20e12, -5.78e12, 2.26e12, -9.29e10]
}
FFEOF

# === solve block: step_02_verification.json ===
cat > /app/outputs/step_02_verification.json <<'FFEOF'
{
  "stress_ratio_contact": 15.0,
  "shear_dominant": true,
  "peak_frequency_khz": 78.0,
  "attenuation_depth_mm": 2.5
}
FFEOF
