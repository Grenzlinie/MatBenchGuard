#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "$OUTDIR"

# === solve block: step_01_band_gaps.csv ===
cat > "$OUTDIR/step_01_band_gaps.csv" <<'FFEOF'
x,band_gap_eV
0,2.30
0.02,2.08
0.05,1.95
0.10,1.80
0.17,1.70
FFEOF
