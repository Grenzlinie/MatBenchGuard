#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: binding_energies.csv ===
#!/bin/bash
cat > /app/outputs/binding_energies.csv <<'FFEOF'
configuration,binding_energy_eV
K_perfect_Csite,6.40
O2_perfect_Aendon_135,0.245
O2_K1_sideon,6.35
O2_defect_inplane_endon,4.10
O2_defect_inplane_sideon,4.64
K_defect_rim,6.80
FFEOF
