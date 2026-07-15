#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_phase_fractions.json ===
cat > "/app/outputs/step_01_phase_fractions.json" << 'FFEOF'
{
  "alloy1_vol_frac_ferrite_850C": 0.49,
  "alloy1_vol_frac_M7C3_850C": 0.51,
  "alloy2_stable_phase_at_800C": "ferrite+M7C3",
  "alloy1_vol_frac_austenite_1300C": 0.57
}
FFEOF

# === solve block: step_02_partition_coefficient.json ===
cat > "/app/outputs/step_02_partition_coefficient.json" << 'FFEOF'
{"Cr_partition_coefficient_1300C": 3.0}
FFEOF

# === solve block: step_03_silicon_effect.txt ===
echo 'Yes, austenite appears at high temperature after removing silicon' > "/app/outputs/step_03_silicon_effect.txt"
