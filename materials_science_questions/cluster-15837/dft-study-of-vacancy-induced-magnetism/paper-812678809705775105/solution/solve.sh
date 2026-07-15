#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: magnetic_moments.csv ===
cat > /app/outputs/magnetic_moments.csv <<'FFEOF'
model,total_magnetic_moment_muB
pristine,0.0
V_S,0.0
V_In,1.830
Sm_In,5.143
Sm_In+V_In,4.658
FFEOF
