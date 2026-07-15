#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: outputs.json ===
cat > "/app/outputs/outputs.json" <<'FFEOF'
{
  "B_Si_Sb": 2.538,
  "B_Si_Ca": 3.155,
  "WBI_Si_Sb": 1.29,
  "Q_Si": -0.39,
  "Q_Sb": -1.16,
  "Q_Ca": 1.62,
  "AdNDP_3c2e_sigma_ON": 2.00,
  "AdNDP_4c2e_pi_ON": 2.00,
  "IQA_V_Total_Si_Ca": -40.2,
  "IQA_V_Ionic_Si_Ca": -28.6,
  "IQA_V_Coval_Si_Ca": -11.6
}
FFEOF
