#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: potential_parameters.json ===
cat > /app/outputs/potential_parameters.json <<'FFEOF'
{
  "short_range": [
    {"interaction": "O²⁻–O²⁻", "A": 7763.013, "rho": 0.277819, "C": 0.0},
    {"interaction": "O²⁻–Al³⁺", "A": 11590.781, "rho": 0.203647, "C": 2.93523},
    {"interaction": "O²⁻–Y³⁺", "A": 10510.057, "rho": 0.250406, "C": 0.0}
  ],
  "shell": [
    {"species": "O²⁻", "Y": -2.815, "k": 40.01},
    {"species": "Al³⁺", "Y": 2.98, "k": 889.11},
    {"species": "Y³⁺", "Y": 3.151, "k": 27077.9}
  ]
}
FFEOF

# === solve block: perfect_crystal_results.json ===
cat > /app/outputs/perfect_crystal_results.json <<'FFEOF'
{
  "lattice_energy": -155.92,
  "unit_cell": {
    "a": 5.3390,
    "b": 7.3727,
    "c": 5.1746
  },
  "interatomic_distances": [
    {"pair": "Y-Y", "distance": 3.640},
    {"pair": "Al-Al", "distance": 3.686},
    {"pair": "Y-Al_1", "distance": 3.145},
    {"pair": "Y-Al_2", "distance": 3.234},
    {"pair": "Y-Al_3", "distance": 3.023},
    {"pair": "Y-Al_4", "distance": 3.471},
    {"pair": "Al-O_1", "distance": 1.899},
    {"pair": "Al-O_2", "distance": 1.910},
    {"pair": "Al-O_3", "distance": 1.929},
    {"pair": "Y-O_1", "distance": 2.326},
    {"pair": "Y-O_2", "distance": 3.097},
    {"pair": "Y-O_3", "distance": 2.232},
    {"pair": "Y-O_4", "distance": 3.002},
    {"pair": "Y-O_5", "distance": 2.495},
    {"pair": "Y-O_6", "distance": 3.268},
    {"pair": "Y-O_7", "distance": 2.266},
    {"pair": "Y-O_8", "distance": 2.567}
  ],
  "static_dielectric": 15.96,
  "high_frequency_dielectric": 3.82,
  "density": 5.345
}
FFEOF

# === solve block: intrinsic_defect_energies.json ===
cat > /app/outputs/intrinsic_defect_energies.json <<'FFEOF'
{
  "isolated": [
    {"defect": "V_O", "energy": 18.87},
    {"defect": "V_Al", "energy": 65.84},
    {"defect": "V_Y", "energy": 52.01},
    {"defect": "O_i", "energy": -44.34},
    {"defect": "Al_i", "energy": -53.67},
    {"defect": "Y_i", "energy": -31.42},
    {"defect": "Y_Al", "energy": 16.71},
    {"defect": "Al_Y", "energy": -9.34}
  ],
  "frenkel": [
    {"type": "Oxygen", "energy_per_defect": -12.74},
    {"type": "Yttrium", "energy_per_defect": 10.30},
    {"type": "Aluminium", "energy_per_defect": 6.09}
  ],
  "schottky": [
    {"type": "YAlO3", "energy_per_defect": 3.71},
    {"type": "Al2O3", "energy_per_defect": 3.54},
    {"type": "Y2O3", "energy_per_defect": 3.81}
  ]
}
FFEOF

# === solve block: redox_energies.json ===
cat > /app/outputs/redox_energies.json <<'FFEOF'
{
  "electronic_defects": {
    "hole_formation": 17.80,
    "electron_formation": 26.33,
    "hole_defect_energy": 9.05,
    "electron_defect_energy": 5.81
  },
  "redox": {
    "oxidation_vacancy_filling": 9.09,
    "oxidation_interstitial_oxygen": -16.38,
    "reduction": 20.63
  }
}
FFEOF

# === solve block: migration_barriers.json ===
cat > /app/outputs/migration_barriers.json <<'FFEOF'
{
  "pathways": [
    {"jump_path": "1→2", "activation_energy": 0.99},
    {"jump_path": "2→6", "activation_energy": 0.99},
    {"jump_path": "1→3", "activation_energy": 0.52},
    {"jump_path": "3→6", "activation_energy": 0.52},
    {"jump_path": "1→4", "activation_energy": 0.30},
    {"jump_path": "4→6", "activation_energy": 0.30},
    {"jump_path": "1→5", "activation_energy": 0.15},
    {"jump_path": "5→6", "activation_energy": 0.15},
    {"jump_path": "2→3", "activation_energy": 0.31},
    {"jump_path": "3→4", "activation_energy": 0.69},
    {"jump_path": "4→5", "activation_energy": 0.29},
    {"jump_path": "5→2", "activation_energy": 0.69}
  ]
}
FFEOF
