#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: barriers.json ===
cat > /app/outputs/barriers.json <<'FFEOF'
{
  "BNNT(5,5)_N-Vacancy-in": 0.39,
  "BNNT(6,6)_N-Vacancy-in": 0.29,
  "BNNT(7,7)_N-Vacancy-in": 0.33
}
FFEOF
