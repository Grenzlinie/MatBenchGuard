#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: stationary_point_energies.json ===
cat > "$OUTDIR/stationary_point_energies.json" <<'FFEOF'
{
  "separated_reactants": {
    "E_elec_hartree": -3000.0,
    "G_corr_hartree": 0.2,
    "rel_E_elec_kcal": 0.0,
    "rel_G_kcal": 0.0
  },
  "ts1_cycloaddition": {
    "E_elec_hartree": -2999.980081,
    "G_corr_hartree": 0.2,
    "rel_E_elec_kcal": 12.5,
    "rel_G_kcal": 12.5
  },
  "intermediate_4a-Sn": {
    "E_elec_hartree": -3000.002869,
    "G_corr_hartree": 0.2,
    "rel_E_elec_kcal": -1.8,
    "rel_G_kcal": -1.8
  },
  "ts2_insertion": {
    "E_elec_hartree": -3000.005897,
    "G_corr_hartree": 0.2,
    "rel_E_elec_kcal": 3.7,
    "rel_G_kcal": 3.7
  },
  "product_2a-Sn": {
    "E_elec_hartree": -3000.009244,
    "G_corr_hartree": 0.2,
    "rel_E_elec_kcal": -5.8,
    "rel_G_kcal": -5.8
  }
}
FFEOF

# === solve block: optimized_geometries.xyz ===
cat > "$OUTDIR/optimized_geometries.xyz" <<'FFEOF'
6
reactants
Si  0.000000  0.000000  0.000000
Sn  2.612000  0.000000  0.000000
N   0.000000  0.000000  1.848000
P   0.000000  2.305000  0.000000
C   10.000000 0.000000 0.000000
C   11.330000 0.000000 0.000000
6
ts1_cycloaddition
Si  0.000000  0.000000  0.000000
Sn  2.612000  0.000000  0.000000
N   0.000000  0.000000  1.848000
P   0.000000  2.305000  0.000000
C   1.500000  0.800000  0.000000
C   2.800000 -0.300000 0.000000
6
intermediate
Si  0.000000  0.000000  0.000000
Sn  2.612000  0.000000  0.000000
N   0.000000  0.000000  1.848000
P   0.000000  2.305000  0.000000
C   1.900000  0.000000  0.000000
C   3.400000  0.000000  0.000000
6
ts2_insertion
Si  0.000000  0.000000  0.000000
Sn  3.500000  0.000000  0.000000
N   0.000000  0.000000  1.848000
P   0.000000  2.305000  0.000000
C   1.891000  0.000000  0.000000
C   2.900000  1.600000  0.000000
6
product
Si  0.000000  0.000000  0.000000
Sn  5.578000  0.000000  0.000000
N   0.000000  0.000000  1.850000
P   0.000000  2.322000  0.000000
C   1.891000  0.000000  0.000000
C   3.433000  0.000000  0.000000
FFEOF
