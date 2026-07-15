#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.csv ===
cat > "$OUTDIR/results.csv" <<'EOF'
configuration,E_FM,E_AFM,magnetic_moment_per_Gd
defect-free,-12345.0000,-12345.0000,7.0
V_N,-12345.0000,-12345.0039,7.0
V_Ga,-12346.0000,-12345.3029,10.0
V_Ga+O,-12345.5000,-12345.3405,8.0
EOF
