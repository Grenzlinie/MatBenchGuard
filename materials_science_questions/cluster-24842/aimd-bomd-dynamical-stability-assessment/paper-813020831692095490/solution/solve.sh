#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: eta1_3b1_CV5_timeseries.csv ===
python3 /solution/generate_cv5.py

# === solve block: eta1_3b1_md_summary.json ===
cat > /app/outputs/eta1_3b1_md_summary.json <<'FFEOF'
{
  "average_CV1": -1.289,
  "average_CV2": 4.301,
  "average_CV3": 2.76,
  "average_CV4": -63.8,
  "average_CV5": -0.363,
  "average_CV6": 76.2,
  "full_cr_rotation_observed": false
}
FFEOF

# === solve block: eta3_3b1_md_summary.json ===
cat > /app/outputs/eta3_3b1_md_summary.json <<'FFEOF'
{
  "conversion_time_ps": 30.6,
  "average_CV1_before": 0.0,
  "average_CV1_after": -1.289
}
FFEOF

# === solve block: free_energy_barriers.json ===
cat > /app/outputs/free_energy_barriers.json <<'FFEOF'
{
  "indenyl_slippage_deltaG_kcal_mol": 8.1,
  "cr_co3_rotation_deltaG_kcal_mol": 16.0,
  "allyl_rotation_deltaG_kcal_mol": 9.1
}
FFEOF
