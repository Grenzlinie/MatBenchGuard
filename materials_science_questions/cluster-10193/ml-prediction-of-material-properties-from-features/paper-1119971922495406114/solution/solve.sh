#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: evaluation_summary.json ===
cat > "$OUTDIR/evaluation_summary.json" <<'ENDOFJSON'
{
  "qm9_in_domain_variance": [0.09, 0.09, 0.21],
  "qm9_out_of_domain_variance": [62.0, 2.7, 3.2, 1.7, 56.0],
  "oc20_intermetallic_variance_median": 0.005,
  "oc20_nonmetal_variance_median": 0.03,
  "gold_variance_au_mean": 0.00022,
  "gold_variance_ag_mean": 0.61304,
  "qm9_test_R2": 0.96,
  "oc20_intermetallic_test_R2": 0.99
}
ENDOFJSON
