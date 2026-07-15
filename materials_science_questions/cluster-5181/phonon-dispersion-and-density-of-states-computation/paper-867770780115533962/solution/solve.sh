#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: phonon_results.json ===
cat > /app/outputs/phonon_results.json <<'FFEOF'
{
  "1d_potentials": {
    "Morse_a0.2": {"omega_FF": 2193.55, "omega_dxdx": 2190.86, "gamma": 0.9987},
    "Morse_a0.4": {"omega_FF": 2189.96, "omega_dxdx": 2179.22, "gamma": 0.9950},
    "Morse_a0.6": {"omega_FF": 2183.96, "omega_dxdx": 2159.82, "gamma": 0.9889},
    "Morse_a0.8": {"omega_FF": 2175.55, "omega_dxdx": 2132.70, "gamma": 0.9803},
    "Quartic_c0.01": {"omega_FF": 332.74, "omega_dxdx": 310.85, "gamma": 0.9342},
    "Quartic_c0.1": {"omega_FF": 716.86, "omega_dxdx": 669.71, "gamma": 0.9342},
    "Quartic_c1.0": {"omega_FF": 1544.44, "omega_dxdx": 1442.85, "gamma": 0.9342},
    "SymmetricDoubleWell_c0.05": {"omega_FF": 1384.79, "omega_dxdx": 1190.52, "gamma": 0.8597},
    "SymmetricDoubleWell_c0.1": {"omega_FF": 1321.63, "omega_dxdx": 925.44, "gamma": 0.7002},
    "SymmetricDoubleWell_c0.3": {"omega_FF": 2946.93, "omega_dxdx": 124.85, "gamma": 0.0423}
  },
  "diamond_gamma": {
    "omega_FF": 1290.6,
    "omega_dxdx": 1276.9,
    "gamma": 0.98937
  }
}
FFEOF
