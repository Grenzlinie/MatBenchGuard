#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: doping_dependence.csv ===
# Write the doping dependence CSV
cat > "$OUTDIR/doping_dependence.csv" <<'EOF'
E_F,normalized_A_D_over_A_G
0.0,1.0000
0.1,0.9191
0.2,0.8511
0.3,0.7925
0.4,0.7419
0.5,0.6979
0.6,0.6592
0.7,0.6248
EOF
