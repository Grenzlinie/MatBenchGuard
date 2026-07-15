#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_polymer_angles.csv ===
cat > "$OUTDIR/step_01_polymer_angles.csv" << 'EOF'
polymer_name,angle_type,angle_value_deg,repeat_length_A
(SiO)₂(OH)₄,Si-O-Si,154.1,4.9
(SiO)₂(OH)₄,Si-O-Si,157.6,4.9
(SiNH)(SiO)(OH)₄,Si-N-Si,129.7,5.1
(SiNH)(SiO)(OH)₄,Si-O-Si,134.6,5.1
(SiCH₂)(SiO)(OH)₄,Si-C-Si,123.7,5.1
(SiCH₂)(SiO)(OH)₄,Si-O-Si,130.5,5.1
EOF

# === solve block: step_02_doped_geometries.csv ===
cat > "$OUTDIR/step_02_doped_geometries.csv" << 'EOF'
system,relaxation_type,lattice_parameter_a_A,SiXSi_angle_deg,SiC_bond_length_A,SiN_bond_length_A
OXY-SOD,f,8.83,156.7,,
1CH2-SOD,i,8.83,126.1,1.81,
1CH2-SOD,f,8.72,119.1,1.81,
1NH-SOD,i,8.83,135.5,,1.69
1NH-SOD,f,8.80,133.2,,1.69
EOF

# === solve block: step_03_strain_energy.csv ===
cat > "$OUTDIR/step_03_strain_energy.csv" << 'EOF'
system,strain_energy_per_defect_eV
1CH2-SOD (f),0.10
1NH-SOD (f),0.15
EOF

# === solve block: step_04_adsorption_energy.csv ===
cat > "$OUTDIR/step_04_adsorption_energy.csv" << 'EOF'
reaction,adsorption_energy_eV
BF3 + Si-O-Si (OXY-SOD),-0.5
BF3 + Si-NH-Si (1NH-SOD),-0.8
EOF

# === solve finalize ===
echo "Oracle artifacts written successfully."
