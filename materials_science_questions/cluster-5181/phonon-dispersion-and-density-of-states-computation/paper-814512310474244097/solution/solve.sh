#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: iteration_results.json ===
cat > /app/outputs/iteration_results.json <<'FFEOF'
[
  {
    "iteration": 0,
    "W0": -462.0,
    "Phi01_xx": 21.1,
    "Phi01_zz": 0.712,
    "Phi02_xx": -2.92,
    "Phi02_zz": 0.469,
    "c_l": 0.969,
    "c_t": 0.516
  },
  {
    "iteration": 1,
    "W0": -431.0,
    "Phi01_xx": 40.6,
    "Phi01_zz": -1.65,
    "Phi02_xx": -2.96,
    "Phi02_zz": 0.481,
    "c_l": 1.48,
    "c_t": 0.673
  },
  {
    "iteration": 2,
    "W0": -438.0,
    "Phi01_xx": 39.8,
    "Phi01_zz": -1.51,
    "Phi02_xx": -2.97,
    "Phi02_zz": 0.483,
    "c_l": 1.41,
    "c_t": 0.679
  },
  {
    "iteration": 3,
    "W0": -438.0,
    "Phi01_xx": 39.7,
    "Phi01_zz": -1.49,
    "Phi02_xx": -2.97,
    "Phi02_zz": 0.483,
    "c_l": 1.41,
    "c_t": 0.678
  }
]
FFEOF
