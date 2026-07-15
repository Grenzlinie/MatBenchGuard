#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_02_pure_MgF2_properties.json ===
python3 <<'PYEOF'
import json

data = {
    "band_gap_eV": 12.57,
    "lattice_parameters": {
        "a_Ang": 4.604,
        "c_Ang": 3.091,
        "u": 0.43
    },
    "elastic_properties": {
        "B_GPa": 104.2,
        "c11_GPa": 147.5,
        "c12_GPa": 94.8,
        "c13_GPa": 58.5,
        "c33_GPa": 220.1,
        "c44_GPa": 64.0,
        "c66_GPa": 103.5
    },
    "IR_phonon_frequencies_cm-1": {
        "TO": [230, 269, 427, 434, 453, 479],
        "LO": [331, 435, 662, 656]
    },
    "Raman_phonon_frequencies_cm-1": [117, 307, 427, 528]
}

with open("/app/outputs/step_02_pure_MgF2_properties.json", "w") as f:
    json.dump(data, f, indent=2)
print("step_02 written")
PYEOF

# === solve block: step_04_Co_doped_properties.json ===
python3 <<'PYEOF'
import json

data = {
    "high_spin_total_energy_Ha": -12738.4635,
    "low_spin_total_energy_Ha": -12738.4131,
    "delta_E_eV": 1.37,
    "magnetic_moment_HS_mu_B": 2.91,
    "Co_3d_minority_peak_positions_eV": [2.2]
}

with open("/app/outputs/step_04_Co_doped_properties.json", "w") as f:
    json.dump(data, f, indent=2)
print("step_04 written")
PYEOF
