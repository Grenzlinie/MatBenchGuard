#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: binding_energies.json ===
cat > "$OUTDIR/binding_energies.json" <<'EOF'
{
  "PW91": {
    "1/4": -8.82,
    "1/2": -8.81,
    "1": -8.44
  },
  "LDA": {
    "1/2": -9.90,
    "1": -9.46
  }
}
EOF
