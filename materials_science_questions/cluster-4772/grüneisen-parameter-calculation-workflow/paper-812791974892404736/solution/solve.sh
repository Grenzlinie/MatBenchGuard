#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_exact_slope_and_ratios.json ===
cat > /app/outputs/step_01_exact_slope_and_ratios.json <<'EOF'
{
  "exact_dS_dT_coefficient": 4.05,
  "exact_T1_T0": 0.89,
  "exact_T1": 1260,
  "simple_T1_T0": 0.83
}
EOF
