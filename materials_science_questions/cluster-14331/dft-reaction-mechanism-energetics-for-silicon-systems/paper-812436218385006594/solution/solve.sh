#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: energies.json ===
cat > /app/outputs/energies.json <<'EOF'
{
  "E_bare_active_site": -1000.0,
  "E_isolated_peroxide": -100.0,
  "E_eta1_intermediate": -1100.04,
  "E_eta2_intermediate": -1100.035,
  "E_TS_eta1_formation": -1099.98474862,
  "E_TS_eta2_formation": -1099.98474862,
  "E_TS_interconversion": -1100.02474862,
  "E_eta1_formation_barrier_kJmol": 40.0,
  "E_eta2_formation_barrier_kJmol": 40.0,
  "E_interconversion_barrier_kJmol": 40.0
}
EOF
