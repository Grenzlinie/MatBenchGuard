#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail

# Install numpy (only dependency)
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: calculated_transformation_strain.csv ===
mkdir -p /app/outputs
cd /app/outputs

python3 << 'PYEOF'
import math, csv
import numpy as np

# Lattice constants for each Ti content (from instruction)
compositions = [
    (49.0, 0.3015, 0.2892, 0.4118, 0.4622, 96.6),
    (49.6, 0.3015, 0.2890, 0.4122, 0.4622, 96.8),
    (50.0, 0.3015, 0.2888, 0.4125, 0.4622, 97.0),
    (50.6, 0.3015, 0.2886, 0.4128, 0.4622, 97.2),
    (51.0, 0.3015, 0.2884, 0.4132, 0.4622, 97.4),
]

# Rotation matrix R (from paper)
R = np.array([
    [-1.0, 0.0, 0.0],
    [0.0, 1.0/np.sqrt(2), -1.0/np.sqrt(2)],
    [0.0, -1.0/np.sqrt(2), 1.0/np.sqrt(2)]
])

# Generate 36 points in the fundamental triangle using a regular grid
# Vertices: v0 = [0,0,1] (001), v1 = [0,1,1]/sqrt(2) (011), v2 = [1,1,1]/sqrt(3) (111)
v0 = np.array([0.0, 0.0, 1.0])
v1 = np.array([0.0, 1.0/np.sqrt(2), 1.0/np.sqrt(2)])
v2 = np.array([1.0/np.sqrt(3), 1.0/np.sqrt(3), 1.0/np.sqrt(3)])

n = 8  # gives 36 points
du = 1.0/(n-1)
directions = []
for i in range(n):
    u = i * du
    for j in range(n - i):
        v = j * du
        w = 1.0 - u - v
        xyz = u * v1 + v * v2 + w * v0
        dir_vec = xyz / np.linalg.norm(xyz)
        directions.append(dir_vec)

rows = []
for ti, a0, a, b, c, beta_deg in compositions:
    beta_rad = math.radians(beta_deg)
    sinβ = math.sin(beta_rad)
    cosβ = math.cos(beta_rad)
    c_prime = c * sinβ
    gamma = cosβ / sinβ   # 1/tanβ
    # T' matrix
    Tp = np.array([
        [a / a0, 0.0, c_prime * gamma / (math.sqrt(2) * a0)],
        [0.0, b / (math.sqrt(2) * a0), 0.0],
        [0.0, 0.0, c_prime / (math.sqrt(2) * a0)]
    ])
    T = R @ Tp @ R.T

    epsilons = []
    for x in directions:
        xp = T @ x
        strain = np.linalg.norm(xp) - 1.0  # |x|=1
        epsilons.append(strain)
    eps_bar = np.mean(epsilons)
    rows.append((ti, eps_bar))

with open('calculated_transformation_strain.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Ti_content', 'epsilon_bar_M'])
    for ti, eb in rows:
        writer.writerow([ti, f'{eb:.6f}'])

PYEOF
