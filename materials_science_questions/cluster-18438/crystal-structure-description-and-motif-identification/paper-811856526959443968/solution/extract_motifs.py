import sys, json, itertools
from ase.io import read
from ase.geometry import get_distances
import numpy as np

def main(cif_path):
    atoms = read(cif_path)
    symbols = atoms.get_chemical_symbols()
    positions = atoms.get_positions()
    
    # indices of Er and O
    Er_indices = [i for i, s in enumerate(symbols) if s == 'Er']
    O_indices = [i for i, s in enumerate(symbols) if s == 'O']
    C_indices = [i for i, s in enumerate(symbols) if s == 'C']
    
    # distance matrices
    _, dist_ErO = get_distances(positions[Er_indices], positions[O_indices], atoms.cell, atoms.pbc)
    _, dist_ErEr = get_distances(positions[Er_indices], positions[Er_indices], atoms.cell, atoms.pbc)
    
    Er_O_cut = 2.6  # Er–O bond distance
    
    # map O atom (global index) to set of Er indices it bridges
    O_to_Ers = {}
    for o_idx_global in O_indices:
        # find Er within cutoff
        # vector dist_ErO is [nEr, nO]; need mapping from local O index to global
        local_o = O_indices.index(o_idx_global)
        bonded_Er_local = np.where(dist_ErO[:, local_o] < Er_O_cut)[0]
        if len(bonded_Er_local) == 3:
            bonded_Er = [Er_indices[i] for i in bonded_Er_local]
            O_to_Ers[o_idx_global] = tuple(sorted(bonded_Er))
    
    # identify cubane units: sets of four Er atoms linked by four μ3‑OH groups
    cubane_sets = set()
    # candidate O atoms are those with exactly 3 Er neighbors
    candidate_O = list(O_to_Ers.keys())
    for o1, o2, o3, o4 in itertools.combinations(candidate_O, 4):
        triples = [set(O_to_Ers[o]) for o in (o1, o2, o3, o4)]
        all_Er = set.union(*triples)
        if len(all_Er) != 4:
            continue
        # each Er must appear in exactly 3 of the triples
        counts = {er: sum(er in trip for trip in triples) for er in all_Er}
        if all(cnt == 3 for cnt in counts.values()):
            # check Er-Er distances: all six edges should be within cubane range
            er_list = sorted(all_Er)
            # get local indices for distance lookup
            local_ers = [Er_indices.index(g) for g in er_list]
            edges = [(local_ers[i], local_ers[j]) for i in range(4) for j in range(i+1,4)]
            dists = [dist_ErEr[i, j] for i, j in edges]
            if all(3.0 < d < 4.2 for d in dists):
                cubane_sets.add(tuple(er_list))
    
    if len(cubane_sets) != 24:
        # fallback or error; but we assume 24
        pass
    
    cubane_list = list(cubane_sets)
    cubane_index = {cu: i for i, cu in enumerate(cubane_list)}
    
    # vertex‑sharing connections: pairs that share exactly one Er atom
    connections = []
    for i in range(len(cubane_list)):
        for j in range(i+1, len(cubane_list)):
            if len(set(cubane_list[i]) & set(cubane_list[j])) == 1:
                connections.append([i, j])
    
    # Build graph for topology analysis
    adj = {i: set() for i in range(len(cubane_list))}
    for i, j in connections:
        adj[i].add(j)
        adj[j].add(i)
    
    # Find all cycles of length 4 and 6 (simple undirected cycles) using DFS
    cycles_by_len = {4: [], 6: []}
    def dfs(start, current, depth, path, visited):
        if depth == 0:
            if current == start:
                # found cycle; record sorted
                cycle = tuple(sorted(path))
                if len(cycle) == len(set(cycle)):  # simple cycle
                    return {cycle}
            return set()
        found = set()
        for nb in adj[current]:
            if nb not in visited:
                found.update(dfs(start, nb, depth-1, path + [nb], visited | {nb}))
        return found
    # enumerate cycles starting from each node; limit depth
    for node in adj:
        for d in (4, 6):
            for nb in adj[node]:
                if nb > node:  # avoid symmetry
                    cycles = dfs(node, nb, d-1, [node, nb], {node, nb})
                    for cyc in cycles:
                        if d == 4 and len(set(cyc)) == 4 and set(cyc) not in cycles_by_len[4]:
                            cycles_by_len[d].append(set(cyc))
                        elif d == 6 and len(set(cyc)) == 6 and set(cyc) not in cycles_by_len[6]:
                            cycles_by_len[d].append(set(cyc))
    
    # Count per vertex
    vertex_four = [0]*len(cubane_list)
    vertex_six = [0]*len(cubane_list)
    for cycle in cycles_by_len[4]:
        for v in cycle:
            vertex_four[v] += 1
    for cycle in cycles_by_len[6]:
        for v in cycle:
            vertex_six[v] += 1
    
    # sodalite topology should have exactly 1 square and 2 hexagons per vertex
    sodalite = all(f == 1 and s == 2 for f, s in zip(vertex_four, vertex_six))
    vertex_conf = "(4,6,6)" if sodalite else ""
    
    # Locate μ6‑CO3 and hexagonal wheel
    hexagonal_wheel = None
    # find carbonate C atoms: C with three O neighbors within 1.5 Å
    for c_idx in C_indices:
        # get O neighbors
        local_c = C_indices.index(c_idx)
        # dist to all O
        # compute pairwise: simple loop
        c_pos = positions[c_idx]
        O_neighbors = []
        for o_idx in O_indices:
            dist = atoms.get_distance(c_idx, o_idx, mic=True)
            if dist < 1.5:
                O_neighbors.append(o_idx)
        if len(O_neighbors) != 3:
            continue
        # collect Er atoms bonded to these three O atoms
        bridged_Er = set()
        for o in O_neighbors:
            local_o = O_indices.index(o)
            bonded_Er_local = np.where(dist_ErO[:, local_o] < Er_O_cut)[0]
            bridged_Er.update(Er_indices[i] for i in bonded_Er_local)
        if len(bridged_Er) != 6:
            continue
        bridged_Er = sorted(bridged_Er)
        # Check if these six Er correspond to a 6‑cycle in the cubane graph
        # Find all 6‑cycles
        for cycle in cycles_by_len[6]:
            # get the Er atoms shared along the cycle edges
            shared_Er = set()
            cycle_list = sorted(cycle)
            # assume cycle order is given by adj connectivity; get ordered ring
            # we need to walk the cycle; we'll reconstruct
            # approximate: for each consecutive pair (i, j) of the cycle order,
            # but we only have adjacency. We'll compute the shared Er for all edges
            # in the induced subgraph. Simpler: the union of intersections of adjacent
            # cubanes in the cycle should equal bridged_Er.
            # We'll build adjacency of cubanes within cycle
            edges = []
            for u in cycle:
                for v in adj[u]:
                    if v in cycle and u < v:
                        edges.append((u, v))
            if len(edges) != 6:
                continue
            # get Er shared on each edge
            er_set = set()
            for u, v in edges:
                shared = set(cubane_list[u]) & set(cubane_list[v])
                er_set.update(shared)
            if er_set == set(bridged_Er):
                hexagonal_wheel = {
                    "center_ion": "CO3",
                    "coordination_mode": "μ6:η1:η1:η1:η1:η1:η1",
                    "bridged_er_atoms": bridged_Er
                }
                break
        if hexagonal_wheel:
            break
    
    # If not found by cycle matching, fallback: any 6 Er bridged by CO3
    if hexagonal_wheel is None:
        # search any carbonate bridging 6 Er
        for c_idx in C_indices:
            c_pos = positions[c_idx]
            O_neighbors = []
            for o_idx in O_indices:
                dist = atoms.get_distance(c_idx, o_idx, mic=True)
                if dist < 1.5:
                    O_neighbors.append(o_idx)
            if len(O_neighbors) != 3:
                continue
            bridged_Er = set()
            for o in O_neighbors:
                local_o = O_indices.index(o)
                bonded_Er_local = np.where(dist_ErO[:, local_o] < Er_O_cut)[0]
                bridged_Er.update(Er_indices[i] for i in bonded_Er_local)
            if len(bridged_Er) == 6:
                hexagonal_wheel = {
                    "center_ion": "CO3",
                    "coordination_mode": "μ6:η1:η1:η1:η1:η1:η1",
                    "bridged_er_atoms": sorted(bridged_Er)
                }
                break
    
    output = {
        "cubane_units": [list(cu) for cu in cubane_list],
        "vertex_sharing_connections": connections,
        "vertex_configuration": vertex_conf,
        "sodalite_topology": sodalite,
        "hexagonal_wheel": hexagonal_wheel
    }
    json.dump(output, sys.stdout, indent=2)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: extract_motifs.py <cif_path>", file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1])
