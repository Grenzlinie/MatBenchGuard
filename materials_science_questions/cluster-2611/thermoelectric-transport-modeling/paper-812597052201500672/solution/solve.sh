#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_effective_mass.json ===
cat > /app/outputs/step_01_effective_mass.json <<'EOF'
{
  "m_star": 1.336
}
EOF
