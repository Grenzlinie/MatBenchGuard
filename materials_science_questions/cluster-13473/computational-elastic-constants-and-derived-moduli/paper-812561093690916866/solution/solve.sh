#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.csv ===
cat > "$OUTDIR/results.csv" <<'CSVEOF'
composite,E_X,E_Y,E_Z,E_Avg,G_R,G_V,G_H,B_R,B_V,B_H,COF,AR
pristine,4.15,4.54,4.18,4.29,1.38,1.52,1.45,3.77,3.81,3.79,0.52,30.8
COOCH3,5.10,5.58,4.71,5.13,1.78,1.82,1.80,3.94,3.98,3.96,0.48,15.9
OH,6.11,6.35,4.58,5.68,1.87,1.95,1.91,3.97,3.99,3.98,0.44,9.6
COOH,6.53,6.08,4.57,5.73,1.96,2.02,1.99,4.30,4.38,4.34,0.36,7.3
CSVEOF
