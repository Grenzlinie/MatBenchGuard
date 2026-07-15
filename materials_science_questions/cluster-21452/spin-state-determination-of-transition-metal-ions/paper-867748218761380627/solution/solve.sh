#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: spin_state_splittings.json ===
cat > /app/outputs/spin_state_splittings.json <<'EOF'
{
  "cas5_splitting_eV": 1.26,
  "cas7_splitting_eV": 0.87,
  "mrci7_splitting_eV": 0.18,
  "mrci11_splitting_eV": -0.006
}
EOF
