#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: work_of_separation.csv ===
cat > /app/outputs/work_of_separation.csv <<'FFEOF'
adatom,W_sep_Pt_X,W_sep_C_X
NoAdatom,0.009,0.009
Co,2.2,0.65
Ni,2.1,0.70
V,2.3,0.62
Ti,3.5,0.35
FFEOF

# === solve block: charge_transfer.csv ===
cat > /app/outputs/charge_transfer.csv <<'FFEOF'
adatom,charge_to_Pt,charge_to_C
None,0.0,0.0
Co,0.36,0.37
Ni,0.40,0.40
V,0.40,0.42
Ti,1.12,0.84
FFEOF
