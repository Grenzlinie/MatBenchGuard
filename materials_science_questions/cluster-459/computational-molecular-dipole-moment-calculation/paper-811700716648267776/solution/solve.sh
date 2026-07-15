#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: spectroscopic_constants.json ===
cat > "$OUTDIR/spectroscopic_constants.json" <<'FFEOF'
{
  "R_e": 1.658,
  "omega_e": 1678.0,
  "B_e": 6.389,
  "alpha_e": 0.18,
  "D_e": 1.9909
}
FFEOF

# === solve block: pdms.json ===
cat > "$OUTDIR/pdms.json" <<'FFEOF'
[
  {"v": 0, "energy": 826, "B_v": 6.249, "pdm": 3.202},
  {"v": 1, "energy": 2429, "B_v": 6.060, "pdm": 3.113},
  {"v": 2, "energy": 3963, "B_v": 5.865, "pdm": 3.008},
  {"v": 3, "energy": 5426, "B_v": 5.663, "pdm": 2.886},
  {"v": 4, "energy": 6816, "B_v": 5.452, "pdm": 2.748},
  {"v": 5, "energy": 8129, "B_v": 5.231, "pdm": 2.594},
  {"v": 6, "energy": 9362, "B_v": 4.998, "pdm": 2.425},
  {"v": 7, "energy": 10511, "B_v": 4.750, "pdm": 2.244},
  {"v": 8, "energy": 11571, "B_v": 4.485, "pdm": 2.052},
  {"v": 9, "energy": 12536, "B_v": 4.198, "pdm": 1.852},
  {"v": 10, "energy": 13401, "B_v": 3.885, "pdm": 1.649},
  {"v": 11, "energy": 14158, "B_v": 3.537, "pdm": 1.446},
  {"v": 12, "energy": 14800, "B_v": 3.145, "pdm": 1.249},
  {"v": 13, "energy": 15315, "B_v": 2.690, "pdm": 1.068},
  {"v": 14, "energy": 15925, "B_v": 1.498, "pdm": 0.870},
  {"v": 15, "energy": 15925, "B_v": 1.498, "pdm": 0.870}
]
FFEOF

# === solve block: tdms.json ===
cat > "$OUTDIR/tdms.json" <<'FFEOF'
[
  {"v": 1, "v_prime": 0, "tdm": 0.16},
  {"v": 2, "v_prime": 0, "tdm": 0.00},
  {"v": 2, "v_prime": 1, "tdm": 0.25},
  {"v": 3, "v_prime": 0, "tdm": 0.00},
  {"v": 3, "v_prime": 1, "tdm": 0.00},
  {"v": 3, "v_prime": 2, "tdm": 0.32},
  {"v": 4, "v_prime": 0, "tdm": 0.00},
  {"v": 4, "v_prime": 1, "tdm": 0.00},
  {"v": 4, "v_prime": 2, "tdm": 0.00},
  {"v": 4, "v_prime": 3, "tdm": 0.42}
]
FFEOF

# === solve block: sers.json ===
cat > "$OUTDIR/sers.json" <<'FFEOF'
[
  {"v": 1, "ser": 32.4},
  {"v": 2, "ser": 69.9},
  {"v": 3, "ser": 101.7},
  {"v": 4, "ser": 143.7}
]
FFEOF
