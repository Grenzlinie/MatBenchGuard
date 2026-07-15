#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: spin_orbit_splittings.csv ===
cat > "$OUTDIR/spin_orbit_splittings.csv" <<'FFEOF'
molecule,state,procedure_I_splitting,procedure_II_splitting,experimental_splitting
BeH,A²π,N/A,2.13,2.14
BH+,A²π,N/A,14.0,14.0
BO,A²π,N/A,119.6,122.4
CH,X²π,28.8,31.4,28.0
CN,,N/A,53.9,52.2
CO+,A²π,N/A,124.5,117.5
CF,X²π,66.4,56.5,77.1
NO,X²π,102.5,100.0,122.1
OH,X²π,126.2,154.1,140
HF+,X²π,295.5,313.7,240
F2+,X²π,298.2,298.2,337
Cl2+,X²π,625.7,625.7,645
Br2+,X²π,2508,2508,2904
I2+,X²π,5111,5111,5162
ClF+,X²π,600.0,619.0,637
BrCl+,X²π,N/A,2364,
ICl+,X²π,N/A,4700,4678
IBr+,X²π,N/A,4859.4,4678
CNC,X²πg,27.6,26.7,26.4
NCO,X²π,83.2,84.1,95.6
CO2+,X²π,154.2,155.2,159.5
CS2+,X²π,N/A,431.9,440.0
C4H2+,X²πg,30.9,32.1,33.3
C4H2+,²πu,N/A,31.5,30.6
FFEOF
