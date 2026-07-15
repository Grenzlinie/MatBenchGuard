#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: final_results.json ===
cat > "/app/outputs/final_results.json" <<'EOF'
{
  "ni1_positive_formation_energy": 6.30,
  "ni1_negative_formation_energy": -1.45,
  "ni1_total_cross_slip_energy": 4.85,
  "ni2_positive_formation_energy": 3.05,
  "ni2_negative_formation_energy": -0.70,
  "ni2_total_cross_slip_energy": 2.35,
  "interaction_energy_lambda_21b": -0.06,
  "activation_energy_tau_0": 1.17,
  "activation_energy_tau_0_00045mu": 0.95
}
EOF
