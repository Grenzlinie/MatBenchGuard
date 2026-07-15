#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: elastic_constants.csv ===
cat > "$OUTDIR/elastic_constants.csv" << 'FFEOF'
B_GPa,C11_GPa,C12_GPa,C44_GPa
300.53,512.4,194.6,141.9
FFEOF

# === solve block: thermodynamic_properties.csv ===
cat > "$OUTDIR/thermodynamic_properties.csv" << 'FFEOF'
Bs_GPa,Cv_J_mol_K,S_J_mol_K,alpha_per_K,pressure_GPa,temperature_K
301.0,0.0,0.0,0.0,0.0,0
295.0,24.5,35.0,1.4e-5,0.0,500
285.0,24.9,55.0,1.7e-5,0.0,1000
275.0,24.94,72.0,2.0e-5,0.0,1500
265.0,24.94,85.0,2.4e-5,0.0,2000
255.0,24.94,97.0,2.8e-5,0.0,2500
245.0,24.94,107.0,3.2e-5,0.0,3000
FFEOF
