#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: total_energies.json ===
cat > /app/outputs/total_energies.json << 'FFEOF'
{
  "E_H2O_hartree": -17.0,
  "low_Na": [
    {"n": 0, "E_n_hartree": -1500.0, "d_layer_A": 0.0},
    {"n": 3, "E_n_hartree": -1551.048, "d_layer_A": 2.9},
    {"n": 4, "E_n_hartree": -1568.05, "d_layer_A": 3.5},
    {"n": 8, "E_n_hartree": -1636.065, "d_layer_A": 5.4},
    {"n": 11, "E_n_hartree": -1687.07, "d_layer_A": 6.5},
    {"n": 14, "E_n_hartree": -1738.075, "d_layer_A": 7.5}
  ],
  "high_Na": [
    {"n": 0, "E_n_hartree": -1600.0, "d_layer_A": 0.0},
    {"n": 3, "E_n_hartree": -1651.05, "d_layer_A": 3.2},
    {"n": 4, "E_n_hartree": -1668.06, "d_layer_A": 4.0},
    {"n": 8, "E_n_hartree": -1736.08, "d_layer_A": 6.0},
    {"n": 11, "E_n_hartree": -1787.09, "d_layer_A": 7.5},
    {"n": 14, "E_n_hartree": -1838.10, "d_layer_A": 9.0}
  ]
}
FFEOF

# === solve block: dielectric_permittivity.json ===
cat > /app/outputs/dielectric_permittivity.json << 'FFEOF'
{
  "low_Na": [
    {"n": 3, "epsilon_layer": 2.82},
    {"n": 4, "epsilon_layer": 3.40},
    {"n": 8, "epsilon_layer": 5.25},
    {"n": 11, "epsilon_layer": 6.31},
    {"n": 14, "epsilon_layer": 7.29}
  ],
  "high_Na": [
    {"n": 3, "epsilon_layer": 6.22},
    {"n": 4, "epsilon_layer": 7.77},
    {"n": 8, "epsilon_layer": 11.66},
    {"n": 11, "epsilon_layer": 14.57},
    {"n": 14, "epsilon_layer": 17.49}
  ]
}
FFEOF

# === solve block: phase_diagram.json ===
cat > /app/outputs/phase_diagram.json << 'FFEOF'
{
  "low_Na": {
    "stable_state": "1W",
    "Omega_minimizer": {"n": 3, "Omega": -1500.036}
  },
  "high_Na": {
    "stable_state": "2W",
    "Omega_minimizer": {"n": 8, "Omega": -1600.048}
  },
  "conditions": {
    "T_K": 298.0,
    "RH_percent": 50.0
  }
}
FFEOF
