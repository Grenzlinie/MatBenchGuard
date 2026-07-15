#!/usr/bin/env python3
"""Generate synthetic but plausible reference artifacts for rocksalt GeSn."""
import json, math, sys

def structural_params():
    return {
        "lattice_constant_A": 6.041,
        "bulk_modulus_Mbar": 0.534,
        "bulk_modulus_pressure_derivative": 4.66
    }

def kpoint_path():
    # High-symmetry points in crystal coordinates (conventional cubic cell)
    # Segments: G->X->W->L->G
    segments = [
        ((0.0, 0.0, 0.0), (1.0, 0.0, 0.0)),    # G to X
        ((1.0, 0.0, 0.0), (1.0, 0.5, 0.0)),    # X to W
        ((1.0, 0.5, 0.0), (0.5, 0.5, 0.5)),    # W to L
        ((0.5, 0.5, 0.5), (0.0, 0.0, 0.0))     # L to G
    ]
    npoints_per_segment = [12, 8, 8, 8]  # ~36 total
    kpoints = []
    for (start, end), n in zip(segments, npoints_per_segment):
        for i in range(n):
            t = i / (n - 1)
            k = tuple((1-t)*s + t*e for s, e in zip(start, end))
            kpoints.append(k)
    return kpoints

def band_eigenvalues_at_nodes():
    # Define band energies at the special points (G, X, W, L, G) for 8 bands.
    # Indices: 0-3 valence (0 highest), 4-7 conduction.
    nodes = {}
    nodes[(0,0,0)] = [0.0, -0.5, -0.8, -1.2, 1.2, 1.6, 2.0, 2.5]   # G
    nodes[(1,0,0)] = [-1.0, -1.3, -1.5, -1.8, 0.8, 1.2, 1.6, 2.0]  # X
    nodes[(1,0.5,0)] = [-0.7, -1.0, -1.2, -1.5, 1.0, 1.4, 1.8, 2.2] # W
    nodes[(0.5,0.5,0.5)] = [-0.4, -0.8, -1.0, -1.3, 1.1, 1.5, 1.9, 2.3] # L
    # G again for closing segment
    nodes[(0,0,0)] = nodes[(0,0,0)]
    return nodes

def phonon_frequencies_at_nodes():
    # 6 branches: 0-2 acoustic, 3-5 optical (cm^-1)
    nodes = {}
    nodes[(0,0,0)] = [0.0, 0.0, 0.0, 150.0, 150.0, 160.0]   # G
    nodes[(1,0,0)] = [80.0, 90.0, 100.0, 170.0, 180.0, 200.0]  # X
    nodes[(1,0.5,0)] = [70.0, 80.0, 90.0, 160.0, 170.0, 190.0] # W
    nodes[(0.5,0.5,0.5)] = [60.0, 70.0, 80.0, 150.0, 160.0, 180.0] # L
    # G again
    nodes[(0,0,0)] = nodes[(0,0,0)]
    return nodes

def interpolate_linear(start_vals, end_vals, t):
    return [s + (e-s)*t for s, e in zip(start_vals, end_vals)]

def generate_band_structure():
    kpoints = kpoint_path()
    nodes = band_eigenvalues_at_nodes()
    special_order = [(0,0,0), (1,0,0), (1,0.5,0), (0.5,0.5,0.5), (0,0,0)]
    result = []
    seg_idx = -1
    i = 0
    for start_k, end_k, npts in [
        ((0,0,0), (1,0,0), 12),
        ((1,0,0), (1,0.5,0), 8),
        ((1,0.5,0), (0.5,0.5,0.5), 8),
        ((0.5,0.5,0.5), (0,0,0), 8)
    ]:
        seg_idx += 1
        start_vals = nodes[start_k]
        end_vals = nodes[end_k]
        for j in range(npts):
            t = j / (npts - 1)
            k = kpoints[i]; i += 1
            vals = interpolate_linear(start_vals, end_vals, t)
            result.append({
                "kpoint": list(k),
                "eigenvalues": [round(v, 4) for v in vals]
            })
    return result

def generate_phonon_dispersion():
    kpoints = kpoint_path()
    nodes = phonon_frequencies_at_nodes()
    result = []
    i = 0
    for start_k, end_k, npts in [
        ((0,0,0), (1,0,0), 12),
        ((1,0,0), (1,0.5,0), 8),
        ((1,0.5,0), (0.5,0.5,0.5), 8),
        ((0.5,0.5,0.5), (0,0,0), 8)
    ]:
        start_vals = nodes[start_k]
        end_vals = nodes[end_k]
        for j in range(npts):
            t = j / (npts - 1)
            k = kpoints[i]; i += 1
            vals = interpolate_linear(start_vals, end_vals, t)
            result.append({
                "kpoint": list(k),
                "frequencies_cm1": [round(v, 4) for v in vals]
            })
    return result

def main():
    if len(sys.argv) != 3 or sys.argv[1] != '--type':
        print("Usage: generate_artifacts.py --type <structural|band_structure|phonon_dispersion>", file=sys.stderr)
        sys.exit(1)
    typ = sys.argv[2]
    if typ == 'structural':
        data = structural_params()
    elif typ == 'band_structure':
        data = generate_band_structure()
    elif typ == 'phonon_dispersion':
        data = generate_phonon_dispersion()
    else:
        print(f"Unknown type: {typ}", file=sys.stderr)
        sys.exit(1)
    print(json.dumps(data, indent=2))

if __name__ == '__main__':
    main()
