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
python3 -c '
import json
hexacoordinated = [
  {
    "complex_id": "Cr(NH3)5F2+",
    "photoactive_state": "4E",
    "excitation_energies": {
      "4B2": 18877,
      "4E": 17953
    },
    "composition": {
      "d_z2": 70.0,
      "d_x2_y2": 30.0
    },
    "delta_p": {
      "F_sigma": 0.031,
      "F_pi": -0.016,
      "F_total": 0.015,
      "Nax_sigma": 0.023,
      "Nax_pi": 0.0,
      "Nax_total": 0.023,
      "Neq_sigma": 0.017,
      "Neq_pi": 0.0,
      "Neq_total": 0.017
    },
    "predicted_leaving_ligand": "(NH3)ax"
  },
  {
    "complex_id": "trans-Cr(NH3)4F2+",
    "photoactive_state": "4E",
    "excitation_energies": {
      "4B2": 18134,
      "4E": 16561
    },
    "composition": {
      "d_z2": 62.5,
      "d_x2_y2": 37.5
    },
    "delta_p": {
      "F_ax_sigma": 0.023,
      "F_ax_pi": -0.012,
      "F_ax_total": 0.011,
      "Neq_sigma": 0.016,
      "Neq_pi": 0.0,
      "Neq_total": 0.016
    },
    "predicted_leaving_ligand": "(NH3)eq"
  },
  {
    "complex_id": "trans-Cr(NH3)4Cl2+",
    "photoactive_state": "4E",
    "excitation_energies": {
      "4B2": 18716,
      "4E": 15742
    },
    "composition": {
      "d_z2": 81.8,
      "d_x2_y2": 18.2
    },
    "delta_p": {
      "Cl_ax_sigma": 0.041,
      "Cl_ax_pi": -0.013,
      "Cl_ax_total": 0.028,
      "Neq_sigma": 0.012,
      "Neq_pi": 0.0,
      "Neq_total": 0.012
    },
    "predicted_leaving_ligand": "Cl-"
  },
  {
    "complex_id": "cis-Cr(NH3)4F2+",
    "photoactive_state": "4B2",
    "excitation_energies": {
      "4B2": 16901,
      "4E": 17254
    },
    "composition": {
      "d_z2": 0.0,
      "d_x2_y2": 100.0
    },
    "delta_p": {
      "F_eq_sigma": 0.031,
      "F_eq_pi": -0.013,
      "F_eq_total": 0.018,
      "Nax_sigma": 0.0,
      "Nax_pi": 0.0,
      "Nax_total": 0.0,
      "Neq_sigma": 0.021,
      "Neq_pi": 0.0,
      "Neq_total": 0.021
    },
    "predicted_leaving_ligand": "(NH3)eq"
  }
]

pentacoordinated = [
  {
    "fragment_id": "Cr(NH3)4F2+",
    "structure": "SP_ap",
    "relative_energies": [{"state": "4B1", "energy": 0.0}]
  },
  {
    "fragment_id": "Cr(NH3)4F2+",
    "structure": "TBP_ax",
    "relative_energies": [{"state": "4A1\u2032", "energy": 1.0}]
  },
  {
    "fragment_id": "Cr(NH3)4F2+",
    "structure": "TBP_eq",
    "relative_energies": [{"state": "4B2", "energy": 2.0}]
  },
  {
    "fragment_id": "Cr(NH3)4F2+",
    "structure": "SP_bas",
    "relative_energies": [{"state": "4A\u2032", "energy": 3.0}]
  },
  {
    "fragment_id": "Cr(NH3)4Cl2+",
    "structure": "SP_ap",
    "relative_energies": [{"state": "4B1", "energy": 0.0}]
  },
  {
    "fragment_id": "Cr(NH3)4Cl2+",
    "structure": "TBP_ax",
    "relative_energies": [{"state": "4A1\u2032", "energy": 1.0}]
  },
  {
    "fragment_id": "Cr(NH3)4Cl2+",
    "structure": "TBP_eq",
    "relative_energies": [{"state": "4B2", "energy": 2.0}]
  },
  {
    "fragment_id": "Cr(NH3)4Cl2+",
    "structure": "SP_bas",
    "relative_energies": [{"state": "4A\u2032", "energy": 3.0}]
  }
]

data = {
  "hexacoordinated": hexacoordinated,
  "pentacoordinated": pentacoordinated
}

with open("'"${OUTDIR}"'" + "/results.json", "w") as f:
    json.dump(data, f, indent=2)
'
