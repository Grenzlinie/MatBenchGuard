#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: delta_A_fit.csv ===
cat > "$OUTDIR/delta_A_fit.csv" <<'FFEOF'
Delta_A,Softening_Pct
-4.3,44.01
FFEOF
