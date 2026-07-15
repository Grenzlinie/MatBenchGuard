#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: band_gaps.csv ===
cat > "$OUTDIR/band_gaps.csv" <<'FFEOF'
System,BandGap
undoped,3.61
N_monodoped,0.69
F_monodoped,3.52
Cl_monodoped,3.28
Br_monodoped,3.24
I_monodoped,2.91
(N,F)_codoped_strI,2.66
(N,F)_codoped_strII,2.43
(N,Cl)_codoped,3.00
(N,Br)_codoped,3.00
(N,I)_codoped,2.90
FFEOF

# === solve block: formation_energies.csv ===
cat > "$OUTDIR/formation_energies.csv" <<'FFEOF'
System,FormationEnergy_OxygenRich,FormationEnergy_OxygenPoor
N_monodoped,5.22,0.79
F_monodoped,-1.00,-3.00
Cl_monodoped,1.50,-0.50
Br_monodoped,2.00,0.00
I_monodoped,2.50,0.50
(N,F)_codoped_strI,0.50,-2.00
(N,F)_codoped_strII,0.64,-1.86
(N,Cl)_codoped,1.00,-1.00
(N,Br)_codoped,1.50,-0.50
(N,I)_codoped,2.00,0.00
FFEOF

# === solve block: absorption_edge.csv ===
cat > "$OUTDIR/absorption_edge.csv" <<'FFEOF'
System,AbsorptionEdgeWavelength
undoped,400
(N,F)_codoped_strI,500
(N,F)_codoped_strII,510
(N,Cl)_codoped,450
(N,Br)_codoped,450
(N,I)_codoped,420
FFEOF

# === solve block: band_edge_alignment.csv ===
cat > "$OUTDIR/band_edge_alignment.csv" <<'FFEOF'
System,VBM_vs_vacuum,CBM_vs_vacuum
undoped,-6.25,-2.65
(N,F)_codoped_strI,-6.00,-3.34
(N,F)_codoped_strII,-5.80,-3.37
(N,Cl)_codoped,-6.30,-3.30
(N,Br)_codoped,-6.20,-3.20
(N,I)_codoped,-6.10,-3.20
FFEOF
