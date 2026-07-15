#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: bde_results.json ===
cat > "$OUTDIR/bde_results.json" <<'FFEOF'
{
  "D0_1b_kcal_per_mol": 63.8,
  "D0_2_kcal_per_mol": 44.9,
  "energy_difference_1b_minus_1a_kcal_per_mol": -4.2
}
FFEOF

# === solve block: nmr_shifts.json ===
cat > "$OUTDIR/nmr_shifts.json" <<'FFEOF'
{
  "13C_carbene_shift_ppm": 290.3,
  "13C_axial_CO_shift_ppm": 254.1,
  "13C_equatorial_CO_shift_ppm": 237.7,
  "13C_average_CO_shift_ppm": 245.9,
  "19F_shift_ppm": 162.8
}
FFEOF

# === solve block: anisotropy_components.json ===
cat > "$OUTDIR/anisotropy_components.json" <<'FFEOF'
{
  "delta_YY_ppm": 546.6,
  "delta_XX_ppm": 190.2,
  "delta_ZZ_ppm": 134.1
}
FFEOF
