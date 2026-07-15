#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: table1_formation_energies.csv ===
cat > "$OUTDIR/table1_formation_energies.csv" <<'EOF'
dopant,formation_energy_eV
undoped,2.16
Fe,0.97
Nb,2.55
La,2.69
EOF

# === solve block: table2_lattice_parameters.csv ===
cat > "$OUTDIR/table2_lattice_parameters.csv" <<'EOF'
system,a_angstrom,c_angstrom,volume_ang3
pure,3.880,4.152,62.521
Nb_on_Pb,3.854,4.002,59.464
Nb_on_Ti,3.885,4.073,61.487
Pb_vacancy,3.819,4.660,67.981
EOF
