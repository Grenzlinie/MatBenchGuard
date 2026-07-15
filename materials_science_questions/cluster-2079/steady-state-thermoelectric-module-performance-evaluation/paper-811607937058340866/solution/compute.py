import csv
import math
import sys

def compute_step1():
    TH = 400.0
    TC = 300.0
    etaC = (TH - TC) / TH
    TcTh = TC / TH
    ZoptTbar_values = [0.1, 0.2, 0.3, 0.4, 0.5]
    chi_list = [0.01 * i for i in range(100)]  # 0.00 .. 0.99
    with open("/app/outputs/step_01_figure1_data.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["χ", "η_eff", "Z_opt_T_bar"])
        for ZoptTbar in ZoptTbar_values:
            for chi in chi_list:
                one_minus_chi = 1.0 - chi
                arg = 1.0 + ZoptTbar / one_minus_chi
                sqrt_arg = math.sqrt(arg)
                eta_eff = etaC * one_minus_chi * (sqrt_arg - 1.0) / (sqrt_arg + TcTh)
                writer.writerow([chi, eta_eff, ZoptTbar])

def compute_step2():
    TH = 400.0
    TC = 300.0
    deltaT = TH - TC
    Tbar = (TH + TC) / 2.0
    S = 1.0
    d = 0.01
    power_factors = [1e-4, 2e-4, 3e-4, 4e-4, 5e-4]
    kappa_list = [0.1 + (100.0 - 0.1) * i / 99.0 for i in range(100)]
    factor_pre = S * deltaT**2 / (2 * d)
    with open("/app/outputs/step_02_figure2_data.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["κ", "W", "power_factor"])
        for pf in power_factors:
            for kappa in kappa_list:
                term1 = 1.0 + pf * TH / (2 * kappa)
                term2 = math.sqrt(1.0 + pf * Tbar / kappa)
                denominator = term1 + term2
                W = pf * factor_pre / denominator
                writer.writerow([kappa, W, pf])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: compute.py step1|step2", file=sys.stderr)
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "step1":
        compute_step1()
    elif cmd == "step2":
        compute_step2()
    else:
        print("Unknown step", file=sys.stderr)
        sys.exit(1)