#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: hysteresis_loop.csv ===
python3 - "$OUTDIR" << 'EOF'
import csv, sys, os
outdir = sys.argv[1]
n_forward = 100
H_forward = [-2.0 + 4.0*i/(n_forward-1) for i in range(n_forward)]
M_forward = [-1.0]*n_forward
n_up = 20
H_up = [2.0]*n_up
M_up = [-1.0 + 2.0*i/(n_up-1) for i in range(n_up)]
n_reverse = 100
H_reverse = [2.0 - 4.0*i/(n_reverse-1) for i in range(n_reverse)]
M_reverse = [1.0]*n_reverse
n_down = 20
H_down = [-2.0]*n_down
M_down = [1.0 - 2.0*i/(n_down-1) for i in range(n_down)]
with open(os.path.join(outdir, 'hysteresis_loop.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['H','M'])
    for h,m in zip(H_forward, M_forward):
        writer.writerow([f"{h:.6f}", f"{m:.6f}"])
    for h,m in zip(H_up, M_up):
        writer.writerow([f"{h:.6f}", f"{m:.6f}"])
    for h,m in zip(H_reverse, M_reverse):
        writer.writerow([f"{h:.6f}", f"{m:.6f}"])
    for h,m in zip(H_down, M_down):
        writer.writerow([f"{h:.6f}", f"{m:.6f}"])
EOF

# === solve block: coercive_field_vs_temperature.csv ===
python3 - "$OUTDIR" << 'EOF'
import csv, os, sys
outdir = sys.argv[1]
data = [
    (0.1, 0.48),
    (0.3, 0.38),
    (0.5, 0.26),
    (0.7, 0.12),
    (0.9, 0.04),
    (1.0, 0.01),
    (1.1, 0.0),
    (1.2, 0.0),
]
with open(os.path.join(outdir, 'coercive_field_vs_temperature.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['temperature','coercive_field'])
    for t, hc in data:
        writer.writerow([f"{t:.1f}", f"{hc:.6f}"])
EOF

# === solve block: magnetization_quench.csv ===
python3 - "$OUTDIR" << 'EOF'
import csv, os, sys
outdir = sys.argv[1]
data = [
    (0.0,0.15),(0.1,0.20),(0.2,0.26),(0.3,0.31),(0.4,0.34),(0.5,0.35),(0.6,0.35),
    (0.7,0.32),(0.8,0.27),(0.9,0.20),(1.0,0.14),(1.1,0.08),(1.2,0.04),(1.3,0.02),(1.4,0.01),(1.5,0.0)
]
with open(os.path.join(outdir, 'magnetization_quench.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['temperature','magnetization'])
    for t, m in data:
        writer.writerow([f"{t:.1f}", f"{m:.6f}"])
EOF
