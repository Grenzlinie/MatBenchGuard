#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
export PATH="/usr/bin:$PATH"
PYTHON="python3"

# === solve block: band_gaps.json ===
cat > "$OUTDIR/band_gaps.json" << 'EOF'
{
  "HATP-COF-1": 1.40,
  "HATP-COF-2": 1.31
}
EOF

# === solve block: dos.json ===
$PYTHON /solution/generate_dos.py
