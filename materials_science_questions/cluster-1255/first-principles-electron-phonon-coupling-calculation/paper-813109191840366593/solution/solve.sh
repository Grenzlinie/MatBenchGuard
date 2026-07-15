#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: la_ta_ratios.csv ===
cat > "$OUTDIR/la_ta_ratios.csv" <<'CSVEOF'
structure,well_width_nm,density_10_15_m2,la_ta_ratio
5.1nm,5.1,1.8,1.59
6.8nm,6.8,2.0,0.92
12nm,12,3.7,0.27
15nm,15,3.6,0.16
HET,,2.8,0.10
CSVEOF
