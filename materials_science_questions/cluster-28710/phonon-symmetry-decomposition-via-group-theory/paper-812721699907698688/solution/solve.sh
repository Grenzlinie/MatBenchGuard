#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: mode_decomposition.json ===
cat > /app/outputs/mode_decomposition.json <<'JSON_EOF'
{
  "A1": {"count": 20, "raman": true, "ir": true},
  "A2": {"count": 16, "raman": false, "ir": false},
  "B1": {"count": 15, "raman": true, "ir": false},
  "B2": {"count": 20, "raman": true, "ir": false},
  "E": {"count": 38, "raman": true, "ir": true}
}
JSON_EOF
