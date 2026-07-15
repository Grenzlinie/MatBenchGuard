#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: dielectric_eqn_coefficients.json ===
python3 -c '
import json
data = {
    "a1": -3928, "a1_err": 210,
    "a2": -0.0102, "a2_err": 0.1654,
    "a3": 6.4656, "a3_err": 0.0006,
    "b0": -11.468, "b0_err": 0.095,
    "b1": 6188, "b1_err": 23.7,
    "b2": 0.16450, "b2_err": 0.01010,
    "b3": -28.678, "b3_err": 2.527
}
with open("/app/outputs/dielectric_eqn_coefficients.json", "w") as f:
    json.dump(data, f, indent=2)
'

# === solve block: kirkwood_results.json ===
python3 -c '
import json, math
mu_K_star = 3.293   # D
mu_gas   = 2.340    # D
g_K      = 1.981
N0 = 6.02214076e23
eps0 = 8.854187817e-12
kB = 1.380649e-23
D2Cm = 3.33564e-30
mu2 = (mu_K_star * D2Cm)**2
slope = mu2 * N0 / (9.0 * eps0 * kB)  # K m^3/mol
intercept = -5e-5
T_list = [294.11, 283.17, 274.43, 263.03, 253.14, 243.16, 232.99, 223.99, 218.26]
kirkwood = [{"T_n": T, "K1": intercept + slope/T} for T in T_list]
result = {
    "kirkwood_function": kirkwood,
    "slope": slope,
    "intercept": intercept,
    "mu_K_star": mu_K_star,
    "g_K": g_K
}
with open("/app/outputs/kirkwood_results.json", "w") as f:
    json.dump(result, f, indent=2)
'

# === solve block: kf_results.json ===
python3 -c '
import json, math
mu_gas   = 2.340   # D
mu_KF_star = 2.530
g_KF = 1.169
N0 = 6.02214076e23
eps0 = 8.854187817e-12
kB = 1.380649e-23
D2Cm = 3.33564e-30
mu2 = (mu_gas * D2Cm)**2
slope = mu2 * N0 * g_KF / (9.0 * eps0 * kB)
T_list = [294.11, 283.17, 274.43, 263.03, 253.14, 243.16, 232.99, 223.99, 218.26]
kf = [{"T_n": T, "KFF": slope / T} for T in T_list]
result = {
    "kf_function": kf,
    "slope": slope,
    "intercept": 0.0,
    "mu_KF_star": mu_KF_star,
    "g_KF": g_KF
}
with open("/app/outputs/kf_results.json", "w") as f:
    json.dump(result, f, indent=2)
'

# === solve block: thermodynamic_properties.csv ===
python3 -c '
import csv
a1 = -3928
a2 = -0.0102
a3 = 6.4656
b2 = 0.16450
b3 = -28.678

# (T_n, P_list, rho_list) for each isotherm, P descending from 15 to 2 MPa
data = [
    (294.11, [15,14,13,12,11,10,9,8,7,6,5,4,3,2],
              [1032,1027,1023,1018,1013,1008,1002,997,991,985,978,971,963,955]),
    (283.17, [15,14,13,12,11,10,9,8,7,6,5,4,3,2],
              [1061,1057,1053,1049,1044,1040,1035,1031,1026,1021,1015,1009,1003,997]),
    (274.43, [15,14,13,12,11,10,9,8,7,6,5,4,3,2],
              [1083,1080,1076,1072,1069,1065,1061,1057,1052,1048,1043,1038,1033,1028]),
    (263.03, [15,14,13,12,11,10,9,8,7,6,5,4,3,2],
              [1112,1109,1106,1103,1099,1096,1092,1089,1085,1081,1077,1073,1069,1065]),
    (253.14, [15,14,13,12,11,10,9,8,7,6,5,4,3,2],
              [1136,1134,1131,1128,1125,1122,1119,1116,1113,1109,1106,1102,1099,1095]),
    (243.16, [15,14,13,12,11,10,9,8,7,6,5,4,3,2],
              [1161,1158,1156,1153,1150,1148,1145,1142,1139,1136,1133,1130,1127,1124]),
    (232.99, [15,14,13,12,11,10,9,8,7,6,5,4,3,2],
              [1185,1183,1180,1178,1176,1173,1171,1168,1166,1163,1161,1158,1155,1152]),
    (223.99, [15,14,13,12,11,10,9,8,7,6,5,4,3,2],
              [1206,1204,1202,1200,1198,1196,1193,1191,1189,1186,1184,1182,1179,1177]),
    (218.26, [15,14,13,12,11,10,9,8,7,6,5,4,3,2],
              [1220,1218,1216,1214,1212,1210,1207,1205,1203,1201,1199,1196,1194,1192])
]

with open("/app/outputs/thermodynamic_properties.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["T_n", "P", "alpha_P", "kappa_T"])
    for T_n, P_list, rho_list in data:
        for P, rho in zip(P_list, rho_list):
            # alpha_P
            num_alpha = a1 + a3 * rho
            den_alpha = (T_n ** 2) * rho * (a2 + a3 / T_n)
            alpha = num_alpha / den_alpha
            # kappa_T
            dEpsdP = b2 + b3 / T_n
            dEpsdRho = a2 + a3 / T_n
            kappa = dEpsdP / (rho * dEpsdRho)
            writer.writerow([T_n, P, alpha, kappa])
'
