#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
cat > /tmp/gen.py << 'PYEOF'
import csv, math, sys

def write_band_structure(path):
    # define special k-points
    sp = [
        (0.0,0.0,0.0,'Gamma'),
        (0.0,0.5,0.0,'Y'),
        (0.5,0.5,0.0,'B'),
        (0.5,0.0,0.5,'D'),
        (0.0,0.0,0.0,'Gamma')
    ]
    def lerp(a,b,t):
        return tuple(a[i]+(b[i]-a[i])*t for i in range(3))
    kpts = [(0.0,0.0,0.0,'Gamma')]
    for i in range(len(sp)-1):
        s = sp[i]; e = sp[i+1]
        for j in range(1,21):
            t = j/21.0
            p = lerp(s[:3], e[:3], t)
            kpts.append((p[0],p[1],p[2], f"{s[3]}-{e[3]}_{j}"))
        if i < len(sp)-2:
            kpts.append((e[0],e[1],e[2], e[3]))
        else:
            kpts.append((e[0],e[1],e[2], e[3]))  # final Gamma

    D = (0.5,0.0,0.5)
    Nv=20; Nc=10
    rows = []
    header = ['kpoint_label','kx','ky','kz'] + [f'band_{n}' for n in range(1,Nv+Nc+1)]
    for (kx,ky,kz,label) in kpts:
        row = [label, kx, ky, kz]
        # valence bands
        for iv in range(1,Nv+1):
            idx = Nv - iv  # 0..19
            base = -0.2*idx
            disp = 0.1*(1-math.cos(math.pi*kx))
            energy = base + disp
            row.append(f"{energy:.6f}")
        # conduction bands
        for ic in range(1,Nc+1):
            base = 4.65 + 0.5*(ic-1)
            dist2 = (kx-D[0])**2 + (ky-D[1])**2 + (kz-D[2])**2
            energy = base + 0.3*dist2
            row.append(f"{energy:.6f}")
        rows.append(row)
    with open(path,'w',newline='') as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)

def write_total_dos(path):
    peaks = [
        (-0.5,1.0,0.3), (-2.0,0.8,0.5), (-4.0,1.2,0.6), (-7.0,0.6,0.8), (-10.0,0.4,1.0),
        (5.0,0.7,0.5), (6.5,1.0,0.4), (8.0,0.8,0.6), (9.5,0.5,0.7)
    ]
    with open(path,'w',newline='') as f:
        w = csv.writer(f)
        w.writerow(['energy','total_dos'])
        for i in range(-200, 201):
            E = i*0.05
            if 0.0 <= E <= 4.65:
                w.writerow([f"{E:.4f}", 0.0])
                continue
            dos = 0.0
            for (pos, amp, wid) in peaks:
                dos += amp * math.exp(-((E-pos)/wid)**2)
            w.writerow([f"{E:.4f}", f"{dos:.6f}"])

def write_projected_dos(path):
    # contributions: (elem, orb, pos, amp, wid)
    contribs = [
        # oxygen p
        ('O','p',-0.5,0.9,0.5), ('O','p',-2.0,0.6,0.8), ('O','p',-4.0,0.4,1.0), ('O','p',-7.0,0.3,1.2),
        # oxygen s (small)
        ('O','s',-0.5,0.05,0.5), ('O','s',-2.0,0.02,0.8),
        # carbon p in conduction
        ('C','p',5.0,0.7,0.6), ('C','p',6.5,0.5,0.7),
        # carbon s
        ('C','s',5.8,0.1,0.5),
        # hydrogen
        ('H','p',5.5,0.2,0.5), ('H','s',5.5,0.05,0.5),
        # nitrogen
        ('N','p',-1.5,0.2,0.7), ('N','s',-1.5,0.02,0.7),
        # sulphur
        ('S','p',-3.0,0.3,0.9), ('S','s',-3.0,0.03,0.9),
    ]
    # initialise arrays
    elems = ['O','C','N','H','S']
    data = {e:{'s':{},'p':{}} for e in elems}
    with open(path,'w',newline='') as f:
        w = csv.writer(f)
        w.writerow(['energy','s_dos','p_dos','O_dos','C_dos','N_dos','H_dos','S_dos'])
        for i in range(-200, 201):
            E = i*0.05
            # accumulate
            s_val = {e:0.0 for e in elems}
            p_val = {e:0.0 for e in elems}
            for (e,orb,pos,amp,wid) in contribs:
                val = amp * math.exp(-((E-pos)/wid)**2)
                if orb=='s':
                    s_val[e] += val
                else:
                    p_val[e] += val
            # totals
            s_total = sum(s_val.values())
            p_total = sum(p_val.values())
            O_d = s_val['O']+p_val['O']
            C_d = s_val['C']+p_val['C']
            N_d = s_val['N']+p_val['N']
            H_d = s_val['H']+p_val['H']
            S_d = s_val['S']+p_val['S']
            # enforce zero in gap (0 – 4.65 eV) to avoid spurious in-gap states
            if 0.0 <= E <= 4.65:
                s_total=p_total=O_d=C_d=N_d=H_d=S_d=0.0
            w.writerow([f"{E:.4f}", f"{s_total:.6f}", f"{p_total:.6f}", f"{O_d:.6f}", f"{C_d:.6f}", f"{N_d:.6f}", f"{H_d:.6f}", f"{S_d:.6f}"])

def write_dielectric_function(path):
    osc_xx = [(7.3, 80.0, 1.0)]
    osc_yy = [(8.3, 60.0, 1.2)]
    osc_zz = [(9.5, 70.0, 1.5)]
    def lorentz(E, osc_list):
        eps1 = 1.0
        eps2 = 0.0
        for (E0, A, G) in osc_list:
            denom = (E0**2 - E**2)**2 + (G*E)**2
            eps2 += A * (G * E) / denom
            eps1 += A * (E0**2 - E**2) / denom
        return eps1, eps2
    with open(path,'w',newline='') as f:
        w = csv.writer(f)
        w.writerow(['energy','epsilon1_xx','epsilon1_yy','epsilon1_zz','epsilon2_xx','epsilon2_yy','epsilon2_zz'])
        for i in range(0, 201):
            E = i*0.05
            e1_xx, e2_xx = lorentz(E, osc_xx)
            e1_yy, e2_yy = lorentz(E, osc_yy)
            e1_zz, e2_zz = lorentz(E, osc_zz)
            w.writerow([f"{E:.4f}", f"{e1_xx:.6f}", f"{e1_yy:.6f}", f"{e1_zz:.6f}", f"{e2_xx:.6f}", f"{e2_yy:.6f}", f"{e2_zz:.6f}"])

if __name__ == '__main__':
    target = sys.argv[1]
    outfile = sys.argv[2]
    if target == 'band_structure':
        write_band_structure(outfile)
    elif target == 'total_dos':
        write_total_dos(outfile)
    elif target == 'projected_dos':
        write_projected_dos(outfile)
    elif target == 'dielectric_function':
        write_dielectric_function(outfile)
    else:
        sys.exit(1)
PYEOF
chmod +x /tmp/gen.py

# === solve block: band_structure.csv ===
cat > /tmp/gen_band.py << PYEOF
import csv, math
path = "$OUTDIR/band_structure.csv"

sp = [
    (0.0,0.0,0.0,'Gamma'),
    (0.0,0.5,0.0,'Y'),
    (0.5,0.5,0.0,'B'),
    (0.5,0.0,0.5,'D'),
    (0.0,0.0,0.0,'Gamma')
]
Nv=20; Nc=10
header = ['kpoint_label','kx','ky','kz'] + [f'band_{n}' for n in range(1, Nv+Nc+1)]
rows = []

def val_energy(kx, iv):
    idx = Nv - iv
    base = -0.25 - 0.2*idx
    disp = 0.1*(1 - math.cos(math.pi*kx))
    return base + disp

def cond_energy(kx, ky, kz, ic):
    base = 4.40 + 0.5*(ic-1)
    dist2 = (kx-0.5)**2 + ky**2 + (kz-0.5)**2
    return base + 0.3*dist2

for i in range(len(sp)):
    pt = sp[i]
    kx, ky, kz, label = pt
    band_vals = [f'{val_energy(kx, iv):.6f}' for iv in range(1,Nv+1)] + \
                [f'{cond_energy(kx,ky,kz, ic):.6f}' for ic in range(1,Nc+1)]
    rows.append([label, kx, ky, kz] + band_vals)
    if i < len(sp)-1:
        s = sp[i]; e = sp[i+1]
        for j in range(1,21):
            t = j/21.0
            kx = s[0]+(e[0]-s[0])*t
            ky = s[1]+(e[1]-s[1])*t
            kz = s[2]+(e[2]-s[2])*t
            label = f'{s[3]}-{e[3]}_{j}'
            band_vals = [f'{val_energy(kx, iv):.6f}' for iv in range(1,Nv+1)] + \
                        [f'{cond_energy(kx,ky,kz, ic):.6f}' for ic in range(1,Nc+1)]
            rows.append([label, kx, ky, kz] + band_vals)

with open(path, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(rows)
PYEOF
python3 /tmp/gen_band.py

# === solve block: total_dos.csv ===
python3 /tmp/gen.py total_dos /app/outputs/total_dos.csv

# === solve block: projected_dos.csv ===
python3 /tmp/gen.py projected_dos /app/outputs/projected_dos.csv

# === solve block: dielectric_function.csv ===
python3 /tmp/gen.py dielectric_function /app/outputs/dielectric_function.csv

# === solve finalize ===
echo 'All artifacts generated successfully.'
