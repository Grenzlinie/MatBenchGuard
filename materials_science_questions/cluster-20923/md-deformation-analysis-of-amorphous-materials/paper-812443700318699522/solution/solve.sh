#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_zero_analysis.json ===
cat > /app/outputs/step_01_zero_analysis.json <<'FFEOF'
{
  "ambient": {
    "a": 14.2,
    "r_c": 3.5,
    "reflections": {
      "200": {
        "a_r_c_ratio": 4.057142857142857,
        "required_ratio_for_zero": 4.0,
        "is_zero": true
      },
      "111": {
        "a_r_c_ratio": 4.057142857142857,
        "required_ratio_for_zero": 3.4641016151377544,
        "is_zero": false
      }
    }
  },
  "compressed": {
    "a": 12.12,
    "r_c": 3.5,
    "reflections": {
      "200": {
        "a_r_c_ratio": 3.462857142857143,
        "required_ratio_for_zero": 4.0,
        "is_zero": false
      },
      "111": {
        "a_r_c_ratio": 3.462857142857143,
        "required_ratio_for_zero": 3.4641016151377544,
        "is_zero": true
      }
    }
  }
}
FFEOF
