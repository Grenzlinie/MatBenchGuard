#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: actuator_results.json ===
cat > /app/outputs/actuator_results.json << 'FFEOF'
{
  "em_driving_range_m": 0.00125,
  "em_max_force_N": 0.00015,
  "pe_max_displacement_m": 0.0000009,
  "pe_max_force_N": 0.012
}
FFEOF
