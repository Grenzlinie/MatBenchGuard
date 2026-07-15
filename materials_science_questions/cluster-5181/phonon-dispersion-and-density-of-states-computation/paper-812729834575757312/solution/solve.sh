#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: thermal_conductivity.csv ===
cat > /app/outputs/thermal_conductivity.csv <<'FFEOF'
phase,kappa
c-Si,121
a-Si,1.4
FFEOF
