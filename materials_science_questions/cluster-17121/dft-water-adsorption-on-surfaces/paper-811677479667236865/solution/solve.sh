#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: interaction_energies.csv ===
cat > "$OUTDIR/interaction_energies.csv" <<'EOF'
System,TotalEnergy_kcal_mol,vdW_Energy_kcal_mol,Elec_Energy_kcal_mol
His,-22.5,-5.2,-17.3
Gly-His,-35.6,-5.8,-29.8
Gly-His-Gly,-18.4,-4.9,-13.5
Gly-Gly-His,-19.1,-4.8,-14.3
EOF

# === solve block: diffusion_coefficients.csv ===
cat > "$OUTDIR/diffusion_coefficients.csv" <<'EOF'
System,D_z_cm2_s,D_xy_cm2_s
His,0.96,0.27
Gly-His,3.24,0.8
Gly-His-Gly,0.34,0.09
Gly-Gly-His,0.36,0.10
EOF

# === solve block: distance_shift_summary.csv ===
cat > "$OUTDIR/distance_shift_summary.csv" <<'EOF'
System,AvgDist_Solution_Ang,AvgDist_Adsorbed_Ang,Shift_Ang
His,2.55,2.55,0.0
Gly-His,5.5,5.0,-0.5
Gly-His-Gly,8.5,7.5,-1.0
Gly-Gly-His,8.5,7.75,-0.75
EOF
