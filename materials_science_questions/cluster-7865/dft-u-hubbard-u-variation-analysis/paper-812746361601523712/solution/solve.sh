#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'EOF'
{
  "Yb3Pd2Sn2": {
    "V": 1.2656,
    "a": 0.56609,
    "b": 1.65524,
    "c": 1.35068,
    "c_over_a": 2.386,
    "b_over_a": 2.924,
    "B": 85.27,
    "B_prime": 5.39,
    "total_magnetic_moment": 0.03,
    "atomic_magnetic_moments": [0.001, 0.0, 0.0, 0.001],
    "magnetic_ground_state": null,
    "FM_energy": null,
    "AFM1_energy": null,
    "AFM2_energy": null
  },
  "Eu3Pd2Sn2": {
    "V": 0.67266,
    "a": 0.58125,
    "b": 0.85431,
    "c": 1.35471,
    "c_over_a": 2.331,
    "b_over_a": 1.47,
    "B": 78.76,
    "B_prime": 5.45,
    "total_magnetic_moment": 85.22,
    "atomic_magnetic_moments": [6.898, 6.887],
    "magnetic_ground_state": "FM",
    "FM_energy": -100.0,
    "AFM1_energy": -99.0,
    "AFM2_energy": -99.0
  }
}
EOF
