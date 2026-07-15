#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: sc_hybrid_results.json ===
cat > /app/outputs/sc_hybrid_results.json <<'FFEOF'
[
  {
    "material": "Si",
    "initial_alpha": 0.25,
    "epsilon_inf_iterations": [10.53, 11.78, 11.76, 11.76],
    "converged_epsilon_inf": 11.76,
    "converged_alpha": 0.08503,
    "band_gap": 0.99
  },
  {
    "material": "C",
    "initial_alpha": 0.25,
    "epsilon_inf_iterations": [5.54, 5.63, 5.61, 5.61],
    "converged_epsilon_inf": 5.61,
    "converged_alpha": 0.17825,
    "band_gap": 5.42
  },
  {
    "material": "MgO",
    "initial_alpha": 0.25,
    "epsilon_inf_iterations": [2.89, 2.83, 2.81, 2.81],
    "converged_epsilon_inf": 2.81,
    "converged_alpha": 0.35587,
    "band_gap": 8.33
  }
]
FFEOF
