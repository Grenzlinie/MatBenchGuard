#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: energy_table.json ===
cat > "$OUTDIR/energy_table.json" <<'FFEOF'
{
  "hexagonal": -0.97,
  "tetragonal": -0.98,
  "triangular": -1.00,
  "square": -0.99
}
FFEOF

# === solve block: phonon_dispersion.json ===
cat > "$OUTDIR/phonon_dispersion.json" <<'FFEOF'
{
  "n_imaginary_modes": 0,
  "min_imaginary_freq": 0.0
}
FFEOF

# === solve block: stability_summary.json ===
cat > "$OUTDIR/stability_summary.json" <<'FFEOF'
{
  "lowest_energy_family": "triangular",
  "dynamically_stable": true
}
FFEOF
