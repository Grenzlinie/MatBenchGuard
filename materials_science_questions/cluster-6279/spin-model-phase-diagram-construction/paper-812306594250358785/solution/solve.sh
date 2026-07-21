#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: critical_points.json ===
cat > "$OUTDIR/critical_points.json" <<'EOF'
[
  {"id": "C1", "K": 4.0},
  {"id": "C2", "K": 2.27492},
  {"id": "C3", "K": 1.74400},
  {"id": "C4", "K": 1.51843},
  {"id": "C5", "K": 1.41463},
  {"id": "C6", "K": 1.36750},
  {"id": "C7", "K": 1.34709},
  {"id": "C8", "K": 1.33869}
]
EOF
