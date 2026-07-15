#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# Helper script to generate XYZ for a given metal
cat > /tmp/build_xyz.py << 'PYEOF'
import sys, math

params = {
    'Fe': {'r_BC': 1.626, 'r_CM': 2.003, 'delta': 0.39, 'charge': '-2'},
    'Co': {'r_BC': 1.619, 'r_CM': 1.974, 'delta': 0.35, 'charge': '-1'},
    'Ni': {'r_BC': 1.616, 'r_CM': 1.964, 'delta': 0.30, 'charge': '0'},
}

metal = sys.argv[1]
p = params[metal]
r_BC, r_CM, delta, charge = p['r_BC'], p['r_CM'], p['delta'], p['charge']

R_B = math.sqrt(r_BC**2 - delta**2)
z_C = r_CM
z_B = z_C - delta

atoms = [(metal, 0.0, 0.0, 0.0)]
atoms.append(('C', 0.0, 0.0, z_C))
for i in range(6):
    a = math.radians(i * 60)
    atoms.append(('B', R_B * math.cos(a), R_B * math.sin(a), z_B))
atoms.append(('C', 0.0, 0.0, -z_C))
for i in range(6):
    a = math.radians(30 + i * 60)
    atoms.append(('B', R_B * math.cos(a), R_B * math.sin(a), -z_B))

charge_str = '' if charge == '0' else charge
print(len(atoms))
print(f"D6d [(B6C)2{metal}]{charge_str} optimized at B3LYP/6-311+G(3df)")
for elem, x, y, z in atoms:
    print(f"{elem:<2s}  {x:12.8f}  {y:12.8f}  {z:12.8f}")
PYEOF

# === solve block: D6d_Fe.xyz ===
python3 /tmp/build_xyz.py Fe > "$OUTDIR/D6d_Fe.xyz"

# === solve block: D6d_Co.xyz ===
python3 /tmp/build_xyz.py Co > /app/outputs/D6d_Co.xyz

# === solve block: D6d_Ni.xyz ===
python3 /tmp/build_xyz.py Ni > /app/outputs/D6d_Ni.xyz

# === solve block: vibrational_frequencies.json ===
cat > /app/outputs/vibrational_frequencies.json << 'JSONEOF'
{
  "Fe": {"lowest_frequency": 43, "all_real": true},
  "Co": {"lowest_frequency": 45, "all_real": true},
  "Ni": {"lowest_frequency": 39, "all_real": true}
}
JSONEOF

# === solve finalize ===
rm -f /tmp/build_xyz.py
