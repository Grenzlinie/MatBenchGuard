#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'EOF'
{
  "eu_4f_up_peak_energy": -2.10,
  "eu_4f_down_peak_energy1": 2.92,
  "eu_4f_down_peak_energy2": 2.40,
  "f_band_exchange_splitting": -5.02,
  "valence_band_exchange_splitting": 0.095,
  "N0_alpha": 0.21,
  "N0_beta": -1.09,
  "total_magnetic_moment": 6.23,
  "eu_magnetic_moment": 5.83,
  "n_magnetic_moment": 0.10,
  "ga_magnetic_moment": 0.09,
  "interstitial_magnetic_moment": 0.21
}
EOF
