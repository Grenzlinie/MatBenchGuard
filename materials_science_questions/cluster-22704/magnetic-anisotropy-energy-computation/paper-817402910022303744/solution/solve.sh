#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: mae_summary.csv ===
cat > /app/outputs/mae_summary.csv <<'FFEOF'
MAE_MJpm3,system
0.52,Fe5PB2
0.38,Fe0.8Co0.2
0.18,Fe0.6Co0.4
-0.18,Fe0.4Co0.6
-0.38,Fe0.2Co0.8
-0.51,Co5PB2
1.10,Fe0.95W0.05
1.10,Fe0.95Re0.05
FFEOF
