#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR='/app/outputs'
mkdir -p "$OUTDIR"

# === solve block: step_01_mg3bi2_gap.txt ===
cat > "$OUTDIR/step_01_mg3bi2_gap.txt" <<'FFEOF'
metallic
FFEOF

# === solve block: step_02_mg3sb2_gap.txt ===
cat > "$OUTDIR/step_02_mg3sb2_gap.txt" <<'FFEOF'
0.12
FFEOF
