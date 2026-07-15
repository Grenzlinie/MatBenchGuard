#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: reproduction_results.json ===
cat > /app/outputs/reproduction_results.json <<'EOF'
{
  "monolayer": {
    "binding_energy_per_atom": -2.92,
    "band_gap": 2.66
  },
  "layering": {
    "bilayer": {
      "PBE": {
        "interlayer_distance": 4.51,
        "binding_energy": -0.01
      },
      "vdW-DF": {
        "interlayer_distance": 3.90,
        "binding_energy": -0.53
      }
    },
    "trilayer": {
      "PBE": {
        "interlayer_distance": 4.53,
        "binding_energy": -0.03,
        "average_interlayer_distance": 4.53
      },
      "vdW-DF": {
        "interlayer_distance": 3.93,
        "binding_energy": -1.12,
        "average_interlayer_distance": 3.93
      }
    }
  },
  "defects": {
    "B_vacancy_N_magnetic_moment": 0.78
  },
  "hydrogen_adsorption": [
    {
      "label": "H-B",
      "adsorption_energy": 2.35,
      "bond_distance": 1.34
    },
    {
      "label": "H-N",
      "adsorption_energy": 3.04,
      "bond_distance": 1.08
    },
    {
      "label": "O-B",
      "adsorption_energy": 1.98,
      "bond_distance": 1.28
    },
    {
      "label": "O-N",
      "adsorption_energy": 2.42,
      "bond_distance": 1.04
    },
    {
      "label": "H-DB",
      "adsorption_energy": -2.39,
      "bond_distance": 1.01
    },
    {
      "label": "H-DN",
      "adsorption_energy": -1.63,
      "bond_distance": 1.21
    },
    {
      "label": "O-DB",
      "adsorption_energy": -2.49,
      "bond_distance": 1.02
    },
    {
      "label": "O-DN",
      "adsorption_energy": -2.14,
      "bond_distance": 1.19
    }
  ]
}
EOF
