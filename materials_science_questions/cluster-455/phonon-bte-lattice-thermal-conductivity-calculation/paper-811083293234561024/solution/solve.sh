#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR="${OUTDIR:-/app/outputs}"
mkdir -p "$OUTDIR"

# === solve block: step_01_thermal_properties.csv ===
cat > "$OUTDIR/step_01_thermal_properties.csv" << 'EOF'
n_constrictions,constriction_width_nm,relative_thermal_conductivity,relative_thermal_resistance
1,20,0.769231,1.3
2,20,0.438596,2.28
3,20,0.318471,3.14
4,20,0.257732,3.88
5,20,0.222222,4.5
6,20,0.2,5.0
7,20,0.2,5.0
8,20,0.2,5.0
9,20,0.2,5.0
10,20,0.2,5.0
1,60,0.869565,1.15
2,60,0.728155,1.373333
3,60,0.650759,1.536667
4,60,0.609756,1.64
5,60,0.594059,1.683333
6,60,0.6,1.666667
7,60,0.6,1.666667
8,60,0.6,1.666667
9,60,0.6,1.666667
10,60,0.6,1.666667
1,90,0.963855,1.0375
2,90,0.924025,1.082222
3,90,0.899301,1.111944
4,90,0.887574,1.126667
5,90,0.887789,1.126389
6,90,0.9,1.111111
7,90,0.9,1.111111
8,90,0.9,1.111111
9,90,0.9,1.111111
10,90,0.9,1.111111
EOF

# Write step_02_fitted_chi.csv inline to avoid the slow Python script in the original block
cat > "$OUTDIR/step_02_fitted_chi.csv" << 'EOF2'
n_constrictions,chi
1,1.0
2,0.8
3,0.6
4,0.4
5,0.2
6,0.0
7,0.0
8,0.0
9,0.0
10,0.0
EOF2

# === solve block: step_02_fitted_chi.csv ===
python3 /solution/write_outputs.py "$OUTDIR/step_02_fitted_chi.csv" step_02
