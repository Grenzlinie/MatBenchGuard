#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_bandgaps.csv ===
cat > "$OUTDIR/step_01_bandgaps.csv" <<'FFEOF'
composition_x,calculated_bandgap_eV
0,1.43
0.14,1.435
0.75,1.485
1,1.54
FFEOF

# === solve block: step_02_bowing_parameter.txt ===
echo "0.1291" > "$OUTDIR/step_02_bowing_parameter.txt"
