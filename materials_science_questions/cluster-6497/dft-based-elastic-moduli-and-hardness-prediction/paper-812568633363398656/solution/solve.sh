#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: phase_properties.csv ===
cat > "$OUTDIR/phase_properties.csv" <<'CSVEOF'
phase,structure,formation_energy_eV_atom,a_A,b_A,c_A,bulk_modulus_GPa
Mg,R-3m,0.0,7.9734,7.9734,7.9734,35.9
Pd,Fm-3m,0.0,2.7394,2.7394,2.7394,169.1
Mg6Pd,Fm-3m,-0.254,19.968,19.968,19.968,58.0
Mg3Pd,P6_3cm,-0.414,7.9136,7.9136,8.3638,59.7
Mg5Pd2,P63/mmc,-0.4642,8.614,8.614,8.1364,62.6
MgPd,Pm-3m,-0.7088,3.1405,3.1405,3.1405,93.7
Mg9Pd11,P4/mmm,-0.6778,4.2110,4.2110,3.4749,114.8
Mg3Pd5,Pbam,-0.6202,5.4378,10.6638,4.1722,110.8
MgPd2,Pnma,-0.5802,5.4545,4.0815,8.11262,119.9
MgPd3,I4/mmm,-0.4724,3.9053,3.9053,15.6214,130.2
CSVEOF

# === solve finalize ===
echo "Oracle output written."
