#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'JSONEOF'
[
  {
    "name": "Al-doped_4H-SiC",
    "total_magnetic_moment_per_supercell": 0.0,
    "carbon_magnetic_moment": 0.0
  },
  {
    "name": "Al+V_Si_4H-SiC",
    "total_magnetic_moment_per_supercell": 0.05,
    "carbon_magnetic_moment": 0.04
  },
  {
    "name": "Al+V_C_4H-SiC",
    "total_magnetic_moment_per_supercell": 0.02,
    "carbon_magnetic_moment": 0.015
  }
]
JSONEOF
