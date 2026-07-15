#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: magnetoelastic_coefficients.json ===
cat > "$OUTDIR/magnetoelastic_coefficients.json" <<'FFEOF'
{
  "G11": 54,
  "G44": 43
}
FFEOF
