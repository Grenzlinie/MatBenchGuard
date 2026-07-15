#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: table_i_velocities.csv ===
cat > "$OUTDIR/table_i_velocities.csv" <<'CSVEOF'
axis,direction_6d,v1,v2,v3,v4,v5,v6
A5,"(1,0,0,0,0,0)",6340.5,3570.0,3570.0,3067.8,3067.8,5386.4
A2,"(1,1̄,0,0,0,0)",6340.1,3570.0,3570.0,1830.8,4383.6,5027.5
A3,"(1,1,1̄,1,1,1̄)",6340.0,3564.1,3575.3,1695.8,4733.3,4750.6
CSVEOF

# === solve block: table_ii_coefficients.csv ===
cat > "$OUTDIR/table_ii_coefficients.csv" <<'FFEOF'
source,a,b,beta,delta,omega0,Theta_D
Expt,2.37e-17,2.37e-43,2.63e-5,9.21e-8,3.148e13,420
Calc_A5,2.92e-17,1.58e-43,2.35e-5,6.15e-8,3.396e13,436
Calc_A2,5.45e-17,1.279e-42,4.39e-5,4.975e-7,2.284e13,354
Calc_A3,6.42e-17,1.992e-42,5.17e-5,7.748e-7,2.095e13,335
FFEOF
