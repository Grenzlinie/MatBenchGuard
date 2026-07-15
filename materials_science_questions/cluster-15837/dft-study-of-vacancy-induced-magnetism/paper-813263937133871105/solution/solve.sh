#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: single_vacancy_results.json ===
cat > "$OUTDIR/single_vacancy_results.json" <<'FFEOF'
[
  {"defect_label": "C1", "formation_energy_ev": 6.34, "magnetic_moment_muB": 1.40, "x_angstrom": 2.53, "y_angstrom": 2.53, "z_angstrom": 2.58},
  {"defect_label": "C2", "formation_energy_ev": 7.81, "magnetic_moment_muB": 2.13, "x_angstrom": 2.51, "y_angstrom": 2.51, "z_angstrom": 2.67},
  {"defect_label": "C3", "formation_energy_ev": 5.84, "magnetic_moment_muB": 2.00, "x_angstrom": 2.47, "y_angstrom": 2.47, "z_angstrom": 2.68},
  {"defect_label": "C4", "formation_energy_ev": 7.62, "magnetic_moment_muB": 0.00, "x_angstrom": 2.46, "y_angstrom": 2.46, "z_angstrom": 2.62},
  {"defect_label": "C5", "formation_energy_ev": 7.54, "magnetic_moment_muB": 2.01, "x_angstrom": 2.47, "y_angstrom": 2.47, "z_angstrom": 2.68},
  {"defect_label": "B1", "formation_energy_ev": 8.63, "magnetic_moment_muB": 2.62, "x_angstrom": 2.71, "y_angstrom": 2.71, "z_angstrom": 2.60},
  {"defect_label": "B2", "formation_energy_ev": 7.30, "magnetic_moment_muB": 1.90, "x_angstrom": 2.66, "y_angstrom": 2.66, "z_angstrom": 2.57},
  {"defect_label": "B3", "formation_energy_ev": 8.81, "magnetic_moment_muB": 3.00, "x_angstrom": 2.65, "y_angstrom": 2.65, "z_angstrom": 2.58},
  {"defect_label": "N1", "formation_energy_ev": 7.37, "magnetic_moment_muB": 0.33, "x_angstrom": 2.15, "y_angstrom": 2.15, "z_angstrom": 2.37},
  {"defect_label": "N2", "formation_energy_ev": 7.23, "magnetic_moment_muB": 1.00, "x_angstrom": 2.43, "y_angstrom": 2.43, "z_angstrom": 2.47},
  {"defect_label": "N3", "formation_energy_ev": 8.26, "magnetic_moment_muB": 1.00, "x_angstrom": 2.41, "y_angstrom": 2.41, "z_angstrom": 2.44}
]
FFEOF

# === solve block: double_vacancy_results.json ===
cat > "$OUTDIR/double_vacancy_results.json" <<'FFEOF'
[
  {"defect_label": "CC1", "formation_energy_ev": 6.04, "magnetic_moment_muB": 0.24},
  {"defect_label": "CC2", "formation_energy_ev": 9.58, "magnetic_moment_muB": 1.33},
  {"defect_label": "CC3", "formation_energy_ev": 5.68, "magnetic_moment_muB": 0.00},
  {"defect_label": "CC4", "formation_energy_ev": 9.82, "magnetic_moment_muB": 0.40},
  {"defect_label": "CC5", "formation_energy_ev": 6.75, "magnetic_moment_muB": 0.00},
  {"defect_label": "BN1", "formation_energy_ev": 9.70, "magnetic_moment_muB": 1.56},
  {"defect_label": "BN2", "formation_energy_ev": 9.97, "magnetic_moment_muB": 0.68},
  {"defect_label": "BN3", "formation_energy_ev": 10.60, "magnetic_moment_muB": 0.00},
  {"defect_label": "BN4", "formation_energy_ev": 12.32, "magnetic_moment_muB": 2.00},
  {"defect_label": "BN5", "formation_energy_ev": 11.66, "magnetic_moment_muB": 1.61},
  {"defect_label": "CB", "formation_energy_ev": 8.86, "magnetic_moment_muB": 1.00},
  {"defect_label": "CN", "formation_energy_ev": 9.11, "magnetic_moment_muB": 0.33}
]
FFEOF

# === solve block: stone_wales_results.json ===
cat > "$OUTDIR/stone_wales_results.json" <<'FFEOF'
[
  {"defect_label": "SW1-N", "formation_energy_ev": 5.38, "magnetic_moment_muB": 0.43},
  {"defect_label": "SW2-N", "formation_energy_ev": 4.20, "magnetic_moment_muB": 0.00},
  {"defect_label": "SW3-N", "formation_energy_ev": 5.33, "magnetic_moment_muB": 0.90},
  {"defect_label": "SW4-N", "formation_energy_ev": 6.76, "magnetic_moment_muB": 0.00},
  {"defect_label": "SW5-N", "formation_energy_ev": 5.23, "magnetic_moment_muB": 1.10},
  {"defect_label": "SW6-N", "formation_energy_ev": 8.61, "magnetic_moment_muB": 0.00},
  {"defect_label": "SW1-B", "formation_energy_ev": 6.63, "magnetic_moment_muB": 0.00},
  {"defect_label": "SW2-B", "formation_energy_ev": 4.26, "magnetic_moment_muB": 0.31},
  {"defect_label": "SW3-B", "formation_energy_ev": 5.21, "magnetic_moment_muB": 0.14},
  {"defect_label": "SW4-B", "formation_energy_ev": 6.90, "magnetic_moment_muB": 0.46},
  {"defect_label": "SW5-B", "formation_energy_ev": 4.51, "magnetic_moment_muB": 0.00},
  {"defect_label": "SW6-B", "formation_energy_ev": 8.16, "magnetic_moment_muB": 0.00}
]
FFEOF
