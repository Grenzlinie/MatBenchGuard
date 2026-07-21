#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: adsorption_energies.csv ===
cat > "$OUTDIR/adsorption_energies.csv" <<'FFEOF'
Model,Orientation,Site,Lambda,z_equilibrium,AdsorptionEnergy
A1,perpendicular,1,,2.35,5.81
A1,parallel,2,,2.336,8.35
A2,parallel,2,1.1,1.895,11.90
A2,parallel,2,1.2,2.193,6.49
A2,parallel,2,1.26,2.336,6.32
A2,parallel,2,1.3,2.434,6.03
B,parallel,2,,1.89,10.2
FFEOF

# === solve block: vibrational_shifts.csv ===
cat > "$OUTDIR/vibrational_shifts.csv" <<'FFEOF'
Model,nu_perp_minus_nu2,nu_parallel_minus_nu2,nu_perp_minus_nu_parallel
A1,12.3,3.3,9
A2,15.4,6.2,9.2
B,-7.1,-16.2,9.1
FFEOF
