#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: computed_properties.json ===
cat <<'PYEOF' | python3
import json
data = [
    {
        "compound": "Be2B",
        "lattice_constant_angstrom": 4.6,
        "bulk_modulus_GPa": 145.11,
        "valence_bandwidth_eV": 13.99,
        "band_gap_Gamma_X_eV": 0.66,
        "total_DOS_at_EF_states_per_eV_cell": 0.77,
        "B_p_DOS_at_EF_states_per_eV_cell": 0.605
    },
    {
        "compound": "AlBeB",
        "lattice_constant_angstrom": 4.96,
        "bulk_modulus_GPa": 140.0,
        "valence_bandwidth_eV": 13.06,
        "band_gap_Gamma_X_eV": 0.0,
        "total_DOS_at_EF_states_per_eV_cell": 0.0,
        "B_p_DOS_at_EF_states_per_eV_cell": 0.0
    },
    {
        "compound": "MgBeB",
        "lattice_constant_angstrom": 5.23,
        "bulk_modulus_GPa": 94.0,
        "valence_bandwidth_eV": 11.28,
        "band_gap_Gamma_X_eV": 0.37,
        "total_DOS_at_EF_states_per_eV_cell": 1.22,
        "B_p_DOS_at_EF_states_per_eV_cell": 0.732
    },
    {
        "compound": "NaBeB",
        "lattice_constant_angstrom": 5.51,
        "bulk_modulus_GPa": 55.30,
        "valence_bandwidth_eV": 9.31,
        "band_gap_Gamma_X_eV": 1.07,
        "total_DOS_at_EF_states_per_eV_cell": 1.83,
        "B_p_DOS_at_EF_states_per_eV_cell": 1.097
    }
]
with open('/app/outputs/computed_properties.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF
