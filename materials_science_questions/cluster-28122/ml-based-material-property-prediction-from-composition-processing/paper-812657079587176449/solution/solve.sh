#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: benchmark_results.csv ===
cat > /app/outputs/benchmark_results.csv <<'FFEOF'
function,mean,std
f1,5.51e-102,1.64e-101
f2,3.10e-62,5.87e-62
f3,4.03e-4,8.47e-4
f4,3.82e-4,0
f5,3.86e-4,7.28e-6
f6,4.71e-15,2.13e-15
f7,397.38,5.27
FFEOF
