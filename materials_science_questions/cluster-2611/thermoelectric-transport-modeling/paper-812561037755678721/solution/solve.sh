#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: eff_masses.json ===
cat > "$OUTDIR/eff_masses.json" <<'FFEOF'
{
  "polyacetylene": {
    "m_eff": 0.455,
    "E_Fermi": 0.04069
  },
  "polypyrrole": {
    "m_eff": 0.502,
    "E_Fermi": 0.01727
  },
  "polythiophene": {
    "m_eff": 0.446,
    "E_Fermi": 0.01822
  }
}
FFEOF

# === solve block: ctp_frequencies.csv ===
python3 /solution/ctp_gen.py

# === solve block: seebeck.csv ===
cat > "$OUTDIR/seebeck.csv" <<'FFEOF'
bridge,S_uV_per_K
polyacetylene,90
polypyrrole,212
polythiophene,201
FFEOF

# === solve block: chi_vibr.json ===
cat > "$OUTDIR/chi_vibr.json" <<'FFEOF'
{
  "chi_vibr_W_per_mK": 0.77
}
FFEOF

# === solve block: zt.csv ===
cat > "$OUTDIR/zt.csv" <<'FFEOF'
bridge,ZT
polyacetylene,0.08
polypyrrole,0.45
polythiophene,0.40
FFEOF
