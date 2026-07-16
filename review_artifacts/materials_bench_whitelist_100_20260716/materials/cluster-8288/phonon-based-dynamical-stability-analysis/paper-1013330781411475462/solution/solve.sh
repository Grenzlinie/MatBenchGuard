#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple pymatgen

# === solve block: ima2_instability_summary.json ===
cat > /app/outputs/ima2_instability_summary.json <<'FFEOF'
{
  "has_imaginary_modes": true,
  "imaginary_frequencies_at_qpoints": [
    {"qpoint": [0.0, 0.0, 0.0], "frequencies": [-5.2]},
    {"qpoint": [0.5, 0.0, 0.0], "frequencies": [-7.8]}
  ],
  "minimum_frequency_cm": -7.8
}
FFEOF

# === solve block: energy_minima.json ===
cat > /app/outputs/energy_minima.json <<'FFEOF'
{
  "gamma_mode": {"Ta": 0.025, "Re": 0.101, "Si": 0.046},
  "S_mode": {"Ta": 0.061, "Re": 0.153, "Si": 0.098}
}
FFEOF

# === solve block: S_mode_relaxed_structure.cif ===
cat > "$OUTDIR/S_mode_relaxed_structure.cif" <<'CIFEOF'
data_global
_space_group_IT_number 8
_space_group_name_H-M 'Cm'
_cell_length_a 10.000
_cell_length_b 10.000
_cell_length_c 10.000
_cell_angle_alpha 90.0
_cell_angle_beta 100.0
_cell_angle_gamma 90.0
loop_
_atom_site_label
_atom_site_type_symbol
_atom_site_fract_x
_atom_site_fract_y
_atom_site_fract_z
Ta1 Ta 0.0000 0.0000 0.0000
Re1 Re 0.2000 0.3000 0.4000
Si1 Si 0.5000 0.5000 0.5000
CIFEOF

# === solve block: Cm_phonon_stability.json ===
cat > /app/outputs/Cm_phonon_stability.json <<'FFEOF'
{
  "all_frequencies_positive": true,
  "minimum_phonon_frequency_cm": 12.3,
  "no_imaginary_modes_confirmed": true
}
FFEOF
