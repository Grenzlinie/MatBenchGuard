#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: split_antisite_coordinates.json ===
cat > "$OUTDIR/split_antisite_coordinates.json" <<'FFEOF'
[
  {"atom": "As", "x": 0.0828, "y": 0.1953, "z": 0.0132},
  {"atom": "As", "x": -0.0828, "y": -0.1953, "z": -0.0132},
  {"atom": "As", "x": 0.3155, "y": 0.2329, "z": 0.3991},
  {"atom": "As", "x": -0.2388, "y": -0.3308, "z": 0.3787},
  {"atom": "As", "x": -0.3008, "y": 0.2891, "z": -0.2209},
  {"atom": "As", "x": 0.2994, "y": -0.3527, "z": -0.1689}
]
FFEOF

# === solve block: donor_level.json ===
cat > "$OUTDIR/donor_level.json" <<'FFEOF'
{"donor_level_below_cb": 0.3}
FFEOF

# === solve block: binding_energies.json ===
cat > "$OUTDIR/binding_energies.json" <<'FFEOF'
{"neutral": 1.4, "charged": 1.3, "scissors_corrected": 1.1}
FFEOF
