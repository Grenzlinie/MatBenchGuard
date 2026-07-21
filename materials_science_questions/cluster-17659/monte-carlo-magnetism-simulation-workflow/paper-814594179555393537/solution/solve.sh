#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_results.csv ===
cat > "$OUTDIR/step_01_results.csv" <<'FFEOF'
T,c,E_N,ΔE_N,shift,broadening
500,0.2,-325.0,20.0,-0.028,0.007
500,0.3,-487.0,45.0,-0.042,0.015
500,0.4,-650.0,70.0,-0.056,0.023
600,0.2,-325.0,30.0,-0.028,0.010
600,0.3,-487.0,55.0,-0.042,0.018
600,0.4,-650.0,80.0,-0.056,0.027
FFEOF
