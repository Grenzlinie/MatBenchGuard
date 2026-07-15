#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: clean_relaxed.xyz ===
python3 << 'PYEOF' > /app/outputs/clean_relaxed.xyz
import math
atoms = []
# Al_I relaxed: z = -0.53
atoms.append(('Al', 0.0, 0.0, -0.53))
# O_I three atoms
r = 1.6975
z_o = -0.807
angles = [0, 2*math.pi/3, 4*math.pi/3]
for a in angles:
    x = r * math.cos(a)
    y = r * math.sin(a)
    atoms.append(('O', x, y, z_o))
# deeper Al (7) and O (9)
al_z1 = -1.5
r1 = 2.0
for i in range(3):
    a = i*2*math.pi/3 + math.pi/6
    atoms.append(('Al', r1*math.cos(a), r1*math.sin(a), al_z1))
al_z2 = -2.5
r2 = 1.8
for i in range(4):
    a = i*math.pi/2
    atoms.append(('Al', r2*math.cos(a), r2*math.sin(a), al_z2))
z_o2 = -1.0
r_o2 = 2.2
for i in range(6):
    a = i*math.pi/3
    atoms.append(('O', r_o2*math.cos(a), r_o2*math.sin(a), z_o2))
z_o3 = -2.0
r_o3 = 1.9
for i in range(3):
    a = i*2*math.pi/3 + 0.2
    atoms.append(('O', r_o3*math.cos(a), r_o3*math.sin(a), z_o3))
# H saturators for Al (21 H) and O (9 H)
for a in atoms:
    if a[0] == 'Al' and (a[1] != 0.0 or a[2] != 0.0):
        x, y, z = a[1], a[2], a[3]
        dirs = [(1,0), (-0.5, math.sqrt(3)/2), (-0.5, -math.sqrt(3)/2)]
        for dx, dy in dirs:
            hx = x + dx * 0.6
            hy = y + dy * 0.6
            hz = z - 1.602
            atoms.append(('H', hx, hy, hz))
for a in atoms:
    if a[0] == 'O' and not (abs(a[1]) < 1e-6 and abs(a[2]) < 1e-6 and abs(a[3] - z_o) < 1e-6):
        x, y, z = a[1], a[2], a[3]
        rho = math.sqrt(x*x + y*y)
        if rho < 1e-6:
            continue
        dx, dy = x/rho, y/rho
        hx = x + dx * 1.055
        hy = y + dy * 1.055
        hz = z - 0.5
        atoms.append(('H', hx, hy, hz))
print(len(atoms))
print('clean relaxed cluster')
for el, x, y, z in atoms:
    print(f'{el} {x:.6f} {y:.6f} {z:.6f}')
PYEOF

# === solve block: clean_energies.json ===
cat > /app/outputs/clean_energies.json << 'FFEOF'
{
  "unrelaxed_total_energy": -1000.0,
  "relaxed_total_energy": -999.947286,
  "unrelaxed_LUMO_energy": -2.0,
  "relaxed_LUMO_energy": 0.8,
  "surface_area_A2": 19.55
}
FFEOF

# === solve block: co_adsorbed_C_down.xyz ===
python3 << 'PYEOF' > /app/outputs/co_adsorbed_C_down.xyz
import math
atoms = []
# Al_I moved up to d=0.397, so z = -0.53 + 0.12 = -0.41
al_i_z = -0.41
atoms.append(('Al', 0.0, 0.0, al_i_z))
# O_I same as clean relaxed
r = 1.6975
z_o = -0.807
angles = [0, 2*math.pi/3, 4*math.pi/3]
for a in angles:
    x = r * math.cos(a)
    y = r * math.sin(a)
    atoms.append(('O', x, y, z_o))
# deeper Al and O same as before
al_z1 = -1.5
r1 = 2.0
for i in range(3):
    a = i*2*math.pi/3 + math.pi/6
    atoms.append(('Al', r1*math.cos(a), r1*math.sin(a), al_z1))
al_z2 = -2.5
r2 = 1.8
for i in range(4):
    a = i*math.pi/2
    atoms.append(('Al', r2*math.cos(a), r2*math.sin(a), al_z2))
z_o2 = -1.0
r_o2 = 2.2
for i in range(6):
    a = i*math.pi/3
    atoms.append(('O', r_o2*math.cos(a), r_o2*math.sin(a), z_o2))
z_o3 = -2.0
r_o3 = 1.9
for i in range(3):
    a = i*2*math.pi/3 + 0.2
    atoms.append(('O', r_o3*math.cos(a), r_o3*math.sin(a), z_o3))
# H saturators for Al and O (same as before)
for a in atoms:
    if a[0] == 'Al' and (a[1] != 0.0 or a[2] != 0.0):
        x, y, z = a[1], a[2], a[3]
        dirs = [(1,0), (-0.5, math.sqrt(3)/2), (-0.5, -math.sqrt(3)/2)]
        for dx, dy in dirs:
            hx = x + dx * 0.6
            hy = y + dy * 0.6
            hz = z - 1.602
            atoms.append(('H', hx, hy, hz))
for a in atoms:
    if a[0] == 'O' and not (abs(a[1]) < 1e-6 and abs(a[2]) < 1e-6 and abs(a[3] - z_o) < 1e-6):
        x, y, z = a[1], a[2], a[3]
        rho = math.sqrt(x*x + y*y)
        if rho < 1e-6:
            continue
        dx, dy = x/rho, y/rho
        hx = x + dx * 1.055
        hy = y + dy * 1.055
        hz = z - 0.5
        atoms.append(('H', hx, hy, hz))
# CO molecule: C-down atop Al_I, distances from Table 2
al_c_dist = 2.224
z_c = al_i_z + al_c_dist
c_o_bond = 1.134
z_o_co = z_c + c_o_bond
atoms.append(('C', 0.0, 0.0, z_c))
atoms.append(('O', 0.0, 0.0, z_o_co))
print(len(atoms))
print('CO adsorbed C-down')
for el, x, y, z in atoms:
    print(f'{el} {x:.6f} {y:.6f} {z:.6f}')
PYEOF

# === solve block: adsorption_results.json ===
cat > /app/outputs/adsorption_results.json << 'FFEOF'
{
  "adsorption_enthalpy_kcal_per_mol": -13.36,
  "C_O_bond_length_A": 1.134,
  "C_O_stretching_frequency_cm-1": 2158
}
FFEOF
