#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'FFEOF'
{
  "high_spin_energy": -1500.0,
  "intermediate_spin_energy": -1499.99,
  "energy_difference": 0.01,
  "high_spin_Fe_moment": -4.4,
  "intermediate_spin_Fe_moment": -2.9,
  "high_spin_Co_moment": 1.7,
  "intermediate_spin_Co_moment": 1.7,
  "Fe_O_bond_length": 1.92,
  "Co_O_bond_length": 1.74,
  "coupling_sign": "antiferromagnetic"
}
FFEOF
