#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: band_gaps.json ===
cat > "$OUTDIR/band_gaps.json" <<'FFEOF'
{
  "GeS_ML": 1.76,
  "GeSe_ML": 1.23,
  "XX": 0.91,
  "XY": 1.02
}
FFEOF

# === solve block: lattice_thermal_conductivity.json ===
cat > "$OUTDIR/lattice_thermal_conductivity.json" <<'FFEOF'
{
  "GeS_ML": 1.16,
  "GeSe_ML": 0.32,
  "XX": 15.21,
  "XY": 17.95
}
FFEOF

# === solve block: zt_values.json ===
cat > "$OUTDIR/zt_values.json" <<'FFEOF'
{
  "GeS_ML": {
    "300K": 0.64,
    "800K": 1.83
  },
  "GeSe_ML": {
    "300K": 0.47,
    "800K": 1.73
  },
  "XX": {
    "300K": 0.13,
    "800K": 0.84
  },
  "XY": {
    "300K": 0.16,
    "800K": 0.83
  }
}
FFEOF
