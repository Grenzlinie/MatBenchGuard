#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="${OUTDIR:-/app/outputs}"
mkdir -p "$OUTDIR"

# === solve block: doped_surface_properties.json ===
cat > "$OUTDIR/doped_surface_properties.json" <<'FFEOF'
{
  "Ta": {
    "surface_distances": [1.82, 1.96, 2.02, 3.53],
    "subsurface_distances": [1.98, 1.98],
    "ce_magnetic_moment": 1.0
  },
  "Nb": {
    "surface_distances": [2.01, 2.02, 2.14, 2.16],
    "subsurface_distances": [2.01, 2.01],
    "ce_magnetic_moment": 1.0
  }
}
FFEOF

# === solve block: no2_adsorption_properties.json ===
cat > "$OUTDIR/no2_adsorption_properties.json" <<'FFEOF'
{
  "Ta": {
    "adsorption_energy": -0.87,
    "n_o_s": 1.37,
    "n_o_n": 1.21
  },
  "Nb": {
    "adsorption_energy": -0.73,
    "n_o_s": 1.38,
    "n_o_n": 1.21
  }
}
FFEOF
