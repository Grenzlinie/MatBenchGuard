#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p $OUTDIR

# === solve block: pKa_results.csv ===
cat > "$OUTDIR/pKa_results.csv" << 'EOF'
molecule,pKa_HF,pKa_B3LYP
1,5.38,5.41
2,0.92,0.62
3,-0.86,-0.63
4,-2.32,-2.66
5,-5.66,-5.79
6,-6.20,-6.34
7,0.81,0.43
8,-1.06,-1.46
9,-3.99,-3.79
10,-2.65,-2.25
11,-4.89,-4.95
12,-5.61,-5.64
EOF
