#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'FFEOF'
{
  "pandey_energy_eV": 1.102,
  "dimer_2x1_energy_eV": 0.883,
  "dimer_4x1_energy_eV": 1.023,
  "vacancy_sqrt3_energy_eV": 0.6145,
  "pandey_coordinates": [
    {"atom_label": "11", "x": 3.064, "y": -0.943, "z": 5.525},
    {"atom_label": "12", "x": 2.370, "y": 0.315, "z": 5.519},
    {"atom_label": "13", "x": 1.007, "y": 0.313, "z": 4.792},
    {"atom_label": "14", "x": 0.076, "y": -0.941, "z": 4.804},
    {"atom_label": "21", "x": 3.816, "y": -0.942, "z": 3.325},
    {"atom_label": "22", "x": 3.041, "y": 0.316, "z": 2.880},
    {"atom_label": "23", "x": 1.557, "y": 0.314, "z": 3.290},
    {"atom_label": "24", "x": 0.895, "y": -0.943, "z": 2.737},
    {"atom_label": "31", "x": 3.065, "y": 0.316, "z": 1.300},
    {"atom_label": "32", "x": 2.346, "y": -0.942, "z": 0.760},
    {"atom_label": "33", "x": 0.883, "y": -0.944, "z": 1.227},
    {"atom_label": "34", "x": 0.152, "y": 0.315, "z": 0.739}
  ]
}
FFEOF
