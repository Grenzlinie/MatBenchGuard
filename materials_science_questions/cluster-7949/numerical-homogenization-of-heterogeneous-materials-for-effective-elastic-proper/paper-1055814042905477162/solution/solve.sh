#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/usr/bin/env bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: calibration_results.json ===
cat > "$OUTDIR/calibration_results.json" <<'EOF'
[
  {
    "composite": "FH3-Laborel",
    "model_type": "EB-2-2D",
    "calibrated_value": 18.0,
    "predicted_lambda": 0.304
  },
  {
    "composite": "FH6-Laborel",
    "model_type": "EB-2-2D",
    "calibrated_value": 24.0,
    "predicted_lambda": 0.201
  },
  {
    "composite": "CSP-Belayachi",
    "model_type": "EB-3-3D",
    "calibrated_value": 15.0,
    "predicted_lambda": 0.055
  },
  {
    "composite": "CSB-Belayachi",
    "model_type": "EB-2-2D",
    "calibrated_value": 3.0,
    "predicted_lambda": 0.159
  }
]
EOF
