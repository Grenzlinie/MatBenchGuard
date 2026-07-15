#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: MA_values.csv ===
cat > /app/outputs/MA_values.csv <<'FFEOF'
cap_material,thickness_ML,MA_erg_per_cm2
Hf,0,1.49
Hf,1,0.62
Hf,2,0.75
Hf,3,0.92
Hf,4,0.72
Hf,5,0.95
Hf,6,0.75
Hf,7,0.98
Hf,8,0.78
Hf,9,1.00
Hf,10,0.80
Ta,0,1.49
Ta,1,1.00
Ta,2,-0.20
Ta,3,-0.32
Ta,4,-0.30
FFEOF
