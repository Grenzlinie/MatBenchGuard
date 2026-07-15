#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_relative_energies.json ===
cat > /app/outputs/step_01_relative_energies.json <<'HEREDOC_END'
{
  "R=OCH3": {
    "reactant_complex": -42,
    "transition_state": 203,
    "product_complex": -65,
    "separate_products": -25
  },
  "R=OH": {
    "reactant_complex": -55,
    "transition_state": -14,
    "product_complex": -63,
    "separate_products": -29
  },
  "R=OSiH3": {
    "reactant_complex": -22,
    "transition_state": 2,
    "product_complex": -34,
    "separate_products": -4
  }
}
HEREDOC_END
