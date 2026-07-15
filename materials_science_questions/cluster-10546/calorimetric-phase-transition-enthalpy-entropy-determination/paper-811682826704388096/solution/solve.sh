#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_alpha_cp_data.csv ===
cat > "$OUTDIR/step_01_alpha_cp_data.csv" <<'FFEOF'
temperature_K,alpha_ppm_per_K,Cp_over_T_J_per_mol_K2
40,0.181333,0.0002
100,4.533333,0.005
200,18.133333,0.02
300,36.266667,0.04
400,49.866667,0.055
500,58.933333,0.065
600,65.28,0.072
720,68.0,0.075
FFEOF

# === solve block: step_02_fit_results.json ===
cat > "$OUTDIR/step_02_fit_results.json" <<'FFEOF'
{
  "slope": 906.6666666666667,
  "gamma_minus": 7.48,
  "r_squared": 1.0
}
FFEOF

# === solve block: step_03_beta_vs_t.csv ===
cat > "$OUTDIR/step_03_beta_vs_t.csv" <<'FFEOF'
temperature_K,beta_GPa_minus_one
40,1.356373
100,33.909333
200,135.637333
300,271.274667
400,373.002667
500,440.821333
600,488.2944
720,508.64
FFEOF
