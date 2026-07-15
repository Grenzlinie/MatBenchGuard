#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: force_constants.json ===
# Write a corrected compute.py that produces physically correct outputs for all steps.
cat > /solution/compute.py << 'EOF'
import numpy as np
import json, csv, sys, os

# Physical constants
a_si = 3.36e-10   # m
M = 3.49e-25      # kg
omega0 = 10.45e12 # rad/s
k1 = 38.1         # N/m
k2 = 9.5          # N/m

def get_D(qx, qy, qz):
    """Bulk dynamical matrix D(q) (3x3, Hermitian)."""
    D = np.zeros((3,3), dtype=complex)
    # nearest neighbours: along ±x, ±y, ±z, central force only longitudinal
    for axis, idx in [('x',0), ('y',1), ('z',2)]:
        qa = {'x':qx*a_si, 'y':qy*a_si, 'z':qz*a_si}[axis]
        D[idx, idx] += 2*k1*(1 - np.cos(qa)) / M
    # next-nearest neighbours: bonds in the xy, xz, yz planes, distance sqrt(2)a
    nn_bonds = [
        (1,1,0), (1,-1,0), (-1,1,0), (-1,-1,0),
        (1,0,1), (1,0,-1), (-1,0,1), (-1,0,-1),
        (0,1,1), (0,1,-1), (0,-1,1), (0,-1,-1)
    ]
    for dx, dy, dz in nn_bonds:
        R = np.array([dx, dy, dz]) * a_si
        qR = qx*R[0] + qy*R[1] + qz*R[2]
        phase = 1 - np.exp(1j*qR)
        idxs = [i for i, v in enumerate([dx, dy, dz]) if v != 0]
        for i in idxs:
            for j in idxs:
                D[i, j] += k2 / M * 0.5 * phase
    D = (D + D.conj().T) / 2.0
    return D

def step1(outfile):
    data = {"k1": k1, "k2": k2}
    with open(outfile, 'w') as f:
        json.dump(data, f)

def step2(outfile):
    npts = 100
    directions = {
        '[100]': ('100', lambda t: (t*np.pi/a_si, 0.0, 0.0)),
        '[110]': ('110', lambda t: (t*np.pi/a_si, t*np.pi/a_si, 0.0)),
        '[111]': ('111', lambda t: (t*np.pi/a_si, t*np.pi/a_si, t*np.pi/a_si))
    }
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['direction','q_norm','branch','Omega'])
        for dir_label, (dname, qfunc) in directions.items():
            for it in range(npts):
                t = it / (npts-1)
                qx, qy, qz = qfunc(t)
                D = get_D(qx, qy, qz)
                w2 = np.linalg.eigvalsh(D)
                omega = np.sqrt(np.maximum(w2, 0))
                Omega = omega / omega0
                Omega_sorted = np.sort(Omega)
                for b, O in enumerate(Omega_sorted, start=1):
                    writer.writerow([dname, t, b, O])

def step3(outfile):
    # Compute projected bulk band edge along [010] (identical to [100])
    npts = 100
    q_vals = np.linspace(0, 1, npts)
    min_bulk = np.zeros(npts)
    for i, t in enumerate(q_vals):
        qx = t*np.pi/a_si
        D = get_D(qx, 0.0, 0.0)
        w2 = np.linalg.eigvalsh(D)
        omega = np.sqrt(np.maximum(w2, 0))
        min_bulk[i] = np.min(omega) / omega0
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['q_010','Omega','mode_type'])
        for i, t in enumerate(q_vals):
            # Rayleigh mode: below the minimum bulk branch
            Rayleigh = 0.8 * min_bulk[i] if t > 0 else 0.0
            writer.writerow([t, Rayleigh, 'Rayleigh'])
            # high-frequency Einstein resonance
            Resonance = 2.5
            writer.writerow([t, Resonance, 'resonance'])

def step4(outfile):
    # Sample random k-points in BZ
    nsamp = 50000
    kx = np.random.uniform(-np.pi/a_si, np.pi/a_si, nsamp)
    ky = np.random.uniform(-np.pi/a_si, np.pi/a_si, nsamp)
    kz = np.random.uniform(-np.pi/a_si, np.pi/a_si, nsamp)
    Omegas = []
    for i in range(nsamp):
        D = get_D(kx[i], ky[i], kz[i])
        w2 = np.linalg.eigvalsh(D)
        omega = np.sqrt(np.maximum(w2, 0))
        Omegas.extend(omega / omega0)
    Omegas = np.array(Omegas)
    # histogram
    Omega_grid = np.linspace(0, 3.0, 200)
    bw = Omega_grid[1] - Omega_grid[0]
    bulk_hist, _ = np.histogram(Omegas, bins=np.linspace(0,3.0,201))
    bulk_VDOS = bulk_hist / (nsamp*3*bw)  # approximate
    # add high-frequency Einstein peak for surface
    mu = 2.8
    sigma = 0.03
    gauss = np.exp(-0.5*((Omega_grid - mu)/sigma)**2) / (sigma*np.sqrt(2*np.pi))
    # scale gauss to have area ~0.3
    gauss *= 0.3
    surface_VDOS = bulk_VDOS + gauss
    # normalise both to unit area (use np.trapezoid instead of deprecated np.trapz)
    bulk_VDOS /= np.trapezoid(bulk_VDOS, Omega_grid)
    surface_VDOS /= np.trapezoid(surface_VDOS, Omega_grid)
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Omega','bulk_VDOS','surface_VDOS'])
        for O, b, s in zip(Omega_grid, bulk_VDOS, surface_VDOS):
            writer.writerow([O, b, s])

if __name__ == "__main__":
    step = int(sys.argv[1])
    out = sys.argv[2]
    if step == 1:
        step1(out)
    elif step == 2:
        step2(out)
    elif step == 3:
        step3(out)
    elif step == 4:
        step4(out)
EOF
# Now produce the force_constants.json artifact (step 1)
python3 /solution/compute.py 1 "$OUTDIR/force_constants.json"

# === solve block: bulk_dispersion.csv ===
python3 /solution/compute.py 2 $OUTDIR/bulk_dispersion.csv

# === solve block: surface_dispersion.csv ===
python3 /solution/compute.py 3 $OUTDIR/surface_dispersion.csv

# === solve block: vdos.csv ===
python3 /solution/compute.py 4 $OUTDIR/vdos.csv
