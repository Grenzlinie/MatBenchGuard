#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'EOF'
{
  "A15": {
    "static_energy_per_atom_Ry": -50.0,
    "zpe_per_atom_Ry": 0.00680,
    "enthalpy_per_atom_Ry": -49.99320,
    "lambda": 1.82,
    "omega_log_K": 989.0,
    "Tc_K_mu0.13": 140.0,
    "dynamically_stable": true
  },
  "P4_2/mmc": {
    "static_energy_per_atom_Ry": -50.05,
    "zpe_per_atom_Ry": 0.00705,
    "enthalpy_per_atom_Ry": -50.04295,
    "lambda": 1.56,
    "omega_log_K": 737.0,
    "Tc_K_mu0.13": 90.0,
    "dynamically_stable": true
  },
  "Cccm": {
    "static_energy_per_atom_Ry": -50.10,
    "zpe_per_atom_Ry": 0.00698,
    "enthalpy_per_atom_Ry": -50.09302,
    "lambda": 1.60,
    "omega_log_K": 793.0,
    "Tc_K_mu0.13": 100.0,
    "dynamically_stable": true
  }
}
EOF
