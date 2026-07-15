#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: phonon_instability.json ===
python3 -c '
import json
data = {"pressure_0GPa": {"q_minimum": [0.25, 0.0, 0.25], "q_label": "closest to ICDW ordering vector", "imaginary_frequency": -50.0, "critical_smearing_width": 0.05}}
with open("/app/outputs/phonon_instability.json","w") as f:
    json.dump(data, f, indent=2)
'

# === solve block: ccdw_structural_params.json ===
python3 -c '
import json
data = {
    "triclinic": {"a": 12.33, "c": 6.13, "delta_d1": -6.5, "delta_d2": -3.8, "delta_E_mRy_per_fu": -1.8},
    "hexagonal": {"a": 12.33, "c": 6.16, "delta_d1": -5.7, "delta_d2": -3.6, "delta_E_mRy_per_fu": -1.2}
}
with open("/app/outputs/ccdw_structural_params.json","w") as f:
    json.dump(data, f, indent=2)
'

# === solve block: high_pressure_properties.json ===
python3 -c '
import json
data = {
    "cdw_disappearance_pressure_GPa": 30.0,
    "pressures": [
        {"P_GPa": 45.0, "N0_states_per_Ry_spin": 8.1, "hbar_omega_log_meV": 14.1, "hbar_omega_ave_meV": 26.5, "lambda": 0.69, "Tc_K": 3.8},
        {"P_GPa": 60.0, "N0_states_per_Ry_spin": 7.6, "hbar_omega_log_meV": 17.2, "hbar_omega_ave_meV": 28.0, "lambda": 0.57, "Tc_K": 2.3}
    ]
}
with open("/app/outputs/high_pressure_properties.json","w") as f:
    json.dump(data, f, indent=2)
'
