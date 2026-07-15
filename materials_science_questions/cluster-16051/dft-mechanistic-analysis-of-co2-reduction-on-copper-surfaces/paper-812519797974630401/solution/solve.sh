#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: o2_dissociation_results.csv ===
cat > /app/outputs/o2_dissociation_results.csv <<'FFEOF'
Model,Barrier_eV,q_Pt,q_Cu,q_O2,d_OO_angstrom
Pt (111),0.23,"0.43, 0.28",,-1.13,2.04
PtCu-1 (111),0.88,0.29,0.65,-1.22,2.21
PtCu-4 (111),0.92,0.36,"0.60, 0.57",-1.30,2.26
IMC (012),0.98,0.13,"0.56, 0.54",-1.26,2.14
FFEOF

# === solve block: co_adsorption_results.csv ===
cat > /app/outputs/co_adsorption_results.csv <<'FFEOF'
Model,Site,DE_eV,q_surface_atom,q_CO,nu_CO_cm1
Pt (111),Pt,1.78,0.227,-0.123,2054
PtCu-1 (111),Pt,1.84,0.180,-0.126,2049
PtCu-1 (111),Cu,0.68,0.530,-0.083,2066
PtCu-4 (111),Pt,1.90,0.119,-0.143,2040
PtCu-4 (111),Cu,0.83,0.505,-0.125,2061
IMC (012),Pt,1.85,-0.058,-0.173,2030
IMC (012),Cu,0.62,0.471,-0.120,2051
FFEOF

# === solve block: co_o2_reaction_results.csv ===
cat > /app/outputs/co_o2_reaction_results.csv <<'FFEOF'
Model,Barrier_eV,d_OO_angstrom,d_CO_angstrom,d_CM_angstrom,q_M
Pt (111),1.68,2.12,1.93,2.37,0.02
PtCu-1 (111),1.78,1.91,1.92,2.49,0.05
PtCu-4 (111),1.48,1.92,1.99,2.50,0.05
IMC (012),0.50,1.81,1.75,2.75,0.35
FFEOF
