#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_MgGa_formation_energy.txt ===
echo '0.783 eV' > /app/outputs/step_01_MgGa_formation_energy.txt

# === solve block: step_02_VN_crossing.txt ===
echo '1.835 eV' > '/app/outputs/step_02_VN_crossing.txt'

# === solve block: step_03_VN_vertical_IE.txt ===
echo '44 meV' > '/app/outputs/step_03_VN_vertical_IE.txt'

# === solve block: step_04_MgGa_PL_transitions.csv ===
printf 'configuration,final_state,energy_eV\nbasal-plane,singlet,3.272\naxial,singlet,3.471\nbasal-plane,triplet,3.228\naxial,triplet,3.196\n' > "/app/outputs/step_04_MgGa_PL_transitions.csv"
