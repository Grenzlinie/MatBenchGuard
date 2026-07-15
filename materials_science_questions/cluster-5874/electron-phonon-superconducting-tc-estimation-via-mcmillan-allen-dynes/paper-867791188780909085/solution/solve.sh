#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_03_tc_results.csv ===
cat > "$OUTDIR/step_03_tc_results.csv" <<'EOF'
pressure,Tc
50,82
100,63
300,61
EOF
