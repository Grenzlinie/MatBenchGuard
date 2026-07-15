#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
python3 /solution/generate_outputs.py

# === solve block: step_02_rotational_constants.json ===
cat > "$OUTDIR/step_02_rotational_constants.json" <<'EOF'
{
  "A_MHz": 20068.0,
  "B_MHz": 1159.9234,
  "C_MHz": 1120.3176
}
EOF

# === solve block: step_03_interaction_energy.json ===
:

# === solve block: step_04_potential_curve.csv ===
:

# === solve block: step_05_morse_fit_params.json ===
:

# === solve block: step_06_wkb_energies.json ===
:
