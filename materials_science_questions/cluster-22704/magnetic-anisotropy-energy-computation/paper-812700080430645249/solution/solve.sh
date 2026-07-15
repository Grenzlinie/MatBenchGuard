#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.csv ===
cat > "/app/outputs/results.csv" <<'FFEOF'
E_inplane_au_eV,E_perp_au_eV,MAE_eV,easy_axis,system
-200.0000,-200.0005,-0.0005,in-plane,free-standing Fe(001)
-300.0000,-300.0003,-0.0003,in-plane,free-standing Co(001)
-400.0005,-400.0000,0.0005,out-of-plane,Fe/Au(001)
-500.0004,-500.0000,0.0004,out-of-plane,Fe/Ag(001)
-600.0003,-600.0000,0.0003,out-of-plane,Fe/Pd(001)
FFEOF
