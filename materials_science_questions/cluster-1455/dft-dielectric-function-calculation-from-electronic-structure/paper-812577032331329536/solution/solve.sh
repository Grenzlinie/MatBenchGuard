#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_optical_constants.json ===
cat > /app/outputs/computed_optical_constants.json <<'EOF'
{
  "CsSnCl3_cubic": {
    "band_gap_eV": 2.93,
    "epsilon1_0": 2.5,
    "n_0": 1.6,
    "plasma_peak_eV": 23.51,
    "Neff_plateau": 29
  },
  "CsSnCl3_orthorhombic": {
    "band_gap_eV": 1.92,
    "epsilon1_0": 3.1,
    "n_0": 1.7,
    "plasma_peak_eV": 20.15,
    "Neff_plateau": 115
  },
  "CsSnBr3_cubic": {
    "band_gap_eV": 1.71,
    "epsilon1_0": 3.2,
    "n_0": 1.8,
    "plasma_peak_eV": 22.5,
    "Neff_plateau": 32
  },
  "CsSnBr3_tetragonal": {
    "band_gap_eV": 1.96,
    "epsilon1_0": 4.1,
    "n_0": 2.0,
    "plasma_peak_eV": 22.0,
    "Neff_plateau": 70
  },
  "CsSnBr3_orthorhombic": {
    "band_gap_eV": 1.28,
    "epsilon1_0": 6.3,
    "n_0": 2.5,
    "plasma_peak_eV": 20.0,
    "Neff_plateau": 131
  },
  "CsSnI3_cubic": {
    "band_gap_eV": 1.33,
    "epsilon1_0": 5.8,
    "n_0": 2.35,
    "plasma_peak_eV": 15.10,
    "Neff_plateau": 38
  },
  "CsSnI3_tetragonal": {
    "band_gap_eV": 1.85,
    "epsilon1_0": 4.5,
    "n_0": 2.10,
    "plasma_peak_eV": 18.32,
    "Neff_plateau": 72
  },
  "CsSnI3_orthorhombic": {
    "band_gap_eV": 1.20,
    "epsilon1_0": 5.9,
    "n_0": 2.40,
    "plasma_peak_eV": 20.55,
    "Neff_plateau": 140
  }
}
EOF
