#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: table_I_reproduction.csv ===
cat > "$OUTDIR/table_I_reproduction.csv" <<'FFEOF'
tetrahedron_number,tetrahedron,bonding_unit,EB_Si2p3_2,deltaEB_N1s
1,Si-Si4,Si,99.6,
2,Si-Si3N,Si3N,100.2,-1.26
3,Si-Si2O,Si2O,100.6,
4,Si-Si2N2,Si3N2,100.8,-0.70
5,Si-Si2ON,Si6O3N2,101.2,-0.12
6,Si-SiN3,SiN,101.4,-0.30
7,Si-Si2O2,SiO,101.6,
8,Si-SiON2,Si6O3N4,101.8,0.18
9,Si-N4,Si3N4,102.0,0
10,Si-SiO2N,Si3ON,102.2,-0.44
11,Si-N3O,Si2ON2,102.4,0.40
12,Si-SiO3,Si2O3,102.6,
13,Si-O2N2,Si3O3N2,102.8,0.77
14,Si-O3N,Si6O9N2,103.2,1.11
15,Si-O4,SiO2,103.6,
FFEOF
