#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: elastic_constants.json ===
cat > /app/outputs/elastic_constants.json <<'FFEOF'
[
  {
    "system": "bulk",
    "C11": 234.87,
    "C22": 363.82,
    "C33": 353.19,
    "C44": 51.58,
    "C55": 63.25,
    "C66": 90.65,
    "C12": 126.23,
    "C13": 157.69,
    "C15": -20.58,
    "C23": 107.6,
    "C25": 8.29,
    "C35": 6.68,
    "C46": 21.44
  },
  {
    "system": "monolayer",
    "C11": 1.57,
    "C22": 124.78,
    "C33": 79.61,
    "C44": 1.72,
    "C55": 0.06,
    "C66": 0.337,
    "C12": 0.33,
    "C13": 9.8,
    "C15": 0.42,
    "C23": 0.21,
    "C25": 0.21,
    "C35": 0.4,
    "C46": 0.15
  },
  {
    "system": "bilayer",
    "C11": 17.57,
    "C22": 187.38,
    "C33": 134.77,
    "C44": 24.73,
    "C55": 0.97,
    "C66": 2.63,
    "C12": 1.05,
    "C13": 7.2,
    "C15": 1.39,
    "C23": 4.43,
    "C25": 1.35,
    "C35": 1.18,
    "C46": 0.67
  },
  {
    "system": "trilayer",
    "C11": 51.37,
    "C22": 499.88,
    "C33": 365.58,
    "C44": 73.64,
    "C55": 0.49,
    "C66": 5.49,
    "C12": 0.57,
    "C13": 13.46,
    "C15": 1.57,
    "C23": 11.21,
    "C25": 1.57,
    "C35": 0.92,
    "C46": -0.51
  }
]
FFEOF

# === solve block: mechanical_properties.json ===
cat > /app/outputs/mechanical_properties.json <<'FFEOF'
[
  {
    "system": "bulk",
    "bulk_modulus": 189.83,
    "shear_modulus": 71.62,
    "Youngs_modulus": 190.86,
    "Poisson_ratio": 0.333,
    "anisotropy_index_B": 0.02,
    "anisotropy_index_G": 0.1
  },
  {
    "system": "monolayer",
    "bulk_modulus": 8.86,
    "shear_modulus": 5.02,
    "Youngs_modulus": 12.66,
    "Poisson_ratio": 0.261,
    "anisotropy_index_B": 0.89,
    "anisotropy_index_G": 0.75
  },
  {
    "system": "bilayer",
    "bulk_modulus": 27.11,
    "shear_modulus": 15.20,
    "Youngs_modulus": 38.41,
    "Poisson_ratio": 0.263,
    "anisotropy_index_B": 0.50,
    "anisotropy_index_G": 0.81
  },
  {
    "system": "trilayer",
    "bulk_modulus": 73.28,
    "shear_modulus": 38.67,
    "Youngs_modulus": 98.66,
    "Poisson_ratio": 0.275,
    "anisotropy_index_B": 0.47,
    "anisotropy_index_G": 0.95
  }
]
FFEOF

# === solve block: thermodynamic_properties.json ===
cat > /app/outputs/thermodynamic_properties.json <<'FFEOF'
[
  {
    "system": "bulk",
    "k_min": 0.28,
    "Theta_D": 750.54,
    "v_m": 9.09,
    "v_l": 7145.69,
    "v_t": 3580.05,
    "saturated_C_V": 20.69
  },
  {
    "system": "monolayer",
    "k_min": 0.49,
    "Theta_D": 460.72,
    "v_m": 64.69,
    "v_l": 3374.48,
    "v_t": 1916.71,
    "saturated_C_V": 27.58
  },
  {
    "system": "bilayer",
    "k_min": 0.35,
    "Theta_D": 602.28,
    "v_m": 29.40,
    "v_l": 4398.02,
    "v_t": 2490.96,
    "saturated_C_V": 24.06
  },
  {
    "system": "trilayer",
    "k_min": 0.29,
    "Theta_D": 717.98,
    "v_m": 9.81,
    "v_l": 6423.18,
    "v_t": 3574.89,
    "saturated_C_V": 22.33
  }
]
FFEOF
