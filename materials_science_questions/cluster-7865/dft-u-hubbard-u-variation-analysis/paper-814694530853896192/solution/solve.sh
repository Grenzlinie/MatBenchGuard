#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: mab_values.csv ===
cat > "$OUTDIR/mab_values.csv" <<'EOF'
ligand,condition,MAB_K
H,isolated,63.4
H,supported,62.7
CH3,isolated,62.7
CH3,supported,61.5
C6H5,isolated,67.3
C6H5,supported,66.1
CHCl2,isolated,61.2
CHCl2,supported,51.1
EOF

# === solve block: bonding_energies.csv ===
cat > "$OUTDIR/bonding_energies.csv" <<'EOF'
ligand,bonding_energy_eV
H,0.9
CH3,0.7
C6H5,1.0
CHCl2,2.7
EOF
