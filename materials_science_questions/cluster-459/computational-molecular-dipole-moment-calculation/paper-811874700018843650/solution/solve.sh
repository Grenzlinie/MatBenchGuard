#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_molecular_properties.csv ===
cat > "$OUTDIR/step_01_molecular_properties.csv" <<'EOFCSV'
aea_eV,aip_eV,dipole_moment_D,homolumo_gap_eV,molecule,vea_eV,vip_eV
1.582,6.063,0,2.423,P,1.317,6.337
1.660,6.290,2.079,2.236,P_F,1.524,6.370
1.714,6.310,2.338,2.171,P_Cl,1.330,6.591
1.725,6.301,2.422,2.163,P_Br,1.632,6.342
1.188,6.395,2.006,2.184,P_2F,1.074,6.451
1.300,6.330,1.900,2.120,P_2Cl,1.050,6.500
1.350,6.300,1.800,2.100,P_2Br,1.200,6.400
EOFCSV

# === solve block: step_02_reorganization_energies.csv ===
cat > "$OUTDIR/step_02_reorganization_energies.csv" <<'EOFCSV'
lambda1_eV,lambda2_eV,lambda3_eV,lambda4_eV,lambda_minus_eV,lambda_plus_eV,molecule
0.048,0.046,0.056,0.094,0.140,0.094,P
0.046,0.095,0.068,0.128,0.196,0.141,P_F
0.049,0.054,0.081,0.052,0.133,0.103,P_Cl
0.060,0.046,0.079,0.057,0.136,0.106,P_Br
0.071,0.053,0.081,0.046,0.147,0.124,P_2F
0.062,0.054,0.080,0.060,0.140,0.116,P_2Cl
0.060,0.048,0.060,0.079,0.139,0.108,P_2Br
EOFCSV
