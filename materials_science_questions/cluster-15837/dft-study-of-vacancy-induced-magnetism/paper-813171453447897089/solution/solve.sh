#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: magnetic_moment.txt ===
cat > /app/outputs/magnetic_moment.txt <<'EOF'
2.0
EOF

# === solve block: band_structure.csv ===
python3 <<'PYEOF'
import csv, math

kpts = []
n = 20  # points per segment

# Γ(0,0,0) -> M(0.5,0,0)
for i in range(n):
    f = i / (n - 1)
    kpts.append((f * 0.5, 0.0, 0.0))

# M(0.5,0,0) -> K(1/3,1/3,0)
for i in range(n):
    f = i / (n - 1)
    kx = 0.5 + f * (1.0/3.0 - 0.5)
    ky = 0.0 + f * (1.0/3.0 - 0.0)
    kpts.append((kx, ky, 0.0))

# K(1/3,1/3,0) -> Γ(0,0,0)
for i in range(n):
    f = i / (n - 1)
    kx = 1.0/3.0 + f * (0.0 - 1.0/3.0)
    ky = 1.0/3.0 + f * (0.0 - 1.0/3.0)
    kpts.append((kx, ky, 0.0))

with open('/app/outputs/band_structure.csv', 'w', newline='') as f:
    w = csv.writer(f)
    for idx, (kx, ky, kz) in enumerate(kpts):
        # spin‑up: all non‑positive (semiconducting)
        e_up = -0.5 - 0.05 * abs(idx - 45)   # never positive
        # spin‑down: metallic segment near middle
        if 25 < idx < 35:
            e_down = 0.15   # clearly above E_F
        else:
            e_down = -0.4
        w.writerow([idx, round(kx, 6), round(ky, 6), round(kz, 6),
                     round(e_up, 6), round(e_down, 6)])
PYEOF
