import json
import sys

data = {
    "binding_energy_Li_on_pure_graphene": -1.73,
    "Li_nO": [
        {"n": 1, "d_O_graphene": 1.98, "d_Li_graphene": 2.13, "d_O_Li": 1.75, "E_b_Li": -3.16, "E_b_cluster": -1.89},
        {"n": 2, "d_O_graphene": 2.85, "d_Li_graphene": 2.12, "d_O_Li": 1.67, "E_b_Li": -3.29, "E_b_cluster": -0.77},
        {"n": 3, "d_O_graphene": 2.79, "d_Li_graphene": 2.03, "d_O_Li": 1.70, "E_b_Li": -3.56, "E_b_cluster": -2.45},
        {"n": 4, "d_O_graphene": 2.92, "d_Li_graphene": [1.89, 4.62], "d_O_Li": [1.79, 1.69], "E_b_Li": -3.27, "E_b_cluster": -2.84}
    ],
    "Li_mOH": [
        {"m": 1, "d_O_graphene": 3.25, "d_Li_graphene": 1.99, "d_O_Li": 1.63, "E_b_Li": -4.52, "E_b_cluster": -0.54},
        {"m": 2, "d_O_graphene": 3.08, "d_Li_graphene": 1.93, "d_O_Li": 1.75, "E_b_Li": -4.17, "E_b_cluster": -2.69},
        {"m": 3, "d_O_graphene": 2.89, "d_Li_graphene": 1.83, "d_O_Li": 1.85, "E_b_Li": -3.48, "E_b_cluster": -3.20}
    ],
    "binding_energies_O_C_ratios": [
        {"config": "C1", "E_b_Li": -3.20, "E_b_cluster": -2.85},
        {"config": "C2", "E_b_Li": -3.11, "E_b_cluster": -2.79},
        {"config": "C3", "E_b_Li": -3.20, "E_b_cluster": -2.87}
    ],
    "H2_adsorption_Li4O": [
        {"n_H2": 3, "E_ad": -0.23},
        {"n_H2": 6, "E_ad": -0.21},
        {"n_H2": 9, "E_ad": -0.20}
    ],
    "H2_adsorption_Li3OH": [
        {"n_H2": 3, "E_ad": -0.26},
        {"n_H2": 6, "E_ad": -0.23}
    ],
    "HSC_adsorption": [
        {"system": "C1", "E_ad": -0.22, "HSC_wt": 6.04},
        {"system": "C2", "E_ad": -0.18, "HSC_wt": 8.67},
        {"system": "C3", "E_ad": -0.15, "HSC_wt": 10.26}
    ]
}

json.dump(data, sys.stdout, indent=2)
