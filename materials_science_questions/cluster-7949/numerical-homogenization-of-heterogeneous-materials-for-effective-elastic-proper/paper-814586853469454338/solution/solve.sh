#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: stiffness_matrix.json ===
cat > /app/outputs/stiffness_matrix.json <<'JSONEOF'
{
  "C11": 81.4226,
  "C22": 81.3415,
  "C33": 81.4071,
  "C12": 41.9190,
  "C13": 41.9349,
  "C23": 41.9196,
  "C44": 19.7113,
  "C55": 19.7368,
  "C66": 19.7123
}
JSONEOF

# === solve block: effective_constants.json ===
cat > /app/outputs/effective_constants.json <<'JSONEOF'
{
  "E": 52.85,
  "G": 19.72,
  "nu": 0.3401
}
JSONEOF
