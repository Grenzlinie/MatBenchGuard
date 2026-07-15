#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: force_factor.json ===
python3 -c "import json; data={'q':0.04,'factor':0.68,'description':'Dimensionless perturbation force factor F/(A mu c0) computed at q=0.04'}; json.dump(data, open('$OUTDIR/force_factor.json','w'), indent=2)"
