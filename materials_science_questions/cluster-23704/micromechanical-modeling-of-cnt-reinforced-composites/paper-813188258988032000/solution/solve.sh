#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: predictions.csv ===
cat > /app/outputs/predictions.csv <<'EOF'
wt%,MA_wt%,predicted_E_GPa
0.05,0,1.71
0.1,0,1.79
0.05,5,1.41
0.1,5,1.59
EOF
