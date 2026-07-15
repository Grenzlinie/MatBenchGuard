#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: decomposition_293K.csv ===
cat > "$OUTDIR/decomposition_293K.csv" <<'FFEOF'
mode,frequency,pure_volume_contribution,pure_temperature_contribution
v1,639,-1.53,-1.15
v4,399,-1.66,1.41
v5,197,0.3,4.48
v6,144,-5.27,27.23
FFEOF
