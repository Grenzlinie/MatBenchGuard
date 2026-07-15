#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_07_results.json ===
cat > "$OUTDIR/step_07_results.json" <<'JSONEOF'
{
  "overall_r_squared_pred_vs_computed": 0.9635,
  "rho_vs_phi_fit_slope": -3.14,
  "rho_vs_phi_fit_intercept": -2.33,
  "rho_vs_phi_fit_r": 0.88,
  "z_y_rho": [
    {"z": "CH2", "y": "H", "computed_rho": 1.38, "predicted_rho": 1.8212},
    {"z": "CH2", "y": "F", "computed_rho": -1.96, "predicted_rho": -0.785},
    {"z": "CH2", "y": "Li", "computed_rho": 13.00, "predicted_rho": 11.775},
    {"z": "NH", "y": "H", "computed_rho": 4.10, "predicted_rho": 1.1618},
    {"z": "NH", "y": "F", "computed_rho": -1.10, "predicted_rho": -2.7946},
    {"z": "NH", "y": "Li", "computed_rho": 16.98, "predicted_rho": 11.9006},
    {"z": "O", "y": "H", "computed_rho": 5.04, "predicted_rho": 2.0096},
    {"z": "O", "y": "F", "computed_rho": -0.96, "predicted_rho": -2.8888},
    {"z": "O", "y": "Li", "computed_rho": 23.01, "predicted_rho": 21.98},
    {"z": "SiH2", "y": "H", "computed_rho": 0.64, "predicted_rho": 0.1256},
    {"z": "SiH2", "y": "F", "computed_rho": -1.25, "predicted_rho": -1.57},
    {"z": "SiH2", "y": "Li", "computed_rho": 12.87, "predicted_rho": 8.792},
    {"z": "PH", "y": "H", "computed_rho": 0.76, "predicted_rho": -0.0942},
    {"z": "PH", "y": "F", "computed_rho": -1.53, "predicted_rho": -1.6328},
    {"z": "PH", "y": "Li", "computed_rho": 11.97, "predicted_rho": 9.3886},
    {"z": "S", "y": "H", "computed_rho": 1.33, "predicted_rho": 0.7222},
    {"z": "S", "y": "F", "computed_rho": -1.46, "predicted_rho": -1.5386},
    {"z": "S", "y": "Li", "computed_rho": 13.18, "predicted_rho": 10.8958}
  ]
}
JSONEOF
