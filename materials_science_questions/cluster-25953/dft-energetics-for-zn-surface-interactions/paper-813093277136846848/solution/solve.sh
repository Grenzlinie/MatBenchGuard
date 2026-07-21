#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: adsorption_results.csv ===
cat > /app/outputs/adsorption_results.csv <<'FFEOF'
system,site,adsorption_energy_eV,I1_I2_bond_length_A
CZTS,Sn,-1.202,3.036
CZTS,Cu,-2.060,3.152
CZTS,Zn,-2.343,3.298
CZTSSe,Sn,-1.419,3.004
CZTSSe,Cu,-1.418,3.090
CZTSSe,Zn,-3.727,3.373
FFEOF
