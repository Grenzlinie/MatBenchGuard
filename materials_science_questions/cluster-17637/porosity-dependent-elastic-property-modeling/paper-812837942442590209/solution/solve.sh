#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: base_case_results.json ===
# base_case_results.json
cat > "$OUTDIR/base_case_results.json" <<'EOF'
{
  "porosity": 0.2,
  "l_over_r": 20,
  "a_over_r": 3,
  "K_apparent": 1.89,
  "strength_reduction": 0.471
}
EOF

# === solve block: parametric_porosity.csv ===
# parametric_porosity.csv
cat > "$OUTDIR/parametric_porosity.csv" <<'EOF'
porosity,K_apparent,strength_reduction
0.05,1.111,0.10
0.10,1.282,0.22
0.15,1.538,0.35
0.20,1.890,0.471
0.25,2.222,0.55
EOF
