#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: heg_sheet_density.csv ===
cat > $OUTDIR/heg_sheet_density.csv <<'EOF'
strain_percent,sheet_density_cm2
-1.78,1.27e13
-0.89,1.185e13
0.0,1.1e13
0.89,1.015e13
1.78,9.3e12
EOF
