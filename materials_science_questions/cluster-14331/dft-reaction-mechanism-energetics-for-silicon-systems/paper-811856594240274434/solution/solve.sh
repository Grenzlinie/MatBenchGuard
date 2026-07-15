#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'FFFILE'
{
  "TS_A_bond_lengths": {
    "P1P2": 2.645,
    "P1Si3": 2.553,
    "P2Si3": 2.478
  },
  "TS_B_bond_lengths": {
    "P1P2": 2.629,
    "P1Si3": 2.663,
    "P2Si3": 2.435,
    "P4Si3": 2.633
  },
  "product_3_bond_lengths": {
    "P1Si3": 2.281,
    "P2Si3": 2.281,
    "P1P2": 3.199
  },
  "DeltaEa_model1": 26.9,
  "DeltaEa_ZPE_model1": 26.6,
  "DeltaEa_model2": 21.8,
  "DeltaEa_ZPE_model2": 21.8
}
FFFILE
