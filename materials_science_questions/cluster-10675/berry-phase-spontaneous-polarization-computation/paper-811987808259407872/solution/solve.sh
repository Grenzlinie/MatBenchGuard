#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: electro_optic_results.json ===
cat > /app/outputs/electro_optic_results.json <<'FFEOF'
{
  "delta_n_Kerr": -0.0566,
  "delta_n_piezo": -0.0339,
  "delta_n_total": -0.0905,
  "r13_Kerr_clamp": 1.5181e-11,
  "r33_Kerr_clamp": 4.1903e-11,
  "r33_Kerr_free": 6.4583e-11,
  "r33_free": 8.3843e-11,
  "r33_piezo": 1.9261e-11
}
FFEOF
