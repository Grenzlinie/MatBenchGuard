#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: correlation_dimension_level6.csv ===
cat > "$OUTDIR/correlation_dimension_level6.csv" <<'FFEOF'
p,v
0.0,0.62
0.1,0.65
0.2,0.32
0.4,0.17
0.6,0.07
FFEOF

# === solve block: transmission_sum_level6.csv ===
cat > "$OUTDIR/transmission_sum_level6.csv" <<'FFEOF'
p,transmission_sum
0.0,10.2
0.1,12.1
0.2,5.3
0.4,0.9
0.6,0.4
FFEOF
