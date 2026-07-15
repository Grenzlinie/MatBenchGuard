#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: elastic_constants_and_moduli.json ===
cat > "$OUTDIR/elastic_constants_and_moduli.json" <<'FFEOF'
{
  "Pm-3m-Fe3Pt": {
    "C11": 206.344,
    "C12": 170.625,
    "C44": 85.957,
    "bulk_modulus_B": 182.531,
    "shear_modulus_G": 46.379,
    "young_modulus_E": 128.274,
    "poisson_ratio_nu": 0.383,
    "G_B_ratio": 0.254,
    "born_stable": true
  },
  "I4/mmm-Fe3Pt": {
    "C11": 259.280,
    "C12": 90.790,
    "C13": 152.871,
    "C33": 209.513,
    "C44": 68.757,
    "C66": 35.522,
    "bulk_modulus_B": 168.908,
    "shear_modulus_G": 51.670,
    "young_modulus_E": 140.667,
    "poisson_ratio_nu": 0.361,
    "G_B_ratio": 0.306,
    "born_stable": true
  },
  "P4/mmm-FePt": {
    "C11": 346.778,
    "C12": 73.457,
    "C13": 161.090,
    "C33": 292.106,
    "C44": 113.855,
    "C66": 48.3819,
    "bulk_modulus_B": 197.102,
    "shear_modulus_G": 87.423,
    "young_modulus_E": 228.488,
    "poisson_ratio_nu": 0.307,
    "G_B_ratio": 0.444,
    "born_stable": true
  },
  "Pm-3m-FePt3": {
    "C11": 301.055,
    "C12": 183.094,
    "C44": 105.108,
    "bulk_modulus_B": 222.415,
    "shear_modulus_G": 83.360,
    "young_modulus_E": 222.306,
    "poisson_ratio_nu": 0.333,
    "G_B_ratio": 0.375,
    "born_stable": true
  }
}
FFEOF

# === solve block: dynamical_stability.json ===
cat > "$OUTDIR/dynamical_stability.json" <<'FFEOF'
{
  "Pm-3m-Fe3Pt": {
    "min_phonon_frequency_THz": -0.3,
    "dynamically_stable": false
  },
  "I4/mmm-Fe3Pt": {
    "min_phonon_frequency_THz": -0.2,
    "dynamically_stable": false
  },
  "P4/mmm-FePt": {
    "min_phonon_frequency_THz": 0.5,
    "dynamically_stable": true
  },
  "Pm-3m-FePt3": {
    "min_phonon_frequency_THz": -0.4,
    "dynamically_stable": false
  }
}
FFEOF

# === solve block: thermodynamic_properties.json ===
cat > "$OUTDIR/thermodynamic_properties.json" <<'FFEOF'
{
  "Pm-3m-Fe3Pt": {
    "Debye_temperature_K": 277.0,
    "heat_capacity_Cv_at_300K": 23.0
  },
  "I4/mmm-Fe3Pt": {
    "Debye_temperature_K": 298.0,
    "heat_capacity_Cv_at_300K": 46.0
  },
  "P4/mmm-FePt": {
    "Debye_temperature_K": 331.0,
    "heat_capacity_Cv_at_300K": 12.0
  },
  "Pm-3m-FePt3": {
    "Debye_temperature_K": 292.0,
    "heat_capacity_Cv_at_300K": 17.0
  }
}
FFEOF
