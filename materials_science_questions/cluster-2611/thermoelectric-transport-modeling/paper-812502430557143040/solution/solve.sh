#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: lattice_parameters.csv ===
cat > "$OUTDIR/lattice_parameters.csv" <<'EOF'
compound,a,b,c,V
Sr3GaAs3,12.706,19.175,6.484,1579.7
Ba3GaAs3,13.3195,19.9121,6.7800,1798.2
EOF

# === solve block: elastic_constants.csv ===
cat > "$OUTDIR/elastic_constants.csv" <<'EOF'
compound,C11,C12,C13,C22,C23,C33,C44,C55,C66
Sr3GaAs3,93.3,22.1,27.2,82.8,26.9,81.5,28.8,28.4,26.5
Ba3GaAs3,84.4,16.8,22.4,79.7,22.9,76.4,20.5,23.4,20.6
EOF

# === solve block: band_gap.csv ===
cat > "$OUTDIR/band_gap.csv" <<'EOF'
compound,band_gap
Sr3GaAs3,1.271
Ba3GaAs3,1.285
EOF

# === solve block: effective_masses.csv ===
cat > "$OUTDIR/effective_masses.csv" <<'EOF'
compound,carrier_type,direction,m_star
Sr3GaAs3,electron,[100],0.39
Sr3GaAs3,electron,[010],0.45
Sr3GaAs3,electron,[001],2.05
Sr3GaAs3,hole,[100],1.61
Sr3GaAs3,hole,[010],0.19
Sr3GaAs3,hole,[001],2.24
Ba3GaAs3,electron,[100],0.43
Ba3GaAs3,electron,[010],1.05
Ba3GaAs3,electron,[001],9.98
Ba3GaAs3,hole,[100],1.73
Ba3GaAs3,hole,[010],0.70
Ba3GaAs3,hole,[001],3.13
EOF

# === solve block: static_dielectric.csv ===
cat > "$OUTDIR/static_dielectric.csv" <<'EOF'
compound,direction,epsilon1_0
Sr3GaAs3,[100],8.33
Sr3GaAs3,[010],8.64
Sr3GaAs3,[001],7.98
Ba3GaAs3,[100],8.66
Ba3GaAs3,[010],9.17
Ba3GaAs3,[001],8.32
EOF
