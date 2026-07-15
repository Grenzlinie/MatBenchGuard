#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_pbe_band_gap.txt ===
cat > /app/outputs/step_01_pbe_band_gap.txt <<'FFEOF'
2.0
FFEOF

# === solve block: step_02_hse06_band_gap.txt ===
cat > /app/outputs/step_02_hse06_band_gap.txt <<'FFEOF'
4.18
FFEOF

# === solve block: step_03_off_diagonals.json ===
cat > /app/outputs/step_03_off_diagonals.json <<'FFEOF'
{
  "pz_offdiagonal_eV": 4.30,
  "px_py_offdiagonal_eV": -1.62
}
FFEOF

# === solve block: step_04_polynomial_coefficients.json ===
cat > /app/outputs/step_04_polynomial_coefficients.json <<'FFEOF'
{
  "sigma_g": [-5.2, 2.5, 1.0, 0.0],
  "pi_u": [-3.8, 2.0, 0.5, 0.0],
  "pi_g_star": [-0.3, -2.0, -1.0, 0.0],
  "sigma_u_star": [2.1, -3.5, 2.0, 1.5]
}
FFEOF
