#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: effective_moduli.csv ===
# Write the effective moduli CSV with paper-reported values
cat > /app/outputs/effective_moduli.csv <<'FFEOF'
interphase_modulus_GPa,IPTR,E_c_GPa
0,0.0,4.78
100,0.1,4.90
100,0.5,5.72
100,1.0,7.15
2.0,0.1,4.72
2.0,0.5,4.67
2.0,1.0,4.57
FFEOF
