#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: dft_results.json ===
cat > "$OUTDIR/dft_results.json" <<'EOF'
{
  "cell_params": {
    "a": 15.93,
    "b": 15.93,
    "c": 3.88
  },
  "bare_C_N_bond_length": 1.17,
  "state_i_energy": -0.285,
  "state_ii_energy": -1.167,
  "state_ii_C_N_bond_length": 1.45,
  "state_iii_energy": -2.945,
  "red_path_iv_energy": -0.013,
  "red_path_v_energy": -3.277,
  "red_path_FS_energy": 0.075,
  "blue_path_vi_energy": 0.981,
  "blue_path_vii_energy": -4.206,
  "blue_path_FS_energy": 0.01
}
EOF
