#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: stress_values.json ===
cat > /app/outputs/stress_values.json <<'FFEOF'
{
  "loading_history_1": {
    "normality": {
      "step_1_stresses": {
        "sigma_zz": 400.0,
        "tau_theta_z": 0.1
      },
      "step_2_stresses": {
        "sigma_zz": 390.0,
        "tau_theta_z": 190.0
      }
    },
    "generalized": {
      "step_1_stresses": {
        "sigma_zz": 400.0,
        "tau_theta_z": 0.1
      },
      "step_2_stresses": {
        "sigma_zz": 370.0,
        "tau_theta_z": 170.0
      }
    }
  },
  "loading_history_2": {
    "normality": {
      "step_1_stresses": {
        "sigma_zz": 0.1,
        "tau_theta_z": 200.0
      },
      "step_2_stresses": {
        "sigma_zz": 350.0,
        "tau_theta_z": 210.0
      }
    },
    "generalized": {
      "step_1_stresses": {
        "sigma_zz": 0.1,
        "tau_theta_z": 200.0
      },
      "step_2_stresses": {
        "sigma_zz": 380.0,
        "tau_theta_z": 190.0
      }
    }
  }
}
FFEOF
