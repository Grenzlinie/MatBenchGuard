#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: miscibility_gap_0GPa.csv ===
cat > "$OUTDIR/miscibility_gap_0GPa.csv" <<'FFEOF'
temperature,x_maj_low,x_maj_high
3500,0.80,0.80
3400,0.79,0.81
3200,0.78,0.84
3000,0.77,0.88
2800,0.755,0.92
2600,0.74,0.95
2400,0.725,0.97
2200,0.715,0.985
2000,0.71,0.99
1800,0.70,0.995
1600,0.695,0.997
1400,0.69,0.998
1200,0.685,0.999
1073,0.68,0.999
FFEOF
