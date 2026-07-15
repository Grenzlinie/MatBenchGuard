#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: simulation_results.csv ===
cat > "$OUTDIR/simulation_results.csv" <<'FFEOF'
specimen,region,signal_cps,noise_Si_cps
A,W,60.9,106.1
A,Ti,43.4,10.9
B,W,60.9,16.5
B,Ti,43.4,1.8
C,W,60.9,31.9
C,Ti,43.4,3.4
U,W,60.9,0.8
U,Ti,43.4,0.3
FFEOF
