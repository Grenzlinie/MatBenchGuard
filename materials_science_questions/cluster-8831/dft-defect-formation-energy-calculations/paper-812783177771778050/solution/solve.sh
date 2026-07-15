#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "$OUTDIR"

# === solve block: dft_results.json ===
# Write the reference DFT results for the TiN/WN₀.₅ superlattice (Λ=3.327 nm)
cat > "$OUTDIR/dft_results.json" <<'FFEOF'
{
  "B": 307.0,
  "G": 125.0,
  "E": 331.0,
  "B_over_G": 2.456,
  "Cauchy_pressure": 80.0,
  "poisson_ratio": 0.32,
  "formation_energy_difference": -0.15,
  "phonon_stable": true
}
FFEOF
