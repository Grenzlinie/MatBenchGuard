#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: barriers.json ===
cat > /app/outputs/barriers.json <<'EOF'
{
  "Cu(100)": 0.92,
  "Cu(110)": 0.62,
  "Cu(111)": 0.97,
  "CuPd(111)": 0.63
}
EOF
