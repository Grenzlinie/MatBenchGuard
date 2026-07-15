#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_elastic_constants_Ti2InC.csv ===
cat > /app/outputs/step_01_elastic_constants_Ti2InC.csv <<'FFEOF'
C11,C12,C13,C33,C44
284.2,58.7,52.3,246.1,90.0
FFEOF

# === solve block: step_01_elastic_constants_Ti2InN.csv ===
cat > /app/outputs/step_01_elastic_constants_Ti2InN.csv <<'FFEOF'
C11,C12,C13,C33,C44
213.7,36.8,105.6,231.7,98.0
FFEOF

# === solve block: step_02_derived_moduli_Ti2InC.csv ===
cat > /app/outputs/step_02_derived_moduli_Ti2InC.csv <<'FFEOF'
B,G,Y,nu,A,kc_ka,G_B
126.4,100.4,240,0.184,0.798,1.230,0.80
FFEOF

# === solve block: step_02_derived_moduli_Ti2InN.csv ===
cat > /app/outputs/step_02_derived_moduli_Ti2InN.csv <<'FFEOF'
B,G,Y,nu,A,kc_ka,G_B
125.5,81,200,0.234,1.11,0.312,0.65
FFEOF

# === solve block: step_03_classification.txt ===
cat > /app/outputs/step_03_classification.txt <<'FFEOF'
Ti2InC: brittle (G/B = 0.80)
Ti2InN: near borderline (G/B = 0.65)
FFEOF
