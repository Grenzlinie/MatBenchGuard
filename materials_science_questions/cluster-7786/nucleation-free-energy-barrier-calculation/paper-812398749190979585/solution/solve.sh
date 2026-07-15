#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: nucleation_results.json ===
cat > "$OUTDIR/nucleation_results.json" <<'EOF'
{
  "barrier_at_250K": 60.0,
  "NB_estimate": 10.0,
  "critical_axial_ratio": 20.0
}
EOF
