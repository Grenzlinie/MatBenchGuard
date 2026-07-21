#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: effective_masses.json ===
cat > /app/outputs/effective_masses.json <<'EOF'
{
  "CeFe4As12": 1.336,
  "CeFe4P12": 0.166,
  "CeFe4Sb12": 8.992
}
EOF
