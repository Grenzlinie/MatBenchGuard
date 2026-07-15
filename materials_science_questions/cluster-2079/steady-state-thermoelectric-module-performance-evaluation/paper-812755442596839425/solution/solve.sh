#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'FFEOF'
{
  "T_steady_C4": 133.0,
  "T_steady_TEC": 112.0,
  "P_chip_C4": 75.8,
  "P_chip_TEC": 67.2,
  "P_TEC": 13.2,
  "COP": 1.4,
  "Npn_cop": 96,
  "Npn_P": 34
}
FFEOF
