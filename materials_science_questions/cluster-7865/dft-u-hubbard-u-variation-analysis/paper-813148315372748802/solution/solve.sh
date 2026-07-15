#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: phase_diagram.csv ===
cat > "$OUTDIR/phase_diagram.csv" << 'FFEOF'
ground_state_symmetry,magnetic_character,strain
P4mm,AFM,-5.6
P4mm,AFM,-5.1
P4mm,AFM,-4.6
Pbam,FM,-4.1
Pbam,FM,-3.6
Pbam,FM,-3.1
Pbam,FM,-2.6
Pbam,FM,-2.1
Pbam,FM,-1.6
Pbam,FM,-1.1
Pbam,FM,-0.6
P21/c,FM,-0.1
P21/c,FM,0.4
Pc,FM,0.9
Pc,FM,1.4
Pc,FM,1.9
Pc,FM,2.4
Pc,FM,2.9
Pc,FM,3.4
Pc,FM,3.9
Pc,FM,4.4
Pc,FM,4.9
Pc,FM,5.4
Pc,AFM,5.89
FFEOF

# === solve block: multiferroic_properties.csv ===
cat > "$OUTDIR/multiferroic_properties.csv" << 'FFEOF'
MAE_001_meV_per_Co,MAE_100_meV_per_Co,Px_muC_cm2,Py_muC_cm2,Pz_muC_cm2,alpha_gaussian_unit,band_gap_eV,strain,total_magnetic_moment_mu_B
0.16,0.61,-7.37,-7.37,3.93,0.00144,0.12,2.3,6.0
FFEOF
