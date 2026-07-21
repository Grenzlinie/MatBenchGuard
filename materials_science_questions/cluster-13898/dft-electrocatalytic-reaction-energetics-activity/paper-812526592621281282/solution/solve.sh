#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: or_results.csv ===
cat > /app/outputs/or_results.csv <<'FFEOF'
model,step2_energy,step3_energy,step4_energy,step5_energy,overpotential
undoped,0.50,1.47,1.48,1.47,0.73
BNC-1_1B,0.53,1.46,1.465,1.465,0.70
BNC-1_2B,0.52,1.47,1.465,1.465,0.71
BNC-1_3B,0.51,1.47,1.47,1.47,0.72
NNC-1,0.53,1.46,1.465,1.465,0.70
SiNC-1,1.00,1.71,1.71,0.50,0.73
PNC-1,0.75,1.39,1.39,1.39,0.48
SNC-1,0.67,1.416,1.417,1.417,0.56
FFEOF