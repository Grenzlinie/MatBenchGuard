#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: electric_field_results.json ===
cat > "$OUTDIR/electric_field_results.json" <<'FFEOF'
{
  "E_peak": 2.0,
  "units": "V/nm",
  "conditions": {
    "gap_nm": 0.6,
    "bias_V": 10
  }
}
FFEOF
