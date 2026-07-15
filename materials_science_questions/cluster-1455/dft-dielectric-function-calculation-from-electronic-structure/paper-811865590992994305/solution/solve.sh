#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
OUTDIR="${OUTDIR:-/app/outputs}"
cat > "${OUTDIR}"/results.json << 'JSONEOF'
{
  "band_gap": 1.76,
  "eps_inf_perp": 6.96,
  "eps_inf_par": 7.51,
  "born_charges": {
    "Mg": [[2.71, 0.00, 0.00], [0.00, 2.71, 0.00], [0.00, 0.00, 2.59]],
    "N": [[-2.54, 0.00, 0.00], [0.00, -2.54, 0.00], [0.00, 0.00, -1.16]],
    "B1": [[0.35, 0.71, -0.03], [0.71, 1.16, -0.05], [-0.10, -0.18, 0.18]],
    "B2": [[-0.36, 0.19, 0.09], [0.19, -0.14, 0.15], [0.07, 0.13, -0.45]],
    "B3": [[-0.54, -0.04, 0.19], [-0.04, -0.58, 0.33], [0.23, 0.41, -0.20]]
  },
  "phonon_frequencies": [
    {"irrep": "Eg", "frequency": 163, "lo_or_to": null},
    {"irrep": "Eg", "frequency": 280, "lo_or_to": null},
    {"irrep": "Eg", "frequency": 516, "lo_or_to": null},
    {"irrep": "Eg", "frequency": 571, "lo_or_to": null},
    {"irrep": "Eg", "frequency": 619, "lo_or_to": null},
    {"irrep": "Eg", "frequency": 737, "lo_or_to": null},
    {"irrep": "Eg", "frequency": 778, "lo_or_to": null},
    {"irrep": "Eg", "frequency": 813, "lo_or_to": null},
    {"irrep": "Eg", "frequency": 849, "lo_or_to": null},
    {"irrep": "Eg", "frequency": 1064, "lo_or_to": null},
    {"irrep": "Eg", "frequency": 1077, "lo_or_to": null},
    {"irrep": "A1g", "frequency": 200, "lo_or_to": null},
    {"irrep": "A1g", "frequency": 530, "lo_or_to": null},
    {"irrep": "A1g", "frequency": 677, "lo_or_to": null},
    {"irrep": "A1g", "frequency": 758, "lo_or_to": null},
    {"irrep": "A1g", "frequency": 789, "lo_or_to": null},
    {"irrep": "A1g", "frequency": 890, "lo_or_to": null},
    {"irrep": "A1g", "frequency": 1023, "lo_or_to": null},
    {"irrep": "A1g", "frequency": 1167, "lo_or_to": null},
    {"irrep": "A1u", "frequency": 427, "lo_or_to": null},
    {"irrep": "A1u", "frequency": 638, "lo_or_to": null},
    {"irrep": "A1u", "frequency": 775, "lo_or_to": null},
    {"irrep": "A2g", "frequency": 307, "lo_or_to": null},
    {"irrep": "A2g", "frequency": 530, "lo_or_to": null},
    {"irrep": "A2g", "frequency": 751, "lo_or_to": null},
    {"irrep": "A2u", "frequency": 281, "lo_or_to": "TO"},
    {"irrep": "A2u", "frequency": 486, "lo_or_to": "TO"},
    {"irrep": "A2u", "frequency": 661, "lo_or_to": "TO"},
    {"irrep": "A2u", "frequency": 794, "lo_or_to": "TO"},
    {"irrep": "A2u", "frequency": 911, "lo_or_to": "TO"},
    {"irrep": "A2u", "frequency": 1008, "lo_or_to": "TO"},
    {"irrep": "A2u", "frequency": 1113, "lo_or_to": "TO"},
    {"irrep": "A2u", "frequency": 310, "lo_or_to": "LO"},
    {"irrep": "A2u", "frequency": 492, "lo_or_to": "LO"},
    {"irrep": "A2u", "frequency": 664, "lo_or_to": "LO"},
    {"irrep": "A2u", "frequency": 798, "lo_or_to": "LO"},
    {"irrep": "A2u", "frequency": 911, "lo_or_to": "LO"},
    {"irrep": "A2u", "frequency": 1008, "lo_or_to": "LO"},
    {"irrep": "A2u", "frequency": 1114, "lo_or_to": "LO"},
    {"irrep": "Eu", "frequency": 127, "lo_or_to": "TO"},
    {"irrep": "Eu", "frequency": 406, "lo_or_to": "TO"},
    {"irrep": "Eu", "frequency": 547, "lo_or_to": "TO"},
    {"irrep": "Eu", "frequency": 634, "lo_or_to": "TO"},
    {"irrep": "Eu", "frequency": 657, "lo_or_to": "TO"},
    {"irrep": "Eu", "frequency": 777, "lo_or_to": "TO"},
    {"irrep": "Eu", "frequency": 785, "lo_or_to": "TO"},
    {"irrep": "Eu", "frequency": 852, "lo_or_to": "TO"},
    {"irrep": "Eu", "frequency": 1052, "lo_or_to": "TO"},
    {"irrep": "Eu", "frequency": 1094, "lo_or_to": "TO"},
    {"irrep": "Eu", "frequency": 232, "lo_or_to": "LO"},
    {"irrep": "Eu", "frequency": 413, "lo_or_to": "LO"},
    {"irrep": "Eu", "frequency": 549, "lo_or_to": "LO"},
    {"irrep": "Eu", "frequency": 634, "lo_or_to": "LO"},
    {"irrep": "Eu", "frequency": 658, "lo_or_to": "LO"},
    {"irrep": "Eu", "frequency": 779, "lo_or_to": "LO"},
    {"irrep": "Eu", "frequency": 786, "lo_or_to": "LO"},
    {"irrep": "Eu", "frequency": 852, "lo_or_to": "LO"},
    {"irrep": "Eu", "frequency": 1079, "lo_or_to": "LO"},
    {"irrep": "Eu", "frequency": 1097, "lo_or_to": "LO"}
  ],
  "eps0_perp": 19.31,
  "eps0_par": 9.59,
  "elastic_constants": {
    "C11": 470.37,
    "C12": 89.80,
    "C13": 98.06,
    "C14": -31.02,
    "C33": 380.45,
    "C44": 173.62
  },
  "bulk_modulus": 210.34,
  "shear_modulus": 176.52
}
JSONEOF
