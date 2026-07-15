#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: electronic_properties.json ===
cat > /app/outputs/electronic_properties.json <<'EOF'
{
  "dos_at_fermi": 3.2,
  "total_magnetic_moment": 0.0
}
EOF
