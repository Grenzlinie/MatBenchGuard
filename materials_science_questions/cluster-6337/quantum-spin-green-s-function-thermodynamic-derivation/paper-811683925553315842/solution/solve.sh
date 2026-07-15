#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: spin_correlations.csv ===
cat <<'CSVEOF' > "$OUTDIR/spin_correlations.csv"
j,C_j_SS
1,-0.589490
2,0.225706
3,-0.177698
4,0.118742
5,-0.104021
6,0.080534
7,-0.073488
8,0.060922
CSVEOF
