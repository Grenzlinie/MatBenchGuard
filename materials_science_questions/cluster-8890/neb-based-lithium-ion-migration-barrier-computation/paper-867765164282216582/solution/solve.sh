#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: activation_energies.json ===
cat > "$OUTDIR/activation_energies.json" <<'EOF'
[
  {
    "material": "Li3N",
    "Ea_0_NEB_eV": 0.03,
    "Ea_AIMD_eV": 0.15,
    "D0_cm2_per_s": 2.5e-05
  },
  {
    "material": "LiGaO2",
    "Ea_0_NEB_eV": 0.78,
    "Ea_AIMD_eV": 1.2,
    "D0_cm2_per_s": 0.05
  },
  {
    "material": "LiIO3",
    "Ea_0_NEB_eV": 0.09,
    "Ea_AIMD_eV": 0.36,
    "D0_cm2_per_s": 0.00035
  },
  {
    "material": "Li3OCl",
    "Ea_0_NEB_eV": 0.37,
    "Ea_AIMD_eV": 0.9,
    "D0_cm2_per_s": 0.014
  }
]
EOF
