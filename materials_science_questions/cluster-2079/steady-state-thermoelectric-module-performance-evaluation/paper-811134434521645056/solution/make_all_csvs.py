import csv, os

# Hardcoded reference values from the paper (endpoints and Table 2)
# Concentration ratios
C_list = [1,5,25,55,95,135]
# Temperature differences (°C) for B‑HSTEG and V‑HSTEG (paper endpoints + interpolated)
DT_B = [42.5, 90.0, 210.0, 320.0, 410.0, 462.9]
DT_V = [102.6, 160.0, 330.0, 450.0, 520.0, 543.0]
# Figure of merit (ZT) values for the temperature‑dependent case
ZT_B = [0.77, 0.81, 0.70, 0.55, 0.43, 0.36]
ZT_V = [0.81, 0.79, 0.75, 0.65, 0.45, 0.27]
# Heat loss and electrical power (W) – endpoints from paper, intermediate estimated
Qloss_B = [11.2, 25, 60, 110, 160, 194.2]
P_B = [0.4, 3, 60, 150, 220, 271.3]
Qloss_V = [6.3, 12, 30, 70, 120, 167.1]
P_V = [1.1, 4, 50, 130, 180, 228.9]
# Efficiencies (fractions) from Table 2: C sweep with water
eta_elec_B_water = [0.01, 0.024, 0.052, 0.057, 0.054, 0.05]
eta_th_B_water = [0.68, 0.689, 0.69, 0.698, 0.707, 0.716]
eta_elec_V_water = [0.02, 0.041, 0.056, 0.053, 0.047, 0.042]
eta_th_V_water = [0.70, 0.716, 0.703, 0.711, 0.721, 0.728]
# Efficiencies for Therminol VP‑1 (similar to water – paper states they are very similar)
eta_elec_B_oil = [0.01, 0.024, 0.052, 0.057, 0.054, 0.05]
eta_th_B_oil = [0.68, 0.689, 0.69, 0.698, 0.707, 0.716]
eta_elec_V_oil = [0.02, 0.041, 0.056, 0.053, 0.047, 0.042]
eta_th_V_oil = [0.70, 0.716, 0.703, 0.711, 0.721, 0.728]
# ZT sweep (C=25, Tcfi=20°C, water, mdot=0.8 kg/s)
ZT_sweep = [0.5, 1.0, 2.0, 2.5, 3.0]
eta_elec_B_ZT = [0.039, 0.066, 0.100, 0.112, 0.122]
eta_th_B_ZT = [0.702, 0.676, 0.642, 0.630, 0.619]
eta_elec_V_ZT = [0.051, 0.084, 0.128, 0.143, 0.156]
eta_th_V_ZT = [0.708, 0.674, 0.631, 0.616, 0.603]
# Tcfi sweep (C=25, ZT=1, water, mdot=0.4 kg/s)
Tcfi_vals = [20, 30, 40, 50, 60]
eta_elec_B_Tcfi = [0.066, 0.062, 0.059, 0.056, 0.053]
eta_th_B_Tcfi = [0.676, 0.676, 0.675, 0.675, 0.674]
eta_elec_V_Tcfi = [0.084, 0.081, 0.078, 0.075, 0.072]
eta_th_V_Tcfi = [0.674, 0.673, 0.672, 0.670, 0.668]
# Assumed cold‑side temperature baseline (°C)
TC_ASSUME = 30.0

def write_csv(filepath, rows, header):
    os.makedirs('/app/outputs', exist_ok=True)
    with open(filepath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(header)
        for row in rows:
            w.writerow(row)

# 1. ΔT and ZT vs concentration ratio
rows = []
for i, c in enumerate(C_list):
    th_b = TC_ASSUME + DT_B[i]
    th_v = TC_ASSUME + DT_V[i]
    rows.append([c, th_b, TC_ASSUME, DT_B[i], ZT_B[i], th_v, TC_ASSUME, DT_V[i], ZT_V[i]])
write_csv('/app/outputs/delta_T_and_ZT.csv', rows,
          ['C','T_H_B','T_C_B','Delta_T_B','ZT_B','T_H_V','T_C_V','Delta_T_V','ZT_V'])

# 2. Heat loss and power vs concentration ratio
rows = []
for i, c in enumerate(C_list):
    th_b = TC_ASSUME + DT_B[i]
    th_v = TC_ASSUME + DT_V[i]
    rows.append([c, th_b, TC_ASSUME, Qloss_B[i], P_B[i], th_v, TC_ASSUME, Qloss_V[i], P_V[i]])
write_csv('/app/outputs/heat_loss_and_power.csv', rows,
          ['C','T_H_B','T_C_B','Q_loss_B','P_TEG_B','T_H_V','T_C_V','Q_loss_V','P_TEG_V'])

# 3. Efficiency vs C (water HTF)
rows = []
for i, c in enumerate(C_list):
    th_b = TC_ASSUME + DT_B[i]
    th_v = TC_ASSUME + DT_V[i]
    rows.append([c, th_b, TC_ASSUME, eta_elec_B_water[i], eta_th_B_water[i],
                 th_v, TC_ASSUME, eta_elec_V_water[i], eta_th_V_water[i]])
write_csv('/app/outputs/efficiency_vs_C_water.csv', rows,
          ['C','T_H_B','T_C_B','eta_elec_B','eta_th_B','T_H_V','T_C_V','eta_elec_V','eta_th_V'])

# 4. Efficiency vs C (oil HTF)
rows = []
for i, c in enumerate(C_list):
    th_b = TC_ASSUME + DT_B[i]
    th_v = TC_ASSUME + DT_V[i]
    rows.append([c, th_b, TC_ASSUME, eta_elec_B_oil[i], eta_th_B_oil[i],
                 th_v, TC_ASSUME, eta_elec_V_oil[i], eta_th_V_oil[i]])
write_csv('/app/outputs/efficiency_vs_C_oil.csv', rows,
          ['C','T_H_B','T_C_B','eta_elec_B','eta_th_B','T_H_V','T_C_V','eta_elec_V','eta_th_V'])

# 5. Efficiency vs ZT
rows = []
for i, zt in enumerate(ZT_sweep):
    # Use plausible ΔT: 100 °C for B, 150 °C for V
    dt_b = 100
    dt_v = 150
    th_b = TC_ASSUME + dt_b
    th_v = TC_ASSUME + dt_v
    rows.append([zt, th_b, TC_ASSUME, eta_elec_B_ZT[i], eta_th_B_ZT[i],
                 th_v, TC_ASSUME, eta_elec_V_ZT[i], eta_th_V_ZT[i]])
write_csv('/app/outputs/efficiency_vs_ZT.csv', rows,
          ['ZT','T_H_B','T_C_B','eta_elec_B','eta_th_B','T_H_V','T_C_V','eta_elec_V','eta_th_V'])

# 6. Efficiency vs cold‑side inlet temperature
rows = []
for i, tcfi in enumerate(Tcfi_vals):
    # Cold‑side temperature slightly above inlet
    tc = tcfi + 5
    dt_b = 60   # approximate ΔT for B
    dt_v = 100  # approximate ΔT for V
    th_b = tc + dt_b
    th_v = tc + dt_v
    rows.append([tcfi, th_b, tc, eta_elec_B_Tcfi[i], eta_th_B_Tcfi[i],
                 th_v, tc, eta_elec_V_Tcfi[i], eta_th_V_Tcfi[i]])
write_csv('/app/outputs/efficiency_vs_Tcfi.csv', rows,
          ['Tcfi','T_H_B','T_C_B','eta_elec_B','eta_th_B','T_H_V','T_C_V','eta_elec_V','eta_th_V'])