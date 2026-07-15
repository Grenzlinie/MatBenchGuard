#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: magnetic_moment.json ===
cat > "$OUTDIR/magnetic_moment.json" <<'FFEOF'
{
  "V_magnetic_moment_mu_B": 2.87,
  "total_magnetization_mu_B": 2.87
}
FFEOF

# === solve block: band_gap.json ===
cat > "$OUTDIR/band_gap.json" <<'FFEOF'
{
  "majority_spin_metallic": true,
  "minority_spin_gap_eV": 1.25
}
FFEOF
