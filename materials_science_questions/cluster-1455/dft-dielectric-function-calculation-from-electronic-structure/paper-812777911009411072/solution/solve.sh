#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results.json ===
cat > "$OUTDIR/results.json" << 'EOF'
{
  "polar_bulk": {
    "total_energy_FM": -15999.722,
    "total_energy_AFM": -15999.565996,
    "Er_eV": 0.278,
    "\u0394E_meV": 156.004,
    "total_magnetic_moment_muB": 4.36,
    "magnetic_moment_Ni1_muB": 1.5912,
    "magnetic_moment_Ni2_muB": 1.5612,
    "ground_state": "FM",
    "half_metallic": false
  },
  "polar_surface": {
    "total_energy_FM": -16000.0,
    "total_energy_AFM": -15999.808096,
    "Er_eV": 0.0,
    "\u0394E_meV": 191.904,
    "total_magnetic_moment_muB": 3.67,
    "magnetic_moment_Ni1_muB": 1.523,
    "magnetic_moment_Ni2_muB": 1.243,
    "ground_state": "FM",
    "half_metallic": true
  },
  "polar_mixed": {
    "total_energy_FM": -15999.767026,
    "total_energy_AFM": -15999.768,
    "Er_eV": 0.232,
    "\u0394E_meV": -0.974,
    "total_magnetic_moment_muB": 0.8,
    "magnetic_moment_Ni1_muB": 1.6721,
    "magnetic_moment_Ni2_muB": -1.334,
    "ground_state": "AFM",
    "half_metallic": false
  },
  "nonpolar_bulk": {
    "total_energy_FM": -15995.599,
    "total_energy_AFM": -15995.549514,
    "Er_eV": 4.401,
    "\u0394E_meV": 49.486,
    "total_magnetic_moment_muB": 4.11,
    "magnetic_moment_Ni1_muB": 1.5339,
    "magnetic_moment_Ni2_muB": 1.5737,
    "ground_state": "FM",
    "half_metallic": true
  },
  "nonpolar_surface": {
    "total_energy_FM": -15996.137,
    "total_energy_AFM": -15996.102554,
    "Er_eV": 3.863,
    "\u0394E_meV": 34.446,
    "total_magnetic_moment_muB": 4.21,
    "magnetic_moment_Ni1_muB": 1.6238,
    "magnetic_moment_Ni2_muB": 1.393,
    "ground_state": "FM",
    "half_metallic": true
  },
  "nonpolar_mixed": {
    "total_energy_FM": -15995.967,
    "total_energy_AFM": -15995.96663,
    "Er_eV": 4.033,
    "\u0394E_meV": 0.37,
    "total_magnetic_moment_muB": 4.07,
    "magnetic_moment_Ni1_muB": 1.5843,
    "magnetic_moment_Ni2_muB": 1.4369,
    "ground_state": "FM",
    "half_metallic": true
  }
}
EOF

# === solve block: dos_nonpolar_bulk.dat ===
python3 /solution/generate_dos.py > /app/outputs/dos_nonpolar_bulk.dat

# === solve block: dos_nonpolar_surface.dat ===
python3 /solution/generate_dos.py > /app/outputs/dos_nonpolar_surface.dat

# === solve block: dos_nonpolar_mixed.dat ===
python3 /solution/generate_dos.py > /app/outputs/dos_nonpolar_mixed.dat
