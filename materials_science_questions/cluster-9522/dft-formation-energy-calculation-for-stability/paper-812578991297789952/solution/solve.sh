#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: hse06_results.json ===
cat > /app/outputs/hse06_results.json <<'EOF'
[
  {
    "compound": "V2TiC2F2",
    "lattice_constant": 2.86,
    "Z2": 1,
    "pbe_system_gap": 35,
    "hse06_system_gap": 211,
    "hse06_gamma_gap": 248
  },
  {
    "compound": "V2ZrC2F2",
    "lattice_constant": 2.99,
    "Z2": 1,
    "pbe_system_gap": 48,
    "hse06_system_gap": 194,
    "hse06_gamma_gap": 254
  },
  {
    "compound": "V2HfC2F2",
    "lattice_constant": 2.96,
    "Z2": 1,
    "pbe_system_gap": 49,
    "hse06_system_gap": 294,
    "hse06_gamma_gap": 389
  },
  {
    "compound": "Nb2TiC2F2",
    "lattice_constant": 3.00,
    "Z2": 1,
    "pbe_system_gap": 52,
    "hse06_system_gap": 234,
    "hse06_gamma_gap": 276
  },
  {
    "compound": "Nb2ZrC2F2",
    "lattice_constant": 3.07,
    "Z2": 1,
    "pbe_system_gap": -5,
    "hse06_system_gap": 120,
    "hse06_gamma_gap": 296
  },
  {
    "compound": "Nb2HfC2F2",
    "lattice_constant": 3.04,
    "Z2": 1,
    "pbe_system_gap": -18,
    "hse06_system_gap": 122,
    "hse06_gamma_gap": 405
  },
  {
    "compound": "Ta2TiC2F2",
    "lattice_constant": 3.01,
    "Z2": 1,
    "pbe_system_gap": -6,
    "hse06_system_gap": 318,
    "hse06_gamma_gap": 482
  },
  {
    "compound": "Ta2ZrC2F2",
    "lattice_constant": 3.04,
    "Z2": 1,
    "pbe_system_gap": -80,
    "hse06_system_gap": 34,
    "hse06_gamma_gap": 489
  },
  {
    "compound": "Ta2HfC2F2",
    "lattice_constant": 3.05,
    "Z2": 1,
    "pbe_system_gap": -23,
    "hse06_system_gap": 126,
    "hse06_gamma_gap": 665
  }
]
EOF
