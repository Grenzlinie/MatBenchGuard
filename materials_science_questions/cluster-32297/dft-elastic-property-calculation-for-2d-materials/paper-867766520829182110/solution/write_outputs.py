import sys
import json

data = {
    "structural": [
        {"system": "H-MoSe2", "a": 3.4, "b": 5.9, "lattice_mismatch": None, "interlayer_distance": None, "binding_energy_per_atom": None},
        {"system": "T-MoSe2", "a": 3.4, "b": 6.1, "lattice_mismatch": None, "interlayer_distance": None, "binding_energy_per_atom": None},
        {"system": "ZT-MoSe2", "a": 3.38, "b": 6.06, "lattice_mismatch": None, "interlayer_distance": None, "binding_energy_per_atom": None},
        {"system": "SO-MoSe2", "a": 6.80, "b": 6.80, "lattice_mismatch": None, "interlayer_distance": None, "binding_energy_per_atom": None},
        {"system": "α-P", "a": 3.41, "b": 4.84, "lattice_mismatch": None, "interlayer_distance": None, "binding_energy_per_atom": None},
        {"system": "β-P", "a": 3.41, "b": 3.41, "lattice_mismatch": None, "interlayer_distance": None, "binding_energy_per_atom": None},
        {"system": "α-P/H-MoSe2", "a": 3.41, "b": 24.18, "lattice_mismatch": 3.2, "interlayer_distance": 3.8, "binding_energy_per_atom": 0.040},
        {"system": "α-P/ZT-MoSe2", "a": 3.41, "b": 24.18, "lattice_mismatch": 1.16, "interlayer_distance": 3.6, "binding_energy_per_atom": 0.040},
        {"system": "α-P/SO-MoSe2", "a": 6.83, "b": 14.51, "lattice_mismatch": 6.7, "interlayer_distance": 3.7, "binding_energy_per_atom": 0.040},
        {"system": "β-P/H-MoSe2", "a": 3.41, "b": 3.41, "lattice_mismatch": 1.08, "interlayer_distance": 3.8, "binding_energy_per_atom": 0.040},
        {"system": "β-P/T-MoSe2", "a": 3.41, "b": 3.41, "lattice_mismatch": 0.98, "interlayer_distance": 3.5, "binding_energy_per_atom": 0.040}
    ],
    "electronic": [
        {"system": "H-MoSe2", "band_gap": 1.13, "band_gap_type": "direct", "band_gap_vs_field": None, "schottky_barrier_height": None, "schottky_barrier_type": None},
        {"system": "T-MoSe2", "band_gap": 0, "band_gap_type": None, "band_gap_vs_field": None, "schottky_barrier_height": None, "schottky_barrier_type": None},
        {"system": "ZT-MoSe2", "band_gap": 0, "band_gap_type": None, "band_gap_vs_field": None, "schottky_barrier_height": None, "schottky_barrier_type": None},
        {"system": "SO-MoSe2", "band_gap": 0, "band_gap_type": None, "band_gap_vs_field": None, "schottky_barrier_height": None, "schottky_barrier_type": None},
        {"system": "α-P", "band_gap": 1.12, "band_gap_type": "direct", "band_gap_vs_field": None, "schottky_barrier_height": None, "schottky_barrier_type": None},
        {"system": "β-P", "band_gap": 2.05, "band_gap_type": "indirect", "band_gap_vs_field": None, "schottky_barrier_height": None, "schottky_barrier_type": None},
        {"system": "α-P/H-MoSe2", "band_gap": 0.67, "band_gap_type": "indirect",
         "band_gap_vs_field": [
             {"field": -1.0, "band_gap": 0.60},
             {"field": -0.5, "band_gap": 0.80},
             {"field": 0.0, "band_gap": 0.67},
             {"field": 0.5, "band_gap": 0.0},
             {"field": 1.0, "band_gap": 0.0}
         ], "schottky_barrier_height": None, "schottky_barrier_type": None},
        {"system": "α-P/ZT-MoSe2", "band_gap": 0, "band_gap_type": None, "band_gap_vs_field": None,
         "schottky_barrier_height": 0.0, "schottky_barrier_type": "p-type"},
        {"system": "α-P/SO-MoSe2", "band_gap": 0, "band_gap_type": None, "band_gap_vs_field": None,
         "schottky_barrier_height": 0.0, "schottky_barrier_type": "p-type"},
        {"system": "β-P/H-MoSe2", "band_gap": 1.10, "band_gap_type": "direct",
         "band_gap_vs_field": [
             {"field": -1.0, "band_gap": 0.60},
             {"field": -0.5, "band_gap": 0.90},
             {"field": 0.0, "band_gap": 1.10},
             {"field": 0.5, "band_gap": 0.80},
             {"field": 1.0, "band_gap": 0.50}
         ], "schottky_barrier_height": None, "schottky_barrier_type": None},
        {"system": "β-P/T-MoSe2", "band_gap": 0, "band_gap_type": None, "band_gap_vs_field": None,
         "schottky_barrier_height": 0.5, "schottky_barrier_type": "n-type"}
    ],
    "mechanical": [
        {"system": "H-MoSe2", "Cx": 107.0, "Cy": 107.2, "vx": 0.34, "vy": 0.34},
        {"system": "T-MoSe2", "Cx": 123.8, "Cy": 123.7, "vx": 0.09, "vy": 0.09},
        {"system": "ZT-MoSe2", "Cx": 111.90, "Cy": 125.21, "vx": 0.27, "vy": 0.30},
        {"system": "SO-MoSe2", "Cx": 46.10, "Cy": 46.10, "vx": 0.63, "vy": 0.63},
        {"system": "α-P", "Cx": 81.60, "Cy": 60.42, "vx": 0.35, "vy": 0.26},
        {"system": "β-P", "Cx": 277.12, "Cy": 276.48, "vx": 0.02, "vy": 0.02},
        {"system": "α-P/H-MoSe2", "Cx": 181.44, "Cy": 149.96, "vx": 0.37, "vy": 0.30},
        {"system": "α-P/ZT-MoSe2", "Cx": 190.43, "Cy": 184.23, "vx": 0.32, "vy": 0.31},
        {"system": "α-P/SO-MoSe2", "Cx": 125.74, "Cy": 110.78, "vx": 0.43, "vy": 0.38},
        {"system": "β-P/H-MoSe2", "Cx": 701.12, "Cy": 703.04, "vx": 0.14, "vy": 0.14},
        {"system": "β-P/T-MoSe2", "Cx": 675.36, "Cy": 675.20, "vx": 0.07, "vy": 0.07}
    ],
    "dielectric": [
        {"system": "H-MoSe2", "lateral_eps": 4.6, "vertical_eps": 2.7},
        {"system": "T-MoSe2", "lateral_eps": 44.6, "vertical_eps": 2.8},
        {"system": "ZT-MoSe2", "lateral_eps": 24.7, "vertical_eps": 2.8},
        {"system": "SO-MoSe2", "lateral_eps": 17.4, "vertical_eps": 1.5},
        {"system": "α-P", "lateral_eps": 3.7, "vertical_eps": 2.2},
        {"system": "β-P", "lateral_eps": 3.0, "vertical_eps": 1.8},
        {"system": "α-P/H-MoSe2", "lateral_eps": 7.6, "vertical_eps": 4.2},
        {"system": "α-P/ZT-MoSe2", "lateral_eps": 23.9, "vertical_eps": 4.0},
        {"system": "α-P/SO-MoSe2", "lateral_eps": 19.3, "vertical_eps": 4.1},
        {"system": "β-P/H-MoSe2", "lateral_eps": 6.5, "vertical_eps": 3.7},
        {"system": "β-P/T-MoSe2", "lateral_eps": 47.4, "vertical_eps": 4.0}
    ]
}

def write_file(category):
    filename = f"/app/outputs/{category}_properties.json"
    with open(filename, 'w') as f:
        json.dump(data[category], f, indent=2)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: write_outputs.py <structural|electronic|mechanical|dielectric>")
        sys.exit(1)
    write_file(sys.argv[1])
