#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_results.json ===
python3 << 'PYEOF'
import json

data = {
    "species1": {
        "Fe_N_nacnac": [1.998, 1.996],
        "Fe_N_NO": [1.705, 1.714],
        "N_O": [1.174, 1.171],
        "delta_mm_per_s": 0.22,
        "DeltaEQ_mm_per_s": 0.83,
        "v_NO_sym_cm-1": 1775,
        "v_NO_asym_cm-1": 1822,
        "Fe_spin_population": 4.2,
        "NO_spin_populations": [-0.6, -0.6],
        "orbital_overlap_S": 0.85,
        "Fe_S_values": [
            "HS Fe(III) S=5/2",
            "HS Fe(II) S=2"
        ],
        "num_singly_occupied_Fe_d_orbitals": 5,
        "num_singly_occupied_NO_pi_orbitals": 4
    },
    "species2": {
        "Fe_N_nacnac": [2.055, 2.052],
        "Fe_N_NO": [1.679, 1.679],
        "N_O": [1.204, 1.199],
        "delta_mm_per_s": 0.25,
        "DeltaEQ_mm_per_s": 1.21,
        "v_NO_sym_cm-1": 1639,
        "v_NO_asym_cm-1": 1684,
        "Fe_spin_population": 3.6,
        "NO_spin_populations": [-0.6, -0.6],
        "orbital_overlap_S": 0.85,
        "Fe_S_values": [
            "HS Fe(II) S=2"
        ],
        "num_singly_occupied_Fe_d_orbitals": 4,
        "num_singly_occupied_NO_pi_orbitals": 4
    }
}

with open("/app/outputs/computed_results.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
