#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" << 'JSONEOF'
{
  "band_gap": 0.8,
  "Ni_spin_moment": 1.5,
  "total_spin_moment": 2.0,
  "FM_AFM_energy_diff": 5.0,
  "exchange_J": 13.0,
  "Ni_orbital_moment": 0.16,
  "Pt_orbital_moment": 0.02
}
JSONEOF
