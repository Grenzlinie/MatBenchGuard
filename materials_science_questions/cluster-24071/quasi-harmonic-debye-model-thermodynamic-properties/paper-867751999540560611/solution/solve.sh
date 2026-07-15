#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: heat_capacity.csv ===
python3 /solution/helper.py heat_capacity

# === solve block: heat_content.csv ===
python3 /solution/helper.py heat_content

# === solve block: vacancy_concentration.csv ===
python3 /solution/helper.py vacancy_concentration
