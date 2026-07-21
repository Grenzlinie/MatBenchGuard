import json
import math
import csv
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('output_file')
    args = parser.parse_args()
    
    with open('/app/outputs/torque_force_values.csv', 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    
    target_kl_force = 0.5
    target_kl_torque = 5.0
    tau_dimless = None
    F_dimless = None
    
    for row in data:
        kl = float(row['k_lambda'])
        if abs(kl - target_kl_torque) < 1e-6:
            tau_dimless = float(row['tau_dimless'])
        if abs(kl - target_kl_force) < 1e-6:
            F_dimless = float(row['F_dimless'])
    
    if tau_dimless is None or F_dimless is None:
        raise ValueError("Could not find required k_lambda values in CSV")
    
    T_kappa = 1e-3
    lam = 1e-9
    a = lam / 10
    A_area = 2e-17
    M_s = 2e6
    gamma = 1.76e11
    alpha = 0.01
    
    s_per_length = (M_s / gamma) * A_area
    
    k_torque = target_kl_torque / lam
    tau_phys = T_kappa * a**2 * k_torque * tau_dimless
    V_FM = tau_phys / (2 * s_per_length)
    
    k_force = target_kl_force / lam
    F_phys = T_kappa * a**2 * k_force**2 * F_dimless
    V_AFM = (lam * F_phys) / (2 * alpha * s_per_length)
    
    result = {
        'k_lambda_torque': target_kl_torque,
        'ferromagnetic_velocity_ms': V_FM,
        'k_lambda_force': target_kl_force,
        'antiferromagnetic_velocity_ms': V_AFM
    }
    
    with open(args.output_file, 'w') as f:
        json.dump(result, f, indent=2)

if __name__ == '__main__':
    main()
