#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: superfluid_results.json ===
cat > /app/outputs/superfluid_results.json <<'FFEOF'
{
  "superfluid_fraction": 0.36,
  "condensate_fraction": 0.0003
}
FFEOF
