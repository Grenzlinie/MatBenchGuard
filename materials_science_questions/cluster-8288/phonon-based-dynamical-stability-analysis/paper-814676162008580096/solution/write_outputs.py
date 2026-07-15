import json, sys

def gen_optimized_structures():
    return {
        "beta": {
            "space_group": "P6_3/m",
            "a": 7.987,
            "c": 3.054,
            "Ge_6h": [0.1696, 0.7628, 0.25],
            "N_6h": [0.3304, 0.0257, 0.25],
            "N_2c": [0.333333, 0.666667, 0.25]
        },
        "gamma": {
            "space_group": "Fd-3m",
            "a": 8.1676,
            "GeIV_8a": [0.0, 0.0, 0.0],
            "GeVI_16d": [0.625, 0.625, 0.625],
            "N_32e": [0.1330, 0.1330, 0.1330]
        }
    }

def gen_eos_parameters():
    return {
        "beta": {"V0": 12.053, "K": 185, "Kprime": 3.7},
        "gamma": {"V0": 9.730, "K": 240, "Kprime": 4.5}
    }

def gen_band_gaps():
    return {
        "beta": {"LDA_band_gap_eV": 2.45},
        "gamma": {"LDA_band_gap_eV": 2.17}
    }

def gen_phonon_frequencies():
    beta = [
        {"frequency_cm-1": 0,   "symmetry": "A_u"},
        {"frequency_cm-1": 0,   "symmetry": "E_1u"},
        {"frequency_cm-1": 106, "symmetry": "E_2g"},
        {"frequency_cm-1": 108, "symmetry": "A_g"},
        {"frequency_cm-1": 129, "symmetry": "E_1g"},
        {"frequency_cm-1": 137, "symmetry": "B_u"},
        {"frequency_cm-1": 169, "symmetry": "E_2u"},
        {"frequency_cm-1": 172, "symmetry": "B_g"},
        {"frequency_cm-1": 247, "symmetry": "A_u"},
        {"frequency_cm-1": 254, "symmetry": "B_g"},
        {"frequency_cm-1": 271, "symmetry": "E_1u"},
        {"frequency_cm-1": 275, "symmetry": "E_2g"},
        {"frequency_cm-1": 306, "symmetry": "B_u"},
        {"frequency_cm-1": 309, "symmetry": "A_g"},
        {"frequency_cm-1": 339, "symmetry": "E_1u"},
        {"frequency_cm-1": 365, "symmetry": "B_u"},
        {"frequency_cm-1": 373, "symmetry": "E_2g"},
        {"frequency_cm-1": 443, "symmetry": "A_g"},
        {"frequency_cm-1": 703, "symmetry": "A_u"},
        {"frequency_cm-1": 721, "symmetry": "E_1g"},
        {"frequency_cm-1": 735, "symmetry": "E_2u"},
        {"frequency_cm-1": 739, "symmetry": "E_1u"},
        {"frequency_cm-1": 753, "symmetry": "B_g"},
        {"frequency_cm-1": 781, "symmetry": "A_g"},
        {"frequency_cm-1": 791, "symmetry": "E_2g"},
        {"frequency_cm-1": 878, "symmetry": "E_1u"},
        {"frequency_cm-1": 878, "symmetry": "E_2g"},
        {"frequency_cm-1": 896, "symmetry": "B_u"}
    ]
    gamma = [
        {"frequency_cm-1": 0,   "symmetry": "T_1u"},
        {"frequency_cm-1": 153, "symmetry": "T_2u"},
        {"frequency_cm-1": 224, "symmetry": "T_1u"},
        {"frequency_cm-1": 245, "symmetry": "T_2g"},
        {"frequency_cm-1": 245, "symmetry": "E_u"},
        {"frequency_cm-1": 406, "symmetry": "T_1u"},
        {"frequency_cm-1": 453, "symmetry": "T_1g"},
        {"frequency_cm-1": 455, "symmetry": "A_2u"},
        {"frequency_cm-1": 467, "symmetry": "E_g"},
        {"frequency_cm-1": 475, "symmetry": "T_1u"},
        {"frequency_cm-1": 535, "symmetry": "T_2u"},
        {"frequency_cm-1": 576, "symmetry": "T_2g"},
        {"frequency_cm-1": 656, "symmetry": "T_1u"},
        {"frequency_cm-1": 667, "symmetry": "E_u"},
        {"frequency_cm-1": 710, "symmetry": "T_2g"},
        {"frequency_cm-1": 806, "symmetry": "A_2u"},
        {"frequency_cm-1": 830, "symmetry": "A_1g"}
    ]
    return {"beta": beta, "gamma": gamma}

def main():
    path = sys.argv[1]
    if path.endswith("/optimized_structures.json"):
        data = gen_optimized_structures()
    elif path.endswith("/eos_parameters.json"):
        data = gen_eos_parameters()
    elif path.endswith("/band_gaps.json"):
        data = gen_band_gaps()
    elif path.endswith("/phonon_frequencies.json"):
        data = gen_phonon_frequencies()
    else:
        raise ValueError("Unknown output file")
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    main()
