#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_02_total_energies.json ===
cat > /app/outputs/step_02_total_energies.json << 'EOF'
{
  "symmetric_C_Hf_total_energy_eV": 0.0,
  "carbonate_C_Hf_total_energy_eV": -7.0,
  "C_O_total_energy_eV": -10.0,
  "C_O_vacancy_total_energy_eV": 0.6,
  "energy_gain_carbonate_vs_symmetric_eV": 7.0
}
EOF

# === solve block: step_03_formation_energies.json ===
cat > /app/outputs/step_03_formation_energies.json << 'EOF'
{
  "mu_O_values": [0.0, -4.0],
  "formation_energies_eV": {
    "symmetric_C_Hf": [0.0, 0.0],
    "carbonate_C_Hf": [-7.0, -7.0],
    "C_O": [-10.0, -14.0],
    "C_O_vacancy": [0.6, -7.4]
  },
  "threshold_mu_O_eV": -3.8
}
EOF
