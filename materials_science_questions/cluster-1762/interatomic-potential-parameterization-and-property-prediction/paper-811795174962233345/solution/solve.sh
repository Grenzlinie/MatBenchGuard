#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: step_00_pure_KTO.json ===
cat > $OUTDIR/step_00_pure_KTO.json <<'EOF'
{
  "TO1_frequency_cm-1": 68.2,
  "TO2_frequency_cm-1": 214.3,
  "TO3_frequency_cm-1": 536.4,
  "electronic_dielectric_constant": 5.15,
  "static_dielectric_constant": 341.3
}
EOF

# === solve block: step_01_single_Li.json ===
cat > $OUTDIR/step_01_single_Li.json <<'EOF'
{
  "Li_energy_[001]_eV": -0.194,
  "Li_displacement_[001]_A": 1.01,
  "total_polarization_Cm2": 0.076,
  "total_dipole_eA": 8.12,
  "Li_dipole_contribution_eA": 1.25,
  "matrix_dipole_contribution_eA": 7.07,
  "Li_energy_[110]_eV": -0.108,
  "Li_displacement_[110]_A": 0.484,
  "Li_energy_[111]_eV": -0.112,
  "Li_displacement_[111]_A": 0.404,
  "A1_eV_per_A2": -0.362,
  "A11_eV_per_A4": 0.156,
  "A12_eV_per_A4": 0.0388,
  "A111_eV_per_A6": 0.0154,
  "A112_eV_per_A6": 1.75028,
  "A123_eV_per_A6": 1.367
}
EOF

# === solve block: step_02_pair_interaction.json ===
cat > $OUTDIR/step_02_pair_interaction.json <<'EOF'
{
  "config_a_energy_relative_to_undisplaced_eV": -0.345,
  "config_b_energy_relative_to_undisplaced_eV": -0.384,
  "config_c_energy_relative_to_undisplaced_eV": -0.551,
  "interaction_energy_config_a_eV": 0.043,
  "interaction_energy_config_b_eV": 0.004,
  "interaction_energy_config_c_eV": -0.163
}
EOF

# === solve block: step_03_energy_barrier.json ===
cat > $OUTDIR/step_03_energy_barrier.json <<'EOF'
{
  "barrier_[111]_path_eV": 0.082,
  "barrier_[110]_path_eV": 0.086
}
EOF

# === solve block: step_04_polar_cluster.json ===
cat > $OUTDIR/step_04_polar_cluster.json <<'EOF'
{
  "chain1_avg_distortion_A": 0.102,
  "chain2_avg_distortion_A": 0.024,
  "chain3_avg_distortion_A": 0.018,
  "lateral_thickness_lattice_constants": 2.0
}
EOF
