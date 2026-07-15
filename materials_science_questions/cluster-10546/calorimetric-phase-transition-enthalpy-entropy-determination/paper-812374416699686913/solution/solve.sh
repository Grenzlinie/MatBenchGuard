#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: transition_results.csv ===
cat > "$OUTDIR/transition_results.csv" <<'FFEOF'
composition,peak_number,delta_H,delta_S
Li0.363WO3,1,433,1.36
Li0.363WO3,2,211,0.45
Li0.363WO3,3,882,1.68
Li0.437WO3,1,357,1.09
Li0.437WO3,2,272,0.59
Li0.478WO3,1,449,1.42
Li0.478WO3,2,236,0.50
FFEOF
