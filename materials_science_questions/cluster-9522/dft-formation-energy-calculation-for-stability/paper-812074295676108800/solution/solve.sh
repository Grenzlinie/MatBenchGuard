#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: formation_enthalpies.json ===
cat > /app/outputs/formation_enthalpies.json << 'FFEOF'
{
  "Zr3Sn": -34.834,
  "Zr48_Sn12_Va4": -12.186,
  "Zr48_Sn12_Zr4": -27.136,
  "Zr48_Sn13_Zr3": -29.940,
  "Zr48_Sn15_Zr1": -33.750,
  "Zr5Sn3": -55.670,
  "Zr5Sn4": -58.490,
  "ZrSn2": -42.905
}
FFEOF
