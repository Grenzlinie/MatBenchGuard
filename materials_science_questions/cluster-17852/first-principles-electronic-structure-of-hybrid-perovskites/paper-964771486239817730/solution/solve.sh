#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: band_gaps_ak13_gam.csv ===
cat > "$OUTDIR/band_gaps_ak13_gam.csv" <<'FFEOF'
compound,band_gap
MAPbCl3,2.90
FAPbCl3,2.88
CsPbCl3-orth,2.98
MAPbBr3,2.39
FAPbBr3,2.40
CsPbBr3-orth,2.62
MAPbI3-tetr,1.42
FAPbI3,1.16
CsPbI3-orth,1.54
HdAPbI4-mon,2.30
Cs2AgBiCl6,2.45
Cs2AgBiBr6,2.18
Cs2AgBiI6,1.33
FFEOF
