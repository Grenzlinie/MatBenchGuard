#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: critical_width.txt ===
cat > /app/outputs/critical_width.txt <<'FFEOF'
13
FFEOF

# === solve block: stress_threshold.json ===
cat > /app/outputs/stress_threshold.json <<'FFEOF'
{
  "tensile_max": -10,
  "compressive_max": 10
}
FFEOF

# === solve block: terrace_ratio.txt ===
cat > /app/outputs/terrace_ratio.txt <<'FFEOF'
1.5
FFEOF
