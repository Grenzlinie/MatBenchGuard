#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results_summary.json ===
cat > /app/outputs/results_summary.json <<'FFEOF'
[
  {
    "element": "Li",
    "structure": "HX",
    "a": 3.091,
    "delta": 0.0,
    "cohesive_energy_per_atom": 1.311,
    "stable": false
  },
  {
    "element": "Li",
    "structure": "bHC",
    "a": 3.102,
    "delta": 1.159,
    "cohesive_energy_per_atom": 1.561,
    "stable": true
  },
  {
    "element": "Li",
    "structure": "bSQ",
    "a": 2.960,
    "delta": 1.085,
    "cohesive_energy_per_atom": 1.538,
    "stable": false
  },
  {
    "element": "Be",
    "structure": "HX",
    "a": 2.126,
    "delta": 0.0,
    "cohesive_energy_per_atom": 2.997,
    "stable": true
  },
  {
    "element": "Be",
    "structure": "bHC",
    "a": 2.157,
    "delta": 0.959,
    "cohesive_energy_per_atom": 3.354,
    "stable": true
  },
  {
    "element": "Be",
    "structure": "bSQ",
    "a": 2.090,
    "delta": 0.799,
    "cohesive_energy_per_atom": 3.181,
    "stable": false
  },
  {
    "element": "Sc",
    "structure": "HX",
    "a": 3.149,
    "delta": 0.0,
    "cohesive_energy_per_atom": 2.706,
    "stable": false
  },
  {
    "element": "Sc",
    "structure": "bHC",
    "a": 3.283,
    "delta": 1.199,
    "cohesive_energy_per_atom": 3.619,
    "stable": true
  },
  {
    "element": "Sc",
    "structure": "bSQ",
    "a": 3.218,
    "delta": 1.038,
    "cohesive_energy_per_atom": 3.553,
    "stable": true
  },
  {
    "element": "Cu",
    "structure": "HX",
    "a": 2.428,
    "delta": 0.0,
    "cohesive_energy_per_atom": 3.154,
    "stable": true
  },
  {
    "element": "Cu",
    "structure": "bHC",
    "a": 2.496,
    "delta": 1.063,
    "cohesive_energy_per_atom": 3.407,
    "stable": true
  },
  {
    "element": "Cu",
    "structure": "bSQ",
    "a": 2.468,
    "delta": 0.912,
    "cohesive_energy_per_atom": 3.280,
    "stable": true
  },
  {
    "element": "Al",
    "structure": "HX",
    "a": 2.682,
    "delta": 0.0,
    "cohesive_energy_per_atom": 2.842,
    "stable": false
  },
  {
    "element": "Al",
    "structure": "bHC",
    "a": 2.748,
    "delta": 1.227,
    "cohesive_energy_per_atom": 3.217,
    "stable": true
  },
  {
    "element": "Al",
    "structure": "bSQ",
    "a": 2.713,
    "delta": 1.088,
    "cohesive_energy_per_atom": 3.085,
    "stable": true
  }
]
FFEOF
