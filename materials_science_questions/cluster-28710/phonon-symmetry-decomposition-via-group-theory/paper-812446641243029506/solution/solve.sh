#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: irrep_decomposition.json ===
cat > "$OUTDIR/irrep_decomposition.json" <<'JSON_EOF'
{
  "phonon_irreps": {
    "Γ1+": 1,
    "Γ2+": 2,
    "Γ3+": 3,
    "Γ1-": 2,
    "Γ2-": 2,
    "Γ3-": 4
  },
  "raman_active": {
    "Γ1+": 1,
    "Γ3+": 3
  },
  "infrared_active": {
    "Γ2+": 2,
    "Γ3-": 4
  }
}
JSON_EOF
