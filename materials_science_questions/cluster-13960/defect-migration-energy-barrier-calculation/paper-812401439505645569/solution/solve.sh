#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_interstitial_energies.csv ===
cat > /app/outputs/step_01_interstitial_energies.csv <<'EOF'
defect_name,formation_energy_eV
grafted,7.0
spiro,5.5
threefold,6.8
EOF

# === solve block: step_02_stack_fault_energies.csv ===
cat > /app/outputs/step_02_stack_fault_energies.csv <<'EOF'
stacking_type,energy_meV_per_Ang2
threefold (AA-type),6.25
fourfold (ABC-type),2.13
EOF

# === solve block: step_03_intimate_frenkel_barrier.csv ===
cat > /app/outputs/step_03_intimate_frenkel_barrier.csv <<'EOF'
barrier_eV
1.4
EOF

# === solve block: step_04_divacancy_energies.csv ===
cat > /app/outputs/step_04_divacancy_energies.csv <<'EOF'
defect_name,formation_energy_eV
V2^1(beta beta),14.6
V2^2(beta beta),13.0
EOF

# === solve block: step_05_stabilization_energies.csv ===
cat > /app/outputs/step_05_stabilization_energies.csv <<'EOF'
interstitial_type,stabilization_energy_eV
threefold,0.7
spiro,1.7
EOF
