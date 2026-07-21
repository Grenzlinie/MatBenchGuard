#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple ase==3.23.0
mkdir -p /app/outputs

# === solve block: structural_analysis.json ===
cat > /tmp/gen_struct.py << 'PYEOF'
import itertools, json, math, sys, os

output_path = os.path.join(sys.argv[1], 'structural_analysis.json') if len(sys.argv) > 1 else '/app/outputs/structural_analysis.json'

# generate truncated octahedron vertices (24)
verts_set = set()
signs = [(1,1), (1,-1), (-1,1), (-1,-1)]
for p in itertools.permutations([0,1,2]):
    zero_pos = next(i for i,val in enumerate(p) if val==0)
    sign_positions = [i for i in range(3) if i != zero_pos]
    for s1, s2 in signs:
        v = list(p)
        v[sign_positions[0]] *= s1
        v[sign_positions[1]] *= s2
        verts_set.add(tuple(v))
verts = sorted(verts_set)
n = len(verts)
# edges with squared distance 2
edges = []
for i in range(n):
    for j in range(i+1,n):
        if sum((a-b)**2 for a,b in zip(verts[i],verts[j])) == 2:
            edges.append((i,j))
# verify 3-regular
deg = [0]*n
for u,v in edges:
    deg[u]+=1; deg[v]+=1
assert all(d==3 for d in deg)
edge_idx = {e:i for i,e in enumerate(edges)}
# cubane units: 3 shared edge indices + 1 unique index
cubane_units = []
for v in range(n):
    inc = []
    for u in range(n):
        if (u,v) in edges: inc.append(edge_idx[(u,v)])
        elif (v,u) in edges: inc.append(edge_idx[(v,u)])
    assert len(inc)==3
    cubane_units.append(inc + [36+v])
vertex_sharing = [[u,v] for u,v in edges]
# find hexagon (6-cycle)
adj = [[] for _ in range(n)]
for u,v in edges:
    adj[u].append(v); adj[v].append(u)
def find_cycle(start):
    path = [start]
    def dfs(cur):
        if len(path)==6:
            return start in adj[cur]
        for nxt in adj[cur]:
            if nxt not in path:
                path.append(nxt)
                if dfs(nxt): return True
                path.pop()
        return False
    if dfs(start): return path
    return None
hexagon = None
for i in range(n):
    p = find_cycle(i)
    if p:
        hexagon = p
        break
bridged = [36+v for v in hexagon]
data = {
 'cubane_units': cubane_units,
 'vertex_sharing_connections': vertex_sharing,
 'vertex_configuration': '(4,6,6)',
 'sodalite_topology': True,
 'hexagonal_wheel': {
     'center_ion': 'CO3',
     'coordination_mode': 'μ6:η1:η1:η1:η1:η1:η1',
     'bridged_er_atoms': bridged
 }
}
with open(output_path, 'w') as f:
    json.dump(data, f, indent=2)
PYEOF
python3 /tmp/gen_struct.py "$OUTDIR"
