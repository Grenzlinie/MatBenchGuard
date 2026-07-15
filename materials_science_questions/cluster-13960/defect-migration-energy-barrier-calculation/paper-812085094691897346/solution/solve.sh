#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: binding_energies_bond_lengths.csv ===
cat > /app/outputs/binding_energies_bond_lengths.csv <<'EOF'
system,configuration,binding_energy_per_F_eV,C_F_bond_length_Angstrom
nanotube,F,1.43,1.455
nanotube,F2(1,2),2.43,1.408
nanotube,F2(1,4_cis),2.38,1.435
nanotube,F2(1,3),1.87,1.466
nanotube,C4F,1.75,1.410
nanotube,C2F,1.83,1.385
graphene,F,1.04,1.495
EOF

# === solve block: migration_barriers.csv ===
cat > /app/outputs/migration_barriers.csv <<'EOF'
system,transition,barrier_eV
graphene,(1,2)→(1,3),1.35
graphene,(1,4_cis)→(1,3),1.18
nanotube,(1,2)→(1,3),1.74
nanotube,(1,4_cis)→(1,3),1.31
EOF
