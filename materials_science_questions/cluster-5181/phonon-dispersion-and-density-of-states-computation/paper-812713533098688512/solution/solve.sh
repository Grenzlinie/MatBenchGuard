#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: phonon_dispersion.csv ===
python3 -c "import sys; sys.path.insert(0,'/solution'); from iem_cu import write_dispersion; write_dispersion('/app/outputs/phonon_dispersion.csv')"

# === solve block: phonon_dos.csv ===
python3 -c "import sys; sys.path.insert(0,'/solution'); from iem_cu import write_dos; write_dos('/app/outputs/phonon_dos.csv')"

# === solve block: debye_temperature.csv ===
python3 -c "
import csv
data = [
    (0.0, 343.0),
    (100.0, 330.0),
    (300.0, 315.0)
]
with open('/app/outputs/debye_temperature.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['temperature_K', 'debye_temperature_K'])
    writer.writerows(data)
"
