#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: all_cluster_properties.csv ===
cat > /app/outputs/all_cluster_properties.csv <<'FFEOF'
cluster_name,freq_cm1,energy_au,dipole_moment_debye,bond_length_ang,homo_lumo_gap_eV,absorption_nm,wbi
Mg3O3,180,-228.379,0.230,1.831,3.92,290,0.28
Mg3S3,96,-33.087,0.380,2.342,3.76,284,0.43
Mg3Se3,80,-30.451,0.437,2.471,3.65,297,0.47
Mg3Te3,68,-26.903,0.566,2.670,3.37,315,0.52
Mg4O4_t,337,-304.593,0.387,1.963,3.59,293,0.17
Mg4S4_t,174,-44.181,0.720,2.499,3.78,261,0.26
Mg4Se4_t,106,-40.659,0.888,2.630,3.70,274,0.29
Mg4Te4_t,72,-35.918,1.220,2.830,3.51,287,0.34
Mg4O4_o,96,-304.571,0.282,1.813,4.30,291,0.26
Mg4S4_o,24,-44.143,0.477,2.321,3.86,287,0.41
Mg4Se4_o,8,-40.621,0.576,2.455,3.67,300,0.46
Mg4Te4_o,6,-35.883,0.698,2.660,3.43,316,0.48
FFEOF
