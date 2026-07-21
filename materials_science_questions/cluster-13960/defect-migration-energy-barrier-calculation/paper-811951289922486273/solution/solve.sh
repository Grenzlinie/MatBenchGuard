#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: transition_states.json ===
python3 <<'PYEOF' > $OUTDIR/transition_states.json
import numpy as np
import json
import heapq
import sys

nx, ny, nz = 20, 40, 20
dx = 0.25
Lx, Ly, Lz = nx*dx, ny*dx, nz*dx

NX, NY, NZ = 3*nx, 3*ny, 3*nz

xs = np.arange(NX)*dx
ys = np.arange(NY)*dx
zs = np.arange(NZ)*dx
X, Y, Z = np.meshgrid(xs, ys, zs, indexing='ij')
E = -np.cos(2*np.pi*X/Lx) - np.cos(2*np.pi*Y/Ly) - np.cos(2*np.pi*Z/Lz)
E_flat = E.ravel()
indices = np.arange(NX*NY*NZ)
ix, iy, iz = np.unravel_index(indices, (NX, NY, NZ))

cent_ix, cent_iy, cent_iz = nx, ny, nz
cent_flat = np.ravel_multi_index((cent_ix, cent_iy, cent_iz), (NX, NY, NZ))

neighbors = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]

def neighbour_flat(i,j,k,di,dj,dk):
    ni = i+di; nj = j+dj; nk = k+dk
    if 0 <= ni < NX and 0 <= nj < NY and 0 <= nk < NZ:
        return np.ravel_multi_index((ni, nj, nk), (NX, NY, NZ))
    return None

target_offsets = [
    (1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)
]
target_flat_to_dir = {}
for di, dj, dk in target_offsets:
    ti = cent_ix + di*nx; tj = cent_iy + dj*ny; tk = cent_iz + dk*nz
    target_flat = np.ravel_multi_index((ti, tj, tk), (NX, NY, NZ))
    dir_sign = (abs(di), abs(dj), abs(dk))
    target_flat_to_dir[target_flat] = dir_sign

wet = np.zeros(NX*NY*NZ, dtype=bool)
wet[cent_flat] = True

unique_energies = np.unique(E_flat)
unique_energies.sort()

recorded_dirs = set()
ts_list = []

for level in unique_energies:
    changed = True
    while changed:
        changed = False
        wet_inds = np.where(wet)[0]
        for u in wet_inds:
            ci, cj, ck = ix[u], iy[u], iz[u]
            for di, dj, dk in neighbors:
                v = neighbour_flat(ci, cj, ck, di, dj, dk)
                if v is not None and not wet[v] and E_flat[v] <= level:
                    wet[v] = True
                    changed = True

    for target_flat, dir_sig in target_flat_to_dir.items():
        if not wet[target_flat] or dir_sig in recorded_dirs:
            continue
        Ntot = NX*NY*NZ
        dist = np.full(Ntot, np.inf)
        parent = np.full(Ntot, -1, dtype=np.int64)
        visited = np.zeros(Ntot, dtype=bool)
        dist[cent_flat] = E_flat[cent_flat]
        heap = [(dist[cent_flat], int(cent_flat))]
        target_reached = False
        while heap:
            max_val, u = heapq.heappop(heap)
            if visited[u]:
                continue
            visited[u] = True
            if u == target_flat:
                target_reached = True
                break
            ci, cj, ck = ix[u], iy[u], iz[u]
            for di, dj, dk in neighbors:
                v = neighbour_flat(ci, cj, ck, di, dj, dk)
                if v is not None and wet[v]:
                    new_max = max(max_val, E_flat[v])
                    if new_max < dist[v]:
                        dist[v] = new_max
                        parent[v] = u
                        heapq.heappush(heap, (new_max, v))
        if not target_reached:
            continue
        path = []
        cur = int(target_flat)
        while cur != -1:
            path.append(cur)
            cur = parent[cur]
        bottleneck_flat = max(path, key=lambda idx: E_flat[idx])
        bottleneck_e = float(E_flat[bottleneck_flat])
        bi, bj, bk = ix[bottleneck_flat], iy[bottleneck_flat], iz[bottleneck_flat]
        x_folded = (bi * dx) % Lx
        y_folded = (bj * dx) % Ly
        z_folded = (bk * dx) % Lz
        ts_list.append({
            "index": len(ts_list) + 1,
            "energy": bottleneck_e,
            "coordinates": [x_folded, y_folded, z_folded]
        })
        recorded_dirs.add(dir_sig)

    if len(recorded_dirs) >= 3:
        break

json.dump(ts_list, sys.stdout, indent=2)
PYEOF
