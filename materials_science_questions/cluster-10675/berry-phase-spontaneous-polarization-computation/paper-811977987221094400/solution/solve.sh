#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'FFEOF'
{
  "isomer_shift_change": 0.103,
  "quadrupolar_splitting_total": -0.484,
  "quadrupolar_splitting_4s_contribution": -0.288,
  "R_4p": 0.51,
  "E_para": 800000000,
  "rho_4s": 0.2
}
FFEOF

# === solve block: temp_dependence.csv ===
python3 /solution/compute_temp.py > /app/outputs/temp_dependence.csv
