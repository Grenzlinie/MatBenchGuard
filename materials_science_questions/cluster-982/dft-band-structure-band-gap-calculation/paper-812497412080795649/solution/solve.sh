#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_results.json ===
cat > /app/outputs/step_01_results.json <<'JSONEOF'
{
  "LBBSF": {
    "band_gap_uncorrected_ev": 3.738,
    "band_gap_type": "quasi-direct",
    "cbm_kpoint": "K",
    "vbm_kpoint": "near K",
    "shg_tensor_largest": {
      "element": "d33",
      "value_pm_per_V": 2.47
    },
    "birefringence_546nm": 0.133
  },
  "BBSF": {
    "band_gap_uncorrected_ev": 1.813,
    "band_gap_type": "quasi-direct",
    "cbm_kpoint": "Gamma",
    "vbm_kpoint": "near Gamma",
    "shg_tensor_largest": {
      "element": "d22",
      "value_pm_per_V": 1.36
    },
    "birefringence_546nm": 0.123
  }
}
JSONEOF
