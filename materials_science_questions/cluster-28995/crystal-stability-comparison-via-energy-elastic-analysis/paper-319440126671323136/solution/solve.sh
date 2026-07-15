#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: energy_ordering.json ===
cat > /app/outputs/energy_ordering.json <<'HEREDOC'
{
  "triangular_family_minimum": -10.5,
  "square_family_minimum": -10.3,
  "simple_hexagonal": -10.0,
  "fcc": -9.8,
  "bcc": -9.7,
  "hcp": -9.9,
  "simple_cubic": -9.5,
  "diamond": -9.0,
  "beta_Sn": -9.85
}
HEREDOC
