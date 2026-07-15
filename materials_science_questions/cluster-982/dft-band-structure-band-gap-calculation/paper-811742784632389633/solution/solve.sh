#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: bulk_eigenvalues.json ===
cat > "$OUTDIR/bulk_eigenvalues.json" <<'FFEOF'
{
  "Gamma15": -2.6,
  "X3": -2.6,
  "X5_prime": -3.7,
  "X4_prime": -6.2
}
FFEOF

# === solve block: elastic_constants.json ===
cat > "$OUTDIR/elastic_constants.json" <<'FFEOF'
{
  "C11": 6.42,
  "C12": 1.48,
  "C44": 1.59
}
FFEOF

# === solve block: surface_state_gamma_energy.txt ===
echo "-2.9" > "$OUTDIR/surface_state_gamma_energy.txt"
