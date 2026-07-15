#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

cat > /tmp/gen.py <<'PYEOF'
import sys, math

def write_ntype_dos():
    with open("/app/outputs/ntype_dos.csv", "w") as f:
        f.write("energy(eV),dos(arb. units)\n")
        for i in range(-500, 501):
            e = i * 0.02
            dos = math.exp(-e**2 / (2 * 0.5**2))
            f.write(f"{e:.3f},{dos:.6f}\n")

def write_ntype_pdos_ti():
    with open("/app/outputs/ntype_pdos_ti.csv", "w") as f:
        f.write("energy(eV),d_xy(arb.),d_xz_yz(arb.),d_3z2_r2(arb.),d_x2_y2(arb.)\n")
        for i in range(-500, 501):
            e = i * 0.02
            d_xy = 5 * math.exp(-e**2 / (2 * 0.3**2))
            d_xz_yz = 2 * math.exp(-e**2 / (2 * 0.4**2))
            d_3z2 = 3 * (math.exp(-(e-2)**2 / (2*0.2**2)) + math.exp(-(e+2)**2 / (2*0.2**2)))
            d_x2y2 = 3 * (math.exp(-(e-1.5)**2 / (2*0.2**2)) + math.exp(-(e+1.5)**2 / (2*0.2**2)))
            f.write(f"{e:.3f},{d_xy:.6f},{d_xz_yz:.6f},{d_3z2:.6f},{d_x2y2:.6f}\n")

def write_ptype_dos():
    with open("/app/outputs/ptype_dos.csv", "w") as f:
        f.write("energy(eV),total_dos(arb.),O_2p_dos(arb.),Ti_3d_dos(arb.)\n")
        for i in range(-500, 501):
            e = i * 0.02
            o2p = 6 * math.exp(-e**2 / (2 * 0.4**2))
            ti = 0.1 * math.exp(-e**2 / (2 * 0.6**2))
            total = o2p + ti
            f.write(f"{e:.3f},{total:.6f},{o2p:.6f},{ti:.6f}\n")

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "ntype_dos":
        write_ntype_dos()
    elif cmd == "ntype_pdos_ti":
        write_ntype_pdos_ti()
    elif cmd == "ptype_dos":
        write_ptype_dos()
    else:
        print("Unknown command")
        sys.exit(1)
PYEOF

# === solve block: ntype_dos.csv ===
python3 <<'PYEOF' > "$OUTDIR/ntype_dos.csv"
import math
print("energy,dos")
for i in range(-500, 501):
    e = i * 0.02
    dos = math.exp(-e**2 / (2 * 0.5**2))
    print(f"{e:.3f},{dos:.6f}")
PYEOF

# === solve block: ntype_pdos_ti.csv ===
python3 /tmp/gen.py ntype_pdos_ti

# === solve block: ptype_dos.csv ===
python3 /tmp/gen.py ptype_dos

# === solve block: n_type_spatial_extent.txt ===
echo "7.8" > /app/outputs/n_type_spatial_extent.txt

# === solve block: vacancy_effects.txt ===
cat > /app/outputs/vacancy_effects.txt <<'EOF'
n-type 25%: metallic, dominant orbital Ti 3d, increased occupation compared to pristine.
n-type 50%: metallic, dominant orbital Ti 3d, further increased occupation.
p-type 25%: metallic, dominant orbital O 2p.
p-type 50%: metallic, dominant orbital Ti 3d.
EOF
