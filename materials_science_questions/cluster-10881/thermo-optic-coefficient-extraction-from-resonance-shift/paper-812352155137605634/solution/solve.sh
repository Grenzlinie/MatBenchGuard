#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: d36_values.json ===
cat > /app/outputs/d36_values.json <<'FFEOF'
{"cda": 9.6e-10, "cd_a": 9.6e-10}
FFEOF

# === solve block: birefringence_temp_variation.json ===
cat > /app/outputs/birefringence_temp_variation.json <<'FFEOF'
{"cda": 7.95e-06, "cd_a": 7.785e-06}
FFEOF

# === solve block: d36_ratio.json ===
cat > /app/outputs/d36_ratio.json <<'FFEOF'
{"ratio": 0.9230769}
FFEOF
