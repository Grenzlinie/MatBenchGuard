#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
python3 -c "import json; data={'Ti_point_ion_potential_V': -51.99, 'O_point_ion_potential_V': 18.61, 'Madelung_constant': 4.807, 'E_i_V_per_m': 28200000000.0, 'E_d_V_per_m': 23800000000.0, 'A': 0.778, 'O_dipole_moment_e_A': 0.778, 'dipolar_potential_Ti_V': -0.489, 'dipolar_potential_O_V': 0.611, 'dipole_energy_contribution_kcal_mol': 50.8, 'total_corrected_lattice_energy_kcal_mol': 2480.0}; json.dump(data, open('/app/outputs/results.json', 'w'))"
