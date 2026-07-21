#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: toughness_ratios.csv ===
cat > "$OUTDIR/toughness_ratios.csv" <<'FFEOF'
poling_field,applied_field,Gss_over_G0
0.0,0.0,2.87
0.0,0.2,2.91
0.0,0.5,3.17
0.0,0.8,4.16
3.0,-1.0,4.0
3.0,-0.5,3.3
3.0,0.0,2.80
3.0,0.5,2.59
3.0,1.0,2.38
-3.0,1.0,4.0
-3.0,0.5,3.3
-3.0,0.0,2.80
-3.0,-0.5,2.59
-3.0,-1.0,2.38
FFEOF
