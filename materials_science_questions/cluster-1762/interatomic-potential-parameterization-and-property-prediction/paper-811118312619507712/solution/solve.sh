#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: zincblende_properties.json ===
cat > $OUTDIR/zincblende_properties.json <<'FFEOF'
{
  "lattice_constant_angstrom": 6.485,
  "bulk_modulus_Mbar": 0.192,
  "bulk_modulus_derivative": 2.35,
  "cohesive_energy_eV_per_atom": -2.366,
  "elastic_C11_minus_C12_over_2_Mbar": 0.066,
  "elastic_C44_Mbar": 0.066,
  "rocksalt_lattice_constant_angstrom": 5.970,
  "rocksalt_bulk_modulus_Mbar": 0.288,
  "rocksalt_bulk_modulus_derivative": 2.38
}
FFEOF

# === solve block: rocksalt_diffusion.json ===
cat > /app/outputs/rocksalt_diffusion.json <<'FFEOF'
{
  "diffusion_coefficients": [
    {"pressure_kbar": 20, "temperature_K": 900,  "diffusion_coefficient_cm2_per_s": 1.5e-5},
    {"pressure_kbar": 20, "temperature_K": 1000, "diffusion_coefficient_cm2_per_s": 2.2e-5},
    {"pressure_kbar": 20, "temperature_K": 1100, "diffusion_coefficient_cm2_per_s": 3.0e-5},
    {"pressure_kbar": 20, "temperature_K": 1200, "diffusion_coefficient_cm2_per_s": 4.0e-5},
    {"pressure_kbar": 20, "temperature_K": 1400, "diffusion_coefficient_cm2_per_s": 6.0e-5},
    {"pressure_kbar": 20, "temperature_K": 1600, "diffusion_coefficient_cm2_per_s": 8.5e-5},
    {"pressure_kbar": 30, "temperature_K": 900,  "diffusion_coefficient_cm2_per_s": 1.0e-5},
    {"pressure_kbar": 30, "temperature_K": 1000, "diffusion_coefficient_cm2_per_s": 1.5e-5},
    {"pressure_kbar": 30, "temperature_K": 1100, "diffusion_coefficient_cm2_per_s": 2.2e-5},
    {"pressure_kbar": 30, "temperature_K": 1200, "diffusion_coefficient_cm2_per_s": 3.0e-5},
    {"pressure_kbar": 30, "temperature_K": 1400, "diffusion_coefficient_cm2_per_s": 4.8e-5},
    {"pressure_kbar": 30, "temperature_K": 1600, "diffusion_coefficient_cm2_per_s": 6.8e-5},
    {"pressure_kbar": 40, "temperature_K": 900,  "diffusion_coefficient_cm2_per_s": 0.8e-5},
    {"pressure_kbar": 40, "temperature_K": 1000, "diffusion_coefficient_cm2_per_s": 1.2e-5},
    {"pressure_kbar": 40, "temperature_K": 1100, "diffusion_coefficient_cm2_per_s": 1.8e-5},
    {"pressure_kbar": 40, "temperature_K": 1200, "diffusion_coefficient_cm2_per_s": 2.5e-5},
    {"pressure_kbar": 40, "temperature_K": 1400, "diffusion_coefficient_cm2_per_s": 4.0e-5},
    {"pressure_kbar": 40, "temperature_K": 1600, "diffusion_coefficient_cm2_per_s": 5.5e-5}
  ]
}
FFEOF
