import json, sys

data = {
    "gamma_Fe6_orbital_population": {
        "Fe_3d": 6.4619,
        "Fe_4s": 0.9763,
        "Fe_4p": 0.5718
    },
    "gamma_prime_Fe6N_orbital_population": {
        "N_2s": 1.566,
        "N_2p": 3.753,
        "Fe_3s": 2.106,
        "Fe_3p": 6.275,
        "Fe_3d": 5.930,
        "Fe_4s": 0.921,
        "Fe_4p": 0.449
    },
    "N_Fe_overlap_population": {
        "N_Fe_3s": -0.010,
        "N_Fe_3p": -0.1227,
        "N_Fe_3d": 0.4335,
        "N_Fe_4s": 0.1149,
        "N_Fe_4p": 0.3696,
        "N_Fe_total": 0.7853
    }
}

with open(sys.argv[1], 'w') as f:
    json.dump(data, f, indent=2)
