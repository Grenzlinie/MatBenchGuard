#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: binding_energies.csv ===
cat > "$OUTDIR/binding_energies.csv" <<'FFEOF'
method,de,d0
B3LYP/6-311++G(3df,3pd),11.1,9.09
MP2/6-311++G(3df,3pd),13.3,12.2
FFEOF

# === solve block: thermodynamic_functions.csv ===
cat > "$OUTDIR/thermodynamic_functions.csv" <<'FFEOF'
property,T100,T298,T1000
Cp,63.93,113.0,178.5
S,282.9,375.9,555.5
H_minus_H298,4.850,22.61,131.3
FFEOF
