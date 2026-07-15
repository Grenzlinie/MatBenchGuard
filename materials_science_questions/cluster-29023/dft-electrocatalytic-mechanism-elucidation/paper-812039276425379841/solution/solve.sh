#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: molecule_results.json ===
cat > "$OUTDIR/molecule_results.json" <<'FFEOF'
[
  {
    "molecule": "BCA",
    "HOMOexp_character": "π",
    "gap_HOMO_exp_LUMO_exp": 4.4,
    "sigma2_present": false
  },
  {
    "molecule": "ortho-PyCA",
    "HOMOexp_character": "σ",
    "gap_HOMO_exp_LUMO_exp": 3.5,
    "sigma2_present": true
  }
]
FFEOF
