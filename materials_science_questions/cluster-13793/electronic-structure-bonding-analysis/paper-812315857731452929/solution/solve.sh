#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: relaxed_params.json ===
cat > /app/outputs/relaxed_params.json <<'FFEOF'
[
  {"compound": "Sc2AlC", "a_A": 3.280, "c_over_a": 4.687, "V_o_A3_per_atom": 17.90, "B_GPa": 99, "E_f_eV_per_atom": -0.445},
  {"compound": "Sc2GaC", "a_A": 3.253, "c_over_a": 4.861, "V_o_A3_per_atom": 18.12, "B_GPa": 96, "E_f_eV_per_atom": -0.489},
  {"compound": "Sc2InC", "a_A": 3.272, "c_over_a": 5.028, "V_o_A3_per_atom": 19.06, "B_GPa": 93, "E_f_eV_per_atom": -0.517},
  {"compound": "Sc2TlC", "a_A": 3.281, "c_over_a": 5.038, "V_o_A3_per_atom": 19.27, "B_GPa": 90, "E_f_eV_per_atom": -0.466},
  {"compound": "ScC", "B_GPa": 154}
]
FFEOF

# === solve block: pseudogap.json ===
cat > /app/outputs/pseudogap.json <<'FFEOF'
[
  {"compound": "Sc2AlC", "pseudogap_energy_eV": -0.4},
  {"compound": "Sc2GaC", "pseudogap_energy_eV": -0.4},
  {"compound": "Sc2InC", "pseudogap_energy_eV": -0.4},
  {"compound": "Sc2TlC", "pseudogap_energy_eV": -0.4}
]
FFEOF
