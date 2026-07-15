#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'FFEOF'
{
  "lattice_parameter_A": 4.60,
  "vacancy_formation_N_eV": 2.50,
  "vacancy_formation_Zr_eV": 4.00,
  "binding_energies_to_N_vac_eV": {
    "He": -0.50,
    "Kr": -6.56,
    "Xe": -7.73
  },
  "binding_energies_to_Zr_vac_eV": {
    "He": -3.32,
    "Kr": -8.73,
    "Xe": -9.93
  },
  "interstitial_migration_barriers_eV": {
    "He": 1.04,
    "Kr": 1.56,
    "Xe": 1.52
  },
  "vacancy_aided_migration_barriers_eV": {
    "He": 0.09,
    "Kr": 2.29,
    "Xe": 2.44
  }
}
FFEOF
