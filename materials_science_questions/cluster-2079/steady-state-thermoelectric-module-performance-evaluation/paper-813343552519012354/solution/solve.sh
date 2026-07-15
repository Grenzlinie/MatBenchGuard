#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: power_savings_table_I.csv ===
cat > "/app/outputs/power_savings_table_I.csv" <<'FFEOF'
block_name,cooling_effect_celsius,power_saving_percent
L-3 Cache,6,7
L-2 Cache,8,2
I-Cache,10,-5
BRED,10,-2
I-Decoder,10,-3
Rename,10,-20
LdStQ,10,-11
ITB,10,-21
DTB,10,-8
Register File,10,-12
I-Scheduler,10,-12
Integer ALU,10,-8
FFEOF

# === solve block: power_savings_table_II.csv ===
cat > "/app/outputs/power_savings_table_II.csv" <<'FFEOF'
tech_node_nm,cache_level,ZT,power_saving_percent
65,L-2 Cache,1,2
65,L-2 Cache,2,5
65,L-3 Cache,1,7
65,L-3 Cache,2,37
45,L-2 Cache,1,7
45,L-2 Cache,2,17
45,L-3 Cache,1,10
45,L-3 Cache,2,50
32,L-2 Cache,1,13
32,L-2 Cache,2,27
32,L-3 Cache,1,16
32,L-3 Cache,2,60
22,L-2 Cache,1,14
22,L-2 Cache,2,29
22,L-3 Cache,1,18
22,L-3 Cache,2,62
FFEOF
