#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p "$OUTDIR"

# === solve block: vacancy_properties.json ===
cat > "$OUTDIR/vacancy_properties.json" <<'FFEOF'
{
  "magnetic_moment_mu_B": 0.889,
  "Delta_E_mag_eV": -0.064
}
FFEOF
