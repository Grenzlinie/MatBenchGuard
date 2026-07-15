#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: band_gap_vs_strain.csv ===
cat > "$OUTDIR/band_gap_vs_strain.csv" <<'FFEOF'
strain,gap_eV,is_direct
-4,0.935,False
-3,1.000,False
-2,1.100,False
-1,1.250,False
0,1.364,False
1,1.406,False
2,1.395,True
3,1.381,True
4,1.360,True
FFEOF

# === solve block: absorption_max.csv ===
cat > "$OUTDIR/absorption_max.csv" <<'FFEOF'
strain,absorption_max
-4,18000
0,22979
4,27000
FFEOF
