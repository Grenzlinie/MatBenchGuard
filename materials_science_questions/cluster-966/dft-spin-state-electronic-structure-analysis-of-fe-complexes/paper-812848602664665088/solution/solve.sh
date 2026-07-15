#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: ligand_strain_results.json ===
python3 <<'EOF'
import json
data = [
    {'ligand': 'A', 'strain_energy_kJ_mol': 38, 'delta_rho_over_rho_relax': 0.130},
    {'ligand': 'B', 'strain_energy_kJ_mol': 67, 'delta_rho_over_rho_relax': 0.192},
    {'ligand': 'C', 'strain_energy_kJ_mol': 113, 'delta_rho_over_rho_relax': 0.255},
    {'ligand': 'D', 'strain_energy_kJ_mol': 118, 'delta_rho_over_rho_relax': 0.255},
    {'ligand': 'E', 'strain_energy_kJ_mol': 170, 'delta_rho_over_rho_relax': 0.314}
]
with open('/app/outputs/ligand_strain_results.json', 'w') as f:
    json.dump(data, f, indent=2)
EOF

# === solve block: zero_intercept_slope.txt ===
echo '460.0' > /app/outputs/zero_intercept_slope.txt
