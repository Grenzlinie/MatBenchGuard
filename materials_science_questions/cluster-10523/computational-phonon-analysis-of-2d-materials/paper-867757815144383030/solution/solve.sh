#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: t_peak_frequency.json ===
cat > /app/outputs/t_peak_frequency.json <<'FFEOF'
{
  "t_peak_frequency_cm-1": 1078
}
FFEOF
