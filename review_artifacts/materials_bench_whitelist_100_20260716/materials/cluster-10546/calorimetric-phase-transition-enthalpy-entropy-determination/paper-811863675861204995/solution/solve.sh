#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_vibrational_frequencies.json ===
# Write the six corrected DFT-calculated wavenumbers from the paper's Table 1.
cat > /app/outputs/step_01_vibrational_frequencies.json <<'FFEOF'
{
  "CH2_scissoring_1": 1488,
  "CH2_scissoring_2": 1496,
  "CH3_asymmetric_stretching": 2932,
  "CH3_symmetric_deforming": 1378,
  "C_NH3_stretching": 1875,
  "NH3_asymmetric_bending": 1577
}
FFEOF
