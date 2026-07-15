#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results.csv ===
cat > /app/outputs/results.csv <<'FFEOF'
phase,formation_energy_eV_per_atom,a_angstrom,b_angstrom,c_angstrom,bulk_modulus_GPa
Mg,0,7.9734,7.9734,7.9734,35.9
Pd,0,2.7394,2.7394,2.7394,169.1
Mg6Pd,-0.254,19.968,19.968,19.968,58.0
Mg3Pd,-0.414,7.9136,7.9136,8.3638,59.7
Mg5Pd2,-0.4642,8.614,8.614,8.1364,62.6
MgPd,-0.7088,3.1405,3.1405,3.1405,93.7
Mg9Pd11,-0.6778,4.2110,4.2110,3.4749,114.8
Mg3Pd5,-0.6202,5.4378,10.6638,4.1722,110.8
MgPd2,-0.5802,5.4545,4.0815,8.11262,119.9
MgPd3,-0.4724,3.9053,3.977,15.6214,130.2
FFEOF
