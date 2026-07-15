#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_properties.json ===
cat > "$OUTDIR/step_01_properties.json" <<'EOF'
{
  "direct_bandgap_eV": 1.83,
  "hole_effective_mass_m0": 0.9,
  "electron_effective_mass_m0": 0.2,
  "formation_energy_meV_per_atom": -150.0
}
EOF
