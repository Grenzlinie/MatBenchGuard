#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: geometries.json ===
cat > /app/outputs/geometries.json <<'FFEOF'
[
  {
    "species": "HSiS",
    "state_label": "X²A'",
    "R_SiS": 3.740,
    "r_XH": 2.861,
    "alpha": 120.8,
    "method": "MP2/basis I",
    "total_energy": -1.2085
  },
  {
    "species": "SiSH",
    "state_label": "X²A'",
    "R_SiS": 4.067,
    "r_XH": 2.559,
    "alpha": 99.4,
    "method": "MP2/basis I",
    "total_energy": -1.2020
  },
  {
    "species": "HSiS⁺",
    "state_label": "X¹Σ⁺",
    "R_SiS": 3.615,
    "r_XH": 2.791,
    "alpha": 180.0,
    "method": "MP2/basis I",
    "total_energy": -0.9165
  },
  {
    "species": "SiSH⁺",
    "state_label": "X¹A'",
    "R_SiS": 3.934,
    "r_XH": 2.591,
    "alpha": 88.0,
    "method": "MP2/basis I",
    "total_energy": -0.9356
  },
  {
    "species": "HSiS⁻",
    "state_label": "X¹A'",
    "R_SiS": 3.932,
    "r_XH": 2.965,
    "alpha": 102.4,
    "method": "MP2/basis I",
    "total_energy": -1.2816
  },
  {
    "species": "HSiS⁻",
    "state_label": "¹³A''",
    "R_SiS": 3.919,
    "r_XH": 2.864,
    "alpha": 122.1,
    "method": "MP2/basis I",
    "total_energy": -1.2338
  },
  {
    "species": "SiSH⁻",
    "state_label": "X³A''",
    "R_SiS": 4.441,
    "r_XH": 2.551,
    "alpha": 97.9,
    "method": "MP2/basis I",
    "total_energy": -1.2334
  },
  {
    "species": "SiSH⁻",
    "state_label": "¹¹A'",
    "R_SiS": 4.167,
    "r_XH": 2.570,
    "alpha": 105.5,
    "method": "MP2/basis I",
    "total_energy": -1.2131
  }
]
FFEOF

# === solve block: frequencies.json ===
cat > /app/outputs/frequencies.json <<'FFEOF'
[
  {
    "species": "HSiS",
    "state_label": "X²A'",
    "omega_SiS": 671,
    "omega_XH": 1935,
    "omega_HAB": 612,
    "scaling_factor": 0.9
  },
  {
    "species": "HSiS⁺",
    "state_label": "X¹Σ⁺",
    "omega_SiS": 784,
    "omega_XH": 2164,
    "omega_HAB": 451,
    "scaling_factor": 0.9
  },
  {
    "species": "HSiS⁻",
    "state_label": "X¹A'",
    "omega_SiS": 557,
    "omega_XH": 1677,
    "omega_HAB": 749,
    "scaling_factor": 0.9
  },
  {
    "species": "HSiS⁻",
    "state_label": "¹³A''",
    "omega_SiS": 530,
    "omega_XH": 1908,
    "omega_HAB": 617,
    "scaling_factor": 0.9
  },
  {
    "species": "SiSH",
    "state_label": "X²A'",
    "omega_SiS": 459,
    "omega_XH": 2507,
    "omega_HAB": 668,
    "scaling_factor": 0.9
  },
  {
    "species": "SiSH⁺",
    "state_label": "X¹A'",
    "omega_SiS": 590,
    "omega_XH": 2434,
    "omega_HAB": 509,
    "scaling_factor": 0.9
  },
  {
    "species": "SiSH⁻",
    "state_label": "X³A''",
    "omega_SiS": 306,
    "omega_XH": 2516,
    "omega_HAB": 575,
    "scaling_factor": 0.9
  },
  {
    "species": "SiSH⁻",
    "state_label": "¹¹A'",
    "omega_SiS": 365,
    "omega_XH": 2434,
    "omega_HAB": 619,
    "scaling_factor": 0.9
  }
]
FFEOF

# === solve block: relative_energies.json ===
cat > /app/outputs/relative_energies.json <<'FFEOF'
{
  "isomerization_neutral": 0.18,
  "isomerization_cation": 0.58,
  "isomerization_anion_ground": 1.43,
  "isomerization_anion_singlet": 1.84,
  "IP_HSiS": 8.09,
  "IP_SiSH": 7.34,
  "EA_HSiS_to_X1A": 2.16,
  "EA_HSiS_to_13A": 1.02,
  "EA_SiSH_to_X3A": 0.91,
  "EA_SiSH_to_11A": 0.50
}
FFEOF
