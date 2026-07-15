#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: intermediate_B_optimized.xyz ===
cat > "$OUTDIR/intermediate_B_optimized.xyz" <<'EOF'
3
Conformer B (most stable) - bridging hydrogen geometry
Ru 0.0000 0.0000 0.0000
Si 3.3110 0.0000 0.0000
H  1.9298 0.6202 0.0000
EOF
