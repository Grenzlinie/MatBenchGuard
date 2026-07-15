#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_nucleation_results.json ===
cat > /app/outputs/step_01_nucleation_results.json <<'FFEOF'
{
  "r_star_673K": 0.442,
  "deltaG_star_673K": 5.08e-20,
  "r_star_923K": 0.313,
  "deltaG_star_923K": 2.54e-20
}
FFEOF
