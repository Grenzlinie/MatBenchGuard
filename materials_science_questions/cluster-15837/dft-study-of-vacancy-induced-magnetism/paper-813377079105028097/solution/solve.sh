#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'EOF'
{
  "single_vacancies": [
    {"system": "Bi2S3_V_Bi", "mu_B": 1.5},
    {"system": "Bi2S3_V_S", "mu_B": 0.0},
    {"system": "ZnS_V_Zn", "mu_B": 1.1},
    {"system": "ZnS_V_S", "mu_B": 0.0}
  ],
  "two_vacancies": [
    {"system": "Bi2S3_V_Bi_Bi1_Bi2", "mu_B": 3.01, "FM_lower_than_AFM": true},
    {"system": "Bi2S3_V_Bi_Bi1_Bi3", "mu_B": 3.6, "FM_lower_than_AFM": true},
    {"system": "Bi2S3_V_Bi_Bi2_Bi3", "mu_B": 4.29, "FM_lower_than_AFM": true},
    {"system": "ZnS_V_Zn_Zn1_Zn2", "mu_B": 2.21, "FM_lower_than_AFM": true},
    {"system": "ZnS_V_Zn_Zn1_Zn3", "mu_B": 2.62, "FM_lower_than_AFM": true},
    {"system": "ZnS_V_Zn_Zn1_Zn4", "mu_B": 3.04, "FM_lower_than_AFM": true}
  ],
  "single_interstitials": [
    {"system": "ZnS_Zn_i", "mu_B": 0.582},
    {"system": "Bi2S3_Bi_i", "mu_B": 0.591}
  ]
}
EOF
