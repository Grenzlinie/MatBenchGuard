#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: adsorption_energies.json ===
cat > /app/outputs/adsorption_energies.json <<'FFEOF'
{
  "terrace_M": {"E_ad": -1.72, "E_reg_rel": 0.92, "E_mol_rel": 0.07, "E_int": -2.72},
  "terrace_Dr": {"E_ad": -1.96, "E_reg_rel": 0.65, "E_mol_rel": 0.22, "E_int": -2.84},
  "terrace_Dl": {"E_ad": -1.11, "E_reg_rel": 1.26, "E_mol_rel": 1.63, "E_int": -3.63},
  "step_M": {"E_ad": -2.68, "E_reg_rel": 0.96, "E_mol_rel": 0.26, "E_int": -3.89},
  "step_Dr": {"E_ad": -3.06, "E_reg_rel": 0.24, "E_mol_rel": 0.17, "E_int": -3.48},
  "step_Dl": {"E_ad": -2.86, "E_reg_rel": 1.00, "E_mol_rel": 1.72, "E_int": -5.58}
}
FFEOF
