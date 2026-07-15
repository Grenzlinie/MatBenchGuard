#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: volume_derivatives.csv ===
cat > "$OUTDIR/volume_derivatives.csv" <<'VEOF'
crystal,V_d_eps0_dV,V2_d2_eps0_dV2
LiF,29.2,153
LiCl,41.9,281
LiBr,44.1,303
NaF,11.7,47
NaCl,15.0,84
NaBr,14.9,85
NaI,18.0,112
KF,12.1,57
KCl,8.52,41
KBr,7.72,35
KI,6.69,33
RbF,16.7,95
RbCl,8.37,48
RbBr,7.24,42
RbI,6.54,38
VEOF

# === solve block: gruneisen_parameters.csv ===
cat > "$OUTDIR/gruneisen_parameters.csv" <<'GEOF'
crystal,gamma_TO,gamma_LO
LiF,2.63,0.96
LiCl,3.04,1.11
LiBr,3.08,1.16
NaF,2.41,1.15
NaCl,2.84,1.43
NaBr,2.91,1.51
NaI,3.17,1.64
KF,2.43,1.14
KCl,2.39,1.35
KBr,2.42,1.43
KI,2.50,1.56
RbF,2.66,1.14
RbCl,2.37,1.33
RbBr,2.37,1.40
RbI,2.43,1.51
GEOF

# === solve block: pressure_derivatives.csv ===
cat > "$OUTDIR/pressure_derivatives.csv" <<'PEOF'
crystal,d_eps0_dP_normalized,d2_eps0_dP2_normalized
LiF,-4.89,84.9
LiCl,-11.94,538
LiBr,-14.12,813
NaF,-4.95,110
NaCl,-10.71,541
NaBr,-12.21,763
NaI,-16.63,1426
KF,-7.27,249
KCl,-10.18,658
KBr,-10.79,814
KI,-11.33,1115
RbF,-9.65,448
RbCl,-10.97,876
RbBr,-11.28,1058
RbI,-12.48,1488
PEOF
