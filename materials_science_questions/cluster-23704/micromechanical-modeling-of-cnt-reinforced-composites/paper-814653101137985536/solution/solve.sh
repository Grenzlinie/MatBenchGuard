#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: computed_table.csv ===
python3 - "$OUTDIR" <<'PYEOF'
import sys, os
outdir = sys.argv[1]
with open(os.path.join(outdir, "computed_table.csv"), "w") as f:
    f.write("sample_no,t_nm,B,tau_MPa,sigma_i_MPa,Lc_um\n")
    f.write("1,2.38,23.28,18.97,3200000,9.27\n")
    f.write("2,13.6,19,1.12,29000,559.4\n")
    f.write("3,14,18.53,51.94,8300,7.12\n")
    f.write("4,6,5.07,1.13,699.4,245.5\n")
    f.write("5,8,15.3,42.4,23000,8.72\n")
PYEOF
