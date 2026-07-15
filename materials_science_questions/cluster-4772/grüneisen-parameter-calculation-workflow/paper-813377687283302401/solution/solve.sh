#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_02_volume_formulation_table.csv ===
cat > /app/outputs/step_02_volume_formulation_table.csv <<'FFEOF'
ln_ratio_volume,substance,temperature_C
0.000,NaCl,0
0.021,NaCl,100
0.041,NaCl,200
0.065,NaCl,300
0.089,NaCl,400
0.110,NaCl,500
0.130,NaCl,600
0.000,KCl,0
0.017,KCl,100
0.033,KCl,200
0.055,KCl,300
0.075,KCl,400
0.100,KCl,500
0.130,KCl,600
FFEOF
