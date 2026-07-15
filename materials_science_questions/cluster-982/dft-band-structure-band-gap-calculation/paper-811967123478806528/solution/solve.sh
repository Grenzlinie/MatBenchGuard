#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_band_gaps.csv ===
cat > /app/outputs/step_01_band_gaps.csv <<'CSVEOF'
system,energy_band_gap_eV,optical_band_gap_eV
La,1.25,2.90
Y,1.40,3.10
Sc,1.55,3.30
CSVEOF

# === solve block: step_02_bond_angles.csv ===
cat > /app/outputs/step_02_bond_angles.csv <<'CSVEOF'
system,Ti_O_Ti_angle_deg
La,161.4
Y,157.5
Sc,156.1
CSVEOF

# === solve block: step_03_formation_energies.csv ===
cat > /app/outputs/step_03_formation_energies.csv <<'CSVEOF'
system,O_vacancy_formation_energy_eV
La,0.41
Y,0.45
Sc,0.39
CSVEOF
