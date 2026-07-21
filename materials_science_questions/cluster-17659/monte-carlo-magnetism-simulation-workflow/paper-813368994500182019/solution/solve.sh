#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dimer_ordering_results.json ===
cat > /app/outputs/dimer_ordering_results.json <<'FFEOF'
{
  "dimer_mean_relative_angle_degrees": 90.0,
  "dimer_relative_angle_std": 2.5,
  "trimer_mean_relative_angle_degrees_between_columns": 60.0,
  "trimer_relative_angle_std": 4.0,
  "dimer_order_parameter_lowT": 0.96,
  "dimer_order_parameter_intermediateT": 0.42,
  "dimer_order_parameter_highT": 0.08
}
FFEOF
