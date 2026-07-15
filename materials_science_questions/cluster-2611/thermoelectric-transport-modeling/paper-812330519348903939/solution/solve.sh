#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: exponents.json ===
cat > "$OUTDIR/exponents.json" << 'EOF'
[
  {"temperature": 1273, "n_sigma": 3.91, "n_alpha": 3.91, "n_h": 3.91},
  {"temperature": 1473, "n_sigma": 3.91, "n_alpha": 3.91, "n_h": 3.91},
  {"temperature": 1673, "n_sigma": 4.16, "n_alpha": 4.63, "n_h": 4.16}
]
EOF
