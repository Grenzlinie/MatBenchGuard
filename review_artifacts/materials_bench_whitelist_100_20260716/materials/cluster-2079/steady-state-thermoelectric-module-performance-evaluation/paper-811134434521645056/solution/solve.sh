#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
python3 /solution/make_all_csvs.py

# === solve block: delta_T_and_ZT.csv ===
echo 'delta_T_and_ZT.csv written'

# === solve block: heat_loss_and_power.csv ===
echo 'heat_loss_and_power.csv written'

# === solve block: efficiency_vs_C_water.csv ===
echo 'efficiency_vs_C_water.csv written'

# === solve block: efficiency_vs_C_oil.csv ===
echo 'efficiency_vs_C_oil.csv written'

# === solve block: efficiency_vs_ZT.csv ===
echo 'efficiency_vs_ZT.csv written'

# === solve block: efficiency_vs_Tcfi.csv ===
echo 'efficiency_vs_Tcfi.csv written'
