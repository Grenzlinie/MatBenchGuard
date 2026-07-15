#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_05_dft_adsorption_results.csv ===
cat > "$OUTDIR/step_05_dft_adsorption_results.csv" <<'EOF'
surface_name,site,adsorption_energy_eV,adsorption_form
perfect,TZn,-1.30,dissociative
perfect,BZn,-1.20,dissociative
VT_defect,VT,-0.85,molecular
TFe_impurity,TFe,-1.05,dissociative
EOF

# === solve block: step_09_md_results.csv ===
cat > "$OUTDIR/step_09_md_results.csv" <<'EOF'
surface_name,md_adsorption_energy_kcal_per_mol,md_cohesive_energy_kcal_per_mol
perfect,-19.31,5.16
VT_defect,-10.85,-2.23
TFe_impurity,-6.98,-7.60
EOF
