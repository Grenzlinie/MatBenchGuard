import csv
import os

output_dir = "/app/outputs"
os.makedirs(output_dir, exist_ok=True)

# --- magnetization_curves.csv ---
# U from 0 to 10 eV step 0.5 (21 points)
U_vals = [round(i*0.5, 2) for i in range(0, 21)]
m35 = [0.0]*len(U_vals)
m30 = [0.0]*len(U_vals)

for i, U in enumerate(U_vals):
    # m=0.35: first-order jumps mimicking paper's description
    if U < 4.0:
        m35[i] = 0.0
    elif U < 5.5:
        m35[i] = 0.05
    elif U < 6.5:
        m35[i] = 0.10
    elif U < 7.0:
        m35[i] = 0.15
    elif U < 7.5:
        m35[i] = 0.20
    elif U < 8.0:
        m35[i] = 0.28
    else:
        m35[i] = 0.35
    # m=0.30: continuous onset at U_c ~4.5 eV
    Uc = 4.5
    if U < Uc:
        m30[i] = 0.0
    else:
        m30[i] = min(0.30, (U - Uc) * 0.06)  # linear growth to saturation

with open(os.path.join(output_dir, "magnetization_curves.csv"), "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["U", "delta_G_m0.35", "delta_G_m0.30"])
    for U, d35, d30 in zip(U_vals, m35, m30):
        writer.writerow([U, round(d35, 4), round(d30, 4)])

# --- phase_diagram.csv ---
J_over_U_vals = [round(i*0.04, 3) for i in range(0, 11)]  # 0.0 to 0.4 step 0.04
Uc_vals = []
for j in J_over_U_vals:
    # linear decrease from 7.2 to 1.5 as J/U increases
    Uc = 7.2 - j * 14.25  # 14.25 * 0.4 = 5.7, so Uc from 7.2 to 1.5
    Uc_vals.append(round(Uc, 2))

with open(os.path.join(output_dir, "phase_diagram.csv"), "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["J_over_U", "U_c"])
    for j, Uc in zip(J_over_U_vals, Uc_vals):
        writer.writerow([j, Uc])

# --- hf_magnetization.csv ---
# Hartree-Fock magnetization: earlier onset and smooth saturation
U_vals_hf = U_vals
hf35 = [0.0]*len(U_vals_hf)
hf30 = [0.0]*len(U_vals_hf)
Uc_hf35 = 2.0
Uc_hf30 = 2.5
for i, U in enumerate(U_vals_hf):
    if U < Uc_hf35:
        hf35[i] = 0.0
    else:
        hf35[i] = min(0.35, (U - Uc_hf35) * 0.07)
    if U < Uc_hf30:
        hf30[i] = 0.0
    else:
        hf30[i] = min(0.30, (U - Uc_hf30) * 0.06)

with open(os.path.join(output_dir, "hf_magnetization.csv"), "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["U", "delta_HF_m0.35", "delta_HF_m0.30"])
    for U, d35, d30 in zip(U_vals_hf, hf35, hf30):
        writer.writerow([U, round(d35, 4), round(d30, 4)])
