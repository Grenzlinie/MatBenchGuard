#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: results.json ===
# Write the scored results.json with the four required keys.
# Q: estimated thermal shock intensity in J/(hr·cm³).
# residual_sigma_theta_at_a: -0.41 * 13790.6 = -5654.146 N/cm².
# S_over_sigma_ys: 0.77
# improvement_percentage: 33.44%
cat > "$OUTDIR/results.json" <<'FFEOF'
{
  "Q": 350000,
  "residual_sigma_theta_at_a": -5654.146,
  "S_over_sigma_ys": 0.77,
  "improvement_percentage": 33.44
}
FFEOF
