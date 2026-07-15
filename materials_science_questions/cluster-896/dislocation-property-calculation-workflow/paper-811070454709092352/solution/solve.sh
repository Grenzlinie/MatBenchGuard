#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.csv ===
cat > "$OUTDIR/results.csv" <<'CSVEOF'
epsilon,s_f,H_c,P,free_energy_derivative
0.06,0,13,0.2742,0.85
0.06,0.10825,16,0.2358,0.65
0.09,0,10,0.3303,1.2
0.09,0.10825,12,0.2904,1.0
0.12,0,7,0.4208,1.5
0.12,0.10825,9,0.3552,1.3
CSVEOF
