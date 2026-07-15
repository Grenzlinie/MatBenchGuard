#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: magnetic_moments.csv ===
cat > "$OUTDIR/magnetic_moments.csv" <<'FFEOF'
element,configuration,magnetic_moment
V,adatom,5.00
V,interstitial,1.00
V,Te_site,1.00
V,Mo_site,0.00
Ti,adatom,4.00
Ti,interstitial,0.00
Ti,Te_site,0.00
Ti,Mo_site,1.00
FFEOF
