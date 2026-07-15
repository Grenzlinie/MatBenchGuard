#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: structure_and_stability.csv ===
cat > /app/outputs/structure_and_stability.csv <<'FFEOF'
property,unit,value
lattice_constant_a,Å,4.019
lattice_constant_b,Å,4.019
exfoliation_energy,J/m^2,0.24
AIMD_stable,boolean,True
phonon_no_imaginary,boolean,True
FFEOF

# === solve block: electronic_properties.csv ===
cat > /app/outputs/electronic_properties.csv <<'FFEOF'
property,unit,value
band_gap,eV,0.75
magnetic_moment,μB/f.u.,8
FFEOF

# === solve block: mae_vs_strain.csv ===
cat > /app/outputs/mae_vs_strain.csv <<'FFEOF'
strain,MAE
-8,100
-6,180
-4,260
-2,340
0,420
2,517.5
4,615
6,712.5
8,810
FFEOF

# === solve block: valley_polarization_vs_strain.csv ===
cat > /app/outputs/valley_polarization_vs_strain.csv <<'FFEOF'
strain,valley_polarization
-8,37
-6,57.25
-4,77.5
-2,97.75
0,118
2,128
4,138
6,148
8,158
FFEOF

# === solve block: curie_temperature.txt ===
cat > /app/outputs/curie_temperature.txt <<'FFEOF'
Tc = 260 K
FFEOF

# === solve block: curie_temperature_modulation.csv ===
cat > /app/outputs/curie_temperature_modulation.csv <<'FFEOF'
condition,strain,doping,Tc
strain_-8_doping_0,-8,0,281
strain_0_doping_0,0,0,260
strain_8_doping_0,8,0,233
strain_0_doping_-0.3,0,-0.3,245
strain_0_doping_0.3,0,0.3,140
FFEOF

# === solve block: berry_and_ahc.csv ===
cat > /app/outputs/berry_and_ahc.csv <<'FFEOF'
kpoint,berry_curvature,anomalous_hall_conductivity
K,0.45,9.5
K',-0.42,9.5
FFEOF
