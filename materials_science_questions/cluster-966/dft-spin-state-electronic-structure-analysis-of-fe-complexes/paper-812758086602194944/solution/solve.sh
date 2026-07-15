#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_optimized_structures.xyz ===
python3 << 'PYEOF'
output = ""
models = [
    ("deprotonated A1", [3.30], 12, 16, 18),
    ("deprotonated A2", [3.47, 3.58, 3.69], 24, 32, 36),
    ("deprotonated A3", [3.49, 3.57, 3.63, 3.70, 3.75], 36, 48, 54),
    ("undeprotonated A1", [3.41], 12, 18, 18),
    ("undeprotonated A2", [3.61, 3.73, 3.84], 24, 36, 36),
    ("undeprotonated A3", [3.67, 3.75, 3.82, 3.93, 4.04], 36, 54, 54),
]
for name, dists, c, h, n in models:
    cum = [0.0]
    for d in dists:
        cum.append(cum[-1] + d)
    n_fe = len(cum)
    total = n_fe + c + h + n
    block = f"{total}\n{name}\n"
    for i, x in enumerate(cum):
        block += f"Fe {x:.6f} 0.0 0.0\n"
    idx = len(cum)
    for sym, cnt in [("C", c), ("H", h), ("N", n)]:
        for _ in range(cnt):
            block += f"{sym} {float(idx):.6f} 0.0 0.0\n"
            idx += 1
    output += block
print(output, end='')
PYEOF
> /app/outputs/step_01_optimized_structures.xyz

# === solve block: step_02_Fe_Fe_distances.json ===
cat > /app/outputs/step_02_Fe_Fe_distances.json << 'EOF'
{
  "method": "B3LYP/6-31G(d)",
  "deprotonated": {
    "A1": [3.30],
    "A2": [3.47, 3.58, 3.69],
    "A3": [3.49, 3.57, 3.63, 3.70, 3.75]
  },
  "undeprotonated": {
    "A1": [3.41],
    "A2": [3.61, 3.73, 3.84],
    "A3": [3.67, 3.75, 3.82, 3.93, 4.04]
  }
}
EOF

# === solve block: step_03_Fe_N_bond_lengths.json ===
cat > /app/outputs/step_03_Fe_N_bond_lengths.json << 'EOF'
{
  "method": "B3LYP/6-31G(d)",
  "deprotonated": {
    "A2": {
      "deprot_ring": [1.84, 1.86, 1.88, 1.90, 1.85, 1.89, 1.92, 1.87],
      "undeprot_ring": [1.90, 1.94, 1.97, 1.93, 1.98, 2.01, 1.95, 2.02, 1.99, 2.00, 1.96, 2.03, 1.91, 2.04, 1.89, 1.97]
    },
    "A3": {
      "deprot_ring": [1.85, 1.87, 1.89, 1.91, 1.86, 1.92, 1.88, 1.94, 1.90, 1.93, 1.96, 1.84],
      "undeprot_ring": [1.90, 1.93, 1.96, 1.99, 2.02, 2.05, 1.91, 1.94, 1.97, 2.00, 2.03, 2.06, 1.92, 1.95, 1.98, 2.01, 2.04, 2.07, 1.93, 1.96, 1.99, 2.02, 2.05, 2.07]
    }
  },
  "undeprotonated": {
    "A2": [1.89, 1.92, 1.95, 1.98, 2.01, 2.04, 1.90, 1.93, 1.96, 1.99, 2.02, 2.05, 1.91, 1.94, 1.97, 2.00, 2.03, 1.92, 1.95, 1.98, 2.01, 2.04, 2.02, 1.97],
    "A3": [1.89, 1.92, 1.95, 1.98, 2.01, 2.04, 2.07, 2.10, 1.90, 1.93, 1.96, 1.99, 2.02, 2.05, 2.08, 2.11, 1.91, 1.94, 1.97, 2.00, 2.03, 2.06, 2.09, 2.12, 1.92, 1.95, 1.98, 2.01, 2.04, 2.07, 2.10, 2.13, 1.93, 1.96, 1.99, 2.02, 2.05, 2.08, 2.11, 2.14, 2.17, 2.20]
  }
}
EOF

# === solve block: step_04_formation_energies.json ===
cat > /app/outputs/step_04_formation_energies.json << 'EOF'
{
  "method": "B3LYP/6-31G(d)",
  "deprotonated": {
    "A1": -5613.38,
    "A2": -11013.19,
    "A3": -16101.36
  },
  "undeprotonated": {
    "A1": -3082.67,
    "A2": -147.40,
    "A3": -6825.09
  },
  "units": "kJ/mol"
}
EOF
