import csv
import sys

def fmt_v(value, decimals=3):
    """Format a float to a fixed number of decimals; avoid scientific notation."""
    return f"{value:.{decimals}f}"

def calc_hill_moduli(C11, C12, C13, C33, C44):
    """Compute Voigt-Reuss-Hill bulk modulus B, shear modulus G,
    Young's modulus E, and Poisson's ratio nu for hexagonal crystals."""
    C66 = (C11 - C12) / 2.0
    M = C11 + C12 + 2*C33 - 4*C13
    C2 = (C11 + C12)*C33 - 2*C13*C13
    BV = (2*(C11 + C12) + 4*C13 + C33) / 9.0
    BR = C2 / M
    GV = (M + 12*C44 + 12*C66) / 30.0
    denom = 3*BV*C44*C66 + C2*(C44 + C66)
    GR = (5 * C2 * C44 * C66) / (2 * denom)
    B = (BV + BR) / 2.0
    G = (GV + GR) / 2.0
    E = 9*B*G / (3*B + G)
    nu = (3*B - 2*G) / (2*(3*B + G))
    return B, G, E, nu

# ----------------------- data from paper Tables 1 & 2 -----------------------
# Only the six mechanically stable compounds
compounds = ["TaC", "WC", "ReC", "OsC", "IrC", "PtC"]

# Elastic constants and lattice parameters (Table 1)
elastic_data = {
    "TaC": {
        "GGA": {"a0": 3.006, "c0": 2.856, "C11": 541, "C12": 188, "C13": 195, "C33": 784, "C44": 96},
        "LDA": {"a0": 3.002, "c0": 2.856, "C11": 543, "C12": 196, "C13": 197, "C33": 790, "C44": 104},
        "Ave": {
            "a0": 3.004, "c0": 2.856,
            "C11": 542, "C12": 192, "C13": 196, "C33": 787, "C44": 100,
            # The paper also gives B=333, G=151, E=393, nu=0.303, but we recompute for consistency
        },
    },
    "WC": {
        "GGA": {"a0": 2.905, "c0": 2.827, "C11": 733, "C12": 221, "C13": 169, "C33": 969, "C44": 307},
        "LDA": {"a0": 2.881, "c0": 2.809, "C11": 768, "C12": 251, "C13": 191, "C33": 1030, "C44": 334},
        "Ave": {
            "a0": 2.893, "c0": 2.818,
            "C11": 751, "C12": 236, "C13": 180, "C33": 999, "C44": 320,
        },
    },
    "ReC": {
        "GGA": {"a0": 2.852, "c0": 2.785, "C11": 772, "C12": 238, "C13": 231, "C33": 1007, "C44": 188},
        "LDA": {"a0": 2.839, "c0": 2.775, "C11": 797, "C12": 252, "C13": 251, "C33": 1035, "C44": 202},
        "Ave": {
            "a0": 2.846, "c0": 2.780,
            "C11": 785, "C12": 245, "C13": 241, "C33": 1021, "C44": 195,
        },
    },
    "OsC": {
        "GGA": {"a0": 2.925, "c0": 2.710, "C11": 441, "C12": 388, "C13": 265, "C33": 852, "C44": 84},
        "LDA": {"a0": 2.897, "c0": 2.693, "C11": 468, "C12": 416, "C13": 318, "C33": 881, "C44": 104},
        "Ave": {
            "a0": 2.911, "c0": 2.701,
            "C11": 455, "C12": 402, "C13": 292, "C33": 867, "C44": 94,
        },
    },
    "IrC": {
        "GGA": {"a0": 3.026, "c0": 2.650, "C11": 495, "C12": 301, "C13": 217, "C33": 837, "C44": 70},
        "LDA": {"a0": 3.011, "c0": 2.640, "C11": 523, "C12": 328, "C13": 241, "C33": 881, "C44": 85},
        "Ave": {
            "a0": 3.019, "c0": 2.645,
            "C11": 509, "C12": 315, "C13": 229, "C33": 859, "C44": 78,
        },
    },
    "PtC": {
        "GGA": {"a0": 3.005, "c0": 2.869, "C11": 353, "C12": 221, "C13": 200, "C33": 528, "C44": 48},
        "LDA": {"a0": 2.979, "c0": 2.850, "C11": 397, "C12": 253, "C13": 234, "C33": 585, "C44": 62},
        "Ave": {
            "a0": 2.992, "c0": 2.859,
            "C11": 375, "C12": 237, "C13": 217, "C33": 556, "C44": 55,
        },
    },
}

# Hardness data (Table 2) – all values taken directly from the paper
hardness_data = {
    "TaC": {
        "GGA": {"d": 2.247, "V": 22.3, "P": 0.395, "v_b": 3.724, "Ep": 1.837, "N_Ef": 1.494, "n_free": 1.153, "Pprime": 0.052, "f_m": 0.131, "H_v": 28.4},
        "LDA": {"d": 2.246, "V": 22.3, "P": 0.395, "v_b": 3.715, "Ep": 1.860, "N_Ef": 1.486, "n_free": 1.125, "Pprime": 0.050, "f_m": 0.128, "H_v": 28.6},
        "Ave": {"d": 2.247, "V": 22.3, "P": 0.395, "v_b": 3.719, "Ep": 1.849, "N_Ef": 1.490, "n_free": 1.139, "Pprime": 0.051, "f_m": 0.129, "H_v": 28.5},
    },
    "WC": {
        "GGA": {"d": 2.193, "V": 20.7, "P": 0.350, "v_b": 3.443, "Ep": 0.550, "N_Ef": 0.300, "n_free": 0.125, "Pprime": 0.006, "f_m": 0.017, "H_v": 32.4},
        "LDA": {"d": 2.177, "V": 20.2, "P": 0.343, "v_b": 3.366, "Ep": 0.495, "N_Ef": 0.316, "n_free": 0.113, "Pprime": 0.006, "f_m": 0.016, "H_v": 33.1},
        "Ave": {"d": 2.185, "V": 20.4, "P": 0.347, "v_b": 3.405, "Ep": 0.523, "N_Ef": 0.308, "n_free": 0.119, "Pprime": 0.006, "f_m": 0.017, "H_v": 32.7},
    },
    "ReC": {
        "GGA": {"d": 2.157, "V": 19.6, "P": 0.347, "v_b": 3.270, "Ep": -1.675, "N_Ef": 0.783, "n_free": 0.881, "Pprime": 0.045, "f_m": 0.129, "H_v": 31.0},
        "LDA": {"d": 2.148, "V": 19.4, "P": 0.338, "v_b": 3.230, "Ep": -1.707, "N_Ef": 0.786, "n_free": 0.864, "Pprime": 0.045, "f_m": 0.132, "H_v": 30.8},
        "Ave": {"d": 2.152, "V": 19.5, "P": 0.343, "v_b": 3.250, "Ep": -1.691, "N_Ef": 0.785, "n_free": 0.872, "Pprime": 0.045, "f_m": 0.131, "H_v": 30.9},
    },
    "OsC": {
        "GGA": {"d": 2.165, "V": 20.1, "P": 0.323, "v_b": 3.347, "Ep": -2.334, "N_Ef": 1.080, "n_free": 1.770, "Pprime": 0.088, "f_m": 0.273, "H_v": 23.2},
        "LDA": {"d": 2.147, "V": 19.6, "P": 0.318, "v_b": 3.261, "Ep": -2.416, "N_Ef": 1.016, "n_free": 1.737, "Pprime": 0.089, "f_m": 0.279, "H_v": 23.7},
        "Ave": {"d": 2.156, "V": 19.8, "P": 0.321, "v_b": 3.304, "Ep": -2.375, "N_Ef": 1.048, "n_free": 1.754, "Pprime": 0.088, "f_m": 0.276, "H_v": 23.5},
    },
    "IrC": {
        "GGA": {"d": 2.193, "V": 21.0, "P": 0.323, "v_b": 3.503, "Ep": -2.818, "N_Ef": 1.223, "n_free": 2.731, "Pprime": 0.130, "f_m": 0.402, "H_v": 17.7},
        "LDA": {"d": 2.183, "V": 20.7, "P": 0.323, "v_b": 3.455, "Ep": -2.859, "N_Ef": 1.212, "n_free": 2.721, "Pprime": 0.131, "f_m": 0.406, "H_v": 18.0},
        "Ave": {"d": 2.188, "V": 20.9, "P": 0.323, "v_b": 3.479, "Ep": -2.838, "N_Ef": 1.218, "n_free": 2.726, "Pprime": 0.131, "f_m": 0.404, "H_v": 17.9},
    },
    "PtC": {
        "GGA": {"d": 2.251, "V": 22.4, "P": 0.295, "v_b": 3.740, "Ep": -3.320, "N_Ef": 0.868, "n_free": 3.849, "Pprime": 0.172, "f_m": 0.582, "H_v": 10.1},
        "LDA": {"d": 2.233, "V": 21.9, "P": 0.297, "v_b": 3.649, "Ep": -3.528, "N_Ef": 0.855, "n_free": 3.905, "Pprime": 0.178, "f_m": 0.601, "H_v": 10.1},
        "Ave": {"d": 2.242, "V": 22.2, "P": 0.296, "v_b": 3.694, "Ep": -3.424, "N_Ef": 0.862, "n_free": 3.877, "Pprime": 0.175, "f_m": 0.591, "H_v": 10.1},
    },
}

def write_lattice_csv():
    out = "/app/outputs/lattice_and_elastic_constants.csv"
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["compound", "xc", "a0", "c0", "C11", "C12", "C13", "C33", "C44", "B", "G", "E", "nu"])
        for comp in compounds:
            ed = elastic_data[comp]
            for xc in ("GGA", "LDA", "Ave"):
                d = ed[xc]
                a0 = d["a0"]
                c0 = d["c0"]
                C11 = d["C11"]
                C12 = d["C12"]
                C13 = d["C13"]
                C33 = d["C33"]
                C44 = d["C44"]
                B, G, E, nu = calc_hill_moduli(C11, C12, C13, C33, C44)
                # For Ave, the paper's own values are nearly identical; this recomputation matches.
                row = [
                    comp,
                    xc,
                    fmt_v(a0, 3),
                    fmt_v(c0, 3),
                    str(int(C11)),
                    str(int(C12)),
                    str(int(C13)),
                    str(int(C33)),
                    str(int(C44)),
                    fmt_v(round(B), 0).split(".")[0],  # integer
                    fmt_v(round(G), 0).split(".")[0],
                    fmt_v(round(E), 0).split(".")[0],
                    fmt_v(nu, 3),
                ]
                w.writerow(row)
    print(f"Written {out}")

def write_hardness_csv():
    out = "/app/outputs/hardness_data.csv"
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["compound", "xc", "d", "V", "P", "v_b", "Ep", "N(E_f)", "n_free", "P'", "f_m", "H_v"])
        for comp in compounds:
            hd = hardness_data[comp]
            for xc in ("GGA", "LDA", "Ave"):
                d = hd[xc]
                row = [
                    comp,
                    xc,
                    fmt_v(d["d"], 3),
                    fmt_v(d["V"], 1),
                    fmt_v(d["P"], 3),
                    fmt_v(d["v_b"], 3),
                    fmt_v(d["Ep"], 3),
                    fmt_v(d["N_Ef"], 3),
                    fmt_v(d["n_free"], 3),
                    fmt_v(d["Pprime"], 3),
                    fmt_v(d["f_m"], 3),
                    fmt_v(d["H_v"], 1),
                ]
                w.writerow(row)
    print(f"Written {out}")

if __name__ == "__main__":
    target = sys.argv[1]
    if target == "lattice_and_elastic_constants.csv":
        write_lattice_csv()
    elif target == "hardness_data.csv":
        write_hardness_csv()
    else:
        print(f"Unknown target: {target}", file=sys.stderr)
        sys.exit(1)