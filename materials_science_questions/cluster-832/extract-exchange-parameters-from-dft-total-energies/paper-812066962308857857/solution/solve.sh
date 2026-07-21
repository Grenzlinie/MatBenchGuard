#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_spinwave_gap.json ===
cat > /app/outputs/step_01_spinwave_gap.json <<'FFEOF'
{
  "spinwave_gap_K": 15.4,
  "g_factor": 2.0
}
FFEOF
