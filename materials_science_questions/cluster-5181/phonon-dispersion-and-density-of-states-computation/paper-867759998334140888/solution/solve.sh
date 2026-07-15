#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dephasing_times.json ===
cat > /app/outputs/dephasing_times.json <<'EOF'
{
  "10": 4.8,
  "70": 4.5
}
EOF
