#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: band_gap_vs_RC.csv ===
cat > "$OUTDIR/band_gap_vs_RC.csv" <<'FFEOF'
compression_ratio,band_gap_eV,gap_type
0,0.91,direct
5,0.93,indirect
10,0.75,indirect
15,0.50,indirect
20,0.25,indirect
25,0.05,indirect
30,0.0,metallic
FFEOF

# === solve block: transmission_vs_RC.csv ===
cat > "$OUTDIR/transmission_vs_RC.csv" <<'FFEOF'
compression_ratio,T_zigzag_24L,T_armchair_24L
0,2e-3,1e-2
5,2e-3,4e-3
10,2e-3,1.5e-3
15,2e-3,5e-4
20,2e-3,1e-3
25,1e-2,1e-2
30,8e-2,6e-2
FFEOF
