#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: decay_results.json ===
cat > /app/outputs/decay_results.json <<'FFEOF'
[
  {"material": "PZT-5H", "boundary_case": "A", "symmetry_mode": "symmetric", "decay_rate_real": 0.382776, "decay_length_over_2c": 6.015},
  {"material": "PZT-5H", "boundary_case": "A", "symmetry_mode": "antisymmetric", "decay_rate_real": 0.547458, "decay_length_over_2c": 4.206},
  {"material": "PZT-5H", "boundary_case": "B", "symmetry_mode": "symmetric", "decay_rate_real": 0.386688, "decay_length_over_2c": 5.955},
  {"material": "PZT-5H", "boundary_case": "B", "symmetry_mode": "antisymmetric", "decay_rate_real": 0.547075, "decay_length_over_2c": 4.209},
  {"material": "PZT-5", "boundary_case": "A", "symmetry_mode": "symmetric", "decay_rate_real": 1.460487, "decay_length_over_2c": 1.577},
  {"material": "PZT-5", "boundary_case": "A", "symmetry_mode": "antisymmetric", "decay_rate_real": 2.919872, "decay_length_over_2c": 0.789},
  {"material": "PZT-5", "boundary_case": "B", "symmetry_mode": "symmetric", "decay_rate_real": 1.857440, "decay_length_over_2c": 1.240},
  {"material": "PZT-5", "boundary_case": "B", "symmetry_mode": "antisymmetric", "decay_rate_real": 1.460763, "decay_length_over_2c": 1.576},
  {"material": "PZT-4", "boundary_case": "A", "symmetry_mode": "symmetric", "decay_rate_real": 1.375904, "decay_length_over_2c": 1.674},
  {"material": "PZT-4", "boundary_case": "A", "symmetry_mode": "antisymmetric", "decay_rate_real": 2.738617, "decay_length_over_2c": 0.841},
  {"material": "PZT-4", "boundary_case": "B", "symmetry_mode": "symmetric", "decay_rate_real": 1.801437, "decay_length_over_2c": 1.278},
  {"material": "PZT-4", "boundary_case": "B", "symmetry_mode": "antisymmetric", "decay_rate_real": 1.379322, "decay_length_over_2c": 1.669},
  {"material": "Ceramic-B", "boundary_case": "A", "symmetry_mode": "symmetric", "decay_rate_real": 1.460152, "decay_length_over_2c": 1.577},
  {"material": "Ceramic-B", "boundary_case": "A", "symmetry_mode": "antisymmetric", "decay_rate_real": 2.914914, "decay_length_over_2c": 0.790},
  {"material": "Ceramic-B", "boundary_case": "B", "symmetry_mode": "symmetric", "decay_rate_real": 1.988510, "decay_length_over_2c": 1.158},
  {"material": "Ceramic-B", "boundary_case": "B", "symmetry_mode": "antisymmetric", "decay_rate_real": 1.461497, "decay_length_over_2c": 1.575}
]
FFEOF
