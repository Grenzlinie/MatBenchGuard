#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'JSONEOF'
{
  "zone_center_phonons": [
    {"mode": "A1", "symmetry": "A1", "frequency_TO": 313, "frequency_LO": null},
    {"mode": "A2_1", "symmetry": "A2", "frequency_TO": 311, "frequency_LO": null},
    {"mode": "A2_2", "symmetry": "A2", "frequency_TO": 345, "frequency_LO": null},
    {"mode": "B1_1", "symmetry": "B1", "frequency_TO": 105, "frequency_LO": null},
    {"mode": "B1_2", "symmetry": "B1", "frequency_TO": 207, "frequency_LO": null},
    {"mode": "B1_3", "symmetry": "B1", "frequency_TO": 362, "frequency_LO": null},
    {"mode": "B2_1", "symmetry": "B2", "frequency_TO": 100, "frequency_LO": 101},
    {"mode": "B2_2", "symmetry": "B2", "frequency_TO": 328, "frequency_LO": 330},
    {"mode": "B2_3", "symmetry": "B2", "frequency_TO": 364, "frequency_LO": 365},
    {"mode": "E_1", "symmetry": "E", "frequency_TO": 82, "frequency_LO": 82},
    {"mode": "E_2", "symmetry": "E", "frequency_TO": 115, "frequency_LO": 115},
    {"mode": "E_3", "symmetry": "E", "frequency_TO": 180, "frequency_LO": 180},
    {"mode": "E_4", "symmetry": "E", "frequency_TO": 325, "frequency_LO": 328},
    {"mode": "E_5", "symmetry": "E", "frequency_TO": 335, "frequency_LO": 340},
    {"mode": "E_6", "symmetry": "E", "frequency_TO": 343, "frequency_LO": 353}
  ],
  "born_effective_charges": [
    {"atom": "Zn", "eigenvalues": [1.76, 1.76, 1.73], "average": 1.75},
    {"atom": "Sn", "eigenvalues": [2.64, 2.50, 2.50], "average": 2.55},
    {"atom": "P", "eigenvalues": [-2.29, -2.16, -1.99], "average": -2.15}
  ],
  "dielectric_constants": {
    "epsilon_inf_perp": 11.91,
    "epsilon_inf_par": 12.01,
    "epsilon_0_perp": 13.74,
    "epsilon_0_par": 13.86
  }
}
JSONEOF
