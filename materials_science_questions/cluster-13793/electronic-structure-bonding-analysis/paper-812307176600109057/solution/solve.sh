#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: optimized_structure.json ===
cat > "$OUTDIR/optimized_structure.json" <<'FFEOF'
{
  "lattice_a": 3.9885,
  "atoms": [
    {"element": "O", "x": 0.0, "y": 0.5, "z": 0.25},
    {"element": "O", "x": 0.0, "y": 0.5, "z": 0.752189},
    {"element": "O", "x": 0.5, "y": 0.0, "z": 0.25},
    {"element": "O", "x": 0.5, "y": 0.0, "z": 0.748394},
    {"element": "O", "x": 0.5, "y": 0.5, "z": 0.0},
    {"element": "O", "x": 0.5, "y": 0.5, "z": 0.5},
    {"element": "Fe", "x": 0.5, "y": 0.5, "z": 0.745723},
    {"element": "Nb", "x": 0.5, "y": 0.5, "z": 0.246352},
    {"element": "Pb", "x": 0.0, "y": 0.0, "z": -0.039843},
    {"element": "Pb", "x": 0.0, "y": 0.0, "z": 0.531113}
  ]
}
FFEOF

# === solve block: polarization.json ===
cat > "$OUTDIR/polarization.json" <<'FFEOF'
{
  "PbFeO3": 18.0,
  "PbNbO3": 58.0
}
FFEOF
