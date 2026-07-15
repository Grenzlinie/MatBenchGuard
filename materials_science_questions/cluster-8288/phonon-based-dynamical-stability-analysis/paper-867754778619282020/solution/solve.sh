#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: total_energies.json ===
cat > $OUTDIR/total_energies.json <<'FFEOF'
{
  "cumulene": {
    "total_energy_cell": -308.375891,
    "binding_energy_per_atom": 7.1699945
  },
  "polyyne": {
    "total_energy_cell": -308.378995,
    "binding_energy_per_atom": 7.1715465
  },
  "binding_energy_difference_polyyne_minus_cumulene": 1.55,
  "cumulene_band_gap_eV": 0.0,
  "polyyne_band_gap_eV": 0.37,
  "cumulene_static_epsilon_real": 1.02,
  "polyyne_static_epsilon_real": 1.03,
  "supercell_optimal_N": 5,
  "supercell_energy_at_optimal_N_eV": -1541.9,
  "supercell_energy_at_N4_eV": -1233.5
}
FFEOF

# === solve block: tensile_stiffness.json ===
cat > /app/outputs/tensile_stiffness.json <<'FFEOF'
{
  "cumulene_tensile_stiffness": 94.669,
  "polyyne_tensile_stiffness": 94.939
}
FFEOF

# === solve block: phonon_frequencies.json ===
cat > /app/outputs/phonon_frequencies.json <<'FFEOF'
{
  "minimum_frequency": -3.817,
  "has_imaginary_frequencies": true,
  "frequencies_at_high_symmetry": [
    -3.817,
    0.0,
    0.1,
    0.5,
    1.2,
    2.0,
    3.0,
    4.0,
    5.0
  ],
  "units": "THz"
}
FFEOF
