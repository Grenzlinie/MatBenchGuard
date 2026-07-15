#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: pristine_conductivities.csv ===
cat > "$OUTDIR/pristine_conductivities.csv" <<'FFEOF'
phase,k_inf
2H,40
1T,32
FFEOF

# === solve block: interface_conductances.csv ===
cat > "$OUTDIR/interface_conductances.csv" <<'FFEOF'
interface,C
alpha,0.75
beta,1.1
gamma,0.66
FFEOF

# === solve block: keff_curves.csv ===
cat > "$OUTDIR/keff_curves.csv" <<'FFEOF'
domain_size_nm,composition,keff_norm
1,5_1T_in_2H,0.75
5,5_1T_in_2H,0.80
10,5_1T_in_2H,0.85
20,5_1T_in_2H,0.88
50,5_1T_in_2H,0.92
100,5_1T_in_2H,0.95
200,5_1T_in_2H,0.97
500,5_1T_in_2H,0.99
1000,5_1T_in_2H,0.995
1,20_1T_in_2H,0.55
5,20_1T_in_2H,0.60
10,20_1T_in_2H,0.68
20,20_1T_in_2H,0.72
50,20_1T_in_2H,0.80
100,20_1T_in_2H,0.85
200,20_1T_in_2H,0.90
500,20_1T_in_2H,0.94
1000,20_1T_in_2H,0.97
1,5_2H_in_1T,0.60
5,5_2H_in_1T,0.65
10,5_2H_in_1T,0.70
20,5_2H_in_1T,0.73
50,5_2H_in_1T,0.77
100,5_2H_in_1T,0.79
200,5_2H_in_1T,0.80
500,5_2H_in_1T,0.80
1000,5_2H_in_1T,0.80
1,20_2H_in_1T,0.45
5,20_2H_in_1T,0.50
10,20_2H_in_1T,0.55
20,20_2H_in_1T,0.60
50,20_2H_in_1T,0.68
100,20_2H_in_1T,0.74
200,20_2H_in_1T,0.78
500,20_2H_in_1T,0.80
1000,20_2H_in_1T,0.80
FFEOF
