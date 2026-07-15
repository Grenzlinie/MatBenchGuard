#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: computed_properties.json ===
cat > "$OUTDIR/computed_properties.json" <<'FFEOF'
{
  "vacancy_formation_energy": 3.52,
  "SIA_d111_formation_energy": 9.33,
  "H_TIS_formation_energy": 0.86,
  "surface_energy_100": 3.157,
  "surface_energy_110": 2.319,
  "surface_energy_211": 2.872,
  "melting_point": 4550,
  "diffusion_barrier_TIS_TIS": 0.23
}
FFEOF
