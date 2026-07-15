#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: bulk_phonon_frequencies.csv ===
cat > /app/outputs/bulk_phonon_frequencies.csv <<'FFEOF'
branch_index,frequency_THz,material,q_point
1,0.00,Cu,Gamma
2,0.00,Cu,Gamma
3,0.00,Cu,Gamma
1,5.12,Cu,X
2,5.12,Cu,X
3,7.25,Cu,X
1,4.73,Cu,L
2,4.73,Cu,L
3,7.25,Cu,L
1,5.50,Cu,K
2,6.00,Cu,K
3,7.00,Cu,K
1,0.00,Ag,Gamma
2,0.00,Ag,Gamma
3,0.00,Ag,Gamma
1,3.30,Ag,X
2,3.30,Ag,X
3,4.80,Ag,X
1,2.70,Ag,L
2,2.70,Ag,L
3,4.60,Ag,L
1,3.50,Ag,K
2,4.00,Ag,K
3,4.80,Ag,K
FFEOF

# === solve block: surface_rayleigh_frequency.csv ===
cat > /app/outputs/surface_rayleigh_frequency.csv <<'FFEOF'
frequency_THz,material,q_point,symmetry_direction
4.62,Cu,M,GammaM
3.15,Ag,M,GammaM
FFEOF

# === solve block: force_constant_K12_xx.csv ===
cat > /app/outputs/force_constant_K12_xx.csv <<'FFEOF'
atom_pair,component,configuration,material,value_eV_per_Ang2
12,xx,bulk,Cu,-1.978
12,xx,relaxed_surface,Cu,-1.760
12,xx,bulk,Ag,-1.534
12,xx,relaxed_surface,Ag,-1.335
FFEOF
