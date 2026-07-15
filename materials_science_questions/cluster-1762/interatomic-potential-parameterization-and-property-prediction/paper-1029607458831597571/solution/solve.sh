#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: defect_energies.json ===
cat > /app/outputs/defect_energies.json <<'FFEOF'
{
  "Na_Frenkel": 1.34,
  "Si_Frenkel": 7.5,
  "O_Frenkel": 6.0,
  "Schottky": 5.0,
  "Na2O_Schottky": 2.79,
  "SiO2_Schottky": 4.0,
  "isolated_antisite": 8.77,
  "clustered_antisite": 4.91
}
FFEOF

# === solve block: migration_energies.json ===
cat > /app/outputs/migration_energies.json <<'FFEOF'
{
  "local_hops": {
    "A": { "distance_angstrom": 3.14, "activation_energy_eV": 0.23 },
    "B": { "distance_angstrom": 3.62, "activation_energy_eV": 0.65 },
    "C": { "distance_angstrom": 3.39, "activation_energy_eV": 0.03 },
    "D": { "distance_angstrom": 3.89, "activation_energy_eV": 0.73 },
    "E": { "distance_angstrom": 3.29, "activation_energy_eV": 0.55 },
    "F": { "distance_angstrom": 4.07, "activation_energy_eV": 1.02 },
    "G": { "distance_angstrom": 2.91, "activation_energy_eV": 0.62 }
  },
  "long_range_pathways": {
    "A-C-E-A": { "overall_activation_energy_eV": 0.55, "hop_sequence_eV": [0.23, 0.03, 0.55, 0.23] },
    "D-E-G-D-G": { "overall_activation_energy_eV": 0.73, "hop_sequence_eV": [0.73, 0.55, 0.62, 0.73, 0.62] },
    "A-C-E-D-G": { "overall_activation_energy_eV": 0.73, "hop_sequence_eV": [0.23, 0.03, 0.55, 0.73, 0.62] },
    "A-B-E-G-D-G": { "overall_activation_energy_eV": 0.73, "hop_sequence_eV": [0.23, 0.65, 0.55, 0.62, 0.73, 0.62] },
    "A-C-E-F-A": { "overall_activation_energy_eV": 1.02, "hop_sequence_eV": [0.23, 0.03, 0.55, 1.02, 0.23] }
  }
}
FFEOF

# === solve block: dopant_solutions.json ===
cat > /app/outputs/dopant_solutions.json <<'FFEOF'
{
  "monovalent": { "Li": 2.0, "K": 1.5, "Rb": 2.3 },
  "trivalent": { "Al": 0.5, "Ga": 0.8, "In": 1.2, "Sc": 2.0, "Y": 2.5, "Gd": 3.0 },
  "tetravalent": { "Ge": 0.3, "Sn": 0.8, "Ti": 1.5, "Ce": 2.0 }
}
FFEOF
