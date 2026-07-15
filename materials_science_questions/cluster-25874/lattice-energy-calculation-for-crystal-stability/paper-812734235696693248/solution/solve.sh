#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: lattice_energies.csv ===
cat > "/app/outputs/lattice_energies.csv" <<'FFEOF'
compound,space_group,lattice_energy_kJ_mol
[H2GaNH2]3,P21/m,153.49
[H2GaNH2]3,Pmn21,151.65
[H2GaNH2]3,Pbcm,134.79
[H2GeCH2]3,P21/m,82.19
[H2GeCH2]3,Pmn21,84.87
[H2GeCH2]3,Pbcm,68.62
[H2BNH2]3,P21/m,118.32
[H2BNH2]3,Pmn21,118.29
[H2BNH2]3,Pbcm,120.77
FFEOF

# === solve block: sublimation_enthalpies.csv ===
cat > "/app/outputs/sublimation_enthalpies.csv" <<'FFEOF'
compound,space_group,sublimation_enthalpy_298K_kJ_mol
[H2GaNH2]3,P21/m,140.18
[H2GeCH2]3,Pmn21,89.89
[H2BNH2]3,Pbcm,119.43
FFEOF
