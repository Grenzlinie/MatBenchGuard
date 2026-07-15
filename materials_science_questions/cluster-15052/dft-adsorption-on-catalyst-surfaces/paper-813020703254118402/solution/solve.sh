#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_energy_barriers.json ===
cat > "$OUTDIR/step_01_energy_barriers.json" << 'FFEOF'
{
  "radical_barrier_eV": 0.79,
  "concerted_barrier_eV": 1.91,
  "forming_energy_OFeN4O_eV": -2.5
}
FFEOF

# === solve block: step_02_volcano_data.json ===
cat > "$OUTDIR/step_02_volcano_data.json" << 'FFEOF'
{
  "formation_energies": {
    "Cr": -2.96,
    "Mn": -2.16,
    "Fe": -2.07,
    "Co": -2.62
  }
}
FFEOF
