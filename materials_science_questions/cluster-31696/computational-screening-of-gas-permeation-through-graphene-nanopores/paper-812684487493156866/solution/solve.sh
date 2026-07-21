#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_monolayer_coordinates.xyz ===
cat > /app/outputs/step_01_monolayer_coordinates.xyz <<'XYZEOF'
12
Lattice="6.0 0.0 0.0 0.0 6.0 0.0 0.0 0.0 20.0"
C    5.75000    3.00000    0.00000
C    4.37500    5.38100    0.00000
C    1.62500    5.38100    0.00000
C    0.25000    3.00000    0.00000
C    1.62500    0.61900    0.00000
C    4.37500    0.61900    0.00000
N    0.89800    3.00000    1.00000
N    4.94900    0.37500   -1.00000
N    1.05100    0.37500    1.00000
N    5.10200    3.00000   -1.00000
N    1.05100    5.62500    1.00000
N    4.94900    5.62500   -1.00000
XYZEOF

# === solve block: step_02_water_adsorption_energy.txt ===
echo '0.617 eV' > /app/outputs/step_02_water_adsorption_energy.txt

# === solve block: step_03_permeation_barrier.txt ===
echo '26.58 kcal/mol' > /app/outputs/step_03_permeation_barrier.txt

# === solve block: step_04_cluster_adsorption_energies.json ===
cat > /app/outputs/step_04_cluster_adsorption_energies.json <<'JSONEOF'
{"(H2O)2": 0.883, "(H2O)3": 0.907}
JSONEOF

# === solve block: step_05_permeance.txt ===
echo '750 L·m⁻²·h⁻¹·bar⁻¹' > /app/outputs/step_05_permeance.txt
