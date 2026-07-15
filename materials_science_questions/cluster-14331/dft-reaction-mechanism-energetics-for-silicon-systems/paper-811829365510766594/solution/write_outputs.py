#!/usr/bin/env python3
import csv
import sys

def write_relative_enthalpies(path):
    data = [
        {"species": "SiH2 + C6H6",                        "G3_H_hartree": "-522.500432", "Delta_H_kJ_mol":    "0.0"},
        {"species": "C6H6...SiH2 complex 1",               "G3_H_hartree": "-522.514872", "Delta_H_kJ_mol":  "-37.9"},
        {"species": "C6H6...SiH2 complex 2",               "G3_H_hartree": "-522.514018", "Delta_H_kJ_mol":  "-35.7"},
        {"species": "tricyclo[4.1.0.0^{2,7}]-1-sila-hept-3-ene", "G3_H_hartree": "-522.515000", "Delta_H_kJ_mol":  "-38.2"},
        {"species": "7-silanorcaradiene",                  "G3_H_hartree": "-522.520904", "Delta_H_kJ_mol":  "-53.7"},
        {"species": "7-silacycloheptatriene",              "G3_H_hartree": "-522.544187", "Delta_H_kJ_mol": "-114.9"},
        {"species": "phenylsilane",                        "G3_H_hartree": "-522.586275", "Delta_H_kJ_mol": "-225.4"},
        {"species": "TSa",                                 "G3_H_hartree": "-522.517208", "Delta_H_kJ_mol":  "-44.0"},
        {"species": "TS1",                                 "G3_H_hartree": "-522.482757", "Delta_H_kJ_mol":   "46.4"},
        {"species": "TS2",                                 "G3_H_hartree": "-522.490696", "Delta_H_kJ_mol":   "25.6"},
        {"species": "TS3",                                 "G3_H_hartree": "-522.510422", "Delta_H_kJ_mol":  "-26.2"},
        {"species": "TS4",                                 "G3_H_hartree": "-522.506974", "Delta_H_kJ_mol":  "-17.2"},
    ]
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["species", "G3_H_hartree", "Delta_H_kJ_mol"])
        w.writeheader()
        w.writerows(data)

def write_rrkm_stabilization(path):
    data = [
        {"product": "7-silanorcaradiene",    "pressure_Torr": 1,   "log_k_over_k_inf": "-3.665", "percent_stabilization":   "0.022"},
        {"product": "7-silanorcaradiene",    "pressure_Torr": 3,   "log_k_over_k_inf": "-3.204", "percent_stabilization":   "0.063"},
        {"product": "7-silanorcaradiene",    "pressure_Torr": 10,  "log_k_over_k_inf": "-2.719", "percent_stabilization":   "0.191"},
        {"product": "7-silanorcaradiene",    "pressure_Torr": 30,  "log_k_over_k_inf": "-2.303", "percent_stabilization":   "0.498"},
        {"product": "7-silanorcaradiene",    "pressure_Torr": 100, "log_k_over_k_inf": "-1.875", "percent_stabilization":   "1.334"},
        {"product": "7-silacycloheptatriene","pressure_Torr": 1,   "log_k_over_k_inf": "-0.403", "percent_stabilization":  "39.5"},
        {"product": "7-silacycloheptatriene","pressure_Torr": 3,   "log_k_over_k_inf": "-0.262", "percent_stabilization":  "54.7"},
        {"product": "7-silacycloheptatriene","pressure_Torr": 10,  "log_k_over_k_inf": "-0.151", "percent_stabilization":  "70.6"},
        {"product": "7-silacycloheptatriene","pressure_Torr": 30,  "log_k_over_k_inf": "-0.083", "percent_stabilization":  "82.6"},
        {"product": "7-silacycloheptatriene","pressure_Torr": 100, "log_k_over_k_inf": "-0.038", "percent_stabilization":  "91.6"},
    ]
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["product", "pressure_Torr", "log_k_over_k_inf", "percent_stabilization"])
        w.writeheader()
        w.writerows(data)

if __name__ == "__main__":
    path = sys.argv[1]
    if "relative_enthalpies" in path:
        write_relative_enthalpies(path)
    elif "rrkm_stabilization" in path:
        write_rrkm_stabilization(path)
    else:
        raise ValueError(f"Unknown output file: {path}")
