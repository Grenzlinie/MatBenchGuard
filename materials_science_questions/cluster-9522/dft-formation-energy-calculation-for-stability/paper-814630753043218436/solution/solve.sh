#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: main_results.json ===
cat > /app/outputs/main_results.json <<'FFEOF'
{
  "formation_energy_kJ_per_mol": -217,
  "band_gap_direct_eV": 0.5,
  "band_gap_type": "direct",
  "o_lattice_parameters": [6.032, 6.134, 12.110]
}
FFEOF
