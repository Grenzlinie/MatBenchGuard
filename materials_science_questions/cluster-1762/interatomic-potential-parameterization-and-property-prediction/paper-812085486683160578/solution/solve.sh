#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: potential_parameters.json ===
python3 -c '
import json
data = {
  "NaCl": {
    "rho_A": 1/3.15,
    "pairs": {
      "Na_Na": {"b_erg": 0.596e-9, "c_ergA6": 1.68e-12, "d_ergA8": 0.8e-12},
      "Na_Cl": {"b_erg": 1.906e-9, "c_ergA6": 11.2e-12, "d_ergA8": 13.9e-12},
      "Cl_Cl": {"b_erg": 5.504e-9, "c_ergA6": 116.0e-12, "d_ergA8": 233.0e-12}
    }
  },
  "KCl": {
    "rho_A": 1/2.97,
    "pairs": {
      "K_K": {"b_erg": 2.230e-9, "c_ergA6": 24.3e-12, "d_ergA8": 24.0e-12},
      "K_Cl": {"b_erg": 2.772e-9, "c_ergA6": 48.0e-12, "d_ergA8": 73.0e-12},
      "Cl_Cl": {"b_erg": 3.110e-9, "c_ergA6": 125.0e-12, "d_ergA8": 250.0e-12}
    }
  },
  "NaKCl": {
    "rho_A": 1/3.06,
    "pairs": {
      "Na_Na": {"b_erg": 0.483e-9, "c_ergA6": 1.68e-12, "d_ergA8": 0.8e-12},
      "Na_K": {"b_erg": 1.184e-9, "c_ergA6": 6.27e-12, "d_ergA8": 4.6e-12},
      "Na_Cl": {"b_erg": 1.581e-9, "c_ergA6": 11.2e-12, "d_ergA8": 13.9e-12},
      "K_K": {"b_erg": 2.903e-9, "c_ergA6": 24.3e-12, "d_ergA8": 24.0e-12},
      "K_Cl": {"b_erg": 3.646e-9, "c_ergA6": 48.0e-12, "d_ergA8": 73.0e-12},
      "Cl_Cl": {"b_erg": 4.137e-9, "c_ergA6": 123.0e-12, "d_ergA8": 246.0e-12}
    }
  },
  "adjusted_pauling_constants": {
    "c_plusplus": 1.11,
    "c_plusminus": 0.96,
    "c_minusminus": 0.75,
    "b_constant_erg": 0.338e-12
  }
}
with open("/app/outputs/potential_parameters.json", "w") as f:
    json.dump(data, f, indent=2)
'

# === solve block: thermodynamic_properties.csv ===
python3 -c '
import csv
rows = [
    {"system": "NaCl", "V_cm3mol": "38.2 ± 0.2", "E_kcalmol": "-166.3 ± 0.1",
     "S_calmolK": "40.1", "G_kcalmol": "-209.7",
     "delta_V_cm3mol": "", "delta_E_kcalmol": "",
     "delta_S_calmolK": "", "delta_G_kcalmol": ""},
    {"system": "KCl", "V_cm3mol": "51.8 ± 0.2", "E_kcalmol": "-149.9 ± 0.1",
     "S_calmolK": "43.2", "G_kcalmol": "-196.7",
     "delta_V_cm3mol": "", "delta_E_kcalmol": "",
     "delta_S_calmolK": "", "delta_G_kcalmol": ""},
    {"system": "(Na,K)Cl", "V_cm3mol": "46.2 ± 0.4", "E_kcalmol": "-157.3 ± 0.1",
     "S_calmolK": "43.1", "G_kcalmol": "-204.0",
     "delta_V_cm3mol": "1.2 ± 0.4", "delta_E_kcalmol": "0.8 ± 0.1",
     "delta_S_calmolK": "1.4", "delta_G_kcalmol": "-0.8"},
]
cols = ["system", "V_cm3mol", "E_kcalmol", "S_calmolK", "G_kcalmol",
        "delta_V_cm3mol", "delta_E_kcalmol", "delta_S_calmolK", "delta_G_kcalmol"]
with open("/app/outputs/thermodynamic_properties.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    w.writerows(rows)
'
