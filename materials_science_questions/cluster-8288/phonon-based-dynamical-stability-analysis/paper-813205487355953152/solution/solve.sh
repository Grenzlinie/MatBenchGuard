#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_structural.json ===
cat > "/app/outputs/step_01_structural.json" <<'FFEOF'
{
  "buckling_amplitude_Ang": 0.579,
  "lattice_constant_Ang": 3.939,
  "bond_length_Ang": 2.357
}
FFEOF

# === solve block: step_02_cohesive.json ===
cat > "/app/outputs/step_02_cohesive.json" <<'FFEOF'
{
  "E_coh_LB_eV_per_cell": -8.746,
  "E_coh_HB_eV_per_cell": -8.644,
  "Delta_F_eV_per_cell": -0.059,
  "E_coh_plus_Delta_F_eV_per_cell": -8.803
}
FFEOF

# === solve block: step_03_phonon_stability.json ===
cat > "/app/outputs/step_03_phonon_stability.json" <<'FFEOF'
{
  "no_imaginary_freq": true,
  "minimum_frequency_cm-1": 0.0,
  "phonon_frequencies_at_Gamma_cm-1": [0.0, 0.0, 0.0]
}
FFEOF

# === solve block: step_04_band_structure.json ===
cat > "/app/outputs/step_04_band_structure.json" <<'FFEOF'
{
  "Fermi_velocity_10e5_m_per_s": 5.60,
  "bandgap_eV": 0.0
}
FFEOF

# === solve block: step_05_hydrogenation.json ===
cat > "/app/outputs/step_05_hydrogenation.json" <<'FFEOF'
{
  "HSiGe": {
    "buckling_amplitude_Ang": 0.7418,
    "Si_Ge_bond_Ang": 2.4145,
    "Si_H_bond_Ang": 1.5165,
    "magnetic_moment_muB": 1,
    "bandgap_eV": 0.6485
  },
  "SiGeH": {
    "buckling_amplitude_Ang": 0.7436,
    "Si_Ge_bond_Ang": 2.4148,
    "Ge_H_bond_Ang": 1.5859,
    "magnetic_moment_muB": 1,
    "bandgap_eV": 0.8604
  },
  "energy_difference_HSiGe_minus_SiGeH_eV": 0.032,
  "Curie_temperature_K": 110
}
FFEOF
