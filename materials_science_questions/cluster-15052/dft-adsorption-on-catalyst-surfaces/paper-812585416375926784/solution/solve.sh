#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: adsorption_energies.json ===
cat > "$OUTDIR/adsorption_energies.json" <<'EOF'
{
  "pattern_a_energy_eV": -0.55,
  "pattern_b_energy_eV": -0.47,
  "pattern_c_energy_eV": -0.28
}
EOF
