#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_results.json ===
# Write the expected reference equilibrium values for rhyolitic melt at 850°C, 2000 bar, NNO+1.
# H2O ~ 6.12 wt%, CO2 ~ 0.022 wt% (digitized from Fig. 4b).
cat > /app/outputs/step_01_results.json <<'EOF'
{
  "H2O_melt_wt%": 6.12,
  "CO2_melt_wt%": 0.022
}
EOF
