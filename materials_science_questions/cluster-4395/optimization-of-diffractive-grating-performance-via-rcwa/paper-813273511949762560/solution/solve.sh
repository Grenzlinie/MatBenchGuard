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
  "resonance_n1.5": 6320.0,
  "resonance_n1.51": 6330.2,
  "shift_nm": 10.2,
  "sensitivity_nm_per_RIU": 1020.0
}
FFEOF
