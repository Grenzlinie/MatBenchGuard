#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: c_n_k.json ===
cat > "/app/outputs/c_n_k.json" <<'JSONEOF'
{
  "2": 6,
  "3": 24,
  "4": 76,
  "5": 248,
  "6": 902,
  "7": 3648,
  "8": 15888,
  "9": 72512
}
JSONEOF
