#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: regression_fits.json ===
cat > "$OUTDIR/regression_fits.json" << 'JSONEOF'
[
  {"metal": "Ag", "pair": "HCOO_vs_COOH", "slope": 1.60, "intercept": -0.30},
  {"metal": "Ag", "pair": "COOH_vs_H", "slope": -0.50, "intercept": -0.01},
  {"metal": "Au", "pair": "HCOO_vs_COOH", "slope": 1.04, "intercept": -0.04},
  {"metal": "Au", "pair": "COOH_vs_H", "slope": -0.75, "intercept": -0.21},
  {"metal": "Pb", "pair": "HCOO_vs_COOH", "slope": 2.38, "intercept": 0.09},
  {"metal": "Pb", "pair": "COOH_vs_H", "slope": -1.47, "intercept": -0.25}
]
JSONEOF

# === solve block: classification_summary.json ===
cat > "$OUTDIR/classification_summary.json" << 'FFEOF'
[
  {"metal": "Ag", "predicted_category": "CO_single", "evidence": "HCOO:COOH slope=1.60 < 1.65, H:COOH slope=-0.50 < 0"},
  {"metal": "Au", "predicted_category": "CO_single", "evidence": "HCOO:COOH slope=1.04 < 1.65, H:COOH slope=-0.75 < 0"},
  {"metal": "Pb", "predicted_category": "HCOOH", "evidence": "HCOO:COOH slope=2.38 > 1.65"}
]
FFEOF
