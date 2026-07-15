#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail

python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
mkdir -p /app/outputs

# === solve block: hparams.json ===
cat > /app/outputs/hparams.json <<'HEREDOC'
{
  "gamma_cm1": 56.0,
  "D_cm1": 30.8,
  "hw_E_cm1": 28.0,
  "V_over_alpha_cm1": 33.6
}
HEREDOC

cat > /app/outputs/zeeman_splitting.json <<'HEREDOC'
[
  {"label": "L_a", "energy_cm1": -0.8, "polarization": "sigma"},
  {"label": "L_b", "energy_cm1": 0.0, "polarization": "pi"},
  {"label": "L_c", "energy_cm1": 0.8, "polarization": "sigma"},
  {"label": "L'_d", "energy_cm1": -0.2, "polarization": "pi"}
]
HEREDOC

# === solve block: zeeman_splitting.json ===
python3 /solution/solve_zeeman.py
