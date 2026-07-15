#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: raman_profile.csv ===
cat > "$OUTDIR/raman_profile.csv" <<'EOF'
laser_energy,intensity
1.85,0.002
1.98,0.003
2.4,1.0
EOF
