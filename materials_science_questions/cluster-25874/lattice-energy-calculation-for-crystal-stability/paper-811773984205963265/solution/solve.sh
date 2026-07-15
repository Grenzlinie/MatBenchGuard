#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: minimization_results.json ===
cat > /app/outputs/minimization_results.json << 'FFEOF'
[
  {
    "compound": "phenothiazine",
    "space_group": "P2_1",
    "cell": {
      "a": 7.57,
      "b": 5.59,
      "c": 10.58,
      "beta": 106.6
    },
    "volume_V": 429.0,
    "molecular_coordinates": {
      "x": 0.29,
      "y": 1.84,
      "z": 3.09,
      "theta": 98.4,
      "phi": 145.6,
      "psi": 22.3
    },
    "agreement_factor_phi": 0.017,
    "packing_coefficient_K": 0.73,
    "lattice_energy_E": -96.1,
    "hessian_positive_eigenvalues": true
  },
  {
    "compound": "phenothiazine",
    "space_group": "Pnma",
    "cell": {
      "a": 7.77,
      "b": 20.39,
      "c": 5.43
    },
    "volume_V": 860.3,
    "molecular_coordinates": {
      "x": 2.19,
      "y": 5.10,
      "z": 0.08,
      "theta": 146.5,
      "phi": 0.0,
      "psi": 0.0
    },
    "agreement_factor_phi": 0.015,
    "packing_coefficient_K": 0.73,
    "lattice_energy_E": -94.8,
    "hessian_positive_eigenvalues": true
  },
  {
    "compound": "phenoselenazine",
    "space_group": "P2_12_12_1",
    "cell": {
      "a": 7.62,
      "b": 20.55,
      "c": 5.93
    },
    "volume_V": 928.6,
    "molecular_coordinates": {
      "x": 2.14,
      "y": 3.09,
      "z": 2.30,
      "theta": 143.6,
      "phi": 92.3,
      "psi": 110.0
    },
    "agreement_factor_phi": 0.006,
    "packing_coefficient_K": 0.71,
    "lattice_energy_E": -96.4,
    "hessian_positive_eigenvalues": true
  }
]
FFEOF
