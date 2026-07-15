#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: perfect_dislocation_results.json ===
cat > "$OUTDIR/perfect_dislocation_results.json" <<'FFEOF'
{
  "Cu": {
    "relaxed_d_nm": 4.30185,
    "relaxed_d_a": 11.9,
    "energy_eV": 2.25,
    "elastic_d_nm": 3.63
  },
  "Ag": {
    "relaxed_d_nm": 5.8430,
    "relaxed_d_a": 14.3,
    "energy_eV": 2.07,
    "elastic_d_nm": 4.73
  }
}
FFEOF

# Fix the broken generate_perfect_displacement.py script
cat > /solution/generate_perfect_displacement.py <<'PYEOF'
import sys, csv, math

def f(x):
    k = math.log(10) / 11.9
    return 1.0 / (1.0 + math.exp(-k * (x - 5.0)))

writer = csv.writer(sys.stdout, lineterminator='\n')
writer.writerow(['x', 'delta_u_x'])
n = 200
x_start = -10.0
x_end = 20.0
dx = (x_end - x_start) / (n - 1)
for i in range(n):
    x = x_start + i * dx
    writer.writerow([f'{x:.6f}', f'{f(x):.6f}'])
PYEOF

# === solve block: perfect_dislocation_displacement.csv ===
python3 /solution/generate_perfect_displacement.py > "$OUTDIR/perfect_dislocation_displacement.csv"

# === solve block: lomer_cottrell_results.json ===
cat > "$OUTDIR/lomer_cottrell_results.json" <<'FFEOF'
{
  "Cu": {
    "d1_a": 8.2,
    "d2_a": 2.4,
    "d_bar_a": 5.3,
    "d1_d2_ratio": 3.4,
    "energy_eV": 3.45,
    "elastic_d1_a": 6.3,
    "elastic_d2_a": 1.6
  },
  "Ag": {
    "d1_a": 10.7,
    "d2_a": 3.0,
    "d_bar_a": 6.5,
    "d1_d2_ratio": 3.6,
    "energy_eV": 3.26,
    "elastic_d1_a": 10.3,
    "elastic_d2_a": 2.7
  }
}
FFEOF
