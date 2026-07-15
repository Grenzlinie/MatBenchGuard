#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'FFEOF'
{
  "efficiency_50um_0deg_left": 0.30,
  "efficiency_50um_0deg_right": 0.70,
  "efficiency_50um_180deg_left": 0.70,
  "efficiency_50um_180deg_right": 0.30,
  "L_2pi_um": 0.478,
  "phase_200um_transmission_deg": 62.0,
  "efficiency_200um_transmission_right": 1.00,
  "phase_200um_reflection_deg": 242.0,
  "efficiency_200um_reflection_left": 1.00
}
FFEOF
