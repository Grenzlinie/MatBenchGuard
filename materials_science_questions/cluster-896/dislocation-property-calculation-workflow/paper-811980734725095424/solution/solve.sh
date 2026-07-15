#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: peierls_stresses.json ===
cat > "/app/outputs/peierls_stresses.json" <<'FFEOF'
{
  "Fe": {
    "chi0": 0.054,
    "chi_neg30": 0.058,
    "chi_pos30": 0.080
  },
  "Nb": {
    "chi0": 0.028,
    "chi_neg30": 0.026,
    "chi_pos30": 0.045
  },
  "W": {
    "chi0": 0.036,
    "chi_neg30": 0.032,
    "chi_pos30": 0.062
  }
}
FFEOF

# === solve block: core_energies.json ===
cat > "/app/outputs/core_energies.json" <<'FFEOF'
{
  "Fe": 0.61,
  "Nb": 0.27,
  "W": 1.43
}
FFEOF
