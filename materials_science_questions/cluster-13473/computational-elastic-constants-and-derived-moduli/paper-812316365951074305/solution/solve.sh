#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
mkdir -p /app/outputs

# === solve block: elastic_constants_systems.csv ===
cat << 'EOF' > "$OUTDIR/elastic_constants_systems.csv"
system,E,G
silica,88.7,41.0
polyimide,4.2,1.5
silica_composite,3.4,1.2
hydroxylated_composite,3.3,1.2
phenoxybenzene_composite,2.2,0.8
functionalized_composite,4.0,1.5
EOF

# === solve block: mori_tanaka_rve.csv ===
python3 /solution/write_outputs.py --output mori_tanaka_rve --file /app/outputs/mori_tanaka_rve.csv

# === solve block: effective_interface_properties.csv ===
python3 /solution/write_outputs.py --output interface --file /app/outputs/effective_interface_properties.csv

# === solve block: moduli_vs_radius.csv ===
python3 /solution/write_outputs.py --output moduli_vs_radius --file /app/outputs/moduli_vs_radius.csv
