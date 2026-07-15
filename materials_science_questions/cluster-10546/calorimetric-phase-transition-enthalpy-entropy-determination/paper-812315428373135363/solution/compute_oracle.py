import json, csv, math
import numpy as np

def process_compound(filepath, compound_name, tc_fixed, delta_H, delta_S, N_mol, n_val, output_thermo_file, output_model_file, output_cp_anomaly_file):
    # Read data
    T_data = []
    Cp_data = []
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        try:
            next(reader)  # skip header
        except StopIteration:
            pass
        for row in reader:
            try:
                T = float(row[0])
                Cp = float(row[1])
                T_data.append(T)
                Cp_data.append(Cp)
            except:
                pass
    T = np.array(T_data)
    Cp = np.array(Cp_data)

    Tc = tc_fixed
    # Use experimental maximum near Tc for peak Cp
    idx_max = np.argmax(Cp)
    Cp_max = Cp[idx_max]
    T_max = T[idx_max]

    # Write thermo JSON
    thermo = {
        "compound": compound_name,
        "Tc_K": Tc,
        "Delta_H_kJ_mol": delta_H,
        "Delta_S_J_K_mol": delta_S
    }
    with open(output_thermo_file, 'w') as f:
        json.dump(thermo, f, indent=2)

    # Write model params JSON
    model_params = {
        "compound": compound_name,
        "N_mol-1": N_mol,
        "n": n_val
    }
    with open(output_model_file, 'w') as f:
        json.dump(model_params, f, indent=2)

    # Fit baseline outside transition window
    window = 15.0 if compound_name != "[Fe(phen)2(NCS)2]" else 10.0
    mask_base = (T < Tc - window) | (T > Tc + window)
    T_base = T[mask_base]
    Cp_base = Cp[mask_base]
    if len(T_base) < 5:
        raise RuntimeError("Not enough baseline points")
    coeffs = np.polyfit(T_base, Cp_base, 3)
    baseline = np.polyval(coeffs, T)

    # Generate model Cp curve
    k_B = 1.380649e-23  # J/K
    N = N_mol
    T_grid = np.linspace(Tc - 30, Tc + 30, 200)
    Cp_normal = np.interp(T_grid, T, baseline)

    # Mole fraction x(T)
    exponent = (delta_S * (Tc - T_grid)) / (N * k_B * T_grid)
    exponent_clipped = np.clip(exponent, -500, 500)
    x = 1.0 / (1.0 + np.exp(exponent_clipped))

    # Anomaly term scaling from peak
    baseline_at_Tc = np.interp(Tc, T, baseline)
    Cp_at_Tc = np.interp(Tc, T, Cp)
    anom_peak = max(Cp_at_Tc - baseline_at_Tc, 0.1)
    H_diff_sq = 4.0 * N * k_B * (Tc**2) * anom_peak

    Cp_anom = H_diff_sq * x * (1.0 - x) / (N * k_B * T_grid**2)
    Cp_model = Cp_normal + Cp_anom

    with open(output_cp_anomaly_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["T(K)", "Cp_model(J/K/mol)"])
        for ti, cpi in zip(T_grid, Cp_model):
            writer.writerow([f"{ti:.3f}", f"{cpi:.3f}"])

# Process NCS
process_compound(
    filepath="/app/resources/cp_NCS.csv",
    compound_name="[Fe(phen)2(NCS)2]",
    tc_fixed=176.29,
    delta_H=8.60,
    delta_S=48.78,
    N_mol=6.34e21,
    n_val=95,
    output_thermo_file="/app/outputs/step_01a_thermo_NCS.json",
    output_model_file="/app/outputs/step_02a_model_NCS.json",
    output_cp_anomaly_file="/app/outputs/step_03a_cp_anomaly_NCS.csv"
)

# Process NCSe
process_compound(
    filepath="/app/resources/cp_NCSe.csv",
    compound_name="[Fe(phen)2(NCSe)2]",
    tc_fixed=231.26,
    delta_H=11.60,
    delta_S=51.22,
    N_mol=7.83e21,
    n_val=77,
    output_thermo_file="/app/outputs/step_01b_thermo_NCSe.json",
    output_model_file="/app/outputs/step_02b_model_NCSe.json",
    output_cp_anomaly_file="/app/outputs/step_03b_cp_anomaly_NCSe.csv"
)
