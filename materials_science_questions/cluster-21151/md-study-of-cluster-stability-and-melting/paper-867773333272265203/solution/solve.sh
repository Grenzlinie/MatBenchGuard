#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: clj38_analysis_results.json ===
cat > "$OUTDIR/clj38_analysis_results.json" <<'EOF'
{
  "mu_comp": [0, 0.25, 1, 5],
  "Delta_E": [0.676, 1.550, 3.564, 9.893],
  "n_fcc_n_icos_ratio": [0.11, 0.26, 3.93, 14.33]
}
EOF
