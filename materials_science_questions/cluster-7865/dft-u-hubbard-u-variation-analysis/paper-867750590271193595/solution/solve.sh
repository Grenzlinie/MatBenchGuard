#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'HEREDOC_END'
[
  {
    "phase": "cubic-EuH9",
    "magnetic_order": "AFM",
    "J1": -6.2578e-22,
    "J2": 1.8056e-23,
    "J3": null,
    "Tc": 24
  },
  {
    "phase": "hexagonal-EuH9",
    "magnetic_order": "FM",
    "J1": 2.6834e-22,
    "J2": 5.3336e-22,
    "J3": null,
    "Tc": 137
  },
  {
    "phase": "Eu8H46",
    "magnetic_order": "FM",
    "J1": 2.5042e-21,
    "J2": 1.4070e-21,
    "J3": 9.1531e-22,
    "Tc": 336
  }
]
HEREDOC_END
