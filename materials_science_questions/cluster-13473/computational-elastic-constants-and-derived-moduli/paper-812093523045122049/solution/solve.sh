#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: elastic_constants.json ===
cat > /app/outputs/elastic_constants.json <<'EOF'
{
  "C11": 12.44,
  "C12": 7.03,
  "C13": 8.36,
  "C33": 12.79,
  "C44": 2.97,
  "C66": 2.63
}
EOF
