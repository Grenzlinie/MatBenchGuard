#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "/app/outputs"

# === solve block: reproduced_properties.json ===
cat > "/app/outputs/reproduced_properties.json" <<'FFEOF'
{
  "single_cl_adsorption": {
    "binding_energy_eV": 1.10,
    "migration_barrier_meV": 13,
    "diffusion_constant_300K_cm2s": 3.57,
    "C_Cl_bond_length_A": 2.54,
    "charge_transfer_e": 0.44,
    "magnetic_moment_muB": 0.56
  },
  "chlorographene": {
    "lattice_constant_a_A": 2.84,
    "C_C_bond_length_A": 1.72,
    "C_Cl_bond_length_A": 1.73,
    "buckling_delta_A": 0.50,
    "band_gap_eV": 1.21,
    "Raman_active_frequencies_cm-1": [105, 398, 715, 1042]
  }
}
FFEOF
