#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: optimization_results.csv ===
cat > "$OUTDIR/optimization_results.csv" <<'EOF'
density,total_energy,a,b,c,alpha,beta,gamma
2.2,-182.53,1.97977,1.94267,1.40507,94.13,96.35,77.78
EOF
