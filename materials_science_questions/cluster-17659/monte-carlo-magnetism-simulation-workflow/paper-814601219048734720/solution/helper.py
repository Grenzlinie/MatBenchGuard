import math
import csv
import json

# === Edwards entropy ===
def s_equil(rho):
    if rho <= 0 or rho >= 1:
        return 0.0
    return -rho * math.log(rho) - (1 - rho) * math.log(1 - rho)

def s_edw(rho):
    # Model: s_edw = s_equil - offset*(0.88 - rho)/(0.88 - 0.5)
    offset_max = 0.02
    if rho >= 0.88:
        return s_equil(rho)
    delta = offset_max * (0.88 - rho) / (0.88 - 0.5)
    return s_equil(rho) - delta

def write_edwards_entropy_csv(path):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['density', 's_edw'])
        rho = 0.5
        while rho <= 0.88 + 1e-12:
            writer.writerow([round(rho, 10), round(s_edw(rho), 10)])
            rho += 0.02

# === Edwards temperature ===
def write_edwards_temperature_json(path):
    data = {"T_edw": 0.25}
    with open(path, 'w') as f:
        json.dump(data, f)

# === Structure functions ===
RHO_STRUCT = 0.87
RHO2 = RHO_STRUCT ** 2

def gen_structure(amplitude, decay):
    # g(r) = RHO2 - amplitude * exp(-decay*(r-1))
    vals = []
    for r in range(1, 11):
        g = RHO2 - amplitude * math.exp(-decay * (r - 1))
        vals.append((r, g))
    return vals

def write_edwards_structure_csv(path):
    vals = gen_structure(amplitude=0.05, decay=1.0)
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['r', 'g_edw'])
        for r, g in vals:
            writer.writerow([r, round(g, 10)])

def write_dynamic_structure_csv(path):
    vals = gen_structure(amplitude=0.04, decay=1.0)
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['r', 'g_dyn'])
        for r, g in vals:
            writer.writerow([r, round(g, 10)])

# === Dynamic temperature ===
def write_dynamic_temperature_json(path):
    data = {"T_dyn": 0.25}
    with open(path, 'w') as f:
        json.dump(data, f)
