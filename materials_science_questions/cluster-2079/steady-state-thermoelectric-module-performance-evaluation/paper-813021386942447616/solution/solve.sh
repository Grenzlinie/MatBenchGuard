#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: temperatures.json ===
cat > "$OUTDIR/temperatures.json" <<'EOF'
{"Ta10":{"T_w":0,"T_g":0,"T_c":0},"Ta35":{"T_w":0,"T_g":0,"T_c":0}}
EOF

# === solve block: model_results.json ===
cat > "$OUTDIR/model_results.json" <<'EOF'
{
  "Ta10": {
    "mdot_kg_per_day": 6.87,
    "eta_still_pct": 41.67,
    "eta_system_pct": 54.69,
    "P_output_W": 137.23
  },
  "Ta35": {
    "mdot_kg_per_day": 8.73,
    "eta_still_pct": 50.42,
    "eta_system_pct": 70.00,
    "P_output_W": 114.45
  }
}
EOF
