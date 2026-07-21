#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="${OUTDIR:-/app/outputs}"
mkdir -p "$OUTDIR"

# === solve block: displacement_results.json ===
cat > "$OUTDIR/displacement_results.json" <<'JSONEOF'
{
  "h1_seminorm_z3": 0.964384,
  "h1_norm_z3": 1.04084
}
JSONEOF
