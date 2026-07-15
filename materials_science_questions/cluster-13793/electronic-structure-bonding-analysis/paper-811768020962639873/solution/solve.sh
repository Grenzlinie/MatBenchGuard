#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: structure_and_elastic.json ===
cat > "$OUTDIR/structure_and_elastic.json" <<'FFEOF'
{
  "a": 4.5149,
  "c": 3.1156,
  "u": 0.3057,
  "B0": 245.56,
  "c11": 308.38,
  "c33": 508.95,
  "c44": 108.63,
  "c66": 208.22,
  "c12": 214.49,
  "c13": 171.05
}
FFEOF

# === solve block: optical_properties.json ===
cat > "$OUTDIR/optical_properties.json" <<'FFEOF'
{
  "n0_perp": 13.93,
  "n0_par": 8.13,
  "eps2_peak_perp_pos": 0.01,
  "eps2_peak_perp_mag": 55.23,
  "eps2_peak_par_pos": 0.82,
  "eps2_peak_par_mag": 25.33,
  "eloss_peak_perp_pos": 22.85,
  "eloss_peak_perp_mag": 11.85,
  "eloss_peak_par_pos": 22.27,
  "eloss_peak_par_mag": 15.85,
  "ext_peak_perp_pos": 0.78,
  "ext_peak_par_pos": 1.33
}
FFEOF
