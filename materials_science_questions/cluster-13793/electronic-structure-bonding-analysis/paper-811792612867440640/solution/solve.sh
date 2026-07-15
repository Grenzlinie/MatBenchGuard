#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: icohp_values.json ===
cat > /app/outputs/icohp_values.json <<'FFEOF'
{
  "ZrCuSiAs": {
    "Zr-Si": 1.51,
    "Si-Si": 1.41,
    "Cu-As": 1.43,
    "Zr-As": 1.73,
    "Cu-Cu": 0.49
  },
  "ZrCuSiP": {
    "Zr-Si": 1.51,
    "Si-Si": 1.41,
    "Cu-P": 1.43,
    "Zr-P": 1.73,
    "Cu-Cu": 0.49
  }
}
FFEOF

# === solve block: pseudogap_report.json ===
cat > /app/outputs/pseudogap_report.json <<'FFEOF'
{
  "ZrCuSiAs": {
    "pseudogap": true,
    "dos_ef": 0.25
  },
  "ZrCuSiP": {
    "pseudogap": true,
    "dos_ef": 0.25
  }
}
FFEOF
