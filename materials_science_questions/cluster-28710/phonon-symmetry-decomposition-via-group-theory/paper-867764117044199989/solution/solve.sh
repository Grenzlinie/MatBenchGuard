#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: displacement_pattern.txt ===
# Write the exact displacement pattern for the B[Cmm2] bush
cat > "$OUTDIR/displacement_pattern.txt" <<'FFEOF'
(A,B|2C,-C|2D,-D|-A,A+B|A,-A-B|-2D,D|-2C,C|-A,-B)
FFEOF
