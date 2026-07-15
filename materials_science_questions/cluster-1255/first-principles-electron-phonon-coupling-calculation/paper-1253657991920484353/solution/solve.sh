#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail

# === solve block: fermi_energies.json ===
cat > "/app/outputs/fermi_energies.json" <<'FFEOF'
{
  "lens": -3.05,
  "monster": 1.62,
  "cap": 0.96,
  "petty-1": -0.088,
  "petty-2": -0.012,
  "lilliputian": 0.00048
}
FFEOF
