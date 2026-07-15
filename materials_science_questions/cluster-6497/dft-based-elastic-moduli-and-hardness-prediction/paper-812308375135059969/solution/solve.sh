#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: si_band_energies.json ===
cat > /app/outputs/si_band_energies.json <<'EOF'
{
  "lda": [
    {"point": "Γ₁₅", "energy_eV": 2.51},
    {"point": "Γ₂'", "energy_eV": 3.21},
    {"point": "X₁", "energy_eV": 0.55},
    {"point": "X₄", "energy_eV": -2.84},
    {"point": "X₃", "energy_eV": 9.94},
    {"point": "L₁", "energy_eV": -6.98},
    {"point": "L₃'", "energy_eV": -1.18},
    {"point": "L₁", "energy_eV": 1.40},
    {"point": "L₃", "energy_eV": 3.25}
  ],
  "nonlocal_expscreening": [
    {"point": "Γ₁₅", "energy_eV": 3.25},
    {"point": "Γ₂'", "energy_eV": 5.31},
    {"point": "X₁", "energy_eV": 4.93},
    {"point": "X₄", "energy_eV": -1.54},
    {"point": "X₃", "energy_eV": 11.26},
    {"point": "L₁", "energy_eV": -5.33},
    {"point": "L₃'", "energy_eV": -0.68},
    {"point": "L₁", "energy_eV": 3.86},
    {"point": "L₃", "energy_eV": 6.56}
  ]
}
EOF
