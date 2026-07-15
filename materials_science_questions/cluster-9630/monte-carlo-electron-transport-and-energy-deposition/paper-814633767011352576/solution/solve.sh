#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: transmission_probabilities.csv ===
cat > /app/outputs/transmission_probabilities.csv <<'CSVEOF'
material,thickness_mg_cm2,energy_keV,model,transmission_probability
Ag,55.0,336.0,Rutherford_Nigam,0.45
Ag,55.0,336.0,Mayol_Salvat,0.193
Ag,55.0,336.0,NIST,0.217
CSVEOF
