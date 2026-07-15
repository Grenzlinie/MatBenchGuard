#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'FFEOF'
{
  "ground_state_configuration": "AFM-G",
  "band_gap_meV": 155.2,
  "oxygen_moment_min_muB": 0.11,
  "oxygen_moment_max_muB": 0.31,
  "relative_energies": {
    "NM": 0.0,
    "FM": null,
    "AFM-S": null,
    "AFM-LR": -92.10,
    "AFM-G": -96.03
  }
}
FFEOF
