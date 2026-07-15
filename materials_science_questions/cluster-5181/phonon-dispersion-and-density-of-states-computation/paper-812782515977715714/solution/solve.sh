#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail

export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# Install numpy (Tsinghua mirror) – required by the intensity generator
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: force_constants.csv ===
#!/bin/bash
# Write force constants CSV with D-D first-neighbor ratio = 1.5
cat > "$OUTDIR/force_constants.csv" <<'FFEOF'
parameter_name,fitted_value,stoichiometric_value,ratio
D_D_1nn,0.15,0.1,1.5
FFEOF

# === solve block: zone_boundary_100.csv ===
#!/bin/bash
python3 /solution/generate.py zone_boundary_100.csv

# === solve block: zone_center_400.csv ===
#!/bin/bash
python3 /solution/generate.py zone_center_400.csv

# === solve block: longitudinal_313_0.csv ===
#!/bin/bash
python3 /solution/generate.py longitudinal_313_0.csv

# === solve finalize ===
echo "Oracle artifacts written successfully."
