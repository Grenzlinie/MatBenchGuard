#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" << 'EOF'
{
  "Ir3Nb_lattice_constant_A": 3.93,
  "Ir3Hf_lattice_constant_A": 3.97,
  "Ir3Nb_bulk_modulus_GPa": 307,
  "Ir3Hf_bulk_modulus_GPa": 270,
  "Ir3Nb_shear_modulus_GPa": 205,
  "Ir3Hf_shear_modulus_GPa": 163,
  "Ir3Nb_GB_ratio": 0.67,
  "Ir3Hf_GB_ratio": 0.60,
  "Ir3Nb_C11_GPa": 510,
  "Ir3Nb_C12_GPa": 206,
  "Ir3Nb_C44_GPa": 240,
  "Ir3Hf_C11_GPa": 403,
  "Ir3Hf_C12_GPa": 203,
  "Ir3Hf_C44_GPa": 205,
  "Ir3Nb_tensile_111_GPa": 35.95,
  "Ir3Nb_tensile_100_GPa": 34.10,
  "Ir3Nb_tensile_110_GPa": 20.62,
  "Ir3Hf_tensile_111_GPa": 31.82,
  "Ir3Hf_tensile_100_GPa": 29.24,
  "Ir3Hf_tensile_110_GPa": 17.74,
  "Ir3Nb_shear_001_110_GPa": 20.86,
  "Ir3Nb_shear_110_1-10_GPa": 16.47,
  "Ir3Nb_shear_111_1-10_GPa": 14.68,
  "Ir3Nb_shear_111_2-11_GPa": 13.51,
  "Ir3Hf_shear_001_110_GPa": 18.00,
  "Ir3Hf_shear_110_1-10_GPa": 14.63,
  "Ir3Hf_shear_111_1-10_GPa": 12.21,
  "Ir3Hf_shear_111_2-11_GPa": 11.36,
  "Ir3Nb_work_of_separation_100_I_Jm2": 6.35,
  "Ir3Nb_work_of_separation_100_II_Jm2": 5.54,
  "Ir3Nb_work_of_separation_110_I_Jm2": 6.39,
  "Ir3Nb_work_of_separation_110_II_Jm2": 5.78,
  "Ir3Hf_work_of_separation_100_I_Jm2": 5.85,
  "Ir3Hf_work_of_separation_100_II_Jm2": 5.61,
  "Ir3Hf_work_of_separation_110_I_Jm2": 5.85,
  "Ir3Hf_work_of_separation_110_II_Jm2": 5.93,
  "Ir3Nb_interface_energy_100_I_Jm2": -0.25,
  "Ir3Nb_interface_energy_100_II_Jm2": 0.54,
  "Ir3Nb_interface_energy_110_I_Jm2": -0.09,
  "Ir3Nb_interface_energy_110_II_Jm2": 0.25,
  "Ir3Hf_interface_energy_100_I_Jm2": -0.01,
  "Ir3Hf_interface_energy_100_II_Jm2": 0.30,
  "Ir3Hf_interface_energy_110_I_Jm2": 0.18,
  "Ir3Hf_interface_energy_110_II_Jm2": 0.02
}
EOF
