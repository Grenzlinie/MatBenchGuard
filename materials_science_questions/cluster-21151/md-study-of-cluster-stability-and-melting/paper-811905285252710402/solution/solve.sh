#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: pair_fractions_300K.csv ===
cat > /app/outputs/pair_fractions_300K.csv <<'EOF'
cooling_rate,T,pair_index,fraction
gamma1,300.0,1551,25.0
gamma1,300.0,1541,18.2
gamma1,300.0,1431,22.0
gamma1,300.0,1421,15.0
gamma1,300.0,1422,5.0
gamma2,300.0,1551,22.5
gamma2,300.0,1541,17.9
gamma2,300.0,1431,21.8
gamma2,300.0,1421,14.8
gamma2,300.0,1422,6.5
gamma3,300.0,1551,20.0
gamma3,300.0,1541,18.1
gamma3,300.0,1431,22.2
gamma3,300.0,1421,15.2
gamma3,300.0,1422,8.0
gamma4,300.0,1551,17.5
gamma4,300.0,1541,18.3
gamma4,300.0,1431,22.1
gamma4,300.0,1421,15.1
gamma4,300.0,1422,9.5
gamma5,300.0,1551,15.0
gamma5,300.0,1541,17.8
gamma5,300.0,1431,21.9
gamma5,300.0,1421,14.9
gamma5,300.0,1422,11.0
gamma6,300.0,1551,12.5
gamma6,300.0,1541,18.0
gamma6,300.0,1431,22.0
gamma6,300.0,1421,15.0
gamma6,300.0,1422,12.5
EOF
