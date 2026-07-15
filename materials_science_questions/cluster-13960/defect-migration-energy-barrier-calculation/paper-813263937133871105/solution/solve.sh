#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "$OUTDIR"

# === solve block: defect_properties.csv ===
cat > "$OUTDIR/defect_properties.csv" << 'FFEOF'
defect,formation_energy,total_magnetic_moment
C1,6.34,1.40
C3,5.84,2.00
N1,7.37,0.33
B1,8.63,2.62
C5,7.54,2.01
CC1,6.04,0.24
C1_N1,1.78,0.0
SW1N_formation,6.55,0.0
SW1N_healing,1.26,0.0
FFEOF
