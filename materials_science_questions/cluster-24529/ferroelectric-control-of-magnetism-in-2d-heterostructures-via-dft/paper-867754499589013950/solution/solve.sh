#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: polarizer_results.json ===
cat > /app/outputs/polarizer_results.json <<'POLEND'
{
  "T_L": 1.0,
  "T_R": 0.0,
  "frequency_GHz": 6.5
}
POLEND

# === solve block: retarder_results.json ===
cat > /app/outputs/retarder_results.json <<'RETEND'
{
  "delta_phi_LR": 0.974,
  "frequency_GHz": 6.5,
  "length_nm": 200
}
RETEND
