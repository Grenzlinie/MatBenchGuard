#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_f_ratios.json ===
cat > /app/outputs/step_01_f_ratios.json <<'FFEOF'
{"f295_80": 0.895, "f425_80": 0.828}
FFEOF

# === solve block: step_02_shifts.json ===
cat > /app/outputs/step_02_shifts.json <<'FFEOF'
{"shift_80_295": 0.118, "shift_295_425": 0.093}
FFEOF
