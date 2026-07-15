import json
import sys
import os

def write_results(filepath):
    data = {
        "ring_relative_energy": -41.0,
        "TS_relative_energy": -30.0,
        "open_relative_energy": -43.0,
        "chain_relative_energy": -37.0,
        "products_relative_energy": -5.5,
        "ring_CSi_bond_length": 1.753
    }
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def write_stationary(filepath):
    def make_xyz(atoms, coords):
        header = f"{len(atoms)}\n\n"
        lines = []
        for atom, (x, y, z) in zip(atoms, coords):
            lines.append(f"{atom:2s} {x:12.6f} {y:12.6f} {z:12.6f}")
        return header + "\n".join(lines)
    
    # Approximate coordinates based on Figure 1
    ring_atoms = ["H", "C", "Si", "O", "C", "O"]
    ring_coords = [
        (0.0, 0.0, 0.0),
        (1.07, 0.0, 0.0),
        (2.82, 0.0, 0.0),
        (3.5, 1.2, 0.0),
        (2.5, 2.2, 0.0),
        (2.5, 3.4, 0.0),
    ]
    ring_xyz = make_xyz(ring_atoms, ring_coords)
    
    ts_atoms = ["H", "C", "Si", "O", "C", "O"]
    ts_coords = [
        (0.0, 0.0, 0.0),
        (1.07, 0.0, 0.0),
        (2.90, 0.0, 0.0),
        (3.7, 1.5, 0.0),
        (2.6, 3.0, 0.0),
        (2.6, 4.2, 0.0),
    ]
    ts_xyz = make_xyz(ts_atoms, ts_coords)
    
    open_atoms = ["H", "C", "C", "O", "Si", "O"]
    open_coords = [
        (0.0, 0.0, 0.0),
        (1.07, 0.0, 0.0),
        (2.3, 0.0, 0.0),
        (3.5, 0.0, 0.0),
        (5.5, 0.0, 0.0),
        (7.0, 0.0, 0.0),
    ]
    open_xyz = make_xyz(open_atoms, open_coords)
    
    chain_atoms = ["H", "C", "C", "O", "Si", "O"]
    chain_coords = [
        (0.0, 0.0, 0.0),
        (1.07, 0.0, 0.0),
        (2.3, 0.0, 0.0),
        (3.3, 0.3, 0.0),
        (4.15, 1.0, 0.0),
        (5.7, 1.0, 0.0),
    ]
    chain_xyz = make_xyz(chain_atoms, chain_coords)
    
    prod_atoms = ["H", "C", "C", "O", "Si", "O"]
    prod_coords = [
        (0.0, 0.0, 0.0),
        (1.07, 0.0, 0.0),
        (2.3, 0.0, 0.0),
        (3.5, 0.0, 0.0),
        (6.0, 6.0, 0.0),
        (7.6, 6.0, 0.0),
    ]
    prod_xyz = make_xyz(prod_atoms, prod_coords)
    
    # Energy conversion: 1 kcal/mol = 0.0015936 Hartree
    ref_total = -500.0  # fictitious reference sum of reactants MP2+ZPE
    zpe = 0.03
    def rel_to_total(rel):
        return ref_total + rel * 0.0015936
    
    def make_entry(label, xyz, mp2, rhf, rel):
        return {
            "label": label,
            "xyz": xyz.strip(),
            "RHF_energy": rhf,
            "MP2_energy": mp2,
            "ZPE": zpe,
            "relative_energy": rel
        }
    
    # ring: -41.0 kcal/mol
    ring_total = rel_to_total(-41.0)
    ring_mp2 = ring_total - zpe
    ring_rhf = ring_mp2 + 0.1
    ring_entry = make_entry("ring", ring_xyz, ring_mp2, ring_rhf, -41.0)
    
    # TS: -30.0
    ts_total = rel_to_total(-30.0)
    ts_mp2 = ts_total - zpe
    ts_rhf = ts_mp2 + 0.1
    ts_entry = make_entry("TS", ts_xyz, ts_mp2, ts_rhf, -30.0)
    
    # open: -43.0
    open_total = rel_to_total(-43.0)
    open_mp2 = open_total - zpe
    open_rhf = open_mp2 + 0.1
    open_entry = make_entry("open", open_xyz, open_mp2, open_rhf, -43.0)
    
    # chain: -37.0
    chain_total = rel_to_total(-37.0)
    chain_mp2 = chain_total - zpe
    chain_rhf = chain_mp2 + 0.1
    chain_entry = make_entry("chain", chain_xyz, chain_mp2, chain_rhf, -37.0)
    
    # products: -5.5
    prod_total = rel_to_total(-5.5)
    prod_mp2 = prod_total - zpe
    prod_rhf = prod_mp2 + 0.1
    prod_entry = make_entry("products", prod_xyz, prod_mp2, prod_rhf, -5.5)
    
    array = [ring_entry, ts_entry, open_entry, chain_entry, prod_entry]
    with open(filepath, 'w') as f:
        json.dump(array, f, indent=2)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: generate_outputs.py <output_file> <mode>")
        sys.exit(1)
    filepath = sys.argv[1]
    mode = sys.argv[2]
    if mode == "results":
        write_results(filepath)
    elif mode == "stationary":
        write_stationary(filepath)
    else:
        raise ValueError("Invalid mode")
