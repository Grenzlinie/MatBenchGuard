#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: band_gaps.csv ===
cat > "$OUTDIR/band_gaps.csv" << 'FFEOF'
layer,band_gap_eV,direct_indirect
bulk,0.90,indirect
1L,1.15,direct
2L,1.15,direct
3L,1.14,direct
4L,1.13,direct
5L,1.11,direct
6L,1.00,direct
FFEOF

# === solve block: work_functions.csv ===
cat > "$OUTDIR/work_functions.csv" << 'FFEOF'
layer,work_function_eV
1L,4.44
2L,4.70
3L,4.95
4L,5.00
5L,5.05
6L,5.10
FFEOF

# === solve block: static_dielectric_constants.csv ===
cat > "$OUTDIR/static_dielectric_constants.csv" << 'FFEOF'
layer,epsilon_static_real
1L,3.28
3L,4.08
5L,4.38
FFEOF
