#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_static_polarizability.json ===
cat > /app/outputs/step_01_static_polarizability.json <<'FFEOF'
{
  "alpha_core": 15.8,
  "alpha_core_valence": -0.47,
  "alpha_tail": 0.2,
  "alpha_total": 398.8,
  "alpha_valence": 383.30,
  "uncertainty_total": 0.8
}
FFEOF

# === solve block: step_02_C3_coefficients.csv ===
cat > /app/outputs/step_02_C3_coefficients.csv <<'FFEOF'
material,C3_core,C3_valence,C3_core_valence,C3_tail,C3_total
perfect_conductor,2.350,2.5309,-0.043,0.004,4.8427
Au,0.706,2.191,-0.017,0.003,2.8823
Si,0.512,1.874,-0.0131,0.0025,2.3756
SiO2,0.310,0.881,-0.0077,0.0012,1.1846
SiNx,0.383,1.335,-0.0098,0.0018,1.7100
ordinary_sapphire,0.527,1.319,-0.0127,0.0019,1.8360
extraordinary_sapphire,0.551,1.315,-0.0132,0.0019,1.8542
birefringent_sapphire,0.5391,1.317,-0.0129,0.0019,1.84523
YAG,0.490,1.283,-0.01975,0.0018,1.7635
FFEOF

# === solve block: step_03_f3_fitting_parameters.csv ===
cat > /app/outputs/step_03_f3_fitting_parameters.csv <<'FFEOF'
surface,A1,A2,B2,B3
Au,1.2525,0.8227,1.0220,0.0423
Si,0.2492,1.1910,1.244,0.0738
SiO2,1.9352,0.6079,0.8679,0.0385
SiNx,0.4169,0.9823,1.0451,0.0668
ordinary_sapphire,2.4229,0.9102,1.3174,0.0625
extraordinary_sapphire,2.5202,0.9809,1.4396,0.0693
birefringent_sapphire,2.4754,0.9471,1.3803,0.06592
YAG,1.9318,0.8565,1.1735,0.0598
FFEOF
