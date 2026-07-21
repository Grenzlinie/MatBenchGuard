#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/usr/bin/env bash
set -euo pipefail

# Install numpy (required by the helper).
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: voltage_vs_frequency.csv ===
python3 /solution/helper.py --output "$OUTDIR/voltage_vs_frequency.csv" --mode voltage

# === solve block: location_vs_frequency.csv ===
python3 /solution/helper.py --output /app/outputs/location_vs_frequency.csv --mode location
