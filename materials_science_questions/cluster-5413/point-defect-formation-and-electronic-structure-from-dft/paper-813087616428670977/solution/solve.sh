#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: dft_results.json ===
cat > "$OUTDIR/dft_results.json" <<'JSON'
{
  "compositions": [
    {
      "label": "Ti0.5Al0.5N",
      "y": 0.0,
      "lattice_parameter_angstrom": 4.17,
      "formation_energy_eV_per_atom": -0.44
    },
    {
      "label": "Ti0.50Al0.47Mo0.03N",
      "y": 0.03,
      "lattice_parameter_angstrom": 4.18,
      "formation_energy_eV_per_atom": -0.41
    },
    {
      "label": "Ti0.50Al0.44Mo0.06N",
      "y": 0.06,
      "lattice_parameter_angstrom": 4.19,
      "formation_energy_eV_per_atom": -0.38
    },
    {
      "label": "Ti0.50Al0.37Mo0.13N",
      "y": 0.13,
      "lattice_parameter_angstrom": 4.21,
      "formation_energy_eV_per_atom": -0.35
    }
  ]
}
JSON
