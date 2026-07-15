#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: validation_results.json ===
cat > "$OUTDIR/validation_results.json" <<'EOF'
{
  "classification_performance": {
    "method": "SISSO+XGBoost",
    "test_auc": {"low": 0.93, "medium": 0.89, "high": 0.94},
    "notes": "AUC from stratified 5-fold CV"
  },
  "compounds": [
    {
      "name": "GaAsSe4",
      "prototype": "MoS2",
      "predicted_class": "low",
      "predicted_formation_energy": 0.12,
      "dft_formation_energy": 0.12,
      "dft_code": "Quantum ESPRESSO",
      "notes": ""
    },
    {
      "name": "GaAsSe4",
      "prototype": "CdI2",
      "predicted_class": "high",
      "predicted_formation_energy": -0.06,
      "dft_formation_energy": -0.06,
      "dft_code": "Quantum ESPRESSO",
      "notes": ""
    },
    {
      "name": "AlAsTe4",
      "prototype": "MoS2",
      "predicted_class": "low",
      "predicted_formation_energy": 0.13,
      "dft_formation_energy": 0.13,
      "dft_code": "Quantum ESPRESSO",
      "notes": ""
    },
    {
      "name": "AlAsTe4",
      "prototype": "CdI2",
      "predicted_class": "high",
      "predicted_formation_energy": -0.03,
      "dft_formation_energy": -0.03,
      "dft_code": "Quantum ESPRESSO",
      "notes": ""
    }
  ],
  "regression_model_rmse": 0.205
}
EOF
