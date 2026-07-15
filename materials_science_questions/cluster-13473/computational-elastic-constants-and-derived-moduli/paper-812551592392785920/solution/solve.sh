#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_properties.csv ===
cat > /app/outputs/step_01_properties.csv << 'FFEOF'
system,r_peak_AA,Tg_K,E_GPa,D_cm2s
EIM2/TFSI-,4.4,371,1.21,1.0e-9
EIM2/Cl-,4.8,436,1.44,5.0e-10
EIM1/TFSI-,4.4,393,1.05,1.0e-9
FFEOF
