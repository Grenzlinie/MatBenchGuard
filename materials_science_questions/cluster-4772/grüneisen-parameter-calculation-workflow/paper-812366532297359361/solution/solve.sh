#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_04_moments_theta_inf.json ===
cat > "$OUTDIR/step_04_moments_theta_inf.json" <<'FFEOF'
{
  "mu2": 1.72e26,
  "mu4": 5.33e52,
  "mu6": 1.91e79,
  "theta_inf": 814
}
FFEOF

# === solve block: step_06_anharmonic_coefficients.json ===
cat > "$OUTDIR/step_06_anharmonic_coefficients.json" <<'FFEOF'
{
  "b1": 8.0e-5,
  "b2": 1.19e-7
}
FFEOF

# === solve block: step_07_gruneisen_functions.csv ===
cat > "$OUTDIR/step_07_gruneisen_functions.csv" <<'FFEOF'
T,gamma_a,gamma_b,gamma_c,gamma_volume
300,0.82,0.98,1.18,1.02
350,0.83,1.02,1.22,1.06
400,0.84,1.06,1.26,1.10
450,0.85,1.10,1.30,1.14
500,0.86,1.12,1.33,1.18
550,0.87,1.14,1.35,1.22
600,0.88,1.16,1.36,1.24
650,0.88,1.16,1.37,1.25
700,0.88,1.17,1.38,1.26
FFEOF
