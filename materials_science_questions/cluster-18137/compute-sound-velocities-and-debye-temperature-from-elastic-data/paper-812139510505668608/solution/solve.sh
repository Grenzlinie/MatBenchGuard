#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_structure.json ===
cat > /app/outputs/step_01_structure.json <<'EOF'
{
  "a_angstrom": 4.672,
  "c_angstrom": 7.775,
  "V_angstrom3": 147.004,
  "Fe_6h_x": 0.17050,
  "Mo_4f_z": 0.06978,
  "total_magnetic_moment_muB": 4.451
}
EOF

# === solve block: step_00_formation_enthalpy.json ===
cat > /app/outputs/step_00_formation_enthalpy.json <<'EOF'
{
  "delta_H_kJ_per_mol": -2.210
}
EOF

# === solve block: step_02_elastic_constants.json ===
cat > /app/outputs/step_02_elastic_constants.json <<'EOF'
{
  "C11_GPa": 459.27,
  "C12_GPa": 170.38,
  "C13_GPa": 105.49,
  "C33_GPa": 379.00,
  "C44_GPa": 113.73,
  "C66_GPa": 144.44
}
EOF

# === solve block: step_03_polycrystalline_moduli.json ===
cat > /app/outputs/step_03_polycrystalline_moduli.json <<'EOF'
{
  "B_GPa": 226.5,
  "G_GPa": 122.8,
  "E_GPa": 312.0,
  "nu": 0.27,
  "B_G_ratio": 1.84,
  "A_100": 0.725,
  "A_001": 1.000,
  "B_a_GPa": 791.13,
  "B_c_GPa": 516.83,
  "A_B_percent": 1.070,
  "A_G_percent": 10.322,
  "A_U": 1.173
}
EOF

# === solve block: step_04_debye_sound_velocities.json ===
cat > /app/outputs/step_04_debye_sound_velocities.json <<'EOF'
{
  "v_s_m_per_s": 3618,
  "v_l_m_per_s": 6449,
  "V_m_m_per_s": 4026,
  "theta_D_K": 520,
  "v_l_001_m_per_s": 6356,
  "v_s_001_m_per_s": 3482,
  "v_l_100_m_per_s": 6997,
  "v_s1_100_m_per_s": 3924,
  "v_s2_100_m_per_s": 3482
}
EOF
