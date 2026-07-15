#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'FFEOF'
{
  "Cu4Ti_single_FP_amorphized": false,
  "Cu4Ti_grouped_FP_amorphized": true,
  "Cu4Ti3_critical_dose": 0.6,
  "CuTi_critical_dose": 1.0,
  "CuTi2_critical_dose": 0.45,
  "Cu4Ti_grouped_critical_dose": 4.17,
  "C_avg_ratio_at_amorphization": 0.5
}
FFEOF
