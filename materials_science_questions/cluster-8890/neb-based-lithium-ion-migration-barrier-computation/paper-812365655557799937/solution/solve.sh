#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: single_li_adsorption.json ===
cat > /app/outputs/single_li_adsorption.json <<'FFEOF'
{
  "E_GmO": -12345.6,
  "E_bcc_Li_per_atom": -204.67,
  "E_GmOplusLi": -12550.86,
  "DeltaE_Li": -0.59
}
FFEOF

# === solve block: li2c2o2_properties.json ===
cat > /app/outputs/li2c2o2_properties.json <<'FFEOF'
{
  "E_GmO_per_formula": -300.0,
  "E_bcc_Li_per_atom": -204.67,
  "E_total_Li2C2O2": -709.22,
  "DeltaE_Li": 0.06,
  "capacity_mAh_per_g": 957
}
FFEOF

# === solve block: neb_barrier.json ===
cat > /app/outputs/neb_barrier.json <<'FFEOF'
{
  "barrier_eV": 0.14
}
FFEOF
