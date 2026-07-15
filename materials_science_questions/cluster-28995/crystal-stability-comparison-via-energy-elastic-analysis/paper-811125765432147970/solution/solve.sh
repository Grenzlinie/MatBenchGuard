#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: rs_stability.txt ===
cat > "$OUTDIR/rs_stability.txt" <<'FFEOF'
1.05
FFEOF

# === solve block: tc_value.txt ===
cat > "$OUTDIR/tc_value.txt" <<'FFEOF'
600
FFEOF
