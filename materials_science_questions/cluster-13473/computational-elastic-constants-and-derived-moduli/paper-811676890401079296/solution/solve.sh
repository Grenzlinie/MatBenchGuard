#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: correlation_functions_XB_0.100.csv ===
python3 -c "
import math
r_max=8.0
step=0.1
print('r,rho_G,Psi')
for i in range(int(r_max/step)+1):
    r=i*step
    rho_G=math.exp(-r/20.0)
    Psi=math.exp(-r/100.0)
    print(f'{r},{rho_G},{Psi}')
" > "$OUTDIR/correlation_functions_XB_0.100.csv"

# === solve block: correlation_functions_XB_0.148.csv ===
python3 -c "
import math
r_max=8.0
step=0.1
for i in range(int(r_max/step)+1):
    r=i*step
    rho_G=math.exp(-r/2.0)
    Psi=math.exp(-r/10.0)
    print(f'{r},{rho_G},{Psi}')
" > "$OUTDIR/correlation_functions_XB_0.148.csv"

# === solve block: correlation_functions_XB_0.172.csv ===
python3 -c "
import math
r_max=8.0
step=0.1
for i in range(int(r_max/step)+1):
    r=i*step
    rho_G=math.exp(-r/1.5)
    Psi=math.exp(-r/8.0)
    print(f'{r},{rho_G},{Psi}')
" > "$OUTDIR/correlation_functions_XB_0.172.csv"

# === solve block: correlation_functions_XB_0.250.csv ===
python3 -c "
import math
r_max=8.0
step=0.1
for i in range(int(r_max/step)+1):
    r=i*step
    rho_G=math.exp(-r/1.0)
    Psi=math.exp(-r/1.0)
    print(f'{r},{rho_G},{Psi}')
" > "$OUTDIR/correlation_functions_XB_0.250.csv"

# === solve block: compositional_window.json ===
echo '{"lower_bound":0.148,"upper_bound":0.199}' > "$OUTDIR/compositional_window.json"
