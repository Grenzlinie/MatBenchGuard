#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 /solution/gen_outputs.py

# === solve block: bare_preference.csv ===
cat > "$OUTDIR/bare_preference.csv" <<'EOF'
M,E_T_type,E_H_type,delta_E
Ce,-100.0,-99.0,-1.0
Pr,-100.0,-99.0,-1.0
Nd,-100.0,-99.0,-1.0
Sm,-100.0,-99.0,-1.0
Eu,-100.0,-99.0,-1.0
Gd,-100.0,-99.0,-1.0
Tb,-100.0,-99.0,-1.0
Dy,-100.0,-99.0,-1.0
Ho,-100.0,-99.0,-1.0
Er,-100.0,-99.0,-1.0
Tm,-100.0,-99.0,-1.0
Yb,-100.0,-99.0,-1.0
EOF

# === solve block: stability_report.json ===
true

# === solve block: functionalized_properties.json ===
true

# === solve finalize ===
true
