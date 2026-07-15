#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: thermal_expansion_coefficients.csv ===
cat > "$OUTDIR/thermal_expansion_coefficients.csv" <<'CSVEOF'
target,value_at_Tr,a0,a1
volume,226.402,2.416e-05,7.30e-09
a_axis,3.14554,4.53e-06,2.80e-09
b_axis,9.86370,1.143e-05,8.6e-10
c_axis,7.29697,8.29e-06,3.52e-09
CSVEOF

# === solve block: fitted_gruneisen_parameters.csv ===
cat > "$OUTDIR/fitted_gruneisen_parameters.csv" <<'CSVEOF'
parameter,fit_target,fitted_value,fitted_esd
theta_D,volume,703,11
Q,volume,2.77e-17,2e-19
V0,volume,225.666,0.006
b,volume,1.9,0.2
theta_D,a_axis,648,37
Q_A,a_axis,13.7e-17,3e-18
a0,a_axis,3.14317,0.00007
b_A,a_axis,21,3
theta_D,b_axis,647,15
Q_A,b_axis,6.31e-17,6e-19
b0,b_axis,9.8485,0.0002
b_A,b_axis,-2.1,0.6
theta_D,c_axis,859,13
Q_A,c_axis,7.30e-17,7e-19
c0,c_axis,7.29006,0.00008
b_A,c_axis,4.3,0.6
CSVEOF

# === solve block: axial_incompressibility_ratios.csv ===
cat > "$OUTDIR/axial_incompressibility_ratios.csv" <<'CSVEOF'
axis,ratio
a,1.88
b,0.86
c,1.0
CSVEOF
