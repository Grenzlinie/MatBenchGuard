#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: effective_masses.json ===
cat > "$OUTDIR/effective_masses.json" <<'EOF'
{
  "MAPbI3_eff_mass_electron": 0.23,
  "MAPbI3_eff_mass_hole": 0.25,
  "MAPbMn_eff_mass_electron": 0.25,
  "MAPbMn_eff_mass_hole": 1.37
}
EOF
