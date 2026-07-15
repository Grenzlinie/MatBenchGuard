#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dft_results.json ===
cat > /app/outputs/dft_results.json <<'EOF'
{
  "3a": {
    "avg_Si_H_bond_length": 1.71,
    "avg_Ru_H_bond_length": 1.71,
    "Ru_Si_bond_length": 2.34,
    "IR_frequencies_cm1": [1683.5, 1755.3]
  },
  "3b": {
    "avg_Si_H_bond_length": 1.70,
    "avg_Ru_H_bond_length": 1.70,
    "Ru_Si_bond_length": 2.36,
    "IR_frequencies_cm1": [1695.3, 1757.7]
  },
  "4": {
    "avg_Si_H_bond_length": 1.767,
    "avg_Ru_H_bond_length": 1.743,
    "Ru_Si_bond_length": 2.192,
    "IR_frequencies_cm1": [1722.23, 1731.91]
  }
}
EOF
