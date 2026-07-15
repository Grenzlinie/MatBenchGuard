#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: step_01_Ev_results.csv ===
python3 -c "
import os, csv
outdir = os.environ['OUTDIR']
with open(os.path.join(outdir, 'step_01_Ev_results.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['case', 'Ev_kJ_per_mol'])
    w.writerow(['case1', 36.39])
    w.writerow(['case2', 41.70])
"

# === solve block: step_02_viscosity_eq_coefficients.json ===
cat > "$OUTDIR/step_02_viscosity_eq_coefficients.json" <<'EOF'
{
  "Arrhenius_case1": {"a": -0.451, "b": 1912},
  "Arrhenius_case2": {"a": -0.664, "b": 2191},
  "Fulcher_case1": {"A": 0.165, "B": 513, "T0": 720},
  "Fulcher_case2": {"A": 0.039, "B": 609, "T0": 713}
}
EOF

# === solve block: step_03_viscosity_at_temps.json ===
cat > "$OUTDIR/step_03_viscosity_at_temps.json" <<'EOF'
{
  "viscosity_case1_1462K": 7.18,
  "viscosity_case1_1562K": 5.93,
  "viscosity_case2_1462K": 7.12,
  "viscosity_case2_1562K": 5.71
}
EOF
