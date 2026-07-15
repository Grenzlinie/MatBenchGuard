#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "${OUTDIR}"

# === solve block: optimized_x.txt ===
cat > "${OUTDIR}/optimized_x.txt" <<'FFEOF'
0.1284
FFEOF

# === solve block: band_analysis.json ===
cat > "${OUTDIR}/band_analysis.json" <<'FFEOF'
{
  "optimized_bandwidth_dx2y2": 0.05,
  "optimized_half_metallic": true,
  "x1450_metallic": true
}
FFEOF

# === solve block: density_peaks.json ===
cat > "${OUTDIR}/density_peaks.json" <<'FFEOF'
{
  "optimized_peak_density": 2.2,
  "x1450_peak_density": 1.3
}
FFEOF
