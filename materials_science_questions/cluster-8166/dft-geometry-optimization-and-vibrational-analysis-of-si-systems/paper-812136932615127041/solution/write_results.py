import csv

data = [
    ["system", "formation_energy_eV", "homo_eV", "lumo_eV", "effective_work_function_eV"],
    ["pure_5_5", 0.0, -4.745, -3.936, 0.405],
    ["model_I", 1.19, -4.708, -4.124, 0.292],
    ["model_II", 1.26, -4.708, -4.124, 0.292],
    ["model_III", 1.47, -4.708, -4.124, 0.292],
    ["model_IV", 7.04, -4.715, -4.229, 0.243],
    ["pure_9_0", 0.0, -4.284, -4.019, 0.133],
    ["model_V", 1.24, -4.264, -4.075, 0.095],
    ["model_VI", 1.68, -4.302, -4.219, 0.042],
]

with open("/app/outputs/results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
