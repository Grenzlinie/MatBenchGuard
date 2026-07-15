#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: effective_formation_energies.csv ===
cat > "$OUTDIR/effective_formation_energies.csv" <<'FFEOF'
defect_type,composition,energy_eV
Fe_vac_alpha,70,1.25
Fe_vac_alpha,75,1.25
Fe_vac_alpha,80,1.26
Fe_vac_gamma,70,2.27
Fe_vac_gamma,75,2.27
Fe_vac_gamma,80,2.28
Al_vac,70,1.41
Al_vac,75,1.39
Al_vac,80,1.38
Fe_antisite_Al,70,0.0
Fe_antisite_Al,75,0.0
Fe_antisite_Al,80,0.0
Al_antisite_Fe_gamma,70,0.0
Al_antisite_Fe_gamma,75,0.0
Al_antisite_Fe_gamma,80,0.0
Al_antisite_Fe_alpha,70,1.79
Al_antisite_Fe_alpha,75,1.82
Al_antisite_Fe_alpha,80,1.84
FFEOF
