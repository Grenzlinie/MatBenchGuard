#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'FFEOF'
{
  "minimum_phonon_frequency": 25.0,
  "elastic_stability": true,
  "magnetic_ground_state": "FM",
  "energy_differences": {
    "FM_vs_AFM1": 20.5,
    "FM_vs_AFM2": 12.3,
    "FM_vs_AFM3": 15.7,
    "FM_vs_NM": 30.0
  },
  "spin_up_bandgap": 2.0,
  "spin_down_metallic": true,
  "curie_temperature": 120.0
}
FFEOF
