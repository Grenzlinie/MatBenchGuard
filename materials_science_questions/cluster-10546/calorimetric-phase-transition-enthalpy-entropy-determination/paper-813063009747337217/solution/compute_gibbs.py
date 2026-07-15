import csv
import math
import os

R_kJ = 8.314 / 1000.0   # kJ/(mol·K)
Delta_Cp = 1.5 * R_kJ   # kJ/(mol·K)

# transition data: (Teq [K], Q [kJ/mol])
transitions = {
    "fccl":    {"Teq": 290.0, "Q": 4.8},
    "dimer":   {"Teq": 280.0, "Q": 10.5},
    "polymer": {"Teq": 370.0, "Q": 25.8},
}

T_start = 200
T_end   = 500
step    = 1

out_path = "/app/outputs/gibbs_free_energies.csv"
os.makedirs(os.path.dirname(out_path), exist_ok=True)

phases = ["fccl", "dimer", "polymer"]

with open(out_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["T", "G_fccl", "G_dimer", "G_polymer"])
    T = T_start
    while T <= T_end + 1e-9:
        row = [round(T, 2)]
        for phase in phases:
            Teq = transitions[phase]["Teq"]
            Q   = transitions[phase]["Q"]
            # ΔH = Q - ∫_T^Teq ΔCp dT = Q - ΔCp*(Teq - T)
            delta_H = Q - Delta_Cp * (Teq - T)
            # ΔS = Q/Teq - ∫_T^Teq (ΔCp/T) dT = Q/Teq - ΔCp*ln(Teq/T)
            delta_S = Q / Teq - Delta_Cp * math.log(Teq / T)
            delta_G = delta_H - T * delta_S
            row.append(round(delta_G, 6))   # at least 2 decimal places
        writer.writerow(row)
        T += step
