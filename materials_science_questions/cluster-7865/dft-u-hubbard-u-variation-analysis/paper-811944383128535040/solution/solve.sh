#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_properties.json ===
cat > /app/outputs/computed_properties.json <<'FFEOF'
{
  "Eu_4f_up_peak": -2.10,
  "Eu_4f_down_peak1": 2.92,
  "Eu_4f_down_peak2": 2.40,
  "Delta_x_f": -7.98,
  "Delta": 0.095,
  "total_magnetic_moment": 6.23,
  "Eu_magnetic_moment": 5.83,
  "N_magnetic_moment": 0.10,
  "Ga_magnetic_moment": 0.09,
  "interstitial_magnetic_moment": 0.21,
  "N0_alpha": 0.21,
  "N0_beta": -1.09
}
FFEOF
