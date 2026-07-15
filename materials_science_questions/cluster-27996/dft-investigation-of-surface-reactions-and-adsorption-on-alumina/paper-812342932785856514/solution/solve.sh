#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy

# === solve block: constrained_scan.csv ===
python3 /solution/generate_scan.py "$OUTDIR/constrained_scan.csv"

# === solve block: step_02_properties.json ===
cat > "$OUTDIR/step_02_properties.json" <<'EOF'
{
  "acid_sites": [
    {"site": "O1", "deprotonation_energy_kJmol": 1178.7, "oh_stretch_frequency_cm1": 3578, "ammonia_adsorption_energy_kJmol": 149.3},
    {"site": "O2", "deprotonation_energy_kJmol": 1180.9, "oh_stretch_frequency_cm1": 3541, "ammonia_adsorption_energy_kJmol": 142.9},
    {"site": "O3", "deprotonation_energy_kJmol": 1174.6, "oh_stretch_frequency_cm1": 3514, "ammonia_adsorption_energy_kJmol": 144.5},
    {"site": "O4", "deprotonation_energy_kJmol": 1179.1, "oh_stretch_frequency_cm1": 3532, "ammonia_adsorption_energy_kJmol": 135.7}
  ]
}
EOF
