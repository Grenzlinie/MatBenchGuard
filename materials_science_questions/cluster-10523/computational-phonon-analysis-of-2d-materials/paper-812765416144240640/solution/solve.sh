#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: structural_parameters.json ===
cat > /app/outputs/structural_parameters.json <<'FFEOF'
{
  "bulk_lattice_constant_angstrom": 5.57,
  "reconstruction_energy_eV_per_dimer": 1.41,
  "dimer_bond_length_angstrom": 2.39,
  "dimer_tilt_angle_degrees": 17
}
FFEOF

# === solve block: phonon_frequencies.json ===
cat > /app/outputs/phonon_frequencies.json <<'FFEOF'
{
  "rocking_mode_Gamma_meV": 14.1,
  "dimer_stretch_ds1_K_meV": 24.5,
  "dimer_stretch_ds2_K_meV": 32.6,
  "backbond_sb_K_meV": 35.5,
  "backbond_sb2_K_meV": 26.3
}
FFEOF

# === solve finalize ===
echo "All scored artifacts written."
