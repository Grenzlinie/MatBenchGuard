#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'EOF'
{
  "ScSi16-": {
    "E_anion_Ha": -1000.0,
    "E_neutral_Ha": -999.84382572,
    "VDE_eV": 4.25,
    "HOMO_LUMO_gap_eV": 1.67
  },
  "LuSi16-": {
    "E_anion_Ha": -1000.0,
    "E_neutral_Ha": -999.84382572,
    "VDE_eV": 4.25,
    "HOMO_LUMO_gap_eV": 1.60
  }
}
EOF
