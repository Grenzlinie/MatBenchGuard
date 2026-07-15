#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: optimized_geometries.csv ===
cat > "$OUTDIR/optimized_geometries.csv" <<'EOF'
molecule,atom1,atom2,distance_angstrom
T+,Si1,H1,1.64
T+,Si2,H1,1.64
T+,Si1,Si2,3.28
T0,Si1,H1,1.48
T0,Si2,H1,4.03
T0,Si1,Si2,5.51
T-,Si1,H1,1.47
T-,Si2,H1,3.75
T-,Si1,Si2,5.22
EOF

# === solve block: total_energies.csv ===
cat > "$OUTDIR/total_energies.csv" <<'EOF'
molecule,energy_hartree
SiH4,-5.976500
SiH3+,-5.087600
SiH3,-5.375500
SiH3-,-5.383000
SiH2,-4.781500
T+,-11.111900
T0,-11.352500
T-,-11.358300
EOF

# === solve block: binding_energies.csv ===
cat > "$OUTDIR/binding_energies.csv" <<'EOF'
molecule,binding_energy_kcal_per_mol
T+,-30.00
T0,-0.31
T-,-0.75
EOF
