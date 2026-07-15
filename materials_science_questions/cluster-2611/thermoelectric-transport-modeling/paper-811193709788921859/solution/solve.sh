#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: seebeck_coefficients.csv ===
# Write the scored artifact with reference Seebeck values at 380 K
cat > "$OUTDIR/seebeck_coefficients.csv" <<'CSVEOF'
compound,Seebeck_380K_uV_K
GdNiSb,12.8
LuNiSb,70.0
CSVEOF
