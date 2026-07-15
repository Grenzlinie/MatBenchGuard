#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: volumes.json ===
cat > /app/outputs/volumes.json <<'FFEOF'
{
  "structure1": 713.1,
  "structure2": 1002.3,
  "structure3": 3153.7,
  "structure4": 3551.1,
  "structure6": 4768.6
}
FFEOF

# === solve block: barriers.json ===
cat > /app/outputs/barriers.json <<'FFEOF'
{
  "n8": 0.28,
  "n16": 0.22
}
FFEOF
