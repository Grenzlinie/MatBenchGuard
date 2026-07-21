#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: T_c_star.txt ===
cat > "$OUTDIR/T_c_star.txt" <<'FFEOF'
4.74
FFEOF

# === solve block: critical_coverages.csv ===
cat > "$OUTDIR/critical_coverages.csv" <<'FFEOF'
J2prime_ratio,critical_coverage
0.0,0.30
-0.5,0.28
FFEOF
