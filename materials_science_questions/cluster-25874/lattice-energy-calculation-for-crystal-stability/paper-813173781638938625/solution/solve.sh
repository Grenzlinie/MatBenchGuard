#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: ice_VIII_energies.json ===
cat > /app/outputs/ice_VIII_energies.json <<'EOF'
{
  "VIII_p": 64.5,
  "VIII_o": 55.0,
  "VIII_mp": 57.8
}
EOF

# === solve finalize ===
# No finalize needed
