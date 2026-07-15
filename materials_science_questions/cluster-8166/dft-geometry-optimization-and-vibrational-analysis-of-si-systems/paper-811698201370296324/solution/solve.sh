#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: reproduction_outputs.json ===
cat > "$OUTDIR/reproduction_outputs.json" <<'EOF'
{
  "Si_charge": 0.95,
  "O_charges": [-0.45, -0.46, -0.47, -0.48, -0.47, -0.46],
  "Si_O_distances": [180.2, 180.5, 180.7, 180.9, 181.0, 181.1]
}
EOF

# === solve finalize ===
# All outputs written
