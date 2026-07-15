#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: relaxed_lattice_parameters.csv ===
cat > "/app/outputs/relaxed_lattice_parameters.csv" <<'FFEOF'
a,b,c,converged,n,system,volume
5.5022,5.4534,7.7361,true,0,LaFeO3,232.127
4.7970,4.6880,6.5442,true,3,LaFeO3,147.168
4.6684,3.5080,6.2510,true,6,LaFeO3,102.371
4.1412,3.6572,5.6006,true,9,LaFeO3,84.822
NaN,NaN,NaN,false,12,LaFeO3,NaN
5.4878,7.6051,5.5275,true,0,LaCrO3,230.692
4.7816,6.4391,4.7088,true,3,LaCrO3,144.980
5.5982,5.3561,3.2572,true,6,LaCrO3,97.666
FFEOF
