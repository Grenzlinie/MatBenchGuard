#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: moduli.json ===
cat > "$OUTDIR/moduli.json" <<'FFEOF'
{
  "young_modulus_GPa": 16.52,
  "shear_modulus_GPa": 3.94
}
FFEOF

# === solve block: diffusion_results.csv ===
cat > "$OUTDIR/diffusion_results.csv" <<'FFEOF'
guest,strain_type,strain_value,diffusion_coefficient_m2_per_s
H2,tensile,0.0,1.00e-9
H2,tensile,7.0,1.20e-9
H2,tensile,10.0,1.50e-9
H2,shear,0.0,1.00e-9
H2,shear,7.0,0.90e-9
H2,shear,10.0,1.05e-9
CO2,tensile,0.0,1.00e-10
CO2,tensile,7.0,2.00e-10
CO2,tensile,10.0,4.50e-10
CO2,shear,0.0,1.00e-10
CO2,shear,7.0,1.10e-10
CO2,shear,10.0,1.15e-10
FFEOF

# === solve block: c2c2_average_lengths.csv ===
cat > "$OUTDIR/c2c2_average_lengths.csv" <<'FFEOF'
strain_type,strain_value,avg_c2c2_length_angstrom
tensile,0,5.15
tensile,7,5.40
tensile,10,5.54
shear,0,5.15
shear,7,5.20
shear,10,5.24
FFEOF

# === solve finalize ===
echo 'Reference oracle artifacts written.'
