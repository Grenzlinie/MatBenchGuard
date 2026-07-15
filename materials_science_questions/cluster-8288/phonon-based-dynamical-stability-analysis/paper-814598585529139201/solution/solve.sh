#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: pristine_results.json ===
cat > "$OUTDIR/pristine_results.json" <<'EOF'
{
  "lattice_constant_A": 3.136,
  "Ni_magnetic_moment_muB": 1.733,
  "AFM_FM_energy_diff_meV": -45.0,
  "HSE06_band_gap_eV": 3.15,
  "band_gap_direct": true
}
EOF

# === solve block: strain_results.json ===
cat > "$OUTDIR/strain_results.json" <<'EOF'
[
  {
    "strain_percent": -10.0,
    "AFM_FM_energy_diff_meV": 47.0,
    "HSE06_band_gap_eV": 2.32
  },
  {
    "strain_percent": -4.0,
    "AFM_FM_energy_diff_meV": 5.0,
    "HSE06_band_gap_eV": 2.80
  },
  {
    "strain_percent": 0.0,
    "AFM_FM_energy_diff_meV": -45.0,
    "HSE06_band_gap_eV": 3.15
  },
  {
    "strain_percent": 4.0,
    "AFM_FM_energy_diff_meV": -30.0,
    "HSE06_band_gap_eV": 3.40
  },
  {
    "strain_percent": 10.0,
    "AFM_FM_energy_diff_meV": -60.0,
    "HSE06_band_gap_eV": 3.95
  }
]
EOF
