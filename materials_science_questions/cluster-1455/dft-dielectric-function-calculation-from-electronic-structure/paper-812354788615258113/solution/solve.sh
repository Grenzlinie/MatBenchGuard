#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: epsilon_inf_si.json ===
cat > "$OUTDIR/epsilon_inf_si.json" <<'EOF'
{
  "epsilon_inf": 12.2
}
EOF
