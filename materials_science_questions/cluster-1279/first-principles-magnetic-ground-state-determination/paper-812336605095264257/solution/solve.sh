#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'FFEOF'
{
  "FM": {
    "energy_per_atom_mRy": 0.0
  },
  "AF": {
    "energy_per_atom_mRy": 8.509
  },
  "NM": {
    "energy_per_atom_mRy": 21.721
  },
  "energy_differences": {
    "AF_minus_FM_mRy": 8.509,
    "NM_minus_FM_mRy": 21.721
  }
}
FFEOF
