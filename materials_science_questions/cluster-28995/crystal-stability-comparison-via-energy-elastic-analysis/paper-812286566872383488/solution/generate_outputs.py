#!/usr/bin/env python3
import json
import math

# ------------------------------------------------------------
# Data for Tables 4, 5, 6, 7
# ------------------------------------------------------------

# --- Table 4: s-levels separation limit ---
s_levels = {
    "fcc": [
        {"lambda": 2.0000, "psi_sq": 0.75,   "m": 6},
        {"lambda": 0.0000, "psi_sq": None,  "m": 3},
        {"lambda": -2.0000,"psi_sq": None,  "m": 3},
        {"lambda": -6.0000,"psi_sq": 0.25,  "m": 1}
    ],
    "hcp": [
        {"lambda": 2.5141, "psi_sq": None,   "m": 2},
        {"lambda": 2.0000, "psi_sq": 0.75,   "m": 2},
        {"lambda": 1.0000, "psi_sq": None,   "m": 2},
        {"lambda": 0.5720, "psi_sq": None,   "m": 2},
        {"lambda": 0.0000, "psi_sq": None,   "m": 1},
        {"lambda": -2.0000,"psi_sq": None,   "m": 1},
        {"lambda": -2.0861,"psi_sq": None,   "m": 2},
        {"lambda": -6.0000,"psi_sq": 0.25,   "m": 1}
    ],
    "icosahedron_VequalV": [
        {"lambda": 2.2361,  "psi_sq": None,   "m": 3},
        {"lambda": 1.7720,  "psi_sq": 0.7926, "m": 1},
        {"lambda": 1.0000,  "psi_sq": None,   "m": 5},
        {"lambda": -2.2361, "psi_sq": None,   "m": 3},
        {"lambda": -6.7720, "psi_sq": 0.2074, "m": 1}
    ],
    "icosahedron_Vsqrt_0_8V": [
        {"lambda": 2.0000,  "psi_sq": None,   "m": 3},
        {"lambda": 1.8870,  "psi_sq": 0.7712, "m": 1},
        {"lambda": 0.8944,  "psi_sq": None,   "m": 5},
        {"lambda": -2.0000, "psi_sq": None,   "m": 3},
        {"lambda": -6.3592, "psi_sq": 0.2288, "m": 1}
    ]
}

# --- Table 5: p-levels separation limit ---
p_levels = {
    "fcc": [
        {"lambda": 2.1912,  "psi_sq": 0.3413, "m": 3},
        {"lambda": 1.6180,  "psi_sq": None,   "m": 3},
        {"lambda": 1.0000,  "psi_sq": None,   "m": 8},
        {"lambda": 0.6180,  "psi_sq": None,   "m": 3},
        {"lambda": 0.5767,  "psi_sq": 0.2871, "m": 3},
        {"lambda": 0.0000,  "psi_sq": None,   "m": 3},
        {"lambda": -0.6180, "psi_sq": None,   "m": 3},
        {"lambda": -1.0000, "psi_sq": None,   "m": 3},
        {"lambda": -1.2644, "psi_sq": 0.0135, "m": 3},
        {"lambda": -1.6180, "psi_sq": None,   "m": 3},
        {"lambda": -2.0000, "psi_sq": None,   "m": 1},
        {"lambda": -2.5035, "psi_sq": 0.3581, "m": 3}
    ],
    "hcp": [
        {"lambda": 2.1905,  "psi_sq": 0.3387, "m": 2},
        {"lambda": 2.1661,  "psi_sq": 0.3505, "m": 1},
        {"lambda": 1.5990,  "psi_sq": None,   "m": 2},
        {"lambda": 1.5960,  "psi_sq": None,   "m": 1},
        {"lambda": 1.1039,  "psi_sq": None,   "m": 1},
        {"lambda": 1.0947,  "psi_sq": None,   "m": 2},
        {"lambda": 1.0224,  "psi_sq": 0.0031, "m": 2},
        {"lambda": 0.9320,  "psi_sq": None,   "m": 1},
        {"lambda": 0.8718,  "psi_sq": 0.0132, "m": 2},
        {"lambda": 0.6885,  "psi_sq": None,   "m": 1},
        {"lambda": 0.6627,  "psi_sq": 0.2052, "m": 2},
        {"lambda": 0.5671,  "psi_sq": 0.2776, "m": 1},
        {"lambda": 0.3788,  "psi_sq": 0.0624, "m": 2},
        {"lambda": 0.3252,  "psi_sq": None,   "m": 2},
        {"lambda": -0.0280, "psi_sq": None,   "m": 1},
        {"lambda": -0.6039, "psi_sq": None,   "m": 1},
        {"lambda": -0.7640, "psi_sq": 0.0000, "m": 2},
        {"lambda": -0.9288, "psi_sq": None,   "m": 1},
        {"lambda": -1.1014, "psi_sq": None,   "m": 2},
        {"lambda": -1.3444, "psi_sq": 0.0285, "m": 2},
        {"lambda": -1.4058, "psi_sq": None,   "m": 1},
        {"lambda": -1.4175, "psi_sq": None,   "m": 2},
        {"lambda": -1.7448, "psi_sq": 0.0116, "m": 1},
        {"lambda": -1.8539, "psi_sq": None,   "m": 1},
        {"lambda": -2.4884, "psi_sq": 0.3603, "m": 1},
        {"lambda": -2.5178, "psi_sq": 0.3487, "m": 2}
    ],
    "icosahedron_VequalV": [
        {"lambda": 2.3625,  "psi_sq": 0.2816, "m": 3},
        {"lambda": 1.8090,  "psi_sq": None,   "m": 3},
        {"lambda": 0.8853,  "psi_sq": None,   "m": 5},
        {"lambda": 0.8090,  "psi_sq": None,   "m": 5},
        {"lambda": 0.6180,  "psi_sq": None,   "m": 3},
        {"lambda": 0.5107,  "psi_sq": 0.3952, "m": 3},
        {"lambda": 0.0000,  "psi_sq": None,   "m": 4},
        {"lambda": -1.3820, "psi_sq": None,   "m": 1},
        {"lambda": -1.6180, "psi_sq": None,   "m": 4},
        {"lambda": -1.6943, "psi_sq": None,   "m": 5},
        {"lambda": -2.6822, "psi_sq": 0.3232, "m": 3}
    ],
    "icosahedron_Vsqrt_0_8V": [
        {"lambda": 2.2594,  "psi_sq": 0.3183, "m": 3},
        {"lambda": 1.6180,  "psi_sq": None,   "m": 3},
        {"lambda": 0.7918,  "psi_sq": None,   "m": 5},
        {"lambda": 0.7236,  "psi_sq": None,   "m": 5},
        {"lambda": 0.5528,  "psi_sq": None,   "m": 3},
        {"lambda": 0.4957,  "psi_sq": 0.3385, "m": 3},
        {"lambda": 0.0000,  "psi_sq": None,   "m": 4},
        {"lambda": -1.2361, "psi_sq": None,   "m": 1},
        {"lambda": -1.4472, "psi_sq": None,   "m": 4},
        {"lambda": -1.5155, "psi_sq": None,   "m": 5},
        {"lambda": -2.5843, "psi_sq": 0.3432, "m": 3}
    ]
}

# --- Table 6: hybridization limit ---
hyb_levels = {
    "fcc": [
        {"lambda": 7.5921,   "psi_sq": 0.3026, "m": 3},
        {"lambda": 5.6904,   "psi_sq": None,   "m": 2},
        {"lambda": 5.0000,   "psi_sq": None,   "m": 3},
        {"lambda": 4.8541,   "psi_sq": None,   "m": 3},
        {"lambda": 4.7371,   "psi_sq": 0.4390, "m": 1},
        {"lambda": 3.3218,   "psi_sq": None,   "m": 3},
        {"lambda": 3.0000,   "psi_sq": None,   "m": 3},
        {"lambda": 2.3020,   "psi_sq": 0.2594, "m": 3},
        {"lambda": 0.0000,   "psi_sq": None,   "m": 11},
        {"lambda": -0.6878,  "psi_sq": 0.3975, "m": 1},
        {"lambda": -0.9641,  "psi_sq": 0.1589, "m": 3},
        {"lambda": -1.8541,  "psi_sq": None,   "m": 3},
        {"lambda": -3.6904,  "psi_sq": None,   "m": 2},
        {"lambda": -3.7942,  "psi_sq": 0.0136, "m": 3},
        {"lambda": -6.0000,  "psi_sq": None,   "m": 1},
        {"lambda": -6.3218,  "psi_sq": None,   "m": 3},
        {"lambda": -10.1358, "psi_sq": 0.2655, "m": 3},
        {"lambda": -11.0493, "psi_sq": 0.1635, "m": 1}
    ],
    "hcp": [
        {"lambda": 7.6215,   "psi_sq": 0.3011, "m": 2},
        {"lambda": 7.4758,   "psi_sq": 0.3198, "m": 1},
        {"lambda": 5.4620,   "psi_sq": 0.0047, "m": 2},
        {"lambda": 5.3144,   "psi_sq": None,   "m": 1},
        {"lambda": 5.2444,   "psi_sq": None,   "m": 2},
        {"lambda": 4.7601,   "psi_sq": 0.6442, "m": 1},
        {"lambda": 4.7515,   "psi_sq": None,   "m": 2},
        {"lambda": 4.3005,   "psi_sq": None,   "m": 1},
        {"lambda": 3.6659,   "psi_sq": 0.0168, "m": 2},
        {"lambda": 3.5888,   "psi_sq": 0.0029, "m": 1},
        {"lambda": 3.3117,   "psi_sq": None,   "m": 1},
        {"lambda": 2.5562,   "psi_sq": 0.1749, "m": 2},
        {"lambda": 2.2711,   "psi_sq": 0.2649, "m": 1},
        {"lambda": 1.9008,   "psi_sq": 0.0853, "m": 2},
        {"lambda": 1.1258,   "psi_sq": None,   "m": 2},
        {"lambda": 0.0000,   "psi_sq": None,   "m": 8},
        {"lambda": -0.1149,  "psi_sq": None,   "m": 1},
        {"lambda": -0.6709,  "psi_sq": 0.0733, "m": 1},
        {"lambda": -0.9399,  "psi_sq": 0.1180, "m": 2},
        {"lambda": -0.9675,  "psi_sq": 0.1257, "m": 1},
        {"lambda": -1.8117,  "psi_sq": None,   "m": 1},
        {"lambda": -2.4320,  "psi_sq": 0.0000, "m": 2},
        {"lambda": -3.5250,  "psi_sq": None,   "m": 2},
        {"lambda": -4.6016,  "psi_sq": 0.0127, "m": 1},
        {"lambda": -5.0816,  "psi_sq": 0.0360, "m": 2},
        {"lambda": -5.0967,  "psi_sq": None,   "m": 2},
        {"lambda": -5.2378,  "psi_sq": 0.0075, "m": 1},
        {"lambda": -6.4299,  "psi_sq": 0.0010, "m": 1},
        {"lambda": -10.0416, "psi_sq": 0.2820, "m": 1},
        {"lambda": -10.2529, "psi_sq": 0.2631, "m": 2},
        {"lambda": -11.1465, "psi_sq": 0.2658, "m": 1}
    ],
    "icosahedron_VequalV": [
        {"lambda": 8.2936,   "psi_sq": 0.2489, "m": 3},
        {"lambda": 5.4271,   "psi_sq": None,   "m": 3},
        {"lambda": 4.7901,   "psi_sq": None,   "m": 5},
        {"lambda": 4.2798,   "psi_sq": 0.4631, "m": 1},
        {"lambda": 4.0902,   "psi_sq": None,   "m": 3},
        {"lambda": 2.4271,   "psi_sq": None,   "m": 5},
        {"lambda": 2.2180,   "psi_sq": 0.3358, "m": 3},
        {"lambda": 0.0000,   "psi_sq": None,   "m": 12},
        {"lambda": -0.7461,  "psi_sq": 0.4043, "m": 1},
        {"lambda": -1.0763,  "psi_sq": 0.1796, "m": 3},
        {"lambda": -4.8541,  "psi_sq": None,   "m": 4},
        {"lambda": -6.2172,  "psi_sq": None,   "m": 5},
        {"lambda": -11.0984, "psi_sq": 0.2357, "m": 3},
        {"lambda": -12.6797, "psi_sq": 0.1326, "m": 1}
    ],
    "icosahedron_Vsqrt_0_8V": [
        {"lambda": 7.8729,   "psi_sq": 0.2816, "m": 3},
        {"lambda": 4.8541,   "psi_sq": None,   "m": 3},
        {"lambda": 4.2844,   "psi_sq": None,   "m": 5},
        {"lambda": 4.4464,   "psi_sq": 0.4540, "m": 1},
        {"lambda": 3.6584,   "psi_sq": None,   "m": 3},
        {"lambda": 2.1708,   "psi_sq": None,   "m": 5},
        {"lambda": 2.1312,   "psi_sq": 0.2934, "m": 3},
        {"lambda": 0.0000,   "psi_sq": None,   "m": 12},
        {"lambda": -0.6818,  "psi_sq": 0.3999, "m": 1},
        {"lambda": -0.9984,  "psi_sq": 0.1705, "m": 3},
        {"lambda": -4.3416,  "psi_sq": None,   "m": 4},
        {"lambda": -5.5608,  "psi_sq": None,   "m": 5},
        {"lambda": -10.4932, "psi_sq": 0.2546, "m": 3},
        {"lambda": -11.9450, "psi_sq": 0.1461, "m": 1}
    ]
}

# --- Table 7: total energies ---
# separation_limit has keys: s1, p1, 2, 3, 4, 5
# hybridization_limit has keys: 1 .. 7
# Each subdict: fcc, hcp, icosahedron_VequalV, icosahedron_Vsqrt_0_8V

total = {
    "separation_limit": {
        "s1":  {"fcc": -24.0000, "hcp": -22.6284, "icosahedron_VequalV": -21.9606, "icosahedron_Vsqrt_0_8V": -20.2464},
        "p1":  {"fcc": -27.1110, "hcp": -26.4979, "icosahedron_VequalV": -27.9533, "icosahedron_Vsqrt_0_8V": -26.1139},
        "2":   {"fcc": -42.3154, "hcp": -42.3679, "icosahedron_VequalV": -48.7442, "icosahedron_Vsqrt_0_8V": -44.7101},
        "3":   {"fcc": -45.4467, "hcp": -45.0080, "icosahedron_VequalV": -46.1907, "icosahedron_Vsqrt_0_8V": -42.2316},
        "4":   {"fcc": -36.8552, "hcp": -36.9660, "icosahedron_VequalV": -37.1180, "icosahedron_Vsqrt_0_8V": -34.0775},
        "5":   {"fcc": -23.8552, "hcp": -23.7861, "icosahedron_VequalV": -25.9143, "icosahedron_Vsqrt_0_8V": -24.0564}
    },
    "hybridization_limit": {
        "1": {"fcc": -114.5224, "hcp": -111.8199, "icosahedron_VequalV": -123.0358, "icosahedron_Vsqrt_0_8V": -114.6533},
        "2": {"fcc": -170.3710, "hcp": -170.9396, "icosahedron_VequalV": -192.9546, "icosahedron_Vsqrt_0_8V": -177.1906},
        "3": {"fcc": -187.9680, "hcp": -190.4565, "icosahedron_VequalV": -200.9046, "icosahedron_Vsqrt_0_8V": -185.1779},
        "4": {"fcc": -188.6558, "hcp": -191.3572, "icosahedron_VequalV": -200.9046, "icosahedron_Vsqrt_0_8V": -185.1779},
        "5": {"fcc": -181.7498, "hcp": -181.1516, "icosahedron_VequalV": -185.1695, "icosahedron_Vsqrt_0_8V": -170.2200},
        "6": {"fcc": -143.5566, "hcp": -143.3510, "icosahedron_VequalV": -146.9648, "icosahedron_Vsqrt_0_8V": -136.0492},
        "7": {"fcc": -83.3142,  "hcp": -83.1588,  "icosahedron_VequalV": -87.1139,  "icosahedron_Vsqrt_0_8V": -81.4418}
    }
}

# Write all four JSON files
import os
out = "/app/outputs"
os.makedirs(out, exist_ok=True)

with open(os.path.join(out, "separation_limit_s_levels.json"), "w") as f:
    json.dump(s_levels, f, indent=2)

with open(os.path.join(out, "separation_limit_p_levels.json"), "w") as f:
    json.dump(p_levels, f, indent=2)

with open(os.path.join(out, "hybridization_limit_levels.json"), "w") as f:
    json.dump(hyb_levels, f, indent=2)

with open(os.path.join(out, "total_energies.json"), "w") as f:
    json.dump(total, f, indent=2)

print("All output files written.")
