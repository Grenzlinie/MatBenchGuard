#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: youngs_modulus_results.csv ===
cat > "$OUTDIR/youngs_modulus_results.csv" <<'FFEOF'
Condition,Youngs_modulus_TPa
L=10_T=300_D0,0.7
L=20_T=300_D0,0.9
L=40_T=300_D0,1.1
L=80_T=300_D0,1.1
L=40_T=100_D0,0.95
L=40_T=300_D0,1.1
L=40_T=500_D0,1.1
L=40_T=300_D0,1.1
L=40_T=300_D5,1.1
L=40_T=300_D10,0.97
L=40_T=300_D20,0.93
FFEOF
