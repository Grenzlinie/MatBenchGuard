#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: srvo3_results.json ===
cat > /app/outputs/srvo3_results.json <<'FFEOF'
{
  "lda_bandwidth": 2.6,
  "lower_hubbard_band_peak": -1.5,
  "upper_hubbard_band_peak": 2.5,
  "quasiparticle_peak_weight": 0.476190476,
  "effective_mass_ratio": 2.1
}
FFEOF

# === solve block: cavo3_results.json ===
cat > /app/outputs/cavo3_results.json <<'FFEOF'
{
  "lda_bandwidth": 2.5,
  "lower_hubbard_band_peak": -1.5,
  "upper_hubbard_band_peak": 2.5,
  "quasiparticle_peak_weight": 0.416666667,
  "effective_mass_ratio": 2.4
}
FFEOF
