#!/usr/bin/env python3
import math

# Equivalent circuit constants for COMSOL coupled solver at T_air=500 K, v_air=45.67 m/s
V_oc = 7.58    # open-circuit voltage [V]
R_in = 4.25    # internal resistance [Ohm]

load_resistances = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
header = "load_resistance_ohm,output_voltage_V,output_power_W"

with open("/app/outputs/step_03_output_power_vs_load.csv", "w") as f:
    f.write(header + "\n")
    for RL in load_resistances:
        V_out = V_oc * RL / (R_in + RL)
        P_out = V_out * V_out / RL
        f.write(f"{RL},{V_out:.4f},{P_out:.4f}\n")
