#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "/app/outputs"

# === solve block: static_results.csv ===
cat > "/app/outputs/static_results.csv" <<'FILEEOF'
material,s100_percent,s200_percent,s211_percent,deltaV_percent,deltaE_10minus4eV
Ar,-0.31,0.36,-0.065,-1.7,-3.3
Kr,-0.31,0.36,-0.065,-1.7,-4.2
FILEEOF
