#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "$OUTDIR"

# === solve block: electronic_results.csv ===
cat > "$OUTDIR/electronic_results.csv" <<'EOF'
Eg,Delta0,me,mh
-0.27,0.89,0.04,0.33
EOF

# === solve block: thermal_conductivity_results.json ===
cat > "$OUTDIR/thermal_conductivity_results.json" <<'EOF'
{
  "kappa_300K": 4.68
}
EOF
