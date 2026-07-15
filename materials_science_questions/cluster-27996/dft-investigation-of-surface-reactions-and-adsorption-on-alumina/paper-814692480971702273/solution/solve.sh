#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: adsorption_energies.json ===
cat > /app/outputs/adsorption_energies.json <<'FFEOF'
{
  "A3_deltaE0": -1.71,
  "A4_deltaE0": -1.77
}
FFEOF

# === solve block: barriers_and_temperatures.json ===
cat > /app/outputs/barriers_and_temperatures.json <<'FFEOF'
{
  "TS2_DeltaEdd": 1.03,
  "TS4_DeltaEdd": 0.69,
  "T_des_TS2": 495,
  "T_des_TS4": 370
}
FFEOF
