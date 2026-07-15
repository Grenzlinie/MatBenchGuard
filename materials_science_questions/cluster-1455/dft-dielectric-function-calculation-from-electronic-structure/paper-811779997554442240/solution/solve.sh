#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_results.json ===
cat <<'EOF' > "$OUTDIR/step_01_results.json"
{
  "Be3N2": {
    "band_gap_eV": 3.26,
    "gap_direct": true,
    "epsilon0": 4.72,
    "eels_shoulder_eV": 10.0,
    "eels_max_eV": 23.2
  },
  "Mg3N2": {
    "band_gap_eV": 1.50,
    "gap_direct": true,
    "epsilon0": 5.69,
    "eels_shoulder_eV": 9.25,
    "eels_max_eV": 18.6
  },
  "Ca3N2": {
    "band_gap_eV": 1.13,
    "gap_direct": false,
    "epsilon0": 6.38
  }
}
EOF

# === solve finalize ===
echo "Output written."
