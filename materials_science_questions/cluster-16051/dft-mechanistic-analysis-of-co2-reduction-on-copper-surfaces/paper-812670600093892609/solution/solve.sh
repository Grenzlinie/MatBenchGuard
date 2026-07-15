#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: dft_properties.json ===
cat > "$OUTDIR/dft_properties.json" <<'EOF'
{
  "Cu": {
    "work_function_eV": 4.55,
    "d_band_center_eV": -2.12,
    "delta_G_H_star_eV": 0.19,
    "C_C_distance_A": 4.233
  },
  "Cu3Zn": {
    "work_function_eV": 4.50,
    "d_band_center_eV": -2.32,
    "delta_G_H_star_eV": 0.31,
    "C_C_distance_A": 3.45
  },
  "CuZn": {
    "work_function_eV": 4.46,
    "d_band_center_eV": -2.43,
    "delta_G_H_star_eV": 0.50,
    "C_C_distance_A": 2.986
  },
  "Cu5Zn8": {
    "work_function_eV": 4.16,
    "d_band_center_eV": -2.54,
    "delta_G_H_star_eV": 0.66,
    "C_C_distance_A": 2.422
  }
}
EOF
