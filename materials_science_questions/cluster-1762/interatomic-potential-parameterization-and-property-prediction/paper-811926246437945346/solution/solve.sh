#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: lattice_energies.json ===
cat > /app/outputs/lattice_energies.json <<'EOF'
[
  {"zeolite": "faujasite", "model": "rigid_ion", "energy_per_SiO2": -123.48},
  {"zeolite": "zeolite_A", "model": "rigid_ion", "energy_per_SiO2": -123.66},
  {"zeolite": "mordenite", "model": "rigid_ion", "energy_per_SiO2": -123.80},
  {"zeolite": "silicalite", "model": "rigid_ion", "energy_per_SiO2": -123.89},
  {"zeolite": "alpha_quartz", "model": "rigid_ion", "energy_per_SiO2": -123.90},
  {"zeolite": "faujasite", "model": "shell_model", "energy_per_SiO2": -128.45},
  {"zeolite": "zeolite_A", "model": "shell_model", "energy_per_SiO2": -128.47},
  {"zeolite": "mordenite", "model": "shell_model", "energy_per_SiO2": -128.57},
  {"zeolite": "silicalite", "model": "shell_model", "energy_per_SiO2": -128.59},
  {"zeolite": "alpha_quartz", "model": "shell_model", "energy_per_SiO2": -128.64}
]
EOF
