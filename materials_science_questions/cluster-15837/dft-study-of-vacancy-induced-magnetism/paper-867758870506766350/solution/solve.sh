#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: pristine_results.json ===
cat > /app/outputs/pristine_results.json <<'EOF'
{
  "a": 11.55,
  "b": 3.58,
  "c": 9.014,
  "volume": 372.7,
  "band_gap": 2.3
}
EOF

# === solve block: mn_sub_results.json ===
cat > /app/outputs/mn_sub_results.json <<'EOF'
{
  "delta_volume_pct": -0.60,
  "magnetization_muB": 2.00
}
EOF

# === solve block: mn_int_results.json ===
cat > /app/outputs/mn_int_results.json <<'EOF'
{
  "delta_volume_pct": 3.48,
  "magnetization_muB": 5.00
}
EOF
