#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: optimal_angles.csv ===
cat > "$OUTDIR/optimal_angles.csv" <<'EOF'
date,alpha1_deg,alpha2_deg
2023-06-21,65.72,-24.41
2023-12-22,33.32,7.98
EOF
