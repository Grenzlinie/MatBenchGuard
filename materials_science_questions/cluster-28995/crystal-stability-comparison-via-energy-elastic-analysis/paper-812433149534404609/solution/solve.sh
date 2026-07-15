#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: computed_properties.json ===
cat > "$OUTDIR/computed_properties.json" <<'FFEOF'
{
  "BCC": {
    "a": 2.8589,
    "Omega0": 11.6833,
    "Ecoh": -4.28,
    "C11": 2.3675,
    "C12": 1.3191,
    "C44": 1.2190,
    "Cprime": 0.5242,
    "K": 1.6686,
    "E_surf_111": 2.2439
  },
  "FCC": {
    "Omega0": 11.152,
    "Ecoh": -4.2229
  },
  "HCP": {
    "Omega0": 10.398,
    "Ecoh": -4.2134
  },
  "phase_transformation": {
    "pressure_BCC_HCP": 110
  }
}
FFEOF
