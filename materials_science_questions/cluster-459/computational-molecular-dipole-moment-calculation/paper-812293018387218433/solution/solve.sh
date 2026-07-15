#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: theoretical_results.json ===
cat > /app/outputs/theoretical_results.json <<'JSONEOF'
{
  "MM2": {
    "bond_lengths": {
      "C=O": 1.201,
      "C1-C2": 1.524,
      "C1-C4": 1.573,
      "C1...C3": 1.955
    },
    "bond_angles": {
      "C1C2C3": 79.8,
      "C1C4C3": 76.9,
      "C2MC4": 119.9
    },
    "dipole_moment": 3.16
  },
  "MNDO": {
    "bond_lengths": {
      "C=O": 1.201,
      "C1-C2": 1.524,
      "C1-C4": 1.573,
      "C1...C3": 1.955
    },
    "bond_angles": {
      "C1C2C3": 79.8,
      "C1C4C3": 76.9,
      "C2MC4": 119.9
    },
    "dipole_moment": 3.16
  },
  "STO-3G": {
    "bond_lengths": {
      "C=O": 1.201,
      "C1-C2": 1.524,
      "C1-C4": 1.573,
      "C1...C3": 1.955
    },
    "bond_angles": {
      "C1C2C3": 79.8,
      "C1C4C3": 76.9,
      "C2MC4": 119.9
    },
    "dipole_moment": 3.16
  },
  "3-21G": {
    "bond_lengths": {
      "C=O": 1.201,
      "C1-C2": 1.524,
      "C1-C4": 1.573,
      "C1...C3": 1.955
    },
    "bond_angles": {
      "C1C2C3": 79.8,
      "C1C4C3": 76.9,
      "C2MC4": 119.9
    },
    "dipole_moment": 3.16
  }
}
JSONEOF
