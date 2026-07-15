#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: adsorption_structures_ir.csv ===
cat > /app/outputs/adsorption_structures_ir.csv << 'EOF'
surface_type,distance_label,distance_angstrom,IR_peak_mode,wavenumber_cm,intensity
AlO_terminated,C_O_Al,1.31,,,
AlO_terminated,C_O_carbonyl,1.23,,,
AlO_terminated,O-H_bridge,1.77,,,
AlO_terminated,,,OH_stretch_surface,3189,
AlO_terminated,,,CO_stretch,1621,
hydroxylated,O_ads_H,1.17,,,
hydroxylated,O_surf_H,1.24,,,
hydroxylated,C_O_carbonyl,1.24,,,
hydroxylated,,,bridge_mode,1700,
hydroxylated,,,OH_stretch_surface,3385,
hydroxylated,,,OH_stretch_surface_bonded,3162,
EOF

# === solve finalize ===
echo 'All oracle artifacts written.'
