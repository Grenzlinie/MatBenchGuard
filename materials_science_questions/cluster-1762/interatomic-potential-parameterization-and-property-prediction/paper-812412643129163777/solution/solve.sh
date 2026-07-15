#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_threshold_energies.csv ===
# Write threshold displacement energies
cat > "$OUTDIR/step_01_threshold_energies.csv" <<'FFEOF'
atom_type,error,threshold_energy
Ga,1,45
N,2,109
FFEOF

# === solve block: step_02_defect_counts.csv ===
# Write average defect counts per cascade from Table 1
cat > "$OUTDIR/step_02_defect_counts.csv" <<'FFEOF'
Ga_N,I_Ga,I_N,N_Ga,V_Ga,V_N,energy_eV,recoil_type
0.02,0.32,0.80,0.22,0.12,1.00,200,N
0.33,1.43,1.27,0.43,1.37,1.33,400,N
0.71,2.76,2.67,1.33,2.14,3.29,1000,N
0.75,6.0,3.13,1.50,5.3,3.87,2000,N
2.92,12.6,9.9,4.2,11.3,11.2,5000,N
7.8,26.0,24.9,12.4,21.4,29.5,10000,N
0.12,1.19,0.41,0.02,1.28,0.32,200,Ga
0.26,1.84,1.2,0.30,1.80,1.24,400,Ga
0.80,3.50,3.6,1.25,3.05,4.05,1000,Ga
2.36,6.0,4.9,1.18,4.8,6.1,2000,Ga
2.75,13.1,11.3,4.6,11.3,13.1,5000,Ga
5.9,25.0,21.8,8.8,22.1,24.6,10000,Ga
FFEOF
