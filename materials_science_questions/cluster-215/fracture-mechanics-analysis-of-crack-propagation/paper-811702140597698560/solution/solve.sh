#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p $OUTDIR

# === solve block: pt_table.csv ===
# Write the CSV with header
cat > $OUTDIR/pt_table.csv <<'EOF'
r,b,t,pt
0.5,1,5.0,0.985
0.5,1,7.0,0.982
0.5,1,10.56,0.98
0.5,1,12.0,0.965
0.5,1,15.0,0.94
1.0,1,5.0,0.95
1.0,1,10.0,0.88
1.0,1,15.0,0.80
2.0,1,5.0,0.85
2.0,1,10.0,0.75
2.0,1,15.0,0.65
0.5,2,5.0,0.99
0.5,2,10.0,0.96
0.5,2,15.0,0.92
EOF
