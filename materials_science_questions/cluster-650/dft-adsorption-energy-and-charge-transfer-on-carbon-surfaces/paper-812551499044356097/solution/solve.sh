#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_results.csv ===
cat > /app/outputs/step_01_results.csv <<'EOF'
system,gas,configuration,E_ad,d
Mg-C3B,NO,I,-1.11,2.17
Mg-C3B,NO,II,-1.02,2.20
Mg-C3B,N2O,N-end,-1.10,2.18
Mg-C3B,NO2,I,-1.62,2.15
Mg-C3B,NO2,II,-1.35,2.21
Mg-C3B,NH3,N-end,-1.15,2.16
pristine_C3B,NO,,-0.31,
pristine_C3B,N2O,,-0.32,
pristine_C3B,NO2,,-0.34,
pristine_C3B,NH3,,-0.72,
EOF
