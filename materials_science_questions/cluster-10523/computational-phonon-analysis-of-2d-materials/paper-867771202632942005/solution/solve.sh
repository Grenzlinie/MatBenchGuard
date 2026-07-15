#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: abc_trilayer_charged_phonon_results.csv ===
cat > "$OUTDIR/abc_trilayer_charged_phonon_results.csv" <<'FFEOF'
doping,spectral_weight,frequency_shift
0,0.0,0.0
1000000000000,0.3,-1.5
5000000000000,1.8,-6.5
10000000000000,3.8,-12.0
20000000000000,6.0,-15.0
FFEOF
