#!/usr/bin/env python3
import json, sys, argparse

def write_qtaim():
    data = [
        # Compound 8 (Table 2)
        {
            "molecule": "8",
            "interaction": "C(17)...H'-C(37)",
            "bond_path_RX": 2.8870,
            "bond_path_RY": 2.1760,
            "rho_b": 7.932e-3,
            "laplacian_rho": 7.406e-3,
            "ellipticity": 2.901,
            "Vr": 4.378e-3,
            "Gr": 5.892e-3
        },
        {
            "molecule": "8",
            "interaction": "C(40)...H-C(14)",
            "bond_path_RX": 2.8182,
            "bond_path_RY": 2.0915,
            "rho_b": 8.659e-3,
            "laplacian_rho": 8.012e-3,
            "ellipticity": 1.658,
            "Vr": 4.806e-3,
            "Gr": 6.409e-3
        },
        {
            "molecule": "8",
            "interaction": "N(16)...H-C(11)",
            "bond_path_RX": 2.7445,
            "bond_path_RY": 1.9847,
            "rho_b": 1.156e-2,
            "laplacian_rho": 1.085e-2,
            "ellipticity": 0.3847,
            "Vr": 6.829e-3,
            "Gr": 8.837e-3
        },
        {
            "molecule": "8",
            "interaction": "N(39)...H-C(34)",
            "bond_path_RX": 2.6645,
            "bond_path_RY": 1.8363,
            "rho_b": 1.376e-2,
            "laplacian_rho": 1.308e-2,
            "ellipticity": 0.2255,
            "Vr": 8.251e-3,
            "Gr": 1.067e-2
        },
        {
            "molecule": "8",
            "interaction": "N(19)...H-C(38)",
            "bond_path_RX": 3.0277,
            "bond_path_RY": 2.1216,
            "rho_b": 3.346e-3,
            "laplacian_rho": 5.159e-3,
            "ellipticity": 0.07899,
            "Vr": 3.294e-3,
            "Gr": 4.226e-3
        },
        {
            "molecule": "8",
            "interaction": "N(42)...H-C(15)",
            "bond_path_RX": 3.0092,
            "bond_path_RY": 2.0551,
            "rho_b": 7.743e-3,
            "laplacian_rho": 6.493e-3,
            "ellipticity": 0.9354,
            "Vr": 4.118e-3,
            "Gr": 5.305e-3
        },
        {
            "molecule": "8",
            "interaction": "C(6) ...H-C(37)",
            "bond_path_RX": 4.0314,
            "bond_path_RY": 2.9757,
            "rho_b": 1.090e-3,
            "laplacian_rho": 9.337e-4,
            "ellipticity": 0.6524,
            "Vr": 4.085e-4,
            "Gr": 6.711e-4
        },
        # Polymorph 9a (Table 3)
        {
            "molecule": "9a",
            "interaction": "H-N(A)...H(ortho)-C(C)",
            "bond_path_RX": 2.7303,
            "bond_path_RY": 1.9148,
            "rho_b": 1.122e-2,
            "laplacian_rho": 1.091e-2,
            "ellipticity": 0.2816,
            "Vr": 6.883e-3,
            "Gr": 8.898e-3
        },
        {
            "molecule": "9a",
            "interaction": "N(A)...H(ortho)-C(F)",
            "bond_path_RX": 2.8231,
            "bond_path_RY": 2.0064,
            "rho_b": 1.254e-2,
            "laplacian_rho": 1.088e-2,
            "ellipticity": 0.4211,
            "Vr": 7.514e-3,
            "Gr": 9.200e-3
        },
        {
            "molecule": "9a",
            "interaction": "N(G)...H(ortho)-C(F)",
            "bond_path_RX": 3.0917,
            "bond_path_RY": 2.0581,
            "rho_b": 5.960e-3,
            "laplacian_rho": 4.855e-3,
            "ellipticity": 0.1300,
            "Vr": 3.088e-3,
            "Gr": 3.972e-3
        },
        {
            "molecule": "9a",
            "interaction": "C(D)...C(F)",
            "bond_path_RX": 3.1648,
            "bond_path_RY": 3.3425,
            "rho_b": 6.218e-3,
            "laplacian_rho": 4.434e-3,
            "ellipticity": 1.251,
            "Vr": 2.530e-3,
            "Gr": 3.482e-3
        },
        {
            "molecule": "9a",
            "interaction": "C(G)...H-CH2",
            "bond_path_RX": 3.5008,
            "bond_path_RY": 2.4909,
            "rho_b": 3.524e-3,
            "laplacian_rho": 2.612e-3,
            "ellipticity": 0.4638,
            "Vr": 1.464e-3,
            "Gr": 2.038e-3
        },
        {
            "molecule": "9a",
            "interaction": "H2C-H...H-C(A)",
            "bond_path_RX": 1.9492,
            "bond_path_RY": 1.9951,
            "rho_b": 1.137e-2,
            "laplacian_rho": 1.096e-2,
            "ellipticity": 0.1079,
            "Vr": 6.917e-3,
            "Gr": 8.942e-3
        },
        # Polymorph 9b (Table 3)
        {
            "molecule": "9b",
            "interaction": "H-N(A)...H(ortho)-C(C)",
            "bond_path_RX": 2.7433,
            "bond_path_RY": 1.9108,
            "rho_b": 1.128e-2,
            "laplacian_rho": 1.108e-2,
            "ellipticity": 0.3629,
            "Vr": 7.046e-3,
            "Gr": 9.061e-3
        },
        {
            "molecule": "9b",
            "interaction": "N(A)...H(ortho)-C(F)",
            "bond_path_RX": 2.8291,
            "bond_path_RY": 2.0260,
            "rho_b": 1.238e-2,
            "laplacian_rho": 1.073e-2,
            "ellipticity": 0.4436,
            "Vr": 7.409e-3,
            "Gr": 9.071e-3
        },
        {
            "molecule": "9b",
            "interaction": "N(G)...H(ortho)-C(F)",
            "bond_path_RX": 3.0989,
            "bond_path_RY": 2.0615,
            "rho_b": 5.888e-3,
            "laplacian_rho": 4.795e-3,
            "ellipticity": 0.1253,
            "Vr": 3.045e-3,
            "Gr": 3.920e-3
        },
        {
            "molecule": "9b",
            "interaction": "C(D)...C(F)",
            "bond_path_RX": 3.1768,
            "bond_path_RY": 3.3453,
            "rho_b": 6.101e-3,
            "laplacian_rho": 4.343e-3,
            "ellipticity": 1.223,
            "Vr": 2.478e-3,
            "Gr": 3.410e-3
        },
        {
            "molecule": "9b",
            "interaction": "C(G)...H-CH2",
            "bond_path_RX": 3.4820,
            "bond_path_RY": 2.4468,
            "rho_b": 3.758e-3,
            "laplacian_rho": 2.777e-3,
            "ellipticity": 0.5031,
            "Vr": 1.572e-3,
            "Gr": 2.174e-3
        },
        {
            "molecule": "9b",
            "interaction": "H2C-H...H-C(A)",
            "bond_path_RX": 1.9307,
            "bond_path_RY": 1.9772,
            "rho_b": 1.182e-2,
            "laplacian_rho": 1.141e-2,
            "ellipticity": 0.1122,
            "Vr": 7.228e-3,
            "Gr": 9.320e-3
        }
    ]
    json.dump(data, sys.stdout, indent=2)

def write_hirshfeld():
    res = {
        "8": {
            "contact_percentages": {
                "HH": 65.0,
                "CH": 20.0,
                "NH": 13.0
            },
            "interaction_energies": []   # no CE-B3LYP energies reported for 8
        },
        "9a": {
            "contact_percentages": {
                "HH": 71.0,
                "CH": 19.8,
                "NH": 8.7
            },
            "interaction_energies": [
                {
                    "polymorph": "9a",
                    "color": "-x, -y, -z",
                    "symop_AB": "-x, -y, -z",
                    "R_AB": 6.65,
                    "E_ele": -27.2,
                    "E_pol": -6.1,
                    "E_dis": -142.6,
                    "E_rep": 73.9,
                    "E_tot": -111.8
                },
                {
                    "polymorph": "9a",
                    "color": "-x, -y, -z",
                    "symop_AB": "-x, -y, -z",
                    "R_AB": 10.59,
                    "E_ele": -6.6,
                    "E_pol": -1.5,
                    "E_dis": -56.5,
                    "E_rep": 29.0,
                    "E_tot": -39.5
                },
                {
                    "polymorph": "9a",
                    "color": "-x, y+1/2, -z+1/2",
                    "symop_AB": "-x, y+1/2, -z+1/2",
                    "R_AB": 15.67,
                    "E_ele": -0.3,
                    "E_pol": -0.1,
                    "E_dis": -5.1,
                    "E_rep": 1.9,
                    "E_tot": -3.7
                },
                {
                    "polymorph": "9a",
                    "color": "x, -y+1/2, z+1/2",
                    "symop_AB": "x, -y+1/2, z+1/2",
                    "R_AB": 11.86,
                    "E_ele": -3.1,
                    "E_pol": -0.9,
                    "E_dis": -32.9,
                    "E_rep": 15.7,
                    "E_tot": -22.9
                },
                {
                    "polymorph": "9a",
                    "color": "-x, y+1/2, -z+1/2",
                    "symop_AB": "-x, y+1/2, -z+1/2",
                    "R_AB": 12.64,
                    "E_ele": -12.9,
                    "E_pol": -2.8,
                    "E_dis": -31.8,
                    "E_rep": 24.9,
                    "E_tot": -28.0
                },
                {
                    "polymorph": "9a",
                    "color": "x, y, z",
                    "symop_AB": "x, y, z",
                    "R_AB": 10.84,
                    "E_ele": -8.4,
                    "E_pol": -1.7,
                    "E_dis": -35.9,
                    "E_rep": 19.2,
                    "E_tot": -29.5
                },
                {
                    "polymorph": "9a",
                    "color": "x, -y+1/2, z+1/2",
                    "symop_AB": "x, -y+1/2, z+1/2",
                    "R_AB": 14.60,
                    "E_ele": -1.9,
                    "E_pol": -0.4,
                    "E_dis": -9.2,
                    "E_rep": 1.8,
                    "E_tot": -9.3
                }
            ]
        },
        "9b": {
            "contact_percentages": {
                "HH": 71.1,
                "CH": 19.7,
                "NH": 8.7
            },
            "interaction_energies": [
                {
                    "polymorph": "9b",
                    "color": "-x, -y, -z",
                    "symop_AB": "-x, -y, -z",
                    "R_AB": 10.60,
                    "E_ele": -6.5,
                    "E_pol": -1.5,
                    "E_dis": -55.6,
                    "E_rep": 27.7,
                    "E_tot": -39.4
                },
                {
                    "polymorph": "9b",
                    "color": "-x, y+1/2, -z+1/2",
                    "symop_AB": "-x, y+1/2, -z+1/2",
                    "R_AB": 15.69,
                    "E_ele": -0.3,
                    "E_pol": -0.1,
                    "E_dis": -4.8,
                    "E_rep": 1.5,
                    "E_tot": -3.6
                },
                {
                    "polymorph": "9b",
                    "color": "x, -y+1/2, z+1/2",
                    "symop_AB": "x, -y+1/2, z+1/2",
                    "R_AB": 14.61,
                    "E_ele": -1.9,
                    "E_pol": -0.4,
                    "E_dis": -8.9,
                    "E_rep": 1.6,
                    "E_tot": -9.1
                },
                {
                    "polymorph": "9b",
                    "color": "x, y, z",
                    "symop_AB": "x, y, z",
                    "R_AB": 10.84,
                    "E_ele": -8.0,
                    "E_pol": -1.7,
                    "E_dis": -35.3,
                    "E_rep": 18.4,
                    "E_tot": -29.0
                },
                {
                    "polymorph": "9b",
                    "color": "x, -y+1/2, z+1/2",
                    "symop_AB": "x, -y+1/2, z+1/2",
                    "R_AB": 11.88,
                    "E_ele": -3.1,
                    "E_pol": -0.9,
                    "E_dis": -32.4,
                    "E_rep": 15.2,
                    "E_tot": -22.7
                },
                {
                    "polymorph": "9b",
                    "color": "-x, -y, -z",
                    "symop_AB": "-x, -y, -z",
                    "R_AB": 6.66,
                    "E_ele": -26.9,
                    "E_pol": -5.9,
                    "E_dis": -141.3,
                    "E_rep": 72.9,
                    "E_tot": -110.8
                },
                {
                    "polymorph": "9b",
                    "color": "-x, y+1/2, -z+1/2",
                    "symop_AB": "-x, y+1/2, -z+1/2",
                    "R_AB": 12.65,
                    "E_ele": -12.3,
                    "E_pol": -2.7,
                    "E_dis": -31.1,
                    "E_rep": 23.3,
                    "E_tot": -27.7
                }
            ]
        }
    }
    json.dump(res, sys.stdout, indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--qtaim", action="store_true")
    group.add_argument("--hirshfeld", action="store_true")
    args = parser.parse_args()
    if args.qtaim:
        write_qtaim()
    else:
        write_hirshfeld()
