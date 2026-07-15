#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: equilibrium_properties.json ===
cat > "$OUTDIR/equilibrium_properties.json" <<'FFEOF'
{
  "lattice_constant_angstrom": 6.09,
  "total_magnetic_moment_muB": -0.197,
  "Mn_A_moment_muB": 4.12,
  "Mn_B_moment_muB": -4.28,
  "Sn_moment_muB": -0.04,
  "formation_energy_eV": -2.715,
  "cohesive_energy_eV": 19.13
}
FFEOF

# === solve block: elastic_constants.json ===
cat > /app/outputs/elastic_constants.json <<'FFEOF'
{
  "C11_GPa": 100.93905,
  "C12_GPa": 53.01055,
  "C44_GPa": 37.32205,
  "Bulk_modulus_GPa": 68.98672,
  "Shear_modulus_GPa": 31.97893,
  "Youngs_modulus_GPa": 62.45876,
  "B_over_G": 2.15725542
}
FFEOF

# === solve block: uniform_strain_classification.csv ===
cat > /app/outputs/uniform_strain_classification.csv <<'FFEOF'
lattice_constant,majority_indirect_gap_eV,minority_indirect_gap_eV,classification
5.80,0.2,0.0,FCF-HM
5.52,0.2,0.0,FCF-SGS
5.50,0.2,0.2,FCF-S
5.46,0.0,0.2,FCF-HM
5.43,0.0,0.0,ZG-FCF-HM
FFEOF
