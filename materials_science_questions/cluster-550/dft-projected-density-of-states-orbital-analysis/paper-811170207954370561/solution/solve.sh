#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# Ensure Python3 is available (the sandbox image includes it)

# === solve block: step_01_structural_params.json ===
cat > /app/outputs/step_01_structural_params.json << 'FFEOF'
{
  "a0": 4.207460,
  "z": 0.198864,
  "B_B_in": 1.79183,
  "B_B_out": 1.67343
}
FFEOF

# === solve block: step_02_elastic_constants.json ===
cat > /app/outputs/step_02_elastic_constants.json << 'FFEOF'
{
  "C11": 349.57400,
  "C12": 26.38020,
  "C44": 86.72740
}
FFEOF

# === solve block: step_03_optical_properties.json ===
cat > /app/outputs/step_03_optical_properties.json << 'FFEOF'
{
  "epsilon2_peak_energy": 5.52,
  "epsilon2_peak_value": 10.0,
  "absorption_peak_energy": 1.15,
  "absorption_peak_value": 128686.0,
  "reflectivity_min_energy": 1.73,
  "reflectivity_min_value": 0.02
}
FFEOF

# === solve block: step_04_transmittance_curve.csv ===
python3 /solution/write_transmittance.py > /app/outputs/step_04_transmittance_curve.csv
