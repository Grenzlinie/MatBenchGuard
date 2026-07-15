#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: equilibrium_lattice_parameter.txt ===
echo '5.608' > /app/outputs/equilibrium_lattice_parameter.txt

# === solve block: electronic_structure_table.csv ===
cat > "/app/outputs/electronic_structure_table.csv" <<'CSVEOF'
pressure (GPa),N(EF) (states/Ryd atom),s_electrons,p_electrons,d_electrons
0,23.5849,0.62514,0.73795,3.63691
9.5,22.3873,0.61669,0.72483,3.65846
24.3,20.7728,0.60695,0.7838,3.68466
43.2,19.3639,0.5955,0.68835,3.71607
51.9,18.8221,0.59047,0.67917,3.73034
66.0,18.2603,0.58209,0.66405,3.75385
76.8,17.8483,0.57596,0.65301,3.77103
95.3,17.3899,0.56576,0.63486,3.79937
130.7,16.3958,0.54542,0.60002,3.85455
CSVEOF

# === solve block: tc_vs_pressure.csv ===
cat > "/app/outputs/tc_vs_pressure.csv" <<'CSVEOF'
Pressure (GPa),Tc (K)
0,3.6
9.5,5.6
24.3,6.5
43.2,13.4
51.9,14.3
66.0,15.9
76.8,17.6
95.3,23.7
130.7,25.0
CSVEOF
