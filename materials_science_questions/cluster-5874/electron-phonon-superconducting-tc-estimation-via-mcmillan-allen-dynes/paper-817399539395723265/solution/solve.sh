#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dft_results.json ===
cat > /app/outputs/dft_results.json <<'FFEOF'
{
  "NbC": {
    "dos_at_fermi": 0.74,
    "soc_splitting_meV": 130,
    "nodal_loops_present_without_soc": true
  },
  "TaC": {
    "dos_at_fermi": 0.64,
    "soc_splitting_meV": 400,
    "nodal_loops_present_without_soc": true
  }
}
FFEOF
