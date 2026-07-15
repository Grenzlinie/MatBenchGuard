#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_single_molecule_geometries.csv ===
cat <<'EOF' > "$OUTDIR/step_01_single_molecule_geometries.csv"
compound_id,substituent,o_H_O_distance_A,o_H_H_distance_A,ring_tilt_angle_deg
unsubstituted_DPU,none,2.40,2.29,40
pCyDPU,CN,2.24,2.22,5
pCyNDPU,CN/NO2,2.20,2.21,5
pCF3DPU,CF3,2.37,2.28,40
pCyHDPU,CN,2.28,2.26,15
pNHDPU,NO2,2.19,2.21,5
pClHDPU,Cl,2.38,2.30,30
EOF

# === solve block: step_02_solid_state_energies.csv ===
cat <<'EOF' > "$OUTDIR/step_02_solid_state_energies.csv"
compound_id,E_lattice_kcal_mol,E_cohesive_kcal_mol,E_strain_kcal_mol,E_dimer_kcal_mol
pCyDPU,-72.83,-94.78,21.95,-49.07
pCyNDPU,-74.60,-97.58,22.98,-57.17
pCF3DPU,-76.72,-105.46,28.74,-73.64
pCyHDPU,-65.17,-87.39,22.22,-57.27
pNHDPU,-90.87,-112.70,21.83,-42.49
pClHDPU,-66.39,-88.55,22.15,-57.38
EOF
